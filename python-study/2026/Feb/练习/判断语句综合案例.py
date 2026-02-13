import random
num = random.randint(1,10)
guess = int(input("猜一个数:"))

if guess > num:
    print("大了")
    guess = int(input("猜一个数:"))

    if guess > num:
        print("大了")
        guess = int(input("猜一个数:"))

        if guess > num:
            print("大了")
            guess = int(input("猜一个数:"))

            if guess > num:
                print("大了,GameOver")
            elif guess < num:
                print("小了,GameOver")
            else:
                print("猜对了,游戏结束!")

        elif guess < num:
            print("小了")
        else:
            print("猜对了")

    elif guess < num:
        print("小了")
        guess = int(input("猜一个数:"))

        if guess < num:
            print("小了")
            guess = int(input("猜一个数:"))

            if guess < num:
                print("小了,GameOver")
            elif guess > num:
                print("大了,GameOver")
            else:
                print("猜对了,游戏结束!")
    else:
        print("猜对了")

elif guess < num:
    print("小了")
    guess = int(input("猜一个数:"))

    if guess < num:
        print("小了")
        guess = int(input("猜一个数:"))

        if guess < num:
            print("小了")
            guess = int(input("猜一个数:"))

            if guess < num:
                print("小了,GameOver")
            elif guess > num:
                print("大了,GameOver")
            else:
                print("猜对了,游戏结束!")
    elif guess > num:
        print("大了")
        guess = int(input("猜一个数:"))

        if guess > num:
            print("大了")
            guess = int(input("猜一个数:"))

            if guess > num:
                print("大了,GameOver")
            elif guess < num:
                print("小了,GameOver")
            else:
                print("猜对了,游戏结束!")
        elif guess < num:
            print("小了")
            guess = int(input("猜一个数:"))

            if guess < num:
                print("小了,GameOver")
            elif guess > num:
                print("大了,GameOver")
            else:
                print("猜对了,游戏结束!")
        else:
            print("猜对了")
else:
    print("猜对了")