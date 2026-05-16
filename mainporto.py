from portofunc import Portofolio



def main():
    portofolio = Portofolio()
    portofolio.add( "BBCA", 10, 6500, 6500)
    portofolio.add( "TLKM", 100, 500, 500)
    portofolio.add( "BMRI", 5, 7500, 7500)

    portofolio.update( "BMRI", 8000)

    portofolio.delete("TLKM")

    portofolio.summarize()


if __name__ == "__main__":
    
    main()