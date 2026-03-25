import math


def laske_yksikkohinta(halkaisija_cm, hinta):
    sade_m = (halkaisija_cm / 2) / 100
    pinta_ala_m2 = math.pi * (sade_m ** 2)
    return hinta / pinta_ala_m2


def main():
    halkaisija1 = float(input("Syötä ensimmäisen pizzan halkaisija (cm): "))
    hinta1 = float(input("Syötä ensimmäisen pizzan hinta (euroa): "))

    halkaisija2 = float(input("Syötä toisen pizzan halkaisija (cm): "))
    hinta2 = float(input("Syötä toisen pizzan hinta (euroa): "))

    yksikkohinta1 = laske_yksikkohinta(halkaisija1, hinta1)
    yksikkohinta2 = laske_yksikkohinta(halkaisija2, hinta2)

    if yksikkohinta1 < yksikkohinta2:
        print("Ensimmäinen pizza antaa paremman vastineen rahalle.")
    elif yksikkohinta2 < yksikkohinta1:
        print("Toinen pizza antaa paremman vastineen rahalle.")
    else:
        print("Molemmat pizzat antavat yhtä hyvän vastineen rahalle.")


if __name__ == "__main__":
    main()