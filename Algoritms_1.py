'''КВАДРАТИЧНЫЕ СОРТИРОВКИ О(N**2)'''

def insert_sort(A):
    '''Сортировка вставками (insert sort)'''
    N = len(A)
    for top in range(1, N):
        k = top
        while k > 0 and A[k-1] > A[k]:
            A[k], A[k-1] = A[k-1], A[k]
            k -= 1
 
def choise_sort(A):
    '''Сортировка выбором (choise sort)'''
    N = len(A)
    for position in range(0, N-1):
        for k in range(position+1, N):
            if A[k] < A[position]:
                A[k], A[position] = A[position], A[k]
    
def bubble_sort(A):
    '''Сортировка пузырьком (bubble sort)'''
    N = len(A)
    for count in range(1, N):
        for k in range(0, N-count):
            if A[k] > A[k+1]:
                A[k], A[k+1] = A[k+1], A[k]

def count_sort(A):
    '''Сортировка подсчетом (count_sort)'''
    number = [0] * len(A)*max(A)
    for i in A:
        number[i] += 1

    A.clear()
    for index, num in enumerate(number):
        if num == 1:
            A.append(index)
        elif num > 0:
            for j in range(num):
                A.append(index)

###########################################################################################################

'''РЕКУРСИВНЫЕ СОРТИРОВКИ'''

def quick_sort(A):
    '''Сортировка Тони Хойара или быстрая сортировка (quick_sort)'''
    if len(A) <= 1:
        return
    barrier_el = A[0]
    low_num = []
    middle_num = []
    big_num = []
    for x in A:
        if x < barrier_el:
            low_num.append(x)
        elif x == barrier_el:
            middle_num.append(x)
        else:
            big_num.append(x)
    quick_sort(low_num)
    quick_sort(big_num)
    k = 0
    for x in low_num+middle_num+big_num:
        A[k] = x; k+=1




def merge_sort(A):
    '''Сортировка слиянием (merge_sort)'''
    def merge(A,B):
        new_list = [0]*(len(A) + len(B))
        i = k = n= 0
        while i < len(A) and k < len(B):
            if A[i] <= B[k]:
                new_list[n] = A[i]; i+=1; n+=1 
            else:
                new_list[n] = B[k]; k+=1; n+=1

        while i < len(A):
            new_list[n] = A[i]; i+=1; n+=1
        while k < len(B):
            new_list[n] = B[k]; k+=1; n+=1
        return new_list
    
    if len(A) <= 1:
        return
    
    middle = len(A) // 2
    left_list = [A[i] for i in range(0, middle)]
    right_list = [A[i] for i in range(middle, len(A))]

    left = merge_sort(left_list)
    right = merge_sort(right_list)
    C = merge(left_list, right_list)

    for i in range(len(A)):
        A[i] = C[i]

def test_sort(sort_algorithm):
    print(f"Тестируем: {sort_algorithm.__doc__}")

    print("testcase #1 ", end="")
    A = [4, 2, 1, 5, 3]
    A_sorted = [1, 2, 3, 4, 5]
    sort_algorithm(A)
    print("OK" if A==A_sorted else "Fail")

    print("testcase #2 ", end="")
    A = [4, 2, 1, 5, 3, 6, 10, 0]
    A_sorted = [0, 1, 2, 3, 4, 5, 6, 10]
    sort_algorithm(A)
    print("OK" if A==A_sorted else "Fail")

    print("testcase #3 ", end="")
    A = [4, 2, 1, 0, 5, 3, 11, 11, 5, 6]
    A_sorted = [0, 1, 2, 3, 4, 5, 5, 6, 11, 11]
    sort_algorithm(A)
    print("OK" if A==A_sorted else "Fail")

    
    print("testcase #4 ", end="")
    A = [1, 1, 1, 0, 1, 1, 1, 0, 1, 1]
    A_sorted = [0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
    sort_algorithm(A)
    print("OK" if A==A_sorted else "Fail")

if __name__ == "__main__":
    test_sort(insert_sort)
    print()
    test_sort(choise_sort)
    print()
    test_sort(bubble_sort)
    print()
    test_sort(count_sort)

#########################################################################################
    
def func(matrix: list, max_mass):
    '''Алгоритм заполнености рюкзака'''
    max_price = 0
    total_ves = 0
    # for i in range(len(matrix)):
    #     price = matrix[i][0]
    #     ves = matrix[i][1]

    #     for j in range(i+1, len(matrix)):
    #         if j == i:
    #             continue
            
    #         if ves <= max_mass and price > max_price:
    #             max_price = price
    #             total_ves = ves

    #         price += matrix[j][0]
    #         ves += matrix[j][1]
            
    #         if ves <= max_mass and price > max_price:
    #             max_price = price
    #             total_ves = ves
    # new_list = [max_price, total_ves]

    # return new_list
    
    for i in range(len(matrix)):
        price = matrix[i][0]
        ves = matrix[i][1]
        if ves <= max_mass and price > max_price:
                max_price = price
                total_ves = ves

        for j in range(len(matrix)):
            if j == i:
                continue
            
            old_price = price
            old_ves = ves
            price += matrix[j][0]
            ves += matrix[j][1]
            
            if ves <= max_mass and price > max_price:
                max_price = price
                total_ves = ves
            else:
                price = old_price
                ves = old_ves

    new_list = [max_price, total_ves]

    return new_list

def test_case(algorithm):
    print(f"Тестируем: {algorithm.__doc__}")

    print("testcase #1 ", end="")
    n = [[300, 200], [600, 400], [2000, 1400], [100, 100], [500, 1000]]
    max_mass = 1500
    summa_ves = [2100, 1500]
    print("OK" if summa_ves==algorithm(n, max_mass) else "Fail")

    print("testcase #2 ", end="")
    n = [[300, 200], [600, 400], [2000, 1000], [100, 100], [500, 1000]]
    max_mass = 1500
    summa_ves = [2700, 1500]
    print("OK" if summa_ves==algorithm(n, max_mass) else "Fail")

    print("testcase #3 ", end="")
    n = [[300, 200], [600, 400], [100, 100], [500, 1000]]
    max_mass = 1500
    summa_ves = [1200, 1500]
    print("OK" if summa_ves==algorithm(n, max_mass) else "Fail")

    print("testcase #4 ", end="")
    n = [[100, 100], [500, 1000]]
    max_mass = 200
    summa_ves = [100, 100]
    print("OK" if summa_ves==algorithm(n, max_mass) else "Fail")

    print("testcase #5 ", end="")
    n = [[300, 200], [600, 400], [100, 100]]
    max_mass = 500
    summa_ves = [700, 500]
    print("OK" if summa_ves==algorithm(n, max_mass) else "Fail")
    
    print("testcase #6 ", end="")
    n = [[300, 200], [600, 400], [400, 100]]
    max_mass = 300
    summa_ves = [700, 300]
    print("OK" if summa_ves==algorithm(n, max_mass) else "Fail")

if __name__ == "__main__":
    test_case(func)
    print()


##################################################################################

a = 'dyubdwyfuydghukqndvtqevgdbcnkdfilglenghlkebhfwwemkfjbgefnmkeydqkendfcbvhreyiwuoiqwmkdkey'

string1 = 'lengh'
string2 = 'key'

def search(a):
    '''Алгоритм поиска строки в строке'''
    count = 0
    vkl2 = len(string1)
    for i in range(len(a)):
        perem = a[i:vkl2]
        if a[i:vkl2] == string1:
            vkl2 += 1; count += 1
            print(string1, count)
        else:
            vkl2 += 1
            
search(a)