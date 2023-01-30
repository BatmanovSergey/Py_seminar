# ** 4. Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# Добавьте игру против бота, можно не добвлять
# Подумайте как наделить бота "интеллектом"


# # Моё решение

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

# # Решение на семинаре

# from random import shuffle, randint

# # CANDIES = 2021
# CANDIES = 121
# CANDIES_LIMIT = 28


# def bot_run(candies: int) -> int:
#     result = candies % CANDIES_LIMIT + 1
#     if not result:
#         result = randint(1, CANDIES_LIMIT + 1)
#     return result


# def moves(pl_act):
#     first, second = players
#     return second if pl_act == first else first


# players = ["human", 'bot' if int(input('Play with bot 1 - yes, 0 - no? ')) else 'person']
# shuffle(players)

# active_player = players[0]
# print(f'1 player - {players[0]}, 2 player - {players[1]}')

# while CANDIES > 0:
#     print(f'\nThere are {CANDIES} sweets on the table, you can take [1 .. {CANDIES_LIMIT}]')
#     print(f"Player {active_player}'s move")

#     if active_player == "bot":
#         get_candies = bot_run(CANDIES)
#         print(f'The bot took {get_candies} candies')
#     else:
#         get_candies = int(input(f'How many candies do you want {active_player}: '))

#     # проверки
#     if get_candies not in range(1, CANDIES_LIMIT + 1):
#         print('Wrong move!')
#     else:
#         CANDIES -= get_candies
#         if CANDIES > 0:
#             active_player = moves(active_player)
#         else:
#             print(f'The player {active_player} won!')

# # # Решение от Алеси

# mode_game = int(input("Для выбора режима игры введите 0 (человек бот) или 1 (человек человек): "))
# import sys
# if 1 > mode_game < 0:
#     print("Вы выбрали несуществующий режим")
#     sys.exit()

# from random import randint
# if mode_game:
#     player1 = input("Введите имя первого игрока: ")
#     player2 = input("Введите имя второго игрока: ")
# else:
#     player1 = input("Введите имя первого игрока: ")
#     player2 = "Бот"
# allsweets = 121
# priority = randint(0, 1)

# if priority:
#     print(f"Первый ходит {player1}")
# else:
#     print(f"Первый ходит {player2}")

# def input_sweets(name):
#     sweets = int(input(f"{name}, введите количество конфет, которое вы возьмете от 1 до 28: "))
#     while sweets < 1 or sweets > 28:
#         sweets = int(input(f"{name}, введите корректное количество конфет: "))
#     return sweets

# def print_results(name, num,  allsweets):
#     print(f"{name} взял {num}, осталось  {allsweets} конфет.")

# while allsweets > 28:
#     if priority:
#         num = input_sweets(player1)
#         allsweets -= num
#         priority = False
#         print_results(player1, num, allsweets)
#     else:
#         if mode_game:
#             num = input_sweets(player2)
#         else:
#             num = allsweets % 29
#         allsweets -= num
#         priority = True
#         print_results(player2, num, allsweets)
# if priority:
#     print(f"Выиграл {player1}")
# else:
#     print(f"Выиграл {player2}")

