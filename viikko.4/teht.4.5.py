yritykset = 0
while yritykset < 5:
    tunnus = input ("Anna käyttäjätunnus")
    ss=input ("Anna salasana")

    if tunnus == "python" and ss == "rules":
        print ("tervetuloa")
        break
    else:
        print ("väärä käyttäjätunnuts")
        yritykset +=1
if yritykset == 5:
    print ("acces denied")
    