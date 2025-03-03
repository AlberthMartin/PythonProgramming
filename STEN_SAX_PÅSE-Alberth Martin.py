import random


def checkResults(user,computer): #En funktion som tar användarens och datorns val som argument.
    if user==computer:
        return "Oavgjort" #Returnerar oavgjort
    elif user==1 and computer==2:
        return "Du vann" 
    elif user==2 and computer==3:
        return "Du vann"
    elif user==3 and computer==1:
        return "Du vann" #Returnerar när du vinner.
    else:
        return "Datorn vann" #Returnerar när datorn vann.

print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*") #Startmeddelande som printar ut vad det är frågan om
print("Välkommen till spelet: Sten-Sax-Påse")
print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
print()


computerpoang=0 #Datorns och användarens poäng vid start
userpoang=0 

totalpoang=int(input("Hur många poäng behövs för att vinna?(Input an integer): "))
#Användaren berättar för systemet hur många poäng det krävs för att vinna.


while totalpoang>computerpoang and totalpoang>userpoang: #Blocket nedan upprepas tills poängen som behövs för att vinna har uppnåtts för datorn eller användaren
    print()
    computer=random.randrange(1,4) #Datorn gör sitt val.
    user=int(input("Gör ditt val:\n 1:Sten\n 2:Sax\n 3:Påse\n>")) #Användaren gör sitt val.
    result=checkResults(user,computer) #Funktionen kollar vem som vinner och resultatet returneras och lagras i result.

    if result=="Du vann": 
        print(result, " (du valde",user,"datorn valde",computer,")") #resultatet printas ut.
        userpoang=userpoang+1 #Användaren får ett poäng när hen vinner.
        
    elif result=="Datorn vann":
        print(result, " (du valde",user,"datorn valde",computer,")")
        computerpoang=computerpoang+1 #Datorn får ett poäng om den vinner

    else: #Om det blev oavgjort.
        print(result, " (du valde",user,"datorn valde",computer,")") 
        computerpoang=computerpoang+0 
        userpoang=userpoang+0 #Om det blev oavgjort får ingendera poäng.

print()
print("Slutställning") # While loopen avslutas då poängen det krävs för att vinna, för någondera, har uppnåtts och slutmeddelande skrivs ut.
print("-------------")
print("Datorn:", computerpoang) #Datorns slutpoäng
print("Användaren:",userpoang) #Användarens slutpoäng

