"""
6. В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток.
После каждой неудачной попытки должно сообщаться, больше или меньше введенное пользователем число,
чем то, что загадано.
Если за 10 попыток число не отгадано, вывести правильный ответ.
"""
import random
print("Программа-игра в угадайку. Программа загадывает целое число от 0 до 100, пользователю дается 10 попыток отгадать число.\nПосле каждого не правильного ответа будет дана подсказка для следующего ответа")
random_number = random.randint(0, 100)
i = 10
while True:
    user_number = int(input("Введите число: "))
    if user_number > random_number:
        print(f'{user_number} больше загаданного числа. У вас осталось {i-1} попыток')

    elif user_number < random_number:
        print(f'{user_number} меньше загаданного числа. У вас осталось {i-1} попыток')
    else:
        print('Поздравляю! Вы отгадали правильное число')
        break
    i-=1
    if i ==0:
        print(f'К сожалению, вы не смогли отгадать число. Было загадано число {random_number}')
        break
