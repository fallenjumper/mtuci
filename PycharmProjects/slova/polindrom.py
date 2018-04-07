test_str = input()
result = True
for i in range(len(test_str)):
    neg_i = i+1
    if test_str[i] != test_str[-neg_i]:
        result = False

if result:
    print('Нужная строка')
else:
    print('Ошибка')
