hemoglobiini_m = 0
hemoglobiini_n = 0

sukupuoli = input("Oletko M vai N? ")
if sukupuoli == "M":hemoglobiini_m = int(input("Mikä on sinun hemoglobiiniarvo? "))

if sukupuoli == "N":hemoglobiini_n = int(input("Mikä on sinun hemoglobiiniarvo? "))

if sukupuoli == "M" and hemoglobiini_m < 134:print("Hemoglobiinisi on alhainen")
elif sukupuoli == "M" and hemoglobiini_m > 195:print("Hemoglobiinisi on korkea")
elif sukupuoli == "M" and 134 <= hemoglobiini_m <= 195:print("Hemoglobiinisi on normaali")

if sukupuoli == "N" and hemoglobiini_n < 117:print("Hemoglobiinisi on alhainen")
elif sukupuoli == "N" and hemoglobiini_n > 175:print("Hemoglobiinisi on korkea")
elif sukupuoli == "N" and 117 <= hemoglobiini_n <= 175:print("Hemoglobiinisi on normaali")