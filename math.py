# Данная программа предназначена для ознакомления
# с синтаксисом и различными простыми конструкциями языка Python.
# В качестве примера реализован алгоритм расчёта средней
# оценки по выбранному предмету для каждого из учеников класса.

import math

# Функция для расчёта средней оценки
def calcAverageGrade(grades):
    totalGrade = 0
    for i in range(len(grades)):
        totalGrade += grades[i]
    return math.ceil(totalGrade / len(grades))

# Список предеметов
discList = 'Математика', 'Русский язык', 'Литературное чтение'
# Список учеников
pupilList = 'Иванов', 'Петров', 'Сидоров'
# Список оценок для учеников
pupilGrades = [None] * len(pupilList)

print("Добро пожаловать!")
print("-----------------")

print("Список предметов:")
for i in range(len(discList)):
    print(str(i+1) + ". " + discList[i])
print("-----------------")

# Выбираем предмет
sel = input("Введите номер предмета и нажмите Enter (Ввод):")
while True:
    try:
        num=int(sel)
        if num >= 1 and num <= len(discList):
            break
    except:
        print("Неверный ввод.")

disc = discList[int(sel) - 1]
print("Вы выбрали предмет " + disc)

# Выбираем ученика или производим расчёт
while True:
    print("Список учеников:")
    for i in range(len(pupilList)):
        print(str(i+1) + ". " + pupilList[i])
    print("-----------------")
    sel = input("Введите номер ученика (или введите букву 'c' для произведения расчёта) и нажмите Enter (Ввод):")
    while True:
        if (sel == 'c'):
            break
        else:
            try:
                num=int(sel)
                if num >= 1 and num <= len(discList):
                    break
            except:
                print("Неверный ввод.")

    if sel != 'c':
        pupilIndex = int(sel) - 1
        print("Вы выбрали ученика " + pupilList[pupilIndex])

        while True:
            sel = input("Введите оценки (от 1 до 10) в виде строки с запятой в качестве разделителя (например 10,9,10,8) и нажмите Enter (Ввод):")
            if len(sel) > 0:
                gradeTokens = sel.split(',')
                grades = list()
                for i in range(len(gradeTokens)):
                    try:
                        grade = int(gradeTokens[i])
                        if grade >= 1 and grade <= 10:
                            grades.append(grade)
                    except:
                        pass
                if len(gradeTokens) == len(grades):
                    print("Вы ввели следующие оценки: " + sel)
                    pupilGrades[pupilIndex] = grades
                    break
            
            print("Неверный ввод.")
    else:
        # Производим расчёт и оканчиваем программу
        print("Средний балл по предмету " + disc + ':')
        for i in range(len(pupilGrades)):
            if pupilGrades[i] is not None:
                print(pupilList[i] + ": " + str(calcAverageGrade(pupilGrades[i])))
        print("Расчёт окончен. Всего хорошего!")
        break
        