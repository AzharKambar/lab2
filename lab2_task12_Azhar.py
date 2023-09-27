try:
        #Вводим возраст
    age = int(input())
    #Задаем условие для определения к какой возрастной группе относится
    if 14 <= age <= 24:
        print('Youth')
        elif 25 <= age <=59:
            print('Maturity')
            elif age >= 60:
                print('Old age')
        else:
    print('Childhood')
except ValueError:
    print('Input is not correct')
