def laske_summa(lukulista):
    return sum(lukulista)

def main():
    testilista = [10, 20, 30, 40, 50]
    summa = laske_summa(testilista)
    print(f"Listan lukujen summa on {summa}")

if __name__ == "__main__":
    main()