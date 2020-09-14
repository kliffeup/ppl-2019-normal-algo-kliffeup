import is_transformation_final_function
import is_transformation_possible_function
import transformation_use_function

# Создаём два списка, первый - для считывания всех подстановок,
string_transformations = []
# второй  - для разделения каждой подстановки на "левую" и "правую" части и сохранении каждой по частям.
string_transformations_upd = []
# Открываем файл 'Input.txt', считываем из него входную строку и список подстановок.
with open("Input.txt") as input_data:
    input_string = input_data.readline()
    for temp_line in input_data:
        string_transformations.append(temp_line.strip())
# Разбиваем каждое преобразование на "левую" и "правую" части, разделитель - " # ".
for i in string_transformations:
    string_transformations_upd.append(i.split(' # '))
# В выходной файл 'Output.txt' записываем промежуточное предупреждение в случаях:
# зацикливания подстановок,
# неправильной работы моей программы.
with open("Output.txt", 'w') as output_data:
    output_data.write('  Если Вы видите это сообщение, то:\n')
    output_data.write('* либо симуляция работы нормального алгорифма зациклилась,\n')
    output_data.write('* либо моя программа дала сбой.')
# Объявляем переменную 'itt_number' в качестве счётчика применения подстановок
itt_number = 0
# Используем цикл while - пока не переберём все подстановки...
while itt_number < len(string_transformations_upd) - 1:
    # ...будем проверять, применима ли очередная подстановка...
    if is_transformation_possible_function.is_transformation_possible(input_string, string_transformations_upd,
                                                                      itt_number):
        # ... - если да, то за одно проверим, является ли она финальной...
        if is_transformation_final_function.is_transformation_final(string_transformations_upd, itt_number):
            # ... и если это так, то удалим символ "финальной подстановки" '.'...
            string_transformations_upd[itt_number][1] = string_transformations_upd[itt_number][1].replace('.', "", 1)
            # и применим её, после чего выйдем из цикла подстановок - ведь мы применили финальную.
            input_string = transformation_use_function.transformation_use(input_string, string_transformations_upd,
                                                                          itt_number)
            break
        # Если подстановка - не финальная, то применим её и обнулим счётчик цикла, дабы начать цикл подстановок заново.
        else:
            input_string = transformation_use_function.transformation_use(input_string, string_transformations_upd,
                                                                          itt_number)
            itt_number = 0
    # Если подстановка - не применима, то просто увеличим счетчик цикла подстановок, тем самым либо перейдя к
    # следующей подстановке, либо выйдя из цикла подстановок, если все они уже были последовательно применены.
    else:
        itt_number += 1
# Запишем получившуюся после серии подстановок строку в выходной файл 'Output.txt'
with open('Output.txt', 'w') as output_data:
    output_data.write(input_string)
