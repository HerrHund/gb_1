#1. Поработайте с переменными, создайте несколько, 
# выведите на экран, запросите у пользователя 
# несколько чисел и строк и сохраните в переменные, выведите на экран.

userName = input('Введите Ваше имя:')

userAge = input('Введите Ваш возраст:')

userLocation = input('Введите Ваш адрес проживания:')

userProfile = {'Имя': userName,
               'Возраст': userAge,
               'Адрес': userLocation}


print('New User ' + ' \n' + userProfile['Имя'] + ' \n' + userProfile['Возраст'] + ' \n' + userProfile['Адрес'])