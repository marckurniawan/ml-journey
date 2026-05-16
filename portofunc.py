class Portofolio:
    def __init__(self):
        self.posisi = []

    def add(self, ticker, lot, harga_beli, harga_sekarang):
        new = {
        "ticker": ticker,
        "lot": lot,
        "harga_beli": harga_beli,
        "harga_sekarang": harga_sekarang,
        }
        self.posisi.append(new)
    
    def delete(self, ticker):
        self.posisi[:] = [i for i in self.posisi if i["ticker"] != ticker]

    def update(self, ticker, harga_baru):
        for i in self.posisi:
            if i["ticker"] == ticker:
                i["harga_sekarang"] = harga_baru
    def hitung_profit(self, harga_sekarang, harga_beli, lot):
        return (harga_sekarang - harga_beli) * lot * 100

    def summarize(self):
        rank_profit = sorted(
            self.posisi,
            key=lambda x: self.hitung_profit(x["harga_sekarang"], x["harga_beli"], x["lot"]),
            reverse=True,
        )

        total_profit = 0

        for position in rank_profit:
            profit = self.hitung_profit(
                position["harga_sekarang"], position["harga_beli"], position["lot"]
            )
            total_profit += profit

            print(f"Ticker: {position['ticker']}")
            print(f"Lot: {position['lot']}")
            print(f"Harga beli: {position['harga_beli']}")
            print(f"Harga sekarang: {position['harga_sekarang']}")
            print(f"Profit : {profit:.2f}")

        print(f"Total profit: {total_profit}")


