from Excel import *
from GUI import *
from MyOCR import *


def main():
    res = vyrobit_okno()
    r = ReadData(res)
    print(f"Vybraný soubor z GUI aaaaaaaaaaaaaaaaaaaaaaaaaaaaa: {r}")

if __name__ == "__main__":
    main()