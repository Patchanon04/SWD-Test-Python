list_test = [1,2,1,3,5,6,4]
max_num = list_test[0]
for num in list_test:
    if num > max_num:
        max_num = num
result = list_test.index(max_num)
print(f'max number at index = {result}') 