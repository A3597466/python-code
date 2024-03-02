import random

def get_user_choice():
    while True:
        user_choice = input("请选择（石头s、剪刀j、布b）：")
        if user_choice in ["s", "j", "b"]:
            return user_choice
        else:
            print("输入错误，请重新选择。")

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "平局"
    elif (user_choice == "s" and computer_choice == "j") or \
         (user_choice == "j" and computer_choice == "b") or \
         (user_choice == "b" and computer_choice == "s"):
        return "用户胜利"
    else:
        return "用户失败"

def play_game():
    print("欢迎来到石头剪刀布游戏！")
    while True:
        user_choice = get_user_choice()
        computer_choice = random.choice(["s", "j", "b"])
        print("用户选择：", user_choice)
        print("电脑选择：", computer_choice)
        result = determine_winner(user_choice, computer_choice)
        print("游戏结果：", result)

        play_again = input("再玩一局？（是y/否n）：")
        if play_again != "y":
            break

play_game()


