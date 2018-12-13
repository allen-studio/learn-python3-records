from sys import exit # 导入sys（系统）模块中的 exit（退出）函数，用于执行后面的exit(0)

def gold_room(): 
    print("This room is full of gold. How much do you take? ")

    choice = input("> ")
    if "0" in choice or "1" in choice:  
        how_much = int(choice)
    else:
        dead("Man, learn to type a number. ")

    if how_much < 50:
        print("Nice, you're not greedy, you win")
        exit(0) # exit(0) 程序运行正常，无错误进行退出
    else:
        print("You greedy bastard!")


def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    print("choice take honey or taunt bear") #试着让熊离开门（拿蜂蜜去引诱熊 或者 嘲讽熊）
    bear_moved = False # 当前熊的移动状态为false，即熊没有移动

    while True:
        choice = input("> ")

        if choice == "take honey": # 拿蜂蜜引诱熊，熊吃嗨了，还拿爪子暴击你的脸，你挂了
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved: # 嘲讽熊，熊移动了
            print("The bear has moved from the door.")
            print("You can go through it now.")
            print("choice taunt bear or open door")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved: # 继续嘲讽熊，你挂了
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved: # 打开门，进入金币房间，调用第3行gold_room()函数
            gold_room()
        else:
            print("I got no idea what that means.")


def cthulhu_room(): # 选择right进入克苏鲁房间
    print("Here you see the great evil cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")
    print("choice flee or head")

    choice = input("> ")

    if "flee" in choice: # 选择flee逃跑，调用 start()函数重新开始
        start()
    elif "head" in choice: # 选择贡献head脑子，直接挂了，调用dead死亡函数
        dead("Well that was tasty!")
    else: # 瞎几把乱输入回到克苏鲁房间重新开始
        cthulhu_room()


def dead(why): # 定义dead死亡函数，传入死亡原因并打印出来，并exit(0)退出函数运行
    print(why, "Good job!")
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door to your left and right.")
    print("Which one do you take?")
    print("choice left or right")

    choice = input("> ")

    if choice == "left": 
        bear_room() # 选择 left 左边，调用第第19行bear_room函数
    elif choice == "right": 
        cthulhu_room() # 选择 right 右边，调用第45行 cthulhu_room函数
    else: # 瞎几把乱输入，直接调用第61行 dead 函数
        dead("You stumble around the room until you starve.")

start() # 代码从start（）开始运行，调用第65行定义的start函数