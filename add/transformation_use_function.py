def transformation_use(input_string, string_transformations_upd, itt_number):
    """ Функция, применяющая подстановку:
    возвращает изменённую после подстановки строку;

        Строка, в которой выполняем подстановку, - 'input_string',
        Кортеж подстановок - список 'string_transformations_upd',
        Номер текущей подстановки - 'itt_number'.

        Если заменяемая подстрока и её замена - не пустые символы,
        то единократно выполняем замену первого на второе;
        Если "левая часть" подстановки - пустой символ,
        то добавляем в начало строки "правую часть" подстановки;
        Если "правая часть" подстановки - пустой символ,
        то исключаем из строки первое вхождение "левой части" подстановки в неё;
        Если обе части подстановки - пустые символы,
        то в исходной строке ничего не меняем;
        И возвращаем изменённую строку.

    """
    if string_transformations_upd[itt_number][0] != '*' and string_transformations_upd[itt_number][1] != '*':
        input_string = input_string.replace(string_transformations_upd[itt_number][0],
                                            string_transformations_upd[itt_number][1], 1)
    elif string_transformations_upd[itt_number][0] == '*' and string_transformations_upd[itt_number][1] != '*':
        input_string = string_transformations_upd[itt_number][1] + input_string
    elif string_transformations_upd[itt_number][0] != '*' and string_transformations_upd[itt_number][1] == '*':
        input_string = input_string.replace(string_transformations_upd[itt_number][0], "", 1)
    else:
        input_string = input_string
    return input_string
