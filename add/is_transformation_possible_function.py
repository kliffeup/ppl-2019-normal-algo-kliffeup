def is_transformation_possible(input_string, string_transformations_upd, itt_number):
    """ Функция проверки применимости подстановки:
    возвращает True, если данная подстановка применима, False - если нет;

        Строка, где проверяем подстановку, - 'input_string',
        Кортеж подстановок - список 'string_transformations_upd',
        Номер текущей подстановки - 'itt_number'.

        Проверяем, входит ли "левая часть" текущей подстановки в строку input_string
        ИЛИ
        является ли "левая часть" подстановки - "пустым" символом * - такую подстановку можно применить к любой строке.
        Если что-то из выше написанного выполняется, то функция возращает True,
        False - в противном случае

    """
    return string_transformations_upd[itt_number][0] in input_string or string_transformations_upd[itt_number][0] == '*'
