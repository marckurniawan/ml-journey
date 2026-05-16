from portofunc import (hitung_profit, add, delete, update, summarize)



def main():
    portofolio = []
    add(portofolio, "BBCA", 10, 6500, 6500)
    add(portofolio, "TLKM", 100, 500, 500)
    add(portofolio, "BMRI", 5, 7500, 7500)

    update(portofolio, "BMRI", 8000)

    delete(portofolio, "TLKM")

    summarize(portofolio)


if __name__ == "__main__":
    
    main()