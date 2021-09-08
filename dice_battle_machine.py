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
        print(self.name + ' ' + 'HP:' + str(self.hp))

# 表示言語を選択する関数
def decide_disp_lang():
    while True:
        disp_lang = input(
            '表示言語を番号で選択してください。\n'
            'Please select the display language by number.\n'
            '\n'
            '1:日本語(Japanese)\n'
            '2:英語(English)\n'
            )
        try:
            disp_lang = int(disp_lang)
        except ValueError:
            print("数字を入力してください。")
        else:
            if disp_lang < 1 or disp_lang > 2:
                print(
                    '1か2で選択してください。\n'
                    'Please select one or two.'
                    )
            elif disp_lang == 1:
                print('選択言語:日本語')
                return disp_lang
            else:
                print('Display language:English')
                return disp_lang

# 両選手の最大HPを決定する関数
def decide_HP(disp_lang):
    while True:
        if disp_lang == 1:
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
        else:
            HP = input("Enter the value of the player's HP (a number greater than or equal to 1):")
            try:
                HP = int(HP)
            except ValueError:
                print("Please enter a number.")
            else:
                if HP <= 0:
                    print("Please enter a number greater than or equal to 1.")
                else:
                    print("HP:" + str(HP))
                    return HP

# ボクサーを作成する関数
def boxer_create(disp_lang):
    while True:
        if disp_lang == 1:
            boxer_name = input("選手の名前を入力してください:")
            if boxer_name == "":
                print("選手の名前を入力してください")
            else:
                boxer = Boxer(boxer_name, HP, DOWN_HP, DICE)
                return boxer
        else:
            boxer_name = input("Please enter name of player:")
            if boxer_name == "":
                print("Please enter name of player.")
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
def decide_dice_num(disp_lang):
    while True:
        if disp_lang == 1:
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
        else:
            dice_num = input("How many dice do you want to use? Please enter a number. Example: 2d6 for '2' :")
            try:
                dice_num = int(dice_num)
            except ValueError:
                print("Please enter a number.")
            else:
                if dice_num <= 0:
                    print("Please enter a number greater than or equal to 1.")
                elif dice_num == 1:
                    print(str(dice_num) + ' dice')
                    return dice_num
                else:
                    print(str(dice_num) + " dices")
                    return dice_num

# ダイスの面数を決定する関数
def decide_dice_size(disp_lang):
    while True:
        if disp_lang == 1:
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
        else:
            dice_size = input("How much size of the dice do you want to use? Please enter a number. For example: '6' for 2d6:")
            try:
                dice_size = int(dice_size)
            except ValueError:
                print("Please enter a number.")
            else:
                if dice_size <= 0:
                    print("Please enter a number greater than or equal to 1.")
                else:
                    print(str(dice_size) + "-sided")
                    return dice_size

# ダウンするHPの数を決定する関数
def decide_down_hp(disp_lang):
    while True:
        if disp_lang == 1:
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
        else:
            down_hp = input("How many damage each do you want to take down? Please enter a number:")
            try:
                down_hp = int(down_hp)
            except ValueError:
                print("Please enter a number.")
            else:
                if down_hp <= 0:
                    print("Please enter a number greater than or equal to 1.")
                else:
                    print("Down for every {} HP of damage".format(str(down_hp)))
                    return down_hp

# 試合タイトルを決定する関数
def make_title_call(disp_lang, red_boxer, blue_boxer, max_round):
    while True:
        if disp_lang == 1:
            match_title = input('試合形式を入力してください。例:「日本フライ級ランキング」「バンタム級世界タイトルマッチ」etc:')
            if match_title == '':
                print('試合形式を入力してください。')
            else:
                title = match_title + str(max_round) + '回戦' + '_' + red_boxer.name + '_VS_' + blue_boxer.name
                return title
        else:
            match_title = input('Please enter the match format. Example: "Japanese Flyweight Ranking", "Bantamweight World Title Match", etc:')
            if match_title == '':
                print('Please enter the match format.')
            else:
                title = match_title + '_' + str(max_round) + 'rounds' + '_' + red_boxer.name + '_VS_' + blue_boxer.name
                return title

# ラウンド数を決定する関数
def decide_max_round(disp_lang):
    while True:
        if disp_lang == 1:
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
        else:
            max_round = input('Enter a number greater than or equal to 1 for the maximum number of rounds. :')
            try:
                max_round = int(max_round)
            except ValueError:
                print('Please enter a number.')
            else:
                if max_round <= 0:
                    print('Please enter a number greater than or equal to 1.')
                else:
                    print(str(max_round) + ' rounds match')
                    return max_round

# 試合のクラス
class Match:
    def __init__(self, disp_lang, hp, down_hp, red_boxer, blue_boxer, title, log_title, max_round, sleeptime) :
        # 最大HP数
        self.HP = hp
        # ダウンHP数
        self.DOWN_HP = down_hp
        # 赤コーナーボクサー
        self.red = red_boxer
        # self.red_dice = []
        # self.red_dice_sum = 0
        # 青コーナーボクサー
        self.blue = blue_boxer
        # self.blue_dice = []
        # self.blue_dice_sum = 0
        # self.damage = 0
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
        self.jp_text = {
            'match_start':"{}\n試合開始!\n\n",
            'round_turn':"{}ラウンド{}ターン目",
            'damage_result':"{}選手に{}のダメージ",
            'dice_result':"赤コーナー:{}:{}={}" + " " + "青コーナー:{}:{}={}",
            'hp_result':"赤コーナー:{}:HP{} vs " + "青コーナー:{}:HP{}",
            'down_result':"{}選手、この試合通算{}回目のダウン。",
            'next_down':"{}選手、次HP{}を切ったらダウン。",
            'ko':"{}選手KO。{}選手の勝利。",
            'heal':"{}選手HP1回復。",
            'both_heal':"両者HP1回復。",
            'turn_elapsed':"1ターン経過。",
            'round_end':"{}ラウンド終了。",
            'all_round_end':"全ラウンド終了。判定に入ります。",
            'judgment_win':"{}選手の判定勝利。",
            'judgment_draw':"本試合、引き分けで終了。"
            }
        self.eng_text = {
            'match_start':"{}\nLet the match begin!\n\n",
            'round_turn':"ROUND {} Turn {}",
            'damage_result':"{} damages for {}.",
            'dice_result':"Red corner:{}:{}={} Blue corner:{}:{}={}",
            'hp_result':"Red corner:{}:HP{} vs Blue corner:{}:HP{}",
            'down_result':"{}'s number of times down:{}",
            'next_down':"Next, if {}'s HP drops below {}, go down.",
            'ko':"{} is knockout. Winner is {}.",
            'heal':"{} is healed 1HP.",
            'both_heal':"Both are healed 1HP.",
            'turn_elapsed':"1 turn elapsed.",
            'round_end':'Round {} ended.',
            'all_round_end':"All rounds are over. We go to decision.",
            'judgment_win':'By the judgment, winner is {}.',
            'judgment_draw':"This match ended in a draw."
            }
        if disp_lang == 1:
            self.disp_text = self.jp_text
        else:
            self.disp_text = self.eng_text
        # ターミナルに表示される文字列
        self.print_text = self.disp_text['match_start'].format(self.title)
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

            # round_turn = str(self.current_round) + "ラウンド" + str(self.current_turn) + "ターン目"
            round_turn = self.disp_text['round_turn'].format(str(self.current_round), str(self.current_turn))

            if red_dice_sum > blue_dice_sum:
                self.blue.before_hp = self.blue.hp
                damage = red_dice_sum - blue_dice_sum
                self.blue.hp -= damage
                # blue_damage_result = self.blue.name + "選手に" + str(damage) + "のダメージ"
                if disp_lang == 1:
                    blue_damage_result = self.disp_text['damage_result'].format(self.blue.name, str(damage))
                else:
                    blue_damage_result = self.disp_text['damage_result'].format(str(damage), self.blue.name)
                # dice_result = "赤コーナー:" + self.red.name + ":" + str(red_dice) + "=" + str(red_dice_sum) + " " + "青コーナー:" + self.blue.name + ":" + str(blue_dice) + "=" + str(blue_dice_sum)
                dice_result = self.disp_text['dice_result'].format(self.red.name, str(red_dice), str(red_dice_sum), self.blue.name, str(blue_dice), str(blue_dice_sum))
                # hp_result = "赤コーナー:" + self.red.name + ":HP" + str(self.red.hp) + " vs " + "青コーナー:" + self.blue.name + ":HP" + str(self.blue.hp)
                hp_result = self.disp_text['hp_result'].format(self.red.name, str(self.red.hp), self.blue.name, str(self.blue.hp))

                self.print_text = round_turn + '\n' + dice_result + '\n' + blue_damage_result + '\n' + hp_result + '\n'

                print(self.print_text)

                self.log_text += self.print_text
                time.sleep(self.sleeptime)

                if self.blue.hp != self.HP and self.blue.hp < (self.blue.down * self.DOWN_HP + 1) and (self.blue.before_hp > self.blue.down * self.DOWN_HP):
                    self.blue.down_count += 1
                    # blue_down_result = self.blue.name + "選手、この試合通算" + str(self.blue.down_count) + "回目のダウン。"
                    blue_down_result = self.disp_text['down_result'].format(self.blue.name, str(self.blue.down_count))
                    self.print_text = blue_down_result + '\n'
                    print(self.print_text)
                    self.log_text += self.print_text
                    if self.blue.hp > 0 and self.blue.hp % self.DOWN_HP == 0:
                        self.blue.down = (self.blue.hp / self.DOWN_HP) - 1
                        # blue_next_down = "次HP" + str(int(self.blue.down * self.DOWN_HP)) + "を切ったらダウン。"
                        blue_next_down = self.disp_text['next_down'].format(self.blue.name, str(int(self.blue.down * self.DOWN_HP)))
                        self.print_text = blue_next_down + '\n'
                        print(self.print_text)
                        self.log_text += self.print_text
                        time.sleep(self.sleeptime)
                    elif self.blue.hp > 0 and self.blue.hp % self.DOWN_HP != 0:
                        self.blue.down = math.floor(self.blue.hp / self.DOWN_HP)
                        # blue_next_down = "次HP" + str(int(self.blue.down * self.DOWN_HP)) + "を切ったらダウン。"
                        blue_next_down = self.disp_text['next_down'].format(self.blue.name, str(int(self.blue.down * self.DOWN_HP)))
                        self.print_text = blue_next_down + '\n'
                        print(self.print_text)
                        self.log_text += self.print_text
                        time.sleep(self.sleeptime)                        
                    elif self.blue.hp <= 0:
                        # blue_ko = self.blue.name + "選手KO。" + self.red.name + "選手の勝利。"
                        blue_ko = self.disp_text['ko'].format(self.blue.name, self.red.name)
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
                # red_damage_result = self.red.name + "選手に" + str(damage) + "のダメージ"
                if disp_lang == 1:
                    red_damage_result = self.disp_text['damage_result'].format(self.red.name, str(damage))
                else:
                    red_damage_result = self.disp_text['damage_result'].format(str(damage), self.red.name)
                # dice_result = "赤コーナー:" + self.red.name + ":" + str(red_dice) + "=" + str(red_dice_sum) + " " + "青コーナー:" + self.blue.name + ":" + str(blue_dice) + "=" + str(blue_dice_sum)
                dice_result = self.disp_text['dice_result'].format(self.red.name, str(red_dice), str(red_dice_sum), self.blue.name, str(blue_dice), str(blue_dice_sum))
                # hp_result = "赤コーナー:" + self.red.name + ":HP" + str(self.red.hp) + " vs " + "青コーナー:" + self.blue.name + ":HP" + str(self.blue.hp)
                hp_result = self.disp_text['hp_result'].format(self.red.name, str(self.red.hp), self.blue.name, str(self.blue.hp))

                self.print_text = round_turn + '\n' + dice_result + '\n' + red_damage_result + '\n' + hp_result + '\n'

                print(self.print_text)

                self.log_text += self.print_text
                time.sleep(self.sleeptime)

                if self.red.hp != self.HP and self.red.hp < (self.red.down * self.DOWN_HP + 1) and (self.red.before_hp > self.red.down * self.DOWN_HP):
                    self.red.down_count += 1
                    # red_down_result = self.red.name + "選手、この試合通算" + str(self.red.down_count) + "回目のダウン。"
                    red_down_result = self.disp_text['down_result'].format(self.red.name, str(self.red.down_count))
                    self.print_text = red_down_result + '\n'
                    print(self.print_text)
                    self.log_text += self.print_text
                    if self.red.hp > 0 and self.red.hp % self.DOWN_HP == 0:
                        self.red.down = (self.red.hp / self.DOWN_HP) - 1
                        # red_next_down = "次HP" + str(int(self.red.down * self.DOWN_HP)) + "を切ったらダウン。"
                        red_next_down = self.disp_text['next_down'].format(self.red.name, str(int(self.red.down * self.DOWN_HP)))
                        self.print_text = red_next_down + '\n'
                        print(self.print_text)
                        self.log_text += self.print_text
                        time.sleep(self.sleeptime)
                    elif self.red.hp > 0 and self.red.hp % self.DOWN_HP != 0:
                        self.red.down = math.floor(self.red.hp / self.DOWN_HP)
                        # red_next_down = "次HP" + str(int(self.red.down * self.DOWN_HP)) + "を切ったらダウン。"
                        red_next_down = self.disp_text['next_down'].format(self.red.name, str(int(self.red.down * self.DOWN_HP)))
                        self.print_text = red_next_down + '\n'
                        print(self.print_text)
                        self.log_text += self.print_text
                        time.sleep(self.sleeptime)                        
                    elif self.red.hp <= 0:
                        # red_ko = self.red.name + "選手KO。" + self.blue.name + "選手の勝利。"
                        red_ko = self.disp_text['ko'].format(self.red.name, self.blue.name)
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
                
                # dice_result = "赤コーナー:" + self.red.name + ":" + str(red_dice) + "=" + str(red_dice_sum) + " " + "青コーナー:" + self.blue.name + ":" + str(blue_dice) + "=" + str(blue_dice_sum)
                dice_result = self.disp_text['dice_result'].format(self.red.name, str(red_dice), str(red_dice_sum), self.blue.name, str(blue_dice), str(blue_dice_sum))
                # hp_result = "赤コーナー:" + self.red.name + ":HP" + str(self.red.hp) + " vs " + "青コーナー:" + self.blue.name + ":HP" + str(self.blue.hp)
                hp_result = self.disp_text['hp_result'].format(self.red.name, str(self.red.hp), self.blue.name, str(self.blue.hp))
                # red_heal = self.red.name + "選手HP1回復。"
                red_heal = self.disp_text['heal'].format(self.red.name)
                # blue_heal = self.blue.name + "選手HP1回復。"
                blue_heal = self.disp_text['heal'].format(self.blue.name)
                # both_heal = "両者HP1回復。"
                both_heal = self.disp_text['both_heal']
                # turn_elapsed = "1ターン経過。"
                turn_elapsed = self.disp_text['turn_elapsed']

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
                    # red_next_down = "赤コーナー:" + self.red.name + "選手、次HP" + str(int(self.red.down * self.DOWN_HP)) + "を切ったらダウン。"
                    red_next_down = self.disp_text['next_down'].format(self.red.name, str(int(self.red.down * self.DOWN_HP)))
                    self.print_text = red_next_down + '\n'
                    print(self.print_text)
                    self.log_text += self.print_text
                    time.sleep(self.sleeptime)
                elif self.red.hp > 0 and self.red.hp % self.DOWN_HP != 0:
                    self.red.down = math.floor(self.red.hp / self.DOWN_HP)
                    # red_next_down = "赤コーナー:" + self.red.name + "選手、次HP" + str(int(self.red.down * self.DOWN_HP)) + "を切ったらダウン。"
                    red_next_down = self.disp_text['next_down'].format(self.red.name, str(int(self.red.down * self.DOWN_HP)))
                    self.print_text = red_next_down + '\n'
                    print(self.print_text)
                    self.log_text += self.print_text
                    time.sleep(self.sleeptime)
                if self.blue.hp > 0 and self.blue.hp % self.DOWN_HP == 0:
                    self.blue.down = (self.blue.hp / self.DOWN_HP) - 1
                    # blue_next_down = "青コーナー:" + self.blue.name + "選手、次HP" + str(int(self.blue.down * self.DOWN_HP)) + "を切ったらダウン。"
                    blue_next_down = self.disp_text['next_down'].format(self.blue.name, str(int(self.blue.down * self.DOWN_HP)))
                    self.print_text = blue_next_down + '\n'
                    print(self.print_text)
                    self.log_text += self.print_text
                    time.sleep(self.sleeptime)
                elif self.blue.hp > 0 and self.blue.hp % self.DOWN_HP != 0:
                    self.blue.down = math.floor(self.blue.hp / self.DOWN_HP)
                    # blue_next_down = "青コーナー:" + self.blue.name + "選手、次HP" + str(int(self.blue.down * self.DOWN_HP)) + "を切ったらダウン。"
                    blue_next_down = self.disp_text['next_down'].format(self.blue.name, str(int(self.blue.down * self.DOWN_HP)))
                    self.print_text = blue_next_down + '\n'
                    print(self.print_text)
                    self.log_text += self.print_text
                    time.sleep(self.sleeptime)
            
            self.current_turn += 1

            if self.current_turn > 3:
                # round_end = str(self.current_round) + "ラウンド終了。"
                round_end = self.disp_text['round_end'].format(str(self.current_round))
                self.print_text = round_end + '\n' + '\n'
                print(self.print_text)
                self.log_text += self.print_text
                self.current_round += 1
                self.current_turn = 1
                time.sleep(self.sleeptime)
            
            if self.current_round > self.MAX_ROUND:
                # all_round_end = "全ラウンド終了。判定に入ります。"
                all_round_end = self.disp_text['all_round_end']
                self.print_text = all_round_end + '\n'
                print(self.print_text)
                self.log_text += self.print_text
                time.sleep(self.sleeptime)

                # red_judgment_win = self.red.name + "選手の判定勝利。"
                red_judgment_win = self.disp_text['judgment_win'].format(self.red.name)
                # blue_judgment_win = self.blue.name + "選手の判定勝利。"
                blue_judgment_win = self.disp_text['judgment_win'].format(self.blue.name)
                # judgment_draw = "本試合、引き分けで終了。"
                judgment_draw = self.disp_text['judgment_draw']


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

# 表示言語決定
disp_lang = decide_disp_lang()

while True:
    # HP決定
    HP = decide_HP(disp_lang)
    # ダウンHP数決定
    DOWN_HP = decide_down_hp(disp_lang)

    # ダイスの個数決定
    dice_num = decide_dice_num(disp_lang)
    # ダイスの面数決定
    dice_size = decide_dice_size(disp_lang)
    # ダイス作成
    DICE = Dice(dice_num, dice_size)
    # print(dice.throw_dice())

    # 赤コーナーのボクサー作成
    if disp_lang == 1:
        print('赤コーナーの選手を作成します')
    else:
        print('Create a player in the red corner.')
    red_boxer = boxer_create(disp_lang)
    # 青コーナーのボクサー作成
    if disp_lang == 1:
        print('青コーナーの選手を作成します')
    else:
        print('Create a player in the blue corner.')
    blue_boxer = boxer_create(disp_lang)

    # ラウンド数決定
    MAX_ROUND = decide_max_round(disp_lang)
    # タイトル決定
    title = make_title_call(disp_lang, red_boxer, blue_boxer, MAX_ROUND)
    print('\n')
    fight_datetime = datetime.now().strftime("%Y%m%d%H%M%S")
    log_title = FIGHT_LOG_DIR + '/' + fight_datetime + '_' + title + '.txt'
    match = Match(hp=HP, disp_lang=disp_lang, down_hp=DOWN_HP, red_boxer=red_boxer, blue_boxer=blue_boxer, title=title, log_title=log_title, max_round=MAX_ROUND, sleeptime=SLEEPTIME)
    match.fight()
    if disp_lang == 1:
        continue_or_exit = input("もう1試合やりますか？　続ける場合「q」以外のキーを、終了する場合「q」を入力してください。:")
    else:
        continue_or_exit = input("Do you want to play one more game?　Enter any key other than 'q' to continue, or 'q' to quit. :")
    if continue_or_exit == 'q':
        break
