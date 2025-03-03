import random
ratta_svar=0
antal_fragor=int(input("Hur många frågor vill du ha: "))
svarighetsgrad=int(input("Vilken svårighetsgrad vill du ha 1.Lätt 2.Medel 3.Svår: "))

if svarighetsgrad==1:
    maxintervall=5
    for tal in range(antal_fragor):
        tal1=random.randrange(1,maxintervall)
        tal2=random.randrange(1,maxintervall)
        print("Vad är",tal1,"*",tal2)
        svaret=int(input("Skriv svaret här: "))
        if svaret==(tal1*tal2):
            print("Rätt svar")
            ratta_svar=ratta_svar+1
            maxintervall=maxintervall+1
        else:
            print("Fel svar, rätta svaret var",tal1*tal2)
                   
elif svarighetsgrad==2:
    maxintervall=11
    for tal in range(antal_fragor):
        tal1=random.randrange(1,maxintervall)
        tal2=random.randrange(1,maxintervall)
        print("Vad är",tal1,"*",tal2)
        svaret=int(input("Skriv svaret här: "))
        if svaret==(tal1*tal2):
            print("Rätt svar")
            ratta_svar=ratta_svar+1
            maxintervall=maxintervall+1
        else:
            print("Fel svar, rätta svaret var",tal1*tal2)

elif svarighetsgrad==3:
    maxintervall=21
    for tal in range(antal_fragor):
        tal1=random.randrange(1,maxintervall)
        tal2=random.randrange(1,maxintervall)
        print("Vad är",tal1,"*",tal2)
        svaret=int(input("Skriv svaret här: "))
        if svaret==(tal1*tal2):
            print("Rätt svar")
            ratta_svar=ratta_svar+1
            maxintervall=maxintervall+1
        else:
            print("Fel svar, rätta svaret var",tal1*tal2)

print("Du svarade rätt på", ratta_svar," av ",antal_fragor)
betyg=(ratta_svar/antal_fragor)*100
if betyg==100:
    print("Ditt betyg blev 5")
elif betyg<100 and betyg>=80:
    print("Ditt betyg blev 4")
elif betyg<80 and betyg>=70:
    print("Ditt betyg blev 3")
elif betyg<70 and betyg>=60:
    print("Ditt betyg blev 2")
elif betyg<60 and betyg>=50:
    print("Ditt betyg blev 1")
else:
    print("Du fick underkänt")
    
    
