my_list = [1, 2, 3, 4, 2, 1, 5, 6, 7, 7, 8, 9, 9]
k = int(input("Введите число сдвига: "))

def shift_list(lst, k):
    k = k % len(lst)
    return lst[k:] + lst[:k]

shifted_numbers = shift_list(my_list, k)
print(shifted_numbers)

# your_list = [int(input('type element: ')) for i in range(int(input('type amount')))]
# k = int(input('type K: '))
#  print(your_list)
# k_list = my_list[k:] + my_list[:k]
# print(k_list)
