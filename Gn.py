
#猜數字遊戲 •	玩家每次輸入猜測數字，程式提示「大了」或「小了」。答對時顯示「恭喜通過！」並結束遊戲。程式需記錄猜測次數，顯示學員的持續進步。
import random
def guess_number_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    print("歡迎來到猜數字遊戲！我已經選好了一個1到100之間的數字。")

    while True:
        user_input = input("請輸入你的猜測（或輸入'q'退出遊戲）：")
        
        if user_input.lower() == 'q':
            print("遊戲結束，謝謝參加！")
            break
        
        try:
            guess = int(user_input)
            attempts += 1
            
            if guess < number_to_guess:
                print("太低了！再試一次。")
            elif guess > number_to_guess:
                print("太高了！再試一次。")
            else:
                print(f"恭喜你！你猜對了，答案就是 {number_to_guess}。你總共猜了 {attempts} 次。")
                break
        except ValueError:
            print("請輸入一個有效的數字或'q'退出遊戲。")

if __name__ == '__main__':
    guess_number_game()