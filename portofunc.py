def hitung_profit(harga_sekarang, harga_beli, lot):
    """itung harga"""
    return (harga_sekarang - harga_beli) * lot * 100


def add(portofolio, ticker, lot, harga_beli, harga_sekarang):
    """
    Masukkan item beserta dengan atributnya ke dalam list dalam bentuk dict
    """
    new = {
        "ticker": ticker,
        "lot": lot,
        "harga_beli": harga_beli,
        "harga_sekarang": harga_sekarang,
    }
    portofolio.append(new)


def delete(portofolio, ticker):
    """
    Hapus item jika namanya match dari list
    """

    portofolio[:] = [i for i in portofolio if i["ticker"] != ticker]


def update(portfolio, ticker,  harga_baru):
    """
    Mengganti harga item tertentu
    """
    for i in portfolio:
        if i["ticker"] == ticker:
            i["harga_sekarang"] = harga_baru


def summarize(portofolio):
    """
    Menampilkan seluruh item di list urut dari profit tertinggi dan seluruh unrealized p&l sekarang
    """
    rank_profit = sorted(
        portofolio,
        key=lambda x: hitung_profit(x["harga_sekarang"], x["harga_beli"], x["lot"]),
        reverse=True,
    )

    total_profit = 0

    for position in rank_profit:
        profit = hitung_profit(
            position["harga_sekarang"], position["harga_beli"], position["lot"]
        )
        total_profit += profit

        print(f"Ticker: {position['ticker']}")
        print(f"Lot: {position['lot']}")
        print(f"Harga beli: {position['harga_beli']}")
        print(f"Harga sekarang: {position['harga_sekarang']}")
        print(f"Profit : {profit:.2f}")

    print(f"Total profit: {total_profit}")


