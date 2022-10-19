
import student_info as si
import cabinet_info as cab


def option():
    print("\nВас приветствует программа мониторинга процессов обучения студентов!")
    ch = int(input('Введите что хотите сделать: \n \
    1: Поиск ID студента по фамилии \n \
    2: Посмотреть класс  и место которое занимает  студент \n \
    3: Выход\n \
    Ваш выбор: '))

    if ch == 1:
        Surn = str(input("Введите фамилию ученика: "))
        if Surn in si.stud_card['Фамилия']:
            index = si.stud_card['Фамилия'].index(Surn)
        print(f"ID:{si.stud_card['ID'][index]}\n{si.stud_card['Имя'][index]} {si.stud_card['Фамилия'][index]}, Дата рождения: {si.stud_card['Дата рождения'][index]}, Успеваемость: {si.stud_card['Успеваемость'][index]}")
        print('\nХотите запросить данные о другом ученике? Y или N: ')
        num = input()
        if num == 'Y' or 'y' or 'У' or 'у':
            option()
        exit()

    elif ch == 2:
        c = input('Введите ID студента для вывода по классам: ')
        if c in cab.class_card['ID']:
            index = cab.class_card['ID'].index(c)
            print(f" {si.stud_card['Фамилия'][index]} cидит в классе - {cab.class_card['Предмет'][index]}, за партой номер - {cab.class_card['Номер парты'][index]}, это {cab.class_card['Ряд'][index]}, парта - {cab.class_card['Вид парты'][index]}, Имя: {si.stud_card['Имя'][index]}, успеваемасть у студента: {si.stud_card['Успеваемость'][index]}")
            print('\nХотите запросить данные о другом ученике? Y или N: ')
            num = input()
            if num == 'Y' or 'y' or 'У' or 'у':
                option()
            exit()
    else:
        print('До встречи в следующий раз')
    exit()


option()
