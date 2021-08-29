import random, math, os, time
from datetime import datetime

# 試合で使用するダイスのクラス
class Dice:
    def __init__(self, dice_num, dice_size):
        self.num = dice_num
        self.size = dice_size
        print(str(self.num) + 'd' + str(self.size))
    
    # ダイスを投げたときの処理
    def throw_dice(self):
        dice_roll = []
        for i in range(self.num):
            num = random.randint(1, self.size)
            dice_roll.append(num)
        return dice_roll

# 対戦するボクサーのクラス
class Boxer:
    def __init__(self, name, hp, down_hp, dice):
        # ボクサーの名前
        self.name = name
        # HPの数
        self.hp = hp
        self.before_hp = 0
        # 1回の試合でダウンできる回数。この回数より多くダウンしてしまったら負け
        # 例：HP20、ダウンするHPの区切り10の場合、ダウンしても負けにならないのは1回まで
        self.down = (hp / down_hp) - 1
        # ダウン回数の記録
        self.down_count = 0
        self.dice = dice
        print(self.name + '選手' + ' ' + 'HP:' + str(self.hp))

# 両選手の最大HPを決定する関数
def decide_HP():
    while True:
        HP = input('選手のHPの値を入力してください（1以上の数字）:')
        try:
            HP = int(HP)
        except ValueError:
            print("数字を入力してください")
        else:
            if HP <= 0:
                print("1以上の数字を入力してください")
            else:
                print("HP:" + str(HP))
                return HP

# ボクサーを作成する関数
def boxer_create():
    while True:
        boxer_name = input("選手の名前を入力してください:")
        if boxer_name == "":
            print("選手の名前を入力してください")
        else:
            boxer = Boxer(boxer_name, HP, DOWN_HP, DICE)
            return boxer

# 対戦ログを保存するフォルダを作成する関数
def make_folder():
    fight_log_dir = "fight_log"
    try:
        os.makedirs(fight_log_dir)
    except FileExistsError:
        pass
    return fight_log_dir

# ダイスの個数を決定する関数
def decide_dice_num():
    while True:
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
                return dice_num

# ダイスの面数を決定する関数
def decide_dice_size():
    while True:
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
                return dice_size

# ダウンするHPの数を決定する関数
def decide_down_hp():
    while True:
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
                return down_hp

# 試合タイトルを決定する関数
def make_title_call(red_boxer, blue_boxer, max_round):
    while True:
        match_title = input('試合形式を入力してください。例:「日本フライ級ランキング」「バンタム級世界タイトルマッチ」etc:')
        if match_title == '':
            print('試合形式を入力してください。')
        else:
            title = match_title + str(max_round) + '回戦' + '_' + red_boxer.name + '_VS_' + blue_boxer.name
            print(title)
            return title

# ラウンド数を決定する関数
def decide_max_round():
    while True:
        max_round = input('最大ラウンド数を1以上の数字で入力してください。:')
        try:
            max_round = int(max_round)
        except ValueError:
            print('数字を入力してください')
        else:
            if max_round <= 0:
                print('1以上の数字を入力してください')
            else:
                print(str(max_round) + 'ラウンド試合')
                return max_round

# 試合のクラス
class Match:
    def __init__(self, hp, down_hp, red_boxer, blue_boxer, title, log_title, max_round, sleeptime) :
        # 最大HP数
        self.HP = hp
        # ダウンHP数
        self.DOWN_HP = down_hp
        # 赤コーナーボクサー
        self.red = red_boxer
        # 青コーナーボクサー
        self.blue = blue_boxer
        # 試合タイトル
        self.title = title
        # ログファイルのパス
        self.log_title = log_title
        # 現在のラウンド
        self.current_round = 1
        # 現在のターン
        self.current_turn = 1
        # 最大ラウンド数
        self.MAX_ROUND = max_round
        # スリープ秒数
        self.sleeptime = sleeptime
        # ターミナルに表示される文字列
        self.print_text = title + '\n' + '試合開始!' + '\n' + '\n'
        # ログファイルに書き込まれる文字列
        self.log_text = ''
        print(self.print_text)
        # 表示された文字列（試合経過）をログファイルに書き込む準備をする
        self.log_text += self.print_text
        time.sleep(self.sleeptime)
    
    # 試合のメソッド
    def fight(self):
        while self.current_round <= self.MAX_ROUND or self.red.hp <= 0 or self.blue.hp <= 0:
            red_dice = self.red.dice.throw_dice()
            blue_dice = self.blue.dice.throw_dice()
            red_dice_sum = sum(red_dice)
            blue_dice_sum = sum(blue_dice)

            round_turn = str(self.current_round) + "ラウンド" + str(self.current_turn) + "ターン目"

            if red_dice_sum > blue_dice_sum:
                self.blue.before_hp = self.blue.hp
                damage = red_dice_sum - blue_dice_sum
                self.blue.hp -= damage
                blue_damage_result = self.blue.name + "選手に" + str(damage) + "のダメージ"
                dice_result = "赤コーナー:" + self.red.name + ":" + str(red_dice) + "=" + str(red_dice_sum) + " " + "青コーナー:" + self.blue.name + ":" + str(blue_dice) + "=" + str(blue_dice_sum)
                hp_result = "赤コーナー:" + self.red.name + ":HP" + str(self.red.hp) + " vs " + "青コーナー:" + self.blue.name + ":HP" + str(self.blue.hp)

                self.print_text = round_turn + '\n' + dice_result + '\n' + blue_damage_result + '\n' + hp_result + '\n'

                print(self.print_text)

                self.log_text += self.print_text
                time.sleep(self.sleeptime)

                if self.blue.hp != self.HP and self.blue.hp < (self.blue.down * self.DOWN_HP + 1) and (self.blue.before_hp > self.blue.down * self.DOWN_HP):
                    self.blue.down_count += 1
                    blue_down_result = self.blue.name + "選手、この試合通算" + str(self.blue.down_count) + "回目のダウン。"
                    self.print_text = blue_down_result + '\n'
                    print(self.print_text)
                    self.log_text += self.print_text
                    if self.blue.hp > 0 and self.blue.hp % self.DOWN_HP == 0:
                        self.blue.down = (self.blue.hp / self.DOWN_HP) - 1
                        blue_next_down = "次HP" + str(int(self.blue.down * self.DOWN_HP)) + "を切ったらダウン。"
                        self.print_text = blue_next_down + '\n'
                        print(self.print_text)
                        self.log_text += self.print_text
                        time.sleep(self.sleeptime)
                    elif self.blue.hp > 0 and self.blue.hp % self.DOWN_HP != 0:
                        self.blue.down = math.floor(self.blue.hp / self.DOWN_HP)
                        blue_next_down = "次HP" + str(int(self.blue.down * self.DOWN_HP)) + "を切ったらダウン。"
                        self.print_text = blue_next_down + '\n'
                        print(self.print_text)
                        self.log_text += self.print_text
                        time.sleep(self.sleeptime)                        
                    elif self.blue.hp <= 0:
                        blue_ko = self.blue.name + "選手KO。" + self.red.name + "選手の勝利。"
                        self.print_text = blue_ko + '\n'
                        print(self.print_text)
                        self.log_text += self.print_text
                        with open(self.log_title, mode='w', encoding='utf-8') as f:
                            f.write(self.log_text)
                        time.sleep(self.sleeptime)
                        break

            elif  blue_dice_sum > red_dice_sum:
                self.red.before_hp = self.red.hp
                damage = blue_dice_sum - red_dice_sum
                self.red.hp -= damage
                red_damage_result = self.red.name + "選手に" + str(damage) + "のダメージ"
                dice_result = "赤コーナー:" + self.red.name + ":" + str(red_dice) + "=" + str(red_dice_sum) + " " + "青コーナー:" + self.blue.name + ":" + str(blue_dice) + "=" + str(blue_dice_sum)
                hp_result = "赤コーナー:" + self.red.name + ":HP" + str(self.red.hp) + " vs " + "青コーナー:" + self.blue.name + ":HP" + str(self.blue.hp)

                self.print_text = round_turn + '\n' + dice_result + '\n' + red_damage_result + '\n' + hp_result + '\n'

                print(self.print_text)

                self.log_text += self.print_text
                time.sleep(self.sleeptime)

                if self.red.hp != self.HP and self.red.hp < (self.red.down * self.DOWN_HP + 1) and (self.red.before_hp > self.red.down * self.DOWN_HP):
                    self.red.down_count += 1
                    red_down_result = self.red.name + "選手、この試合通算" + str(self.red.down_count) + "回目のダウン。"
                    self.print_text = red_down_result + '\n'
                    print(self.print_text)
                    self.log_text += self.print_text
                    if self.red.hp > 0 and self.red.hp % self.DOWN_HP == 0:
                        self.red.down = (self.red.hp / self.DOWN_HP) - 1
                        red_next_down = "次HP" + str(int(self.red.down * self.DOWN_HP)) + "を切ったらダウン。"
                        self.print_text = red_next_down + '\n'
                        print(self.print_text)
                        self.log_text += self.print_text
                        time.sleep(self.sleeptime)
                    elif self.red.hp > 0 and self.red.hp % self.DOWN_HP != 0:
                        self.red.down = math.floor(self.red.hp / self.DOWN_HP)
                        red_next_down = "次HP" + str(int(self.red.down * self.DOWN_HP)) + "を切ったらダウン。"
                        self.print_text = red_next_down + '\n'
                        print(self.print_text)
                        self.log_text += self.print_text
                        time.sleep(self.sleeptime)                        
                    elif self.red.hp <= 0:
                        red_ko = self.red.name + "選手KO。" + self.blue.name + "選手の勝利。"
                        self.print_text = red_ko + '\n'
                        print(self.print_text)
                        self.log_text += self.print_text
                        with open(self.log_title, mode='w', encoding='utf-8') as f:
                            f.write(self.log_text)
                        time.sleep(self.sleeptime)
                        break

            else:
                self.red.before_hp = self.red.hp
                self.blue.before_hp = self.blue.hp
                heal = 1

                if self.red.hp < self.HP:
                    self.red.hp += heal
                if self.blue.hp < self.HP:
                    self.blue.hp += heal
                
                dice_result = "赤コーナー:" + self.red.name + ":" + str(red_dice) + "=" + str(red_dice_sum) + " " + "青コーナー:" + self.blue.name + ":" + str(blue_dice) + "=" + str(blue_dice_sum)
                hp_result = "赤コーナー:" + self.red.name + ":HP" + str(self.red.hp) + " vs " + "青コーナー:" + self.blue.name + ":HP" + str(self.blue.hp)
                red_heal = self.red.name + "選手HP1回復。"
                blue_heal = self.blue.name + "選手HP1回復。"
                both_heal = "両者HP1回復。"
                turn_elapsed = "1ターン経過。"

                self.print_text = round_turn + '\n' + dice_result + '\n'
                print(self.print_text)
                self.log_text += self.print_text

                if self.red.before_hp < self.HP and self.blue.before_hp == self.HP:
                    self.print_text = red_heal + '\n'
                    
                elif self.blue.before_hp < self.HP and self.red.before_hp == self.HP:
                    self.print_text = blue_heal + '\n'
                    
                elif self.red.before_hp < self.HP and self.blue.before_hp < self.HP:
                    self.print_text = both_heal + '\n'
                    
                else:
                    self.print_text = turn_elapsed + '\n'
                
                self.print_text += hp_result + '\n'
                print(self.print_text)
                self.log_text += self.print_text

                if self.red.hp > 0 and self.red.hp % self.DOWN_HP == 0:
                    self.red.down = (self.red.hp / self.DOWN_HP) - 1
                    red_next_down = "赤コーナー:" + self.red.name + "選手、次HP" + str(int(self.red.down * self.DOWN_HP)) + "を切ったらダウン。"
                    self.print_text = red_next_down + '\n'
                    print(self.print_text)
                    self.log_text += self.print_text
                    time.sleep(self.sleeptime)
                elif self.red.hp > 0 and self.red.hp % self.DOWN_HP != 0:
                    self.red.down = math.floor(self.red.hp / self.DOWN_HP)
                    red_next_down = "赤コーナー:" + self.red.name + "選手、次HP" + str(int(self.red.down * self.DOWN_HP)) + "を切ったらダウン。"
                    self.print_text = red_next_down + '\n'
                    print(self.print_text)
                    self.log_text += self.print_text
                    time.sleep(self.sleeptime)
                if self.blue.hp > 0 and self.blue.hp % self.DOWN_HP == 0:
                    self.blue.down = (self.blue.hp / self.DOWN_HP) - 1
                    blue_next_down = "青コーナー:" + self.blue.name + "選手、次HP" + str(int(self.blue.down * self.DOWN_HP)) + "を切ったらダウン。"
                    self.print_text = blue_next_down + '\n'
                    print(self.print_text)
                    self.log_text += self.print_text
                    time.sleep(self.sleeptime)
                elif self.blue.hp > 0 and self.blue.hp % self.DOWN_HP != 0:
                    self.blue.down = math.floor(self.blue.hp / self.DOWN_HP)
                    blue_next_down = "青コーナー:" + self.blue.name + "選手、次HP" + str(int(self.blue.down * self.DOWN_HP)) + "を切ったらダウン。"
                    self.print_text = blue_next_down + '\n'
                    print(self.print_text)
                    self.log_text += self.print_text
                    time.sleep(self.sleeptime)
            
            self.current_turn += 1

            if self.current_turn > 3:
                round_end = str(self.current_round) + "ラウンド終了。"
                self.print_text = round_end + '\n' + '\n'
                print(self.print_text)
                self.log_text += self.print_text
                self.current_round += 1
                self.current_turn = 1
                time.sleep(self.sleeptime)
            
            if self.current_round > self.MAX_ROUND:
                all_round_end = "全ラウンド終了。判定に入ります。"
                self.print_text = all_round_end + '\n'
                print(self.print_text)
                self.log_text += self.print_text
                time.sleep(self.sleeptime)

                red_judgment_win = self.red.name + "選手の判定勝利。"
                blue_judgment_win = self.blue.name + "選手の判定勝利。"
                judgment_draw = "本試合、引き分けで終了。"


                if self.red.hp > self.blue.hp:
                    self.print_text = hp_result + '\n' + red_judgment_win
                    print(self.print_text)
                    self.log_text += self.print_text
                    with open(self.log_title, mode='w', encoding='utf-8') as f:
                            f.write(self.log_text)
                    time.sleep(self.sleeptime)
                    break
                elif self.blue.hp > self.red.hp:
                    self.print_text = hp_result + '\n' + blue_judgment_win
                    print(self.print_text)
                    self.log_text += self.print_text
                    with open(self.log_title, mode='w', encoding='utf-8') as f:
                            f.write(self.log_text)
                    time.sleep(self.sleeptime)
                    break
                else:
                    self.print_text = hp_result + '\n' + judgment_draw
                    print(self.print_text)
                    self.log_text += self.print_text
                    with open(self.log_title, mode='w', encoding='utf-8') as f:
                            f.write(self.log_text)
                    time.sleep(self.sleeptime)
                    break

SLEEPTIME = 3

# 対戦ログ保存フォルダ作成
FIGHT_LOG_DIR = make_folder()
# HP決定
HP = decide_HP()
# ダウンHP数決定
DOWN_HP = decide_down_hp()

# ダイスの個数決定
dice_num = decide_dice_num()
# ダイスの面数決定
dice_size = decide_dice_size()
# ダイス作成
DICE = Dice(dice_num, dice_size)
# print(dice.throw_dice())

# 赤コーナーのボクサー作成
print('赤コーナーの選手を作成します')
red_boxer = boxer_create()
# 青コーナーのボクサー作成
print('青コーナーの選手を作成します')
blue_boxer = boxer_create()

# ラウンド数決定
MAX_ROUND = decide_max_round()
# タイトル決定
title = make_title_call(red_boxer, blue_boxer, MAX_ROUND)
print('\n')
fight_datetime = datetime.now().strftime("%Y%m%d%H%M%S")
log_title = FIGHT_LOG_DIR + '/' + fight_datetime + '_' + title + '.txt'
match = Match(hp=HP, down_hp=DOWN_HP, red_boxer=red_boxer, blue_boxer=blue_boxer, title=title, log_title=log_title, max_round=MAX_ROUND, sleeptime=SLEEPTIME)
match.fight()