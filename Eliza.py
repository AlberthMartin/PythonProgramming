import string
import random
import logging

positiva=["Berätta mer","Jag förstår...", "Ahaa...", "Jag lyssnar...", "Okej", "Kan du förklara...", "Berätta ännu mera...", "Jag förstår verkligen...", "Jahaaaja..."]
negativa=["Säger du nej bara för att vara negativ?","Inte det?","Är du säker","Är det sant?" ,"Varför inte??","Är du 100% sekär?", "Är det du berättar sant?"]
familjeproblem=["Är din bror likadan??", "Är din syster likadan??", "Vad störande!","Tycker du att du borde bli behandlad annorlunda eller??","Sådana är föräldrar..."]
avsluta=["hej då","tack och gonatt","jag måste gå","hejs svejs", "jag orkar inte med dig","tjingeling"]
olagligatecken=["!","?",".",":",",","<",">","#","€","%"]

def main():
    starttext()
    
    while True:
        text = str(input("\n> "))
        log(text) #Loggar texten som skrivs in av användaren.
        text = text.lower()
        if text in avsluta:
            break
        else:
            svaret=svara(text)
            print(svaret) #printer returnerade svaret av funktionen
            log(svaret) #Loggar eliza's svar.
            
    print("Tack för besöket. Betala in 150 EUR på mitt konto.")

def starttext():
    print ("**************************************************")
    print ()
    print (" Välkommen till Elizas mottagning ")
    print ()
    print ("**************************************************")
    print ()
    print ('(Du kan sluta när som helst genom att svara "Hej då")')
    print ()
    print ('Berätta för mig om dina problem...')


def svara(text):
    urspr_ord=str.split(text)
    nya_ord=urspr_ord[ : ]

    if urspr_ord[-1][-1] in olagligatecken:
        urspr_ord[len(urspr_ord)-1]=urspr_ord[len(urspr_ord)-1][:-1]
    #Om "jag älskar dig!" tar bort olagliga tecken på slutet -->"jag älskar dig"
    
    for i in range(len(urspr_ord)):
        if urspr_ord[i]=="jag":
            nya_ord[i]="du"
        elif urspr_ord[i]=="min":
            nya_ord[i]="din"
        elif urspr_ord[i]=="mitt":
            nya_ord[i]="ditt"
        elif urspr_ord[i]=="mig":
            nya_ord[i]="dig"
        elif urspr_ord[i]=="mina":
            nya_ord[i]="dina"
        elif urspr_ord[i]=="du":
            nya_ord[i]="jag"
        elif urspr_ord[i]=="din":
            nya_ord[i]="min"
        elif urspr_ord[i]=="ditt":
            nya_ord[i]="mitt"
        elif urspr_ord[i]=="dig":
            nya_ord[i]="mig"
        elif urspr_ord[i]=="dina":
                nya_ord[i]="mina"
        
    if "nej" in urspr_ord or "aldrig" in urspr_ord:
        return(random.choice(negativa))
    
    elif "mamma" in urspr_ord or "pappa" in urspr_ord:
        return(random.choice(familjeproblem))
            
    elif nya_ord==urspr_ord:
        return(random.choice(positiva))
        
    else:
        return(" ".join(nya_ord)+"?")


#Logging koden
logName="eliza"
logFileName=logName+'.log'

logger=logging.getLogger(logName)
hdlr=logging.FileHandler(logFileName)

formatter=logging.Formatter('%(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 


logger.setLevel(logging.INFO)

logFile = open( logFileName,"w")
logFile.write("")
logFile.close()

def log(s):
    logger.info(s)



main()
