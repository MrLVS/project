list = ["Камень", "Ножницы", "Бумага"]
print("Давайте поиграем в \"Камень, ножницы, бумагу\" с компьютером!")
time.sleep(2)
comp_choice = random.randint(1,3)
if comp_choice == 1:
    line = list[0]
elif comp_choice == 2:
    line = list[1]
elif comp_choice == 3:
    line = list[2]

print(dedent("""Считаем до трех и выбираем:
                1 - Камень;
                2 - Ножницы;
                3 - Бумагу; """))

time.sleep(1)
print("1")
time.sleep(1.5)
print("2")
time.sleep(1)
print("3")
p_choice = int(input("Выберите вариант и введите номер: \n"))

if p_choice == 1:
    print("Вы выбрали: ", list[0])
    print("Компьютер выбрал: ", line)
    if comp_choice == 1:
        print("Ничья!")
    elif comp_choice == 2:
        print("Вы выиграли!Поздравляю!")
    else:
        print("Компьютер выиграл! Роботы победили!")
elif p_choice == 2:
    print("Вы выбрали: ", list[1])
    print("Компьютер выбрал: ", line)
    if comp_choice == 1:
        print("Компьютер выиграл! Роботы победили!")
    elif comp_choice == 2:
        print("Ничья!")
    else:
        print("Вы выиграли!Поздравляю!")
elif p_choice == 3:
    print("Вы выбрали: ", list[2])
    print("Компьютер выбрал: ", line)
    if comp_choice == 1:
        print("Вы выиграли!Поздравляю!")
    elif comp_choice == 2:
        print("Компьютер выиграл! Роботы победили!")
    else:
        print("Ничья!")
