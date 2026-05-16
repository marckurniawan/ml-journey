from portofunc import Portofolio


def input_angka(prompt):
    while True:
        try:
            angka = int(input(f"{prompt}"))
            break
        except ValueError:
            print("Masukkan integer")
    return angka

def main():
    portofolio = Portofolio()
    portofolio.muat()
    while True:
        perintah = input("> ").lower()
        
        if perintah == "add":
            # minta input ticker, lot, harga
            ticker = input("Enter ticker: ").upper()
            lot = input_angka("Enter lot: ")
            harga_beli = input_angka("Masukkan harga beli: ")
            harga_sekarang = input_angka("Masukkan harga sekarang: ")
            try:
                portofolio.add(ticker, lot, harga_beli, harga_sekarang)
            except ValueError as e:
                print(f"{e} (harus > 0)")
        elif perintah == "delete":
            # minta input ticker
            ticker = input("Enter ticker: ").upper()
            try:
                portofolio.delete(ticker)
            except ValueError as e:
                print(f"Error: {e}")
        elif perintah == "update":
            ticker = input("Enter ticker: ").upper()
            harga_baru = input_angka("Masukkan harga baru:")
            try:
                portofolio.update(ticker, harga_baru)
            except ValueError as e:
                print(f"{e}")
        elif perintah == "summarize":
            # panggil summarize
            portofolio.summarize()
        elif perintah == "keluar":
            # simpan dan break
            portofolio.simpan()
            break
        else:
            print("Perintah tidak dikenal")

if __name__ == "__main__":
    main()