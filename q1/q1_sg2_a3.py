while True:
    try:
        birthyear=int(input("Enter your birth year: "))
        if birthyear<1900:
            print("Invalide Year. it should not be earlier than 1900")
        else:
            break
    except ValueError:
        print("Invalid input. Enter a valid year")

remeinder=birthyear%12
zodiacsign=["Monkey (猴 / Hóu)", "Rooster (鸡 / Jī)", "Dog (狗 / Gǒu)", "Pig (猪 / Zhū)", "Rat (鼠 / Shǔ)", "Ox (牛 / Niú)", "Tiger (虎 / Hǔ)", "Rabbit (兔 / Tù)", "Dragon (龙 / Lóng)", "Snake (蛇 / Shé)", "Horse (马 / Mǎ)", "Goat (羊 / Yáng)"]
calculatedzodiac=zodiac[remeinder]
print(f"Your Chinese Zodiac Sign is : {calculatedzodiac}")
