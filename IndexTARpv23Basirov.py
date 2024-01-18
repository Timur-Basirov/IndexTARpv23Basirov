print("Tere! Olen sinu uus sõber - Python!")
try:
    nimi=input("Mis on sinu nimi?")
    print(nimi+", oi kui ilus nimi!")
    index=(int(input(nimi+"! Kas leian Sinu keha indeksi? 0-ei, 1-jah => ")))
    if index==1:
        pikkus=float(input("Pikkus on: "))
        mass=int(input("Mass on: "))
        indeks=mass/((0.01*pikkus)**2)
        print(nimi+"! Sinu keha index on:", indeks)
        if indeks<16:
            answer="Tervisele ohtlik alakaal"
        elif indeks<=16:
            answer="Alakaal"
        elif indeks<=19:
            answer="Normaalkaal"
        elif indeks<=25:
            answer="Ülekaal"
        elif indeks<=30:
            answer="Rasvumine"
        elif indeks<=35:
            answer="Tugev rasvumine"
        elif indeks<=40:
            answer="Tervisele ohtlik rasvumine"
        print(answer)
    else:
        print("Kahju! See on väga kasulik info!")
        print()
        print("Kohtumiseni, "+nimi+"! Igavesti sinu, Python!")
except:
    print("Value error")