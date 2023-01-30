# * 3. Создайте программу для игры в "Крестики-нолики". 
# Поле 3x3. Игрок - игрок, без бота.

# # Решение 1

board = list(range(1,13))

def draw_board(board):
    print ("-" * 13)
    for i in range(3):
        print ("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print ("-" * 13)

def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input("Куда поставим " + player_token+"? ")
        try:
            player_answer = int(player_answer)
        except:
            print ("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(board[player_answer-1]) not in "XO"):
                board[player_answer-1] = player_token
                valid = True
            else:
                print ("Эта клеточка уже занята")
        else:
            print ("Некорректный ввод. Введите число от 1 до 9 чтобы походить.")

# # Вариант другой записи take_input
# def take_input(player_token):
#     valid = False
#     while not valid:
#         player_answer = input("Куда поставим " + player_token+"? ")
#         if player_answer.isdigit():
#             player_answer = int(player_answer)
#             if 1 <= player_answer <= 9:
#                 if (str(board[player_answer-1]) not in "XO"):
#                     board[player_answer-1] = player_token
#                     valid = True
#                 else:
#                     print ("Эта клеточка уже занята")
#             else:
#                 print ("Некорректный ввод. Введите число от 1 до 9 чтобы походить.")
#         else:
#             print ("Некорректный ввод. Вы уверены, что ввели число?")

def check_win(board):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print (tmp, "выиграл!")
                win = True
                break
        if counter == 9:
            print ("Ничья!")
            break
    draw_board(board)

main(board)

# # Решение на семинаре

board = list(map(str, range(1, 10)))

def draw_board():
    print('-' * 20)
    for i in range(3):
        for k in range(3):
            print(f"{board[k + i * 3]:^5}", end=" ")
        print(f"\n{'-' * 20}")
    print()

def place_sign(token):
    global board
    while True:
        answer = input(f"Enter a number from 1 to 9.\nSelect a position {token}? ")
        if answer.isdigit() and int(answer) in range(1, 10):
            answer = int(answer)
            pos = board[answer - 1]
            if pos not in (chr(10060), chr(11093)):
                board[answer - 1] = chr(10060) if token == "X" else chr(11093)
                break
            else:
                print(f"This cell is already occupied{chr(9995)}{chr(129292)}")
        else:
            print(f"Incorrect input{chr(9940)}. Are you sure you entered a correct number?")

def check_win():
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    n = [board[x[0]] for x in win_coord if board[x[0]] == board[x[1]] == board[x[2]]]
    return n[0] if n else n

def main():
    counter = 0
    draw_board()
    while True:
        place_sign("O") if counter % 2 else place_sign("X")
        draw_board()

        if counter > 3:
            if check_win():
                print(f"{check_win()} - WIN{chr(127942)}{chr(127881)}!")
                break
        if counter == 8:
            print(f"Drawn game {chr(129318)}{chr(129309)}!")
            break
        counter += 1

main()

# # Решение от Даниила

"""
Создайте программу для игры в ""Крестики-нолики"". Игра реализуется в терминале, игроки ходят поочередно, 
необходимо вывести карту(как удобнее, можно например в виде списка, внутри которого будут 3 списка по 3 элемента, 
каждый из которого обозначает соответсвующие клетки от 1 до 9), сделать проверку не занята ли клетка, 
на которую мы хотим поставить крестик или нолик, 
и проверку на победу(стоят ли крестики или нолик в ряд по диагонали, вертикали, горизонтали)
"""

def print_menu():
    print('1). Новая игра.')
    print('2). Выход.')

    choice = int(input())
    while choice > 2 or choice < 1:
        choice = int(input('Некорректный ввод!\n'))
    return choice

def printTable(table: list):
    def get_symbol(id):
        if id == 1:
            return '❌'
        elif id == 2:
            return '⭕'
        else:
            return '🔲'
    print()
    for row in table:
        for pos in row:
            print(get_symbol(pos), end='')
        print()

def new_game(table: list):
    table.clear()
    for i in range(3):
        table.append([0, 0, 0])

def set_symbol(table, row, pos, id):
    row -= 1
    pos -= 1
    if 0 <= row < len(table) and 0 <= pos < len(table) and table[row][pos] == 0 :
        table[row][pos] = id
        return True
    else:
        return False

def check_win(table):
    # Проверка строк
    count_null = 0
    for row in table:
        count_null += row.count(0)
        if row.count(1) == 3: 
            return (True, 1)
        elif row.count(2) == 3:
            return (True, 2)
            
    # Проверка столбцов 
    for pos in range(len(table)):
        count_o = 0
        count_x = 0
        for row in range(len(table)):
            if table[row][pos] == 1:
                count_x += 1
            elif table[row][pos] == 2:
                count_o += 1
            # Анализ результата
            if count_x == 3:
                return (True, 1)
            elif count_o == 3:
                return (True, 2)

    # Проверка диагоналей
    count_o = 0
    count_x = 0
    for pos in range(len(table)):
        if table[len(table) - pos - 1][pos] == 1:
            count_x += 1
        elif table[len(table) - pos - 1][pos] == 2:
            count_o += 1
            # Анализ результата
            if count_x == 3:
                return (True, 1)
            elif count_o == 3:
                return (True, 2)

    count_o = 0
    count_x = 0
    for pos in range(len(table)):
        if table[pos][pos] == 1:
            count_x += 1
        elif table[pos][pos] == 2:
            count_o += 1
        # Анализ результата
        if count_x == 3:
            return (True, 1)
        elif count_o == 3:
            return (True, 2)
    
    if count_null == 0:
        return (True, 3)

    return (False,)

game_map = []
while print_menu() != 2:
    # Запуск игры
    new_game(game_map)
    stage = 0
    while not check_win(game_map)[0]:
        printTable(game_map)
        stage += 1        
        if stage % 2 == 1:
            x, y = map(int, input('Ход 1 игрока. Введите координату в формате X Y\n').split())
            while not set_symbol(game_map, y, x, 1):
                x, y = map(int, input('Неверный ввод! Введите координату в формате X Y. Например 1 2\n').split())

        else:
            x, y = map(int, input('Ход 2 игрока. Введите координату в формате X Y\n').split())
            while not set_symbol(game_map, y, x, 2):
                x, y = map(int, input('Неверный ввод! Введите координату в формате X Y. Например 1 2\n').split())

    winer = check_win(game_map)[1]
    if winer == 3:
        print('Ничья')
    else:
        print(f'Победил игрок {winer}')
