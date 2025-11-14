
#猜數字遊戲 •	玩家每次輸入猜測數字，程式提示「大了」或「小了」。答對時顯示「恭喜通過！」並結束遊戲。程式需記錄猜測次數，顯示學員的持續進步。

import random
def guess_number_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    print("歡迎來到猜數字遊戲！請在1到100之間猜一個數字。")

    while True:
        try:
            guess = int(input("請輸入你的猜測："))
            attempts += 1

            if guess < number_to_guess:
                print("小了！再試一次。")
            elif guess > number_to_guess:
                print("大了！再試一次。")
            else:
                print(f"恭喜通過！你總共猜了 {attempts} 次。")
                break
        except ValueError:
            print("請輸入一個有效的整數。")
            