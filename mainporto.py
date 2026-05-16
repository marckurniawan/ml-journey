from portofunc import Portofolio



def main():
    portofolio = Portofolio()
    portofolio.muat()

    
    portofolio.summarize()

    portofolio.simpan()

    


if __name__ == "__main__":
    
    main()