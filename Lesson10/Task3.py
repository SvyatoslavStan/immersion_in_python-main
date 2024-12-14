"""Задача 3. Крестики-нолики
Создайте программу, которая реализует игру «Крестики-нолики».
Для этого напишите:
1. Класс, который будет описывать поле игры.
class Board:
# Класс поля, который создаёт у себя экземпляры клетки.
# Пусть класс хранит информацию о состоянии поля (это может быть список из
девяти элементов).
# Помимо этого, класс должен содержать методы:
# «Изменить состояние клетки». Метод получает номер клетки и, если клетка не
занята, меняет её состояние. Если состояние удалось изменить, метод возвращает
True, иначе возвращается False.
# «Проверить окончание игры». Метод не получает входящих данных, но
возвращает True/False. True — если один из игроков победил, False — если
победителя нет.
2. Класс, который будет описывать одну клетку поля:
class Cell:
# Клетка, у которой есть значения:
# занята она или нет;
# номер клетки;
# символ, который клетка хранит (пустая, крестик, нолик).
3. Класс, который описывает поведение игрока:
class Player:
# У игрока может быть:
# имя,
# количество побед.
# Класс должен содержать метод:
# «Сделать ход». Метод ничего не принимает и возвращает ход игрока (номер
клетки). Введённый номер нужно обязательно проверить.
4. Класс, который управляет ходом игры:
class Game:
# класс «Игры» содержит атрибуты:
# состояние игры,
# игроки,
# поле.
# А также методы:
# Метод запуска одного хода игры. Получает одного из игроков, запрашивает у
игрока номер клетки, изменяет поле, проверяет, выиграл ли игрок. Если игрок победил,
возвращает True, иначе False.
# Метод запуска одной игры. Очищает поле, запускает цикл с игрой, который
завершается победой одного из игроков или ничьей. Если игра завершена, метод
возвращает True, иначе False.
# Основной метод запуска игр. В цикле запускает игры, запрашивая после каждой
игры, хотят ли игроки продолжать играть. После каждой игры выводится текущий счёт
игроков.
Подсказка № 1
Начните с создания класса Cell, который будет хранить номер клетки, символ
(крестик, нолик или пустое значение), и состояние занятости клетки. Это позволит
каждой клетке иметь своё собственное состояние.
Подсказка № 2
Создайте класс Board, который содержит список из 9 объектов Cell. Этот список
будет представлять игровое поле.
Подсказка № 3
В классе Board создайте метод display_board, который будет выводить текущее
состояние доски на экран. Используйте простой цикл и форматирование строк для
создания наглядного интерфейса.
Подсказка № 4
Напишите метод в классе Board, который изменяет символ клетки, если она не занята.
Метод должен проверять состояние клетки перед изменением и возвращать True или
False в зависимости от успеха операции.
Подсказка № 5
В классе Board создайте метод check_game_over, который проверяет все возможные
победные комбинации. Если одна из них выполнена, метод должен возвращать True.
Подсказка № 6
Создайте класс Player, который будет хранить имя игрока, его символ (X или O), и
количество побед. Также добавьте метод для запроса хода игрока.
Подсказка № 7
Создайте класс Game, который будет управлять процессом игры. В этот класс включите
игроков и доску. Добавьте метод, который выполняет ход игрока и проверяет окончание
игры.
Подсказка № 8
В классе Game создайте метод play_one_game, который будет запускать одну
партию. Этот метод должен очищать доску, поочередно запрашивать ходы игроков и
завершаться либо победой одного из игроков, либо ничьей.
Подсказка № 9
Добавьте метод reset_board в класс Board, который будет сбрасывать состояние
всех клеток. Этот метод понадобится, чтобы начать новую партию с чистого листа.
Подсказка № 10
В классе Game создайте основной метод start_games, который будет в цикле
запускать новые игры до тех пор, пока игроки хотят продолжать. Не забудьте добавить
возможность показа текущего счёта и сброса доски перед началом новой игры.
"""

class Cell:
    def __init__(self, number):
        self.number = number
        self.symbol = ' '  # Пустая клетка по умолчанию
        self.is_taken = False

    def set_symbol(self, symbol):
        if not self.is_taken:
            self.symbol = symbol
            self.is_taken = True
            return True
        return False


class Board:
    def __init__(self):
        self.cells = [Cell(i) for i in range(1, 10)]

    def display_board(self):
        board = ""
        for i in range(9):
            board += f" {self.cells[i].symbol} "
            if (i + 1) % 3 == 0:
                board += "\n"
            else:
                board += "|"
        print(board)

    def reset_board(self):
        for cell in self.cells:
            cell.symbol = ' '
            cell.is_taken = False

    def update_cell(self, cell_number, symbol):
        return self.cells[cell_number - 1].set_symbol(symbol)

    def check_game_over(self):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # горизонтали
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # вертикали
            [0, 4, 8], [2, 4, 6]             # диагонали
        ]
        for combo in winning_combinations:
            if (self.cells[combo[0]].symbol == self.cells[combo[1]].symbol == 
                self.cells[combo[2]].symbol and self.cells[combo[0]].symbol != ' '):
                return True
        return all(cell.is_taken for cell in self.cells)  # Ничья, если все клетки заняты


class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.wins = 0

    def make_move(self):
        while True:
            try:
                cell_number = int(input(f"{self.name}, введите номер клетки (1-9): "))
                if 1 <= cell_number <= 9:
                    return cell_number
                else:
                    print("Введите число от 1 до 9.")
            except ValueError:
                print("Неверный ввод. Попробуйте снова.")


class Game:
    def __init__(self, player1, player2):
        self.board = Board()
        self.players = [player1, player2]
        self.current_player_index = 0

    def play_turn(self):
        player = self.players[self.current_player_index]
        self.board.display_board()
        while True:
            cell_number = player.make_move()
            if self.board.update_cell(cell_number, player.symbol):
                break
            else:
                print("Клетка занята, попробуйте снова.")
        if self.board.check_game_over():
            self.board.display_board()
            print(f"Поздравляем, {player.name} выиграл!")
            player.wins += 1
            return True
        self.current_player_index = 1 - self.current_player_index  # Меняем игрока
        return False

    def play_one_game(self):
        self.board.reset_board()
        print("Новая игра началась!")
        while not self.board.check_game_over():
            if self.play_turn():
                return
        self.board.display_board()
        print("Игра закончилась ничьей!")

    def start_games(self):
        while True:
            self.play_one_game()
            print(f"Счёт: {self.players[0].name} - {self.players[0].wins}, "
                  f"{self.players[1].name} - {self.players[1].wins}")
            if input("Хотите сыграть ещё раз? (да/нет): ").lower() != "да":
                print("Спасибо за игру!")
                break


if __name__ == "__main__":
    player1 = Player(input("Введите имя игрока 1: "), "X")
    player2 = Player(input("Введите имя игрока 2: "), "O")
    game = Game(player1, player2)
    game.start_games()
