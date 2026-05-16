import numpy as np

# todays_price = 1000

# price_fivedays = np.array([9200, 9350, 9100, 9400, 9450])

# mean = np.mean(price_fivedays)

# print(mean)

name = input("What is the ticker : ")
purchase_price = input(float("How much is the purchase price for the stock : "))
selling_price = input(float("How much is the selling price for the stock : "))
lot = input(float("How many lot(s) : "))

shares = lot * 100

total = purchase_price * shares
total_net = total + 0.1 * total

selling = selling_price * shares
selling_net = selling_price - 0.2 * selling

pnl = total_net - selling_net


def inital(purchase_price, lot, fee_beli = 0.1):
    modal = purchase_price * 100 * lot
    fee = modal * fee_beli
    return modal + fee

def jual(selling_price, lot, fee_jual = 0.2):
    harga_jual = selling_price * 100 * lot
    fee = harga_jual * fee_jual
    
    return harga_jual - fee

def hitung_ProfitorLoss(total_beli, total_jual):
        return total_jual - total_beli
