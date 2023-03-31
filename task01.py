# n = int(input("Введите число "))
# def find_fibonacci_index_by_value(value):
#     prev, curr = 0, 1 
#     index = 2
#     while curr < value:
#         prev, curr = curr, prev + curr
#         index += 1
#     return index if curr == value else -1
# print(find_fibonacci_index_by_value(n))
# n = int(input())

# temps = [int(input()) for i in range(n)]

# max_days = 0
# days = 0
# for temp in temps:
#     if temp > 0:
#         days += 1
#     else:
#         if days > max_days:
#             max_days = days
#         days = 0
# if days > max_days:
#     max_days = days
# print(max_days)
import random

N = int(input("Ввведите число: "))
random_array = [random.randint(1, 9) for i in range(N)]
print(random_array)

def find_min_max(array):
  min_val = float('-inf')
  max_val = float('-inf')
  
  for num in array:
    if num > max_val:
      max_val = num
    if num < min_val:
      min_val = num
      
  return (min_val, max_val)
print(find_min_max(random_array))