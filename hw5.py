#5. Запросите у пользователя значения выручки и издержек фирмы. 
# Определите, с каким финансовым результатом работает фирма 
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки). 
# Выведите соответствующее сообщение. 
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке). 
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.



def businessROI():
    try:
        viruchka = float(input('Ваша выручка:- '))
        zatraty = float(input('Ваши затраты:- '))

        pribul = viruchka - zatraty
        priRent = pribul
        rentabelnost = float(pribul / viruchka) * 100

        
        if pribul > 0:
            
                print('Вы в в плюсе и ваша прибыль составляет: ' + str(pribul) + '$')
                

                print('Рентабельность составляет= ' + str(round(rentabelnost, 2)) + '%')


                workers = int(input('Сколько у Вас работников?:-'))
                workerDohod = pribul / workers
                print('Прибыль на одного сотрудника = ' + str(round(workerDohod)) + '$')
            
            

        elif pribul < 0:
                print('Вы в минусе на:' + str(pribul) + '$')

    except ValueError:
                print("ошибочка, пробуем еще раз")
                return businessROI()
businessROI()