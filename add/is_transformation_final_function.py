def is_transformation_final(string_transformations_upd, itt_number):
    """ Функция проверки финальности подстановки:
    возвращает True, если данная подстановка финальная, False - в ином случае;

        Кортеж подстановок - список 'string_transformations_upd',
        Номер текущей подстановки - 'itt_number'.

        Если начало "правой части" подстановки - символ '.',
        что на языке "алгорифмов" означает финальность подстановки,
        то возращаем True и False - если имеем дело не с финальной подстановкой

    """
    return string_transformations_upd[itt_number][1].find('.') == 0
