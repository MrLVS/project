def card_check():
        # Запрашиваем номер карты
        card_number = list(input("Введите номер карты: "))
        # Вычитаем единицу, т.к. последняя цифа в номере контрольная и ее не учитываем.
        len_num = len(card_number) - 1
        # Проверяем условие, четное количество или нет
        if len_num % 2 == 0:
            # Генерируем список четных чисел из номера карты с определенными условиями
            even_num = [int(v) * 2 - 9 if int(v) * 2 > 9 else int(v)*2
                for i, v in enumerate(card_number,1) if i % 2 == 0]
                #Генерируем список нечетных чисел из номера карты
            odd_num = [int(v) for i,v in enumerate(card_number,1) if i % 2 == 1]
            # Получаем сумму значений списков
            sum_nums = sum(even_num) + sum(odd_num)
             # Проверяем кратность суммы 10
            if sum_nums % 10 == 0:
                print("Номер верный. Карта принята.")
            else:
                print("Номер не верный. Попробуйте еще раз.")
        elif len_num % 2 == 1:
                odd_num = [int(v) * 2 - 9 if int(v) * 2 > 9 else int(v)*2
                for i, v in enumerate(card_number,1) if i % 2 == 1]
                even_num = [int(v) for i,v in enumerate(card_number,1) if i % 2 == 0]
                sum_nums = sum(even_num) + sum(odd_num)
                if sum_nums % 10 == 0:
                    print("Номер верный. Карта принята.")
                else:
                    print("Номер не верный. Попробуйте еще раз.")


card_check()
