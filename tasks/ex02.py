def prime_factors(num):

    lst = []
    i = num
    while num!=1:
        for j in range(2,100):
            if not num%j:
                num = num/j
                lst.append(j)
    if lst[0]==i:
        lst.append(1)
    return lst

def product_numbers(num):
    lst = []
    product_of_numbers = 1
    for i in range(1, num+1):
        product_of_numbers *= i
        lst.append(product_of_numbers)
    return lst
