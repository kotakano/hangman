import random
def hangman(word):
    wrong = 0
    stages =["",
             "__________           ",
             "|                    ",
             "|         |          ",
             "|         O          ",
             "|        /|\         ",
             "|        / \         ",
             "|                    "
             ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ!")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "1文字予想してね"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ち！")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け！正解は {}。".format(word))

if __name__ == "__main__":
    answers = []
    num = int(input("入力する英単語の数を数字で入力してください。"))
    for i in range(num):
        words = input("{}つ目の英単語を入力してください。".format(i+1))
        answers.append(words)
    word = answers[random.randint(0,len(answers)-1)]
    hangman(word)
