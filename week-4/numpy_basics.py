import numpy as np

# import numpy as np

# # Python list
# harga_list = [9200, 9350, 9100, 9400, 9500]

# # NumPy array
# harga_array = np.array([9200, 9350, 9100, 9400, 9500])



# todays_return = (todays_price - yesterdays_price) / yesterdays_price * 100

# print(harga_array.mean())
# print(harga_array.std())
# print(harga_array.min())
# print(harga_array.max())

# print(todays_return)

def analisis_harga(harga_array):
    """
    Menerima numpy array harga saham.
    Return dict berisi:
    - mean, std, min, max
    - return harian (array)
    - apakah volatile (True jika std > 2% dari mean)
    """
    todays_price = harga_array[1:]
    yesterdays_price = harga_array[:-1]
    todays_return = (todays_price - yesterdays_price) / yesterdays_price * 100
    
    volatile = True if harga_array.std() > 0.02 * harga_array.mean() else False
    volatile = harga_array.std() > 0.02 * harga_array.mean()
    
    datas = {
       "mean" : harga_array.mean(),
       "std" : harga_array.std(),
       "maximum" : harga_array.max(), 
       "minimum" : harga_array.min(),
       "volatile" : volatile,
       "daily_return" : todays_return
    }

    return datas

data = np.array([
    [9200, 1200000, 0.0],
    [9350, 1500000, 1.6],
    [9100,  980000, -2.7],
    [9400, 1300000, 3.2],
    [9500, 1100000, 1.1],
])

# harga = data[:, 0]
# print(analisis_harga(harga)["mean"])



harga = np.array([9200, 9350, 9100, 9400, 9500])
hasil = analisis_harga(harga)
for k, v in hasil.items():
    print(f"{k}: {v}")