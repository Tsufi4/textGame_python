jmeno = input("Zadej jméno: ")

print("Vítej v dobrodružství plném překážek a pastí!")
print(f"Jsi {jmeno}, dobrodruh v tomto temném podzemí, a tvým cílem je z něho utéct.")

while True:
    print("\nJeskyně")
    print("Ocitl jsi se v temné jeskyni.")
    print("Vidíš 2 otvory, z pravého slyšíš zvuky a z levého vidíš světlo. Kam se vydáš?")

    choice1 = input("Zadej 'levý' nebo 'pravý': ").lower().strip()

    if choice1 == "levý":
        print("\nVydal ses doleva a našel jsi místnost osvícenou pochodněmi.")
        print("V místnosti s 3 dveřmi jsi našel 3 truhly, ale můžeš otevřít jen jednu. Kterou z nich otevřeš: 'červenou,' 'modrou,' nebo 'zelenou'?")
        while True:
            choice2 = input("Zadej 'červenou' 'modrou' nebo 'zelenou': ").lower().strip()

            if choice2 == "červenou":
                print("\nV truhle byla past, která tě zabila.")
                break
            elif choice2 == "modrou":
                print("\nNašel jsi meč v truhle.")
                print("Po získání meče jsi náhle slyšel zvuky a viděl, že se jedna z dveří otevírá a na tebe vybíhají monstra.")
                print("Máš tři možnosti: buď se pokusit bojovat mečem, který jsi právě získal, nebo se pokusit utéct jednou ze dvou zbývajících dveří.")
                
                while True:
                    choice3 = input("Zadej 'boj' nebo 'dveře1' nebo 'dveře2': ").lower().strip()
                    if choice3 == "boj":
                        print("\nCo tě to napadlo! Umíš snad bojovat s mečem? Hned první monstrum tě zabilo.")
                        break
                    elif choice3 == "dveře1":
                        print("Úspěšně jsi zvládl utéct před monstrem za dveřmi, avšak za dveřmi je propast, ve které umíráš.")
                        break
                    elif choice3 == "dveře2":
                        print("\nZvládl jsi uniknout monstrům skrz druhé dveře. Za nimi tě čeká zvláštní postava.")
                        print("Postava ti nabídla dvě další možnosti: můžeš se vydat hlouběji do jeskyně, nebo se vrátit ven. Co uděláš?")
                        
                        while True:
                            choice4 = input("Zadej 'hlouběji' nebo 'ven': ").lower().strip()
                            if choice4 == "hlouběji":
                                print("\nPokračoval jsi hlouběji do jeskyně.")
                                while True:
                                    print("Pokračuješ hlouběji do jeskyně a narazíš na rozbitý most. Co uděláš?")
                                    choice5 = input("Zadej 'přejít' nebo 'vrátit se': ").lower().strip()

                                    if choice5 == "přejít":
                                        print("\nPřešel jsi most a pokračuješ dál do místnosti v tajemném podzemí.")
                                        print("Našel jsi další dveře. Prozkoumáš místnost nebo otevřeš dveře?")
                                        while True:
                                            choice6 = input("Zadej 'otevřít' nebo 'prozkoumat': ").lower().strip()
                                            if choice6 == "otevřít":
                                                print("Otevřel jsi dveře a narazil na skrytou komnatu s pokladem!")
                                                print("Pak jsi uslyšel, jak se za tebou dveře zavřely.")
                                                print("Gratulujeme, našel jsi tajemný poklad a dokončil dobrodružství tím že jsi UMŘEL!!!!. (Umřel jsi hlady, protože tvým cílem bylo dostat se z jeskyně, ne najít poklad.)")
                                                break
                                            elif choice6 == "prozkoumat":
                                                print("Rozhodl jsi se prozkoumat místnost a narazil jsi na staré artefakty, a jeden z nich ti umožnil se teleportovat na vrchol. Gratulujeme!")
                                                break
                                            else:
                                                print("Neplatný vstup. Zadej 'otevřít' nebo 'prozkoumat'.")
                                        break
                                    elif choice5 == "vrátit se":
                                        print("\nRozhodl jsi se vrátit zpět, kde tě znovu čeká zvláštní postava.")
                                        print("Postava tě tiše čeká, co jí řekneš.")
                                        print("Na výběr máš:\na: Říct pravdu o tom, že ses bál.\nb: Říct, že jsi narazil na slepou uličku.\nc: Poprosit ji o radu jak se odtud dostat.")
                                        while True:
                                            choice7 = input("Zadej 'a' nebo 'b' nebo 'c': ").lower().strip()
                                            if choice7 == "a":
                                                print("Otevřel jsi dveře a narazil na skrytou komnatu s pokladem!")
                                                print("Naštval jsi postavu: Umíráš.")
                                                break
                                            elif choice7 == "b":
                                                print("Naštval jsi postavu: Umíráš.")
                                                break
                                            elif choice7 == "c":
                                                print("Naštval jsi postavu: Umíráš.")
                                                break
                                            else:
                                                print("Neplatný vstup. Zadej 'a' nebo 'b' nebo 'c'.")
                                        break
                                    else:
                                        print("Neplatný vstup. Zadej 'přejít' nebo 'vrátit se'.")
                                break
                            elif choice4 == "ven":
                                print("\nPostava tě zavraždila s těmito slovy: 'Slabí tu nemají co dělat.'")
                            else:
                                print("\nNeplatný vstup. Zadej 'hlouběji' nebo 'ven'.")
                        break
                    else:
                        print("\nNeplatný vstup. Zadej 'hlouběji' nebo 'ven'.")
                
                break
            elif choice2 == "zelenou":
                print("\nZ truhly vylezl had, který tě zabil.")
                break
            else:
                print("\nNeplatný vstup. Zadej 'červenou,' 'modrou,' nebo 'zelenou'.")
        
    elif choice1 == "pravý":
        print("\nVešel jsi do místnosti plné monster. Snědli tě zaživa.")
    
    else:
        print("\nNeplatný vstup. Zadej 'levý' nebo 'pravý'.")
        continue  

    play_again = input("Chceš hrát znovu (ano/ne)? ").lower().strip()
    if play_again != "ano":
        break

print("\nZávěr: Konec")
print("Tvé dobrodružství skončilo. Možná jsi nepřežil, ale měl jsi vzrušující cestu!")

print("Děkujeme za hraní únikového dobrodružství!")
