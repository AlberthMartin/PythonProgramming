#Alberth Martin, Alexander Kjellman och William Sjöblad


def encrypt(message,key):
#Funktion som krypterar meddelanden.
#"message"=meddelandet man vill kryptera.
#"key"= nyckeln som man krypterar utgående från.
    encrypted_message=""
    #Tom sträng som sedan fylls med encrypterade bokstäverna
    for character in message:
        #Krypterar varje bokstav i meddelande enskilt.
        if character.isupper():
            #Om bokstaven i meddelandet är stor bokstav.
            old_ascii=ord(character)
            #returnerar ASCII-värdet för bokstaven
            new_ascii=(old_ascii+key-65)%26+65
            #Ger ett nytt ASCII-värde till bokstaven utgående från key'n man satte in (nya bokstaven är "key" steg frammåt i alfabetet alltså A skulle bli D då key=3)
            new_char=chr(new_ascii)
            #returnerar tecknet för den nya bokstaven, utgående från det nya ASCII-värdet.
            encrypted_message+=new_char
            # Tillsätter det krypterade tecknet i stringen "encrypted_massage".
        elif character.islower():
            #Motsvarande för små bokstäver
            old_ascii=ord(character) 
            new_ascii=(old_ascii+key-97)%26+97 #97 för små bokstäver istället för 65 som för stora bokstäver.
            new_char=chr(new_ascii)
            encrypted_message+=new_char
        else:
            encrypted_message+=character
             #Om inte tecknet är stor eller liten bokstav krypteras det inte utan bara skrivs ut som det är.
    return encrypted_message
    #Funktionen returnerar det krypterade meddelandet


def decrypt(message,key):
#Funktion som dekrypterar ett meddelande.
#Tar som parametrar "message"=meddelandet man vill dekryptera och "key"=nyckeln för att konvertera bokstäverna rätt.
#Till stort sätt lika som funktionen ovan som krypterar meddelanden.
#Ända skillnaden att man subtraherar "key" från tidigare ASCII,
#medan man i krypterarfunktionen adderar "key" till tidigare ASCII.
    decrypted_message=""
    for character in message:
        if character.isupper():
            old_ascii=ord(character)
            new_ascii=(old_ascii-key-65)%26+65
            new_char=chr(new_ascii)
            decrypted_message+=new_char
        elif character.islower():
            old_ascii=ord(character)
            new_ascii=(old_ascii-key-97)%26+97
            new_char=chr(new_ascii)
            decrypted_message+=new_char
        else:
            decrypted_message+=character
    return decrypted_message


def break_crypt(message):
#En funktion som bryter förskjutningschiffern genom att testa alla förflyttningsmöjligheter (26st) med en for loop.
    for key in range(26): #Testar att decryptera meddelandet med alla möjliga keys (26st)
#Koden nedan är i stort sett en kopia av koden i funktionen encrypt(message,key)
        encrypted_message="" 
        for character in message:
            if character.isupper():
                old_ascii=ord(character)
                new_ascii=(old_ascii+key-65)%26+65
                new_char=chr(new_ascii)
                encrypted_message+=new_char
            elif character.islower():
                old_ascii=ord(character)
                new_ascii=(old_ascii+key-97)%26+97
                new_char=chr(new_ascii)
                encrypted_message+=new_char
            else:
                encrypted_message+=character
        print(encrypted_message) #printar ut meddelandet för varje key.


def get_key():
#Funktion som ber användaren mata in "key" man vill använda och returnerar sedan "key"
    key=int(input("Input the key (an integer value): "))
    return key


def get_message():
#Funktion som ber användaren mata in meddelande som sparas i "message" som sedan returneras.
    message=input("Input the message here: ")
    return message


def action():
#Huvudfunktionen som anropar funktionerna ovan och gör programmet mera användarvänligt.

    while True:
    #Programmet upprepas till användaren väljer q.
        print()
        print("What would you like to do? ")
        choice=input("e: encrypt\nd: decrypt\nb: break\nq: quit\n>")
        #sparar användarens val i variabeln choice och utifrån det vet programmet vad som ska göras till näst.

        if choice.lower() == 'q': 
            break #programmet avslutas
        
        elif choice.lower() == 'd':
            key=get_key() 
            message=get_message()
            plaintext=decrypt(message,key)
            #Funktionen decrypt(message,key) anropas, tar in parametrarna "key" och "message" ovan och utifrån det dekrypterar meddelandet som sedan returneras och
            #sparas i "plaintext"
            print("The decrypted message is %s" % plaintext) 
    
        elif choice.lower() == 'e':
            key=get_key()
            message=get_message()
            cryptotext=encrypt(message,key)
            #Funktionen encrypt(message,key) anropas, tar in parametrarna "key" och "message" ovan och utifrån det enkrypterar meddelandet som sedan returneras och
            #sparas i "cryptotext."
            print("The encrypted message is %s" % cryptotext)

        elif choice.lower() == 'b':
            message=get_message()
            break_crypt(message)
            #Funktionen break_crypt(message) anropas och använder parametern "message" som frågades efter ovan.

action() #Huvudfunktionen anropas.

