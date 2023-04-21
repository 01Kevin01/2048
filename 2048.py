import random
import os

# Tahta boyutu
BOARD_SIZE = 4

# Başlangıç ekranı
print("2048 Oyununa Hoş Geldiniz!")
print("Oyunu oynamak için yön tuşlarını kullanın.")
print("Oyunu bitirmek için 'q' tuşuna basın.")

# Oyun tahtası
board = [[0 for i in range(BOARD_SIZE)] for j in range(BOARD_SIZE)]

# Oyunu başlatmak için 2 adet 2'lik kutu oluşturuyoruz.
def start_game():
    add_new_box()
    add_new_box()
    print_board()

# Oyun tahtasını yazdıran fonksiyon
def print_board():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Score: ", get_score())
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            print(board[i][j], end="\t")
        print()

# Yeni kutu eklemek için kullanılan fonksiyon
def add_new_box():
    x, y = get_random_empty_box()
    board[x][y] = 2 if random.random() < 0.9 else 4

# Rastgele bir boş kutu seçmek için kullanılan fonksiyon
def get_random_empty_box():
    empty_boxes = []
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] == 0:
                empty_boxes.append((i, j))
    return random.choice(empty_boxes)

# Oyunun skorunu hesaplayan fonksiyon
def get_score():
    return sum([sum(row) for row in board])

# Kutuları yukarı taşıyan fonksiyon
def move_up():
    moved = False
    for j in range(BOARD_SIZE):
        for i in range(1, BOARD_SIZE):
            if board[i][j] != 0:
                for k in range(i, 0, -1):
                    if board[k-1][j] == 0:
                        board[k-1][j] = board[k][j]
                        board[k][j] = 0
                        moved = True
                    elif board[k-1][j] == board[k][j]:
                        board[k-1][j] *= 2
                        board[k][j] = 0
                        moved = True
                        break
    return moved

# Kutuları aşağı taşıyan fonksiyon
def move_down():
    moved = False
    for j in range(BOARD_SIZE):
        for i in range(BOARD_SIZE - 2, -1, -1):
            if board[i][j] != 0:
                for k in range(i, BOARD_SIZE - 1):
                    if board[k+1][j] == 0:
                        board[k+1][j] = board[k][j]
                        board[k][j] = 0
                        moved = True
                    elif board[k+1][j] == board[k][j]:
                        board[k+1][j] *= 2
                        board[k][j] = 0
                        moved = True
                        break
    return moved

# Kutuları sola taşıyan fonksiyon
def move_left():
    moved = False
    for i in range(BOARD_SIZE):
        for j in range(1, BOARD_SIZE):
            if board[i][j] != 0:
                for k in range(j, 0, -1):
                    if board[i][k-1] == 0:
                        board[i][k-1] = board[i][k]
                        board[i][k] = 0
                        moved = True
                    elif board[i][k-1] == board[i][k]:
                        board[i][k-1] *= 2
                        board[i][k] = 0
                        moved = True
                        break
    return moved

# Kutuları sağa taşıyan fonksiyon
def move_right():
    moved = False
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE - 2, -1, -1):
            if board[i][j] != 0:
                for k in range(j, BOARD_SIZE - 1):
                    if board[i][k+1] == 0:
                        board[i][k+1] = board[i][k]
                        board[i][k] = 0
                        moved = True
                    elif board[i][k+1] == board[i][k]:
                        board[i][k+1] *= 2
                        board[i][k] = 0
                        moved = True
                        break
    return moved

# Yön tuşlarını algılayan ana oyun döngüsü
def main():
    start_game()
    while True:
        key = input()
        if key == 'q':
            print("Oyun bitti!")
            break
        elif key == 'w':
            moved = move_up()
        elif key == 's':
            moved = move_down()
        elif key == 'a':
            moved = move_left()
        elif key == 'd':
            moved = move_right()
        else:
            moved = False

        if moved:
            add_new_box()

        print_board()

        # Oyunun bitip bitmediğini kontrol ediyoruz
        if is_game_over():
            print("Oyun bitti!")
            break

# Oyunun bitip bitmediğini kontrol eden fonksiyon
def is_game_over():
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] == 0:
                return False
            if i != BOARD_SIZE - 1 and board[i][j] == board[i+1][j]:
                return False
            if j != BOARD_SIZE - 1 and board[i][j] == board[i][j+1]:
                return False
    return True

# Oyunu başlatıyoruz
main()

while True:
    pass  # Sonsuz döngü