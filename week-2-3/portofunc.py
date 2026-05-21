import json


class Portofolio:
    def __init__(self):
        self.posisi = []

    def _cek_ticker(self, ticker):
        if not [i for i in self.posisi if i["ticker"] == ticker]:
            return False
        return True

    def add(self, ticker, lot, harga_beli, harga_sekarang):
        if harga_beli <= 0 :
            raise ValueError(f"Harga beli tidak valid")
        if harga_sekarang <= 0:
            raise ValueError(f"Harga sekarang tidak valid")
        elif lot <= 0:
            raise ValueError(f"Lot yang anda masukkan tidak valid")
        new = {
        "ticker": ticker,
        "lot": lot,
        "harga_beli": harga_beli,
        "harga_sekarang": harga_sekarang,
        }
        self.posisi.append(new)
    
    def delete(self, ticker):
        if not self._cek_ticker(ticker):
            raise ValueError(f"Ticker {ticker} tidak ditemukan")
        else:
            self.posisi[:] = [i for i in self.posisi if i["ticker"] != ticker]

    def update(self, ticker, harga_baru):
        if not self._cek_ticker(ticker) :
            raise ValueError(f"Ticker {ticker} tidak ditemukan")
        elif harga_baru <= 0:
            raise ValueError(f"Harga yang anda masukkan ({harga_baru}) tidak valid")
        else:         
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

    def simpan(self, filename="portofolio.json"):
        """Simpan self.posisi ke file JSON."""
        with open(filename, "w") as f:
            json.dump(self.posisi, f)

    def muat(self, filename="portofolio.json"):
        """Baca file JSON dan isi self.posisi."""
        try:
            with open(filename, "r") as f:
                self.posisi = json.load(f)
        except FileNotFoundError:
            pass