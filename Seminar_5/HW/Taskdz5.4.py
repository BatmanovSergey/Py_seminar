# ** 4. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# Добавьте игру против бота, можно не добвлять
# Подумайте как наделить бота "интеллектом"

from random import choice

amount_candies = int(input("Введите количество конфет: "))

def game_selection(amount):
    print("Выбор игры:")
    num = int(input("Играть с ботом: ДА - нажмите 1, НЕТ - нажмите 0: "))
    if num == 1:
        bot_game(amount)
    elif num == 0:
        players_game(amount)
    else:
        print("Введено некорректное значение")

def bot_game(amount):
    counter = 0
    win = False
    while not win:
        if amount > 0:
            if counter % 2 == 0:
                print("Игрок делает ход.")
                amount = player_choose(amount)  
            else:
                print("Бот делает ход.") 
                amount = bot_choose(amount)
            counter += 1
        else:
            win = True
            if counter % 2 == 0:
                print("Победитель -> Бот")
            else:
                print("Победитель -> Игрок")
                
def players_game(amount):
    counter = 0
    win = False
    while not win:
        if amount > 0:
            if counter % 2 == 0:
                print("Игрок 1 делает ход.")
                amount = player_choose(amount)  
            else:
                print("Игрок 2 делает ход.")
                amount = player_choose(amount) 
            counter += 1
        else:
            win = True
            if counter % 2 == 0:
                print("Победитель -> Игрок 2")
            else:
                print("Победитель -> Игрок 1")

def player_choose(amount):
    valid = False
    while not valid:
        candy_choice = input("Возьмите от 1 до 28 конфет: ")
        if candy_choice.isdigit():
            candy_choice = int(candy_choice)
            if 1 <= candy_choice <= 28:
                valid = True
                amount -= candy_choice        
            else:
                print("Некорректный ввод. Введите число от 1 до 28")    
        else:
            print("Некорректный ввод. Вы уверены, что ввели число?") 
    print(f"На столе лежат конфеты в количестве:{amount}") 
    return amount 

def bot_choose(amount):
       candy_choice = choice(range(1, 29))
       amount -= candy_choice
       print(f"На столе лежат конфеты в количестве:{amount}") 
       return amount

game_selection(amount_candies)