#Список правильных ответов
year_born_Gorky         =   '1868'
year_born_Dostoevsky = '1821'
year_born_Kopernik = '1473'
year_born_Putin = '1952'
year_born_Gagarin = '1934'

#Викторина

while True:
    num_cor_answers = 0
    num_mist = 0
    per_cor_answers = 0.0
    per_mist = 0.0
    answer_year_born_Gorky = input('Год рождения М. Горького?\n')
    answer_year_born_Dostoevsky = input('Год рождения Ф.М. Достоевского?\n')
    answer_year_born_Kopernik = input('Год рождения Н. Коперника?\n')
    answer_year_born_Putin = input('Год рождения В.В. Путина?\n')
    answer_year_born_Gagarin = input('Год рождения Ю.А. Гагарина?\n')
    #Правильный ответ 1868
    if answer_year_born_Gorky == year_born_Gorky:
        num_cor_answers += 1
    # Правильный ответ 1821
    if answer_year_born_Dostoevsky == year_born_Dostoevsky:
        num_cor_answers += 1
     # Правильный ответ 1473
    if answer_year_born_Kopernik == year_born_Kopernik:
        num_cor_answers += 1
# Правильный ответ 1952
    if answer_year_born_Putin == year_born_Putin:
        num_cor_answers += 1
    # Правильный ответ 1934
    if answer_year_born_Gagarin == year_born_Gagarin:
        num_cor_answers += 1

#Подсчитываем статистику по викторине
    num_mist = 5 - num_cor_answers
    per_cor_answers = num_cor_answers * 100.0 / 5.0
    per_mist = 100 - per_cor_answers

    #Выводим результат
    print('РЕЗУЛЬТАТ:')
    print('Количество правильных ответов:   ', num_cor_answers)
    print('Количество неправильных ответов: ', num_mist)
    print('Процент правильных ответов:      ', per_cor_answers,'%')
    print('Процент неправильных ответов:    ', per_mist, '%')
    #Проверяем хочет ли пользователь сыграть еще раз
    repeat_victory = input('\nНачать игру сначала?(да/нет)\n')
    if repeat_victory == 'нет':
        break
