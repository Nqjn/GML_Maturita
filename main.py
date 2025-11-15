from Excel import *
from GUI import *
from MyOCR import *


def main():
    res = vyrobit_okno()
    print(f"Vybraný soubor z GUI aaaaaaaaaaaaaaaaaaaaaaaaaaaaa: {res}")
    r = ReadData(res)
    print(f"Vybraný soubor z GUI aaaaaaaaaaaaaaaaaaaaaaaaaaaaa neyrdkyurdku: {r}")

if __name__ == "__main__":
    main()