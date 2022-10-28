def delet_symbol(line):
    words = line.split(' ')
    new_words = []
    for word in words:
        if 'а' not in word:
            if 'б' not in word:
                if 'в' not in word:
                    new_words.append(word)
    return ' '.join(new_words)


def sum_num(number):

    amouth = 0
    for i in str(number):
        if i != "." and i != '-':
            amouth += int(i)
    return amouth


def inject(num):
    while True:
        try:
            num = int(num)
            return True
        except ValueError:
            if num.isalpha():
                return "Введены буквы"
            else:
                return "Введены непонятные символы"


def sum_odd(lissst):
    lst = lissst
    summer = 0
    for i in range(1,len(lst),2):
        summer+=lst[i]
    return summer


def product_numbers(num):
    lst = []
    product_of_numbers = 1
    for i in range(1, num+1):
        product_of_numbers *= i
        lst.append(product_of_numbers)
    return lst
