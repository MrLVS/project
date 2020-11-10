#Программа для нутрициологов.
from textwrap import dedent

def activity_coefficient(activity):
    if activity == "1":
        acoeff = 1.2
    elif activity == "2":
        acoeff = 1.38
    elif activity == "3":
        acoeff = 1.46
    elif activity == "4":
        acoeff = 1.55
    elif activity == "5":
        acoeff = 1.64
    elif activity == "6":
        acoeff = 1.73
    elif activity == "7":
        acoeff = 1.9
    else:
        print("Введите значение от 1 до 7.")
    print("Коэффициент активности: ", acoeff)
    return acoeff


def greeting():
    print(dedent("""
    Для начала расчетов укажите, вы мужчина или женщина?
    1 - мужчина, 2 - женщина."""))
    choice = int(input(">>> "))
    if choice == 1:
        man()
    else:
        woman()

def BMI(weight, height):

    BMI = weight / (height / 100) ** 2
    BMI = round(BMI, 2)

    if BMI <= 18.5:
        conclusion = "недостатком веса."
    elif 18.5 < BMI <= 25:
        conclusion = "нормальным весом."
    elif 25 < BMI < 30:
        conclusion = "избыточный вес. Предожирение."
    elif 30 < BMI <= 35:
        conclusion = "ожирением 1 степени."
    else:
        conclusion = "ожирением 2 и выше степени."

    print("Индекс массы тела = ", BMI, "Человек с", conclusion)
    return BMI

def perfect_weight(height):
    if height <= 165:
        perfect_weight = height - 100
    elif 165 < height <= 175:
        perfect_weight = height - 105
    else:
        perfect_weight = height - 110
    print("Идеальный вес: ", perfect_weight, "кг.")
    return perfect_weight

def corrected_body_mass(perfectweight, weight):
    m = perfectweight + 0.25 * (weight - perfectweight)
    return m

def man():
    # Вводим параметры
    height = int(input("Введите свой рост в см: "))
    weight = float(input("Введите свой вес в кг: "))
    age = int(input("Введите свой возраст: "))
    activity = input(dedent("""
    Выберете вариант физической активности, которая соответствует
    вашему образу жизни:
    1 - \"Физическая нагрузка отсутствует или минимальная.\"
    2 - \"Тренировки средней тяжести 3 раза в неделю.\"
    3 - \"Тренировки средней тяжести 5 раз в неделю.\"
    4 - \"Интенсивные тренировки 5 раз в неделю.\"
    5 - \"Тренировки каждый день.\"
    6 - \"Интенсивные тренировки каждый день или по 2 раза в день.\"
    7 - \"Ежедневная нагрузка + физическая работа.\"\n
    """))


    # Получаем значения с функций
    pweight = perfect_weight(height) # идеальный веса
    mass = corrected_body_mass(pweight, weight) # скорректированная масса тела
    bmi = BMI(weight,height) # индекс массы тела
    activ_coeff = activity_coefficient(activity) # коэффициент активности

    # Считаем базовые калории в зависимости от индекса массы тела
    if bmi <= 30:
        calories = 66.5 + 13.75 * weight + 5 * height - 6.78 * age
        print("Базовые калории: ", round(calories,2))
    else:
        calories = 66.5 + 13.75 * mass + 5 * height - 6.78 * age
        print("Базовые калории: ", round(calories,2))

    day_calories = round(calories * activ_coeff, 2)
    print(f"Калории для поддержания массы тела: {day_calories} калл.")

    x = input(dedent("""
    Вы планируете худеть или набирать массу?
    1 - "Худеть."
    2 - "Набирать массу."
    """))
    if x == "1":
        new_day_calories = round(day_calories - (day_calories * 0.2), 2) # Худеем
        if activ_coeff == 1.2:
            protein_gramm = 1.2 * pweight
        elif activ_coeff == 1.38:
            protein_gramm = 1.5 * pweight
        else:
            protein_gramm = 1.8 * pweight

        protein_kall = protein_gramm * 4

        if activ_coeff == 1.2:
            fat_gramm = 0.8 * pweight
        else:
            fat_gramm = 1 * pweight
        fat_kall = fat_gramm * 9
        carbohydrates_kall = new_day_calories - (protein_kall + fat_kall)
        carbohydrates_gram = round(carbohydrates_kall / 4, 1)
        print(dedent(f"""
        Суточная норма БЖУ:
        Белки: {protein_gramm} г,
        Жиры: {fat_gramm} г,
        Углеводы {carbohydrates_gram} г"""))
        print(f"Суточная норма ккал для похудения: {new_day_calories} калл")

    elif x == "2":
        new_day_calories = round(day_calories - (day_calories * 0.2), 2) # НАбор веса
        if activ_coeff == 1.2:
            protein_gramm = 1.2 * pweight
        elif activ_coeff == 1.38:
            protein_gramm = 1.5 * pweight
        else:
            protein_gramm = 1.8 * pweight

        protein_kall = protein_gramm * 4

        fat_gramm = 1 * pweight
        fat_kall = fat_gramm * 9
        carbohydrates_kall = new_day_calories - (protein_kall + fat_kall)
        carbohydrates_gram = round(carbohydrates_kall / 4, 1)
        print(dedent(f"""
        Суточная норма БЖУ:
        Белки: {protein_gramm} г,
        Жиры: {fat_gramm} г,
        Углеводы {carbohydrates_gram} г"""))
        print(f"Суточная норма ккал для похудения: {new_day_calories} калл")











def woman():
    height = int(input("Введите свой рост в см: "))
    weight = float(input("Введите свой вес в кг: "))
    age = int(input("Введите свой возраст: "))
    activity = input(dedent("""
    Выберете вариант физической активности, которая соответствует
    вашему образу жизни:
    1 - \"Физическая нагрузка отсутствует или минимальная.\"
    2 - \"Тренировки средней тяжести 3 раза в неделю.\"
    3 - \"Тренировки средней тяжести 5 раз в неделю.\"
    4 - \"Интенсивные тренировки 5 раз в неделю.\"
    5 - \"Тренировки каждый день.\"
    6 - \"Интенсивные тренировки каждый день или по 2 раза в день.\"
    7 - \"Ежедневная нагрузка + физическая работа.\"\n
    """))

    pweight = perfect_weight(height) # идеальный веса
    mass = corrected_body_mass(pweight, weight) # скорректированная масса тела
    bmi = BMI(weight,height) # индекс массы тела
    activ_coeff = activity_coefficient(activity) # коэффициент активности


    if bmi <= 30:
        calories = 665 + 9.56 * weight + 1.85 * height - 4.68 * age
        print("Базовые калории: ", round(calories,2))
    else:
        calories = 665 + 9.56 * mass + 1.85 * height - 4.68 * age
        print("Базовые калории: ", round(calories,2))

    day_calories = round(calories * activ_coeff, 2)
    print(f"Калории для поддержания массы тела: {day_calories} калл.")

    x = input(dedent("""
    Вы планируете худеть или набирать массу?
    1 - "Худеть."
    2 - "Набирать массу."
    """))

    if x == "1":
        new_day_calories = round(day_calories - (day_calories * 0.2), 2) # Худеем
        if activ_coeff == 1.2:
            protein_gramm = 1.2 * pweight
        elif activ_coeff == 1.38:
            protein_gramm = 1.2 * pweight
        else:
            protein_gramm = 1.5 * pweight

        protein_kall = protein_gramm * 4

        if activ_coeff == 1.2:
            fat_gramm = 0.8 * pweight
        else:
            fat_gramm = 1 * pweight

        fat_kall = fat_gramm * 9
        carbohydrates_kall = new_day_calories - (protein_kall + fat_kall)
        carbohydrates_gram = round(carbohydrates_kall / 4, 1)
        print(dedent(f"""
        Суточная норма БЖУ:
        Белки: {protein_gramm} г,
        Жиры: {fat_gramm} г,
        Углеводы {carbohydrates_gram} г"""))
        print(f"Суточная норма ккал для похудения: {new_day_calories} калл")

    elif x == "2":
        new_day_calories = round(day_calories + (day_calories * 0.2), 2) # Набор массы
        if activ_coeff == 1.2:
            protein_gramm = 1.2 * pweight
        else:
            protein_gramm = 1.5 * pweight

        protein_kall = protein_gramm * 4
        fat_gramm = 1 * pweight
        fat_kall = fat_gramm * 9
        carbohydrates_kall = new_day_calories - (protein_kall + fat_kall)
        carbohydrates_gram = round(carbohydrates_kall / 4, 1)
        print(dedent(f"""
        Суточная норма БЖУ:
        Белки: {protein_gramm} г,
        Жиры: {fat_gramm} г,
        Углеводы {carbohydrates_gram} г"""))


        print(f"Суточная норма ккал для набора веса: {new_day_calories} калл")







greeting()
