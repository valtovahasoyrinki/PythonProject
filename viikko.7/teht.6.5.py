def karsi_parittomat(lukulista):
    return [luku for luku in lukulista if luku % 2 == 0]


def main():
    alkuperainen_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    karsittu_lista = karsi_parittomat(alkuperainen_lista)

    print(f"Alkuperäinen lista: {alkuperainen_lista}")
    print(f"Karsittu lista: {karsittu_lista}")


if __name__ == "__main__":
    main()