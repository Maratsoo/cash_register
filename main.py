#
# Kases aparāts
#
# 0.5pt pievienot jaunu preci - nosaukumu un cenu
#     0.5pt preces nosaukumam jābūt no 2 līdz 120 simboliem (jābūt validācijai, rādīt paziņojumu ja neder)
#     0.5pt preces cenai jābūt veselam skaitlim vai daļskaitlim ar vērtību no 0 līdz 9999 (jābūt validācijai, rādīt paziņojumu ja neder)
# 0.5pt dzēst preci pēc kārtas numura
# 0.5pt atcelt ievadu / iztukšot preču sarakstu
# 0.5pt piemērot atlaidi, ievadīt summu procentos
# 0.5pt samaksāt, ja iedota lielāka summa - izdrukāt atlikumu
# 0.5pt izdrukāt čeku uz ekrāna - preces nosaukumus un summas
#     0.5pt izdrukāt piemēroto atlaidi (ja ir)
#     0.5pt izdrukāt kopējo summu

# 1pt programmas stāvoklis tiek glabāts JSON faila un programmas sākumā tiek ielasīts un beigās saglabāts
# 1pt kodam ir jēdzīgi komentāri, pirms "if, for, while" koda konstrukcijam
# 1pt koda palaišanas brīdī nerādās kļūdas
# 1pt mainīgo un funkciju nosaukumi atspoguļo izmantošanas būtību, bez saisinājumiem, rakstīti snake_case stilā
# 1pt izmaiņas saglabātas versiju vadības sistēmā Git, savs fork
#
# Dokumentācija
# Mainīgie - https://www.w3schools.com/python/python_variables.asp
# Operācijas ar mainīgiem - https://www.w3schools.com/python/python_operators.asp
# Mainīgo drukāšana - https://www.w3schools.com/python/python_variables_output.asp
# Nosacījumi, zarošana, if ... else - https://www.w3schools.com/python/python_conditions.asp
# For cikls - https://www.w3schools.com/python/python_for_loops.asp
# Github Fork (repozitorija kopija) - https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo
# Saraksti - https://www.w3schools.com/python/python_lists.asp
# Vārdnīcas - https://www.w3schools.com/python/python_dictionaries.asp
# Klonēt repozitoriju - hhttps://code.visualstudio.com/docs/sourcecontrol/intro-to-git
#


import json

produkts = []

with open('check.json') as openfile:
    produkts = json.load(openfile)


while True:
    print("Kases aparāts")
    print("---------------------")
    print("1. Pievienot Produktu")
    print("2. Dzēst Prece")
    print("3. Noņemiet pirmo elementu sarakstā")
    print("4. Check")
    print("5 Print visas produkrus ar summu")
    print("6. Exit")
    choice = input("Enter your choice (1-6)")

    if choice == '1':
        produkta = input("pievienot produktu nosaukums: ")
        produkta_cena = input("pievienot produktu cenu (1-9999) ")

        if len(produkta) < 2 or len (produkta) > 120:
            print ("Nosaukums neder")
        pass
        produkta_cena = float(produkta_cena)
        if produkta_cena < 0 or produkta_cena > 9999:
            print ("cena neder")
        pass
        produkta_cena = round (produkta_cena,2)

        produkts.append({"nosaukums": produkta,"cena":produkta_cena})
        print ("Produkts pievienots")
    pass

    if choice == '2':
        dzest = input("Ievadi prece: ")
        produkts.pop(dzest)
        print("Produkts noņemts")
    pass

    if choice == '3':
        Dzēst_visi =  input("Vai tiešām vēlaties dzēst sarakstu?(Jā/Ne)")
        if Dzēst_visi == "Jā":
            produkts.pop(0)
            print("Sarakts dzēst")
        if Dzēst_visi == "Ne":
            print("Saraksts nav dzēsts")
    pass
    if choice == '4':
        print("-------Check-------")
        total_sum = 0
        for produkts in produkts:
            nosaukums = produkts["nosaukums"]
            cena = produkts ["cena"]
            print(f"{nosaukums}: {"cena"}")
            total_sum += cena

            atlaides_proc = 10
            aatlaides_sum = total_sum*(atlaides_proc/100)
            print (f"atlaide summa:{aatlaides_sum}")
            kopsumma = total_sum-aatlaides_sum
            print (f"Summa:{kopsumma}")
    pass

    if choice == "5":
        print(produkts)
    if choice == '6':
        print("Exiting")
        break

        