def password(num):
    cipher = ''
    for i in range(1, num):
        for j in range(i + 1, num):
            if num % (i + j) == 0:
                cipher += str(i) + str(j)
    return cipher

print('Число в первой вставке:')
result = (password(int(input())))
print('Шифр:', result,)