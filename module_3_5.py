def get_multiplied_digits(number) :
    str_number = str(number)            # преобразуем число с строку
    if str_number.endswith("0") :       # проверяем условие, не оканчивается ли заданное число (number) 0
        str_number=str(number//10)      # для более общего примера
    else :
        str_number = str(number)

    first = int(str_number[0])          # получение 1-ой цифры number в числовом представлении
    if len(str_number) > 1 :            # если длина строки > 1 продолжаем рекурсивный процесс
        return first * get_multiplied_digits(int(str_number[1:]))
    else :                              # отсекая первую цифру, до конца числа
        return first                    # в этом случае возвращаем последнюю цифру
# Выводим на консоль результат с исходным кодом get_multiplied_digits(40203)
# get_multiplied_digits(40203) -> 4*get_multiplied_digits(203) -> 4*2*get_multiplied_digits(3) -> 4*2*3
result = get_multiplied_digits(40203)
print(result)
