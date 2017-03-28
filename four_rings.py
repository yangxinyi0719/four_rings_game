import random

chessboard = [[0 for j in range(8)] for i in range(6)]  # chessboard
col_size = 8
row_size = 6


# chessboard为6*8的棋盘，初始化置0
# col_size为列数6
# row_size为行数8


def rand_filename():
    # 随机生成一个文件名
    string_num = str(random.randint(10000, 100000))
    filename = "four_rings_" + string_num + ".txt"
    return filename


def create_file():
    # 新建并打开一个txt文件
    fp = open(rand_filename(), "w+")
    return fp


def init(fp):
    # 显示游戏规则
    # 初始化界面
    print("**************四连环游戏**************")
    print("只要你四个棋子可以相连成一行、一列或一条斜线，你就赢啦!")
    print("TIP：每次只能选择8行中的一行")
    print("x代表的是你的棋子,o代表ai的棋子")
    print("**************************************\n")
    print("The game begins! This is the initial chessboard:")
    fp.write("**************四连环游戏**************\n")
    fp.write("只要你四个棋子可以相连成一行、一列或一条斜线，你就赢啦!\n")
    fp.write("TIP：每次只能选择8行中的一行\n")
    fp.write("x代表的是你的棋子,o代表ai的棋子\n")
    fp.write("**************************************\n\n")
    fp.write("The game begins! This is the initial chessboard:\n")
    refresh_screen(fp)


def refresh_screen(fp):
    # 刷新当前的棋盘，同时打印到txt中
    print(" 1 2 3 4 5 6 7 8")
    fp.write(" 1 2 3 4 5 6 7 8\n")
    for i in range(row_size):
        for j in range(col_size):
            if chessboard[row_size - 1 - i][j] == 0:  # blank
                print("| ", end='')
                fp.write("| ")
            elif chessboard[row_size - 1 - i][j] == 1:  # user
                print("|x", end='')
                fp.write("|x")
            elif chessboard[row_size - 1 - i][j] == 2:  # ai
                print("|o", end='')
                fp.write("|o")
        print("|\n")
        fp.write("|\n")
    print("-----------------")
    fp.write("-----------------\n")


def user_move(fp):
    # 用户下棋，输入错误则重新输入，遇到满的列也重新输入
    input_location = -1
    while input_location == -1:
        temp_location = input("Your turn! Choose one column(1-8):")
        fp.write("Your turn! Choose one column(1-8):\n")
        if '0' < temp_location < '9' and len(temp_location) == 1:
            input_location = int(temp_location) - 1
            if chessboard[5][input_location] == 0:
                for i in range(row_size):
                    if chessboard[i][input_location] == 0:
                        chessboard[i][input_location] = 1
                        break
                    else:
                        continue
            else:
                print("This column is full! Choose another!")
                fp.write("This column is full! Choose another!\n")
                input_location = -1
        else:
            print("input error! Please input again!")
            fp.write("input error!Please input again!\n")

    refresh_screen(fp)


def ai_move(fp):
    # ai随机下棋，遇到满的列随机再换一列
    print("Ai is moving...")
    fp.write("Ai is moving...\n")
    input_location = -1
    while input_location == -1:
        input_location = random.randint(0, 7)
        if chessboard[5][input_location] == 0:
            for i in range(row_size):
                if chessboard[i][input_location] == 0:
                    chessboard[i][input_location] = 2
                    break
                else:
                    continue
        else:
            #   print("This column is full!")
            input_location = -1

    refresh_screen(fp)


def judge_win():
    # 判断各方的棋子是否可以组成一行，一列或一斜线
    # 前一个循环是判断一行，一列和右上斜线
    # 后一个循环判断左上斜线和上一个循环中漏掉的一列
    for j in range(col_size - 3):
        for i in range(row_size - 3):
            if chessboard[i][j] == chessboard[i][j + 1] == chessboard[i][j + 2] == chessboard[i][j + 3] == 1 \
                    or chessboard[i][j] == chessboard[i + 1][j] == chessboard[i + 2][j] == chessboard[i + 3][j] == 1 \
                    or chessboard[i][j] == chessboard[i + 1][j + 1] == chessboard[i + 2][j + 2] == chessboard[i + 3][
                                j + 3] == 1:

                #  print("you win!")
                return 1
            elif chessboard[i][j] == chessboard[i][j + 1] == chessboard[i][j + 2] == chessboard[i][j + 3] == 2 \
                    or chessboard[i][j] == chessboard[i + 1][j] == chessboard[i + 2][j] == chessboard[i + 3][j] == 2 \
                    or chessboard[i][j] == chessboard[i + 1][j + 1] == chessboard[i + 2][j + 2] == chessboard[i + 3][
                                j + 3] == 2:
                #  print("ai wins!")
                return 2
    for j in range(3, col_size):
        for i in range(row_size - 3):
            if chessboard[i][j] == chessboard[i + 1][j - 1] == chessboard[i + 2][j - 2] == chessboard[i + 3][j - 3] \
                    == 1 or chessboard[i][j] == chessboard[i + 1][j] == chessboard[i + 2][j] == chessboard[i + 3][
                j] == 1:
                return 1
            elif chessboard[i][j] == chessboard[i + 1][j - 1] == chessboard[i + 2][j - 2] == chessboard[i + 3][
                        j - 3] == 2 \
                    or chessboard[i][j] == chessboard[i + 1][j] == chessboard[i + 2][j] == chessboard[i + 3][j] == 2:
                return 2
    return 0


def is_chessboard_full():
    # 判断棋盘是否满
    for j in range(col_size):
        if chessboard[row_size - 1][j] == 0:
            return 0
    return 1


def main():
    # 进行下棋，并判断是否胜利或平局
    fp = create_file()
    init(fp)
    while 1:
        user_move(fp)
        judge = judge_win()
        if judge == 1:
            print("you win the game! Congratulations!")
            fp.write("you win the game! Congratulations!\n")
            break
        elif judge == 2:
            print("Ai win the game! Sorry you lost.")
            fp.write("Ai win the game! Sorry you lost.\n")
            break
        if is_chessboard_full():
            print("平局!")
            fp.write("平局!\n")
            break

        ai_move(fp)
        judge = judge_win()
        if judge == 1:
            print("you win the game! Congratulations!")
            fp.write("you win the game! Congratulations!\n")
            break
        elif judge == 2:
            print("Ai win the game! Sorry you lost.")
            fp.write("Ai win the game! Sorry you lost.\n")
            break
        if is_chessboard_full():
            print("平局!")
            fp.write("平局!\n")
            break
    fp.close()


if __name__ == "__main__":
    main()
