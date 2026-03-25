def gallonat_litroiksi(gallonat):
    return gallonat * 3.785

def main():
    while True:
        gallonat = float(input("Syötä bensiinin määrä gallonoina: "))
        if gallonat < 0:
            break
        litrat = gallonat_litroiksi(gallonat)
        print(f"Määrä on {litrat} litraa.")

if __name__ == "__main__":
    main()