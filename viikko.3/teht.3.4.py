vuosiluku=int(input("Sano joku vuosiluku"))
if vuosiluku <0:
    print("Sano psoitiivinen vuosiluku")
if vuosiluku >0:
    if vuosiluku % 400==0:
        print(f"vuonna {vuosiluku} oli karkauspäivä")
    elif vuosiluku % 100 == 0:
        print(f"vuonna {vuosiluku} ei ollut karkauspäivä")
    elif vuosiluku % 4 == 0:
        print(f"vuonna {vuosiluku} oli karkauspäivä")
    else:
        print(f"vuonna {vuosiluku} ei ollut karkauspäivä")


