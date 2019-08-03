import random, re, math

def start():
    while True:
        s = input("試合を開始する場合「試合開始」と入力してください:")
        if s == "試合開始":
            print("試合を開始します")
            break
        else:
            print("「試合開始」と入力してください")

def title_call():
    while True:
        global title
        title = input("タイトルコールを入力してください:")
        if title == "":
            print("タイトルコールを入力してください")
        else:
            print(title)
            break

def decide_red_name():
    while True:
        global red_name
        red_name = input("赤コーナーの選手の名前を入力してください:")
        if red_name == "":
            print("赤コーナーの選手の名前を入力してください")
        else:
            print("赤コーナー:" + red_name + "選手")
            break

def decide_blue_name():
    while True:
        global blue_name
        blue_name = input("青コーナーの選手の名前を入力してください:")
        if blue_name == "":
            print("青コーナーの選手の名前を入力してください")
        else:
            print("青コーナー:" + blue_name + "選手")
            break

def decide_dice_num():
    while True:
        global dice_num
        dice_num = input("何個のダイスを使いますか？ 数字を入力してください。例:2d6の場合「2」:")
        try:
            dice_num = int(dice_num)
        except ValueError:
            print("数字を入力してください。")
        else:
            if dice_num <= 0:
                print("1以上の数字を入力してください")
            else:
                print(str(dice_num) + "個")
                break

def decide_dice_size():
    while True:
        global dice_size
        dice_size = input("何面のダイスを使いますか？数字を入力してください。例:2d6の場合「6」:")
        try:
            dice_size = int(dice_size)
        except ValueError:
            print("数字を入力してください。")
        else:
            if dice_size <= 0:
                print("1以上の数字を入力してください")
            else:
                print(str(dice_size) + "面")
                break

def decide_round_num():
    while True:
        global round_num
        round_num = input("何ラウンドの試合ですか？ 数字を入力してください:")
        try:
            round_num = int(round_num)
        except ValueError:
            print("数字を入力してください")
        else:
            if round_num <= 0:
                print("1以上の数字を入力してください")
            else:
                print(str(round_num) + "ラウンド")
                break

def decide_hp():
    while True:
        global hp
        hp = input("初期ヒットポイントを数字で入力してください:")
        try:
            hp = int(hp)
        except ValueError:
            print("数字を入力してください")
        else:
            if hp <= 0:
                print("1以上の数字を入力してください")
            else:
                print("HP" + str(hp))
                break

def decide_down_hp():
    while True:
        global down_hp
        down_hp = input("いくつのダメージごとにダウンさせますか？ 数字を入力してください:")
        try:
            down_hp = int(down_hp)
        except ValueError:
            print("数字を入力してください")
        else:
            if down_hp <= 0:
                print("1以上の数字を入力してください")
            else:
                print(str(down_hp) + "HPのダメージごとにダウン")
                break

def dice(a, b):
    global dice_roll
    dice_roll = []
    for i in range(a):
        num = random.randint(1, b)
        dice_roll.append(num)
    return dice_roll

def fight():
    i = hp / down_hp

    red_hp = hp
    blue_hp = hp
    current_round = 1
    current_turn = 1
    blue_down = i - 1
    red_down = i - 1

    while current_round <= round_num or red_hp <= 0 or blue_hp <= 0:
        turn_call = input("「ラウンド数-ターン数」を入力してください。3ターンで1ラウンド経過です。例:1ラウンド1回目のダイスの場合:1-1:")

        if turn_call == str(current_round) + "-" + str(current_turn):
            red_dice = dice(dice_num, dice_size)
            blue_dice = dice(dice_num, dice_size)
            red_dice_sum = sum(red_dice)
            blue_dice_sum = sum(blue_dice)

            if red_dice_sum > blue_dice_sum:
                before_blue_hp = blue_hp
                damage = red_dice_sum - blue_dice_sum
                blue_hp -= damage
                print(title)
                print(str(current_round) + "ラウンド" + str(current_turn) + "ターン目")
                print("赤コーナー:" + red_name + ":" + str(red_dice) + "=" + str(red_dice_sum) + " " + "青コーナー:" + blue_name + ":" + str(blue_dice) + "=" + str(blue_dice_sum))
                print(blue_name + "選手に" + str(damage) + "のダメージ")
                print("赤コーナー:" + red_name + ":HP" + str(red_hp) + " vs " + "青コーナー:" + blue_name + ":HP" + str(blue_hp))

                if blue_hp != hp and blue_hp < (blue_down * down_hp + 1) and (before_blue_hp > blue_down * down_hp):
                    print(blue_name + "選手1回ダウン。")
                    if blue_hp > 0 and blue_hp % down_hp == 0:
                        blue_down = (blue_hp / down_hp) - 1
                        print("次HP" + str(int(blue_down * down_hp)) + "を切ったらダウン。")
                    elif blue_hp > 0 and blue_hp % down_hp != 0:
                        blue_down = math.floor(blue_hp / down_hp)
                        print("次HP" + str(int(blue_down * down_hp)) + "を切ったらダウン。")

            elif blue_dice_sum > red_dice_sum:
                before_red_hp = red_hp
                damage = blue_dice_sum - red_dice_sum
                red_hp -= damage
                print(title)
                print(str(current_round) + "ラウンド" + str(current_turn) + "ターン目")
                print("赤コーナー:" + red_name + ":" + str(red_dice) + "=" + str(red_dice_sum) + " " + "青コーナー:" + blue_name + ":" + str(blue_dice) + "=" + str(blue_dice_sum))
                print(red_name + "選手に" + str(damage) + "のダメージ")
                print("赤コーナー:" + red_name + ":HP" + str(red_hp) + " vs " + "青コーナー:" + blue_name + ":HP" + str(blue_hp))

                if red_hp != hp and red_hp < (red_down * down_hp + 1) and (before_red_hp > red_down * down_hp):
                    print(red_name + "選手1回ダウン。")
                    if red_hp > 0 and red_hp % down_hp == 0:
                        red_down = (red_hp / down_hp) - 1
                        print("次HP" + str(int(red_down * down_hp)) + "を切ったらダウン。")
                    elif red_hp > 0 and red_hp % down_hp != 0:
                        red_down = math.floor(red_hp / down_hp)
                        print("次HP" + str(int(red_down * down_hp)) + "を切ったらダウン。")

            else:
                before_red_hp = red_hp
                before_blue_hp = blue_hp
                heal = 1

                if red_hp < hp:
                    red_hp += heal
                if blue_hp < hp:
                    blue_hp += heal
                print(title)
                print(str(current_round) + "ラウンド" + str(current_turn) + "ターン目")
                print("赤コーナー:" + red_name + ":" + str(red_dice) + "=" + str(red_dice_sum) + " " + "青コーナー:" + blue_name + ":" + str(blue_dice) + "=" + str(blue_dice_sum))
                if before_red_hp < hp and before_blue_hp == hp:
                    print(red_name + "選手HP1回復。")
                elif before_blue_hp < hp and before_red_hp == hp:
                    print(blue_name + "選手HP1回復。")
                elif before_red_hp < hp and before_blue_hp < hp:
                    print("両者HP1回復。")
                else:
                    print("1ターン経過。")
                print("赤コーナー:" + red_name + ":HP" + str(red_hp) + " vs " + "青コーナー:" + blue_name + ":HP" + str(blue_hp))
                if red_hp > 0 and red_hp % down_hp == 0:
                    red_down = (red_hp / down_hp) - 1
                    print("赤コーナー:" + red_name + "選手、次HP" + str(int(red_down * down_hp)) + "を切ったらダウン。")
                elif red_hp > 0 and red_hp % down_hp != 0:
                    red_down = math.floor(red_hp / down_hp)
                    print("赤コーナー:" + red_name + "選手、次HP" + str(int(red_down * down_hp)) + "を切ったらダウン。")
                if blue_hp > 0 and blue_hp % down_hp == 0:
                    blue_down = (blue_hp / down_hp) - 1
                    print("青コーナー:" + blue_name + "選手、次HP" + str(int(blue_down * down_hp)) + "を切ったらダウン。")
                elif blue_hp > 0 and blue_hp % down_hp != 0:
                    blue_down = math.floor(blue_hp / down_hp)
                    print("青コーナー:" + blue_name + "選手、次HP" + str(int(blue_down * down_hp)) + "を切ったらダウン。")


            if red_hp <= 0:
                print(red_name + "選手KO。" + blue_name + "選手の勝利。")
                break
            elif blue_hp <= 0:
                print(blue_name + "選手KO。" + red_name + "選手の勝利。")
                break

            current_turn += 1

            if current_turn > 3:
                print(str(current_round) + "ラウンド終了。")
                current_round += 1
                current_turn = 1

            if current_round > round_num:
                print("全ラウンド終了。判定に入ります。")

                if red_hp > blue_hp:
                    print(title)
                    print("赤コーナー:" + red_name + ":HP" + str(red_hp) + " vs " + "青コーナー:" + blue_name + ":HP" + str(blue_hp))
                    print(red_name + "選手の判定勝利。")
                    break
                elif blue_hp > red_hp:
                    print(title)
                    print("赤コーナー:" + red_name + ":HP" + str(red_hp) + " vs " + "青コーナー:" + blue_name + ":HP" + str(blue_hp))
                    print(blue_name + "選手の判定勝利。")
                    break
                else:
                    print(title)
                    print("赤コーナー:" + red_name + ":HP" + str(red_hp) + " vs " + "青コーナー:" + blue_name + ":HP" + str(blue_hp))
                    print("本試合、引き分けで終了。")
                    break

        else:
            print("「ラウンド数-ターン数」が間違っています。正しくは" + str(current_round) + "-" + str(current_turn) + "です。")

start()
title_call()
decide_red_name()
decide_blue_name()
decide_dice_num()
decide_dice_size()
decide_round_num()
decide_hp()
decide_down_hp()
fight()
