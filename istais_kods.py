import datetime
import json

def main(): # šī funkcija koordinē visa koda darbību
    pirma_izvele = lietotaja_izvele()
    if pirma_izvele == "1":
        pirmreizejs_lietotajs()
        jautajumi_res = jautajumi()
        kalkulacija(jautajumi_res)
    else:
        atkartots_lietotajs()

def lietotaja_izvele(): # šī funkcija uzzin, vai lietotājs ir pirmreizējs vai atkārtots.
    while True:
        ja_ne = input("\nLabdien! Esmu rīks, kurš palīdzēs tev pārvaldīt savus viedtālruņa lietošanas pamatus!\n Lai komunicētu ar šo programmu, ieraksti ciparu pirms vēlamās atbildes (piemēram, 1 vai 2) \n Vai šo programmu izmanto pirmo reizi? \n1. Jā\n2. Nē\nIzvēle: ").strip()
        if ja_ne == "1":
            return "1"
        elif ja_ne == "2":
            return "2"
        else:
            print("Nepareiza ievade.")

def pirmreizejs_lietotajs(): # Ja lietoājs ir pirmreizējs, funkcija piedāvā atbildēt uz 6 jautājumiem
    # Ja lietotājs piekrīt, funkcija uzdos šos 6 jautājumus un par katru atbildi tiks piešķirts konkrēts punktu skaits.
    # Ja lietotājs nevēlas atbildēt uz jautājumiem, funkcija beidz darbību un lietotājam to ir jāpalaiž vēlreiz.
    while True:
        izvele = input(
            "\nPrieks, ka esi izvēlējies šo programmu!\nTev tiks uzdoti 6 jautājumi, izvēlies atbildi, kas tevi raksturo vistuvāk.\nVai vēlies turpināt?\n1. Jā\n2. Nē\n").strip()
        if izvele == "1":
            print("Tātad...")
            return True
        elif izvele == "2":
            programmas_izvade()
            exit() # izbeidz programmas darbību
        else:
            print("Nepareiza ievade, lūdzu izvēlies 1 vai 2.")

def jautajumi():  # Funkcija uzdod jautājumus un saskaita par katru jautājumu saņemtos punktus.
     # Kopējo punktu summa funkcija atgriež un tā tiek padota tālāk citai funkcijai.
    punkti = 0
    print("Sekojošie jautājumi izvērtēs to, vai par daudz laika pavadi ierīcēs un vai tās pārlieku ietekmē tavu dzīvesveidu.")
    
    # pirmais jautājums
    pirmais = input("1. Vai tavs darbs/nodarbošanās liek tev skatīties vairāk nekā 2 stundas ekrānā?\n1. Jā\n2. Nē: ")
    if pirmais == "1":
        punkti += 3
    elif pirmais == "2":
        punkti += 1
    else:
        print("Nepareiza ievade.")

    # otrais jautājums
    otrais = input("Cik daudz laika, tavuprāt, tu pavadi skatoties ekrānā ārpus darba vai nodarbošanās vajadzībām? \n1. Mazāk nekā 2 stundas\n2. Mazāk nekā 3 stundas\n3. Mazāk nekā 4 stundas\n4. Mazāk nekā 5 stundas\n5. Mazāk nekā 6 stundas\n6. Vairāk nekā 6 stundas\n7. Nezinu: ")
    if otrais == "1":
        punkti += 1
    elif otrais == "2":
        punkti += 1
    elif otrais == "3":
        punkti += 2
    elif otrais == "4":
        punkti += 2
    elif otrais == "5":
        punkti += 3
    elif otrais == "6":
        punkti += 4
    elif otrais == "7":
        punkti += 3
    else:
        print("Nepareiza ievade.")

    # trešais jautājums
    tresais = input("Kurš no tālāk dotajiem piemēriem vislabāk tevi raksturo?\n1. Mobilo telefonu izmantoju salīdzinoši reti. Izmantoju to saziņai ar tuviniekiem, draugiem, ik pa laikam palasu ziņas un reizi pa reizei uzmetu acis sociālajiem tīkliem.\n2. Katru rītu mostoties, telefons ir pirmais, ko paņemu rokā, lai pārbaudītu ziņas.\n3. Katru dienu rītu sāku nedaudz pasēdēt internetā, pirms došanās uz darbu.\n4. Mana dzīve bez telefona nav iedomājama, pavadītais laiks telefonā neapšaubāmi neatstāj pietiekami daudz laika citām dienas aktivitātēm un traucē man laicīgi iet gulēt: ")
    if tresais == "1":
        punkti += 1
    elif tresais == "2":
        punkti += 2
    elif tresais == "3":
        punkti += 3
    elif tresais == "4":
        punkti += 4
    else:
        print("Nepareiza ievade.")

    # ceturtais jautājums
    ceturtais = input("Cik bieži pēc skatīšanās ekrānos tev miglojas redze, sāp acis vai sāp galva?\n1. Nekad\n2. Reizi dažos mēnešos\n3. Dažas reizes mēnesī\n4. Dažas reizes nedēļā\n5. Praktiski katru dienu: ")
    if ceturtais == "1":
        punkti += 1
    elif ceturtais == "2":
        punkti += 1
    elif ceturtais == "3":
        punkti += 2
    elif ceturtais == "4":
        punkti += 4
    elif ceturtais == "5":
        punkti += 5
    else:
        print("Nepareiza ievade.")

    # piektais jautājums
    piektais = input("Cik bieži tu zaudē laika izjūtu lietojot viedierīces?\n1. Nekad\n2. Reti\n3. Dažreiz\n4. Bieži\n5. Praktiski vienmēr: ")
    if piektais == "1":
        punkti += 1
    elif piektais == "2":
        punkti += 1
    elif piektais == "3":
        punkti += 2
    elif piektais == "4":
        punkti += 4
    elif piektais == "5":
        punkti += 5
    else:
        print("Nepareiza ievade.")

    # sestais jautājums
    sestais = input("Cik bieži tu ēd skatoties telefonā?\n1. Nekad\n2. Retumis\n3. Bieži\n4. Vienmēr: ")
    if sestais == "1":
        punkti += 1
    elif sestais == "2":
        punkti += 1
    elif sestais == "3":
        punkti += 2
    elif sestais == "4":
        punkti += 4
    else:
        print("Nepareiza ievade.")

    print(f"Jūsu rezultāts ir: {punkti}")
    return punkti

def kalkulacija(punkti): # Šī funkcija balstoties uz saņemto punktu skaitu uzrādīs lietotājam piemērotu atbildi.
    iznakums = punkti
    if iznakums >= 16:
        teksts = "Tev ir nopietnas problēmas ar ekrānlaiku. Tev ir obligāti jāpārskata viedierīču lietošanas paradumus."
    elif 11 <= iznakums <= 15:
        teksts = "Tavs ekrānlaiks ir pārmērīgs. Ieteicams pārskatīt ierīču lietošanas ieradumus."
    elif 6 <= iznakums <= 10:
        teksts = "Tev ir iespējams vēl samazināt savu ekrānlaiku."
    else:
        teksts = "Nevainojams rezultāts."
    print(teksts)
    return teksts

def rakstit_datus(rakstamie_dati):
    try:
        # Ielādē esošos datus, ja datu nav, tad datus uztver kā tukšu sarakstu.
        try:
            with open("aplikacijas.json", "r", encoding="utf-8") as datne:
                esosie_dati = json.load(datne)
        except FileNotFoundError:
            esosie_dati = []

        esosie_dati.append(rakstamie_dati)
        
        with open("aplikacijas.json", "w", encoding="utf-8") as datne:
            json.dump(esosie_dati, datne, ensure_ascii=False, indent=4)
        print("\nDati ir saglabāti failā 'aplikacijas.json'.")
    except Exception as e:
        print(f"Radās kļūda saglabājot datus: {e}")

def skatit_datus():
    try:
        with open("aplikacijas.json", "r", encoding="utf-8") as datne:
            dati_programmas = json.load(datne)
            if dati_programmas:
                # Sakārto datus pēc datuma
                # Izmanto funkciju lambda, lai definētu atslēgu pēc kā jākārto (nez kāpēc dažos gadījumos nestrādā)
                dati_programmas.sort(key=lambda x: datetime.datetime.strptime(x.get('datums', '1900-01-01'), "%Y-%m-%d") if x.get('datums') else datetime.datetime.min)
                #Šeit saprotami tiek attēloti dati no JSON faila
                print("\n--- Saglabātie dati (Sakārtoti pēc datuma) ---")
                for i, ievade in enumerate(dati_programmas):
                    print(f"\n--- Ieraksts #{i+1} ---")
                    print(f"Datums: {ievade.get('datums', 'Nav norādīts')}")
                    
                    kopejais_ekranlaiks = ievade.get('kopējais_ekrānlaiks', {})
                    kopa_stundas = kopejais_ekranlaiks.get('stundas', 0)
                    kopa_minutes = kopejais_ekranlaiks.get('minūtes', 0)
                    print(f"Kopējais ekrānlaiks: {kopa_stundas} stundas un {kopa_minutes} minūtes")

                    aplikaciju_lietojums = ievade.get('aplikāciju_lietojums', [])
                    if aplikaciju_lietojums:
                        print("Aplikāciju lietojums:")
                        for aplikacija in aplikaciju_lietojums:
                            aplikacija_nosaukums = aplikacija.get('nosaukums', 'Nezināma aplikācija')
                            aplikacija_stundas = aplikacija.get('stundas', 0)
                            aplikacija_minutes = aplikacija.get('minūtes', 0)
                            print(f"  - {aplikacija_nosaukums}: {aplikacija_stundas} stundas un {kopa_minutes} minūtes")
                    else:
                        print("Nav reģistrētu datu.")

                    brīdinājums = ievade.get('brīdinājums', None) # Parmaina uz none
                    if brīdinājums: # Tiks izvadīts brīdinājums tikai ja ir brīdinājums
                        print(f"Brīdinājums: {brīdinājums}")
                    
                    print("-" * 30) # labakai redzamibai
            else:
                print("\nDatu fails ir tukšs.")
    except FileNotFoundError:
        print("\nNav atrasts datu fails 'aplikacijas.json'.")

def atkartots_lietotajs():
    while True:
        print("\nSveicināts atpakaļ. Ko vēlies darīt?")
        print("1. Izpildīt testu atkārtoti")
        print("2. Skatīt savus datus")
        print("3. Ievadīt jaunus datus par ekrānlaiku")
        print("4. Iziet no programmas") # Opcija beigt programmas darbību
        izvele = input("Izvēle: ").strip()
        if izvele == "1":
            jautajumi_res = jautajumi()
            kalkulacija(jautajumi_res)
        elif izvele == "2":
            skatit_datus()
        elif izvele == "3":
            ekranlaiks()
        elif izvele == "4": # Opcija beigt programmas darbību.
            programmas_izvade()
            break
        else:
            print("Ievades kļūda, lūdzu izvēlies no 1 līdz 4.")

def programmas_izvade(): # Ja lietotājs izvēlas izbeigt programmas darbību, tiks iedarbināta šī funkcija, kura no lietotāja atsveicināsies.
    print("\nPaldies, ka izmantoji šo programmu.\nLai Tev izdevusies diena!")

def ekranlaiks(): # ar šīs funkcijas palīdzību lietotājs ievada savus datus par ekrānlaiku.
    # ievadi lietotājs var apturēt ar komandu "beigt", kā  rezultātā visi dati tiks ierakstīti JSON failā.
    sodienas_datums_input = input("Vai izmantot šodienas datumu? (1. Jā / 2. Nē): ").strip().lower()
    
    datums = "" 
    if sodienas_datums_input == '2':
        while True:
            cits_datums = input("Ievadi datumu (GGGG-MM-DD): ").strip()
            try:
                datetime.datetime.strptime(cits_datums, "%Y-%m-%d")
                datums = cits_datums
                break
            except ValueError:
                print("Nederīgs datums/datuma formāts. Pamēģini vēlreiz.")
    else:
        datums = datetime.date.today().strftime("%Y-%m-%d")

    aplikacijas_lietojums = [] 
    kopejais_minutes = 0

    print("\nReģistrē aplikāciju nosaukumus un tajās patērēto laiku.")
    print("Lūdzu, neievadi aplikācijas, kuras izmanto darba vai mācību vajadzībām.")
    print("Lai beigtu ievadi, ieraksti 'beigt' kā aplikācijas nosaukumu.")

    while True:
        nosaukums = input("Aplikācijas nosaukums: ").strip()
        if nosaukums.lower() == 'beigt':
            break
        
        while True:
            print("Tagad atsevišķi būs jāievada aplikācijā pavadītais laiks stundās un pāri palikušajās minūtēs.")
            stundas_str = input(f"Cik stundas tu pavadīji {nosaukums}? (veselas stundas): ").strip()
            minutes_str = input("Cik minūtes palika pāri izņemot veselās stundas? (0–59): ").strip()
            try:
                stundas = int(stundas_str)
                minutes = int(minutes_str)
                if minutes < 0 or minutes >= 60 or stundas < 0:
                    raise ValueError
                break # Iziet no True, ja ievade nepareiza
            except ValueError:
                print("Nederīga ievade. Lūdzu ievadiet veselus skaitļus.")
        
        kopa_minutes_aplikacijas = stundas * 60 + minutes
        aplikacijas_lietojums.append({'nosaukums': nosaukums, 'stundas': stundas, 'minutes': minutes})
        kopejais_minutes += kopa_minutes_aplikacijas
        print(f"Pievienots: {nosaukums}, pavadītais laiks - {stundas} stundas {minutes} minūtes\n")
    
    kopa_stundas = kopejais_minutes // 60
    kopa_minutes = kopejais_minutes % 60
    
    bridinajums = None
    if kopejais_minutes > 240: # Izsaka bridinajumu, ja pavaditas vairak neka 4 stundas pie ekrana.
        bridinajums = "Tu šodien esi pavadījis vairāk nekā 4 stundas pie ekrāna. Samazini savu ekrānlaiku!."
        print(f"\n{bridinajums}")

    rezultats = {
        'datums': datums,
        'kopējais_ekrānlaiks': {'stundas': kopa_stundas, 'minūtes': kopa_minutes},
        'aplikāciju_lietojums': aplikacijas_lietojums,
        'brīdinājums': bridinajums
    } #sis bus tas, kas tiks ierakstits JSON

    print(f"\nKopējais ekrāna laiks: {kopa_stundas}h {kopa_minutes}min")
    rakstit_datus(rezultats)


if __name__ == '__main__':
    main()