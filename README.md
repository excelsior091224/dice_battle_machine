# dice_battle_machine
## 説明書（日本語版）
### このスクリプトについて
これは、ダイスを使って2人のキャラクターを戦わせるゲームです。

1回のターンごとに両者が指定された数・指定された面のダイスを振り、ダイスの出目が大きかったキャラクターが小さかったキャラクターに差分のダメージを与えます。

3回ターンが経過すると1ラウンド経過し、指定したラウンド数まで動作します。

どちらかのHP（体力）が0以下になるか、指定されたラウンドを終了したら試合終了です。

勝敗はどちらかのHPが0以下になったらKO（ノックアウト）、そうでなければHPの数で判定されます。

### 使用言語
Python3（Python 3.8.10でテスト済み）

### 遊び方
1. ページの「Code」→「Download Zip」でファイル一式をダウンロードし、任意のディレクトリに配置してください。gitが使える環境ならばクローンでも大丈夫です。
2. 実行方法
   1. MacまたはLinuxの場合
      1. Python3をインストールしてください。最新のものであることが望ましいです。
      2. ターミナル（端末）を起動してください。
      3. ターミナルにおいてcdコマンドを使ってdice_battle_machine.pyを配置したディレクトリに移動してください。
      4. `python3 dice_battle_machine.py`と入力して実行してください。
   2. WindowsでコマンドプロンプトもしくはPowerShellの使用に慣れている場合
      1. Python3をインストールしてください。最新のものであることが望ましいです。
      2. コマンドプロンプトもしくはPowerShellを起動してください。
      3. コマンドプロンプトもしくはPowerShellにおいてcdコマンドを使ってdice_battle_machine.pyを配置したディレクトリに移動してください。
      4. `python dice_battle_machine.py`と入力して実行してください。
   3. Windowsでコマンドプロンプト等の使用に慣れていない場合
      1. 「for_windows」ディレクトリ内の「dice_battle_machine.exe」を実行してください。
         * 注意: exe化にはnuitkaを使用していますが、対策ソフト等にマルウェアとして誤検出される可能性があります。その場合、大変申し訳ありませんが2の方法を使って実行してください。
3. 「表示言語を番号で選択してください。Please select the display language by number.　1:日本語(Japanese)　2:英語(English)」と表示されるので、1か2で選択してください。以後は選択した言語で表示されます。
4. 「選手のHPの値を入力してください（1以上の数字）:」と表示されるので、HP（ヒットポイント、体力）の値を1以上の整数で入力してください。
5. 「いくつのダメージごとにダウンさせますか？ 数字を入力してください:」と表示されるので、正の整数で入力してください。
6. 「何個のダイスを使いますか？ 数字を入力してください。例:2d6の場合「2」:」と表示されるので、正の整数で入力してください。
7. 「何面のダイスを使いますか？数字を入力してください。例:2d6の場合「6」:」と表示されるので、正の整数で入力してください。
8. 「赤コーナーの選手を作成します 選手の名前を入力してください:」と表示されるので、名前を決めて入力してください。
9. 「青コーナーの選手を作成します 選手の名前を入力してください:」と表示されるので、名前を決めて入力してください。
10. 「最大ラウンド数を1以上の数字で入力してください。:」と表示されるので、正の整数で入力してください。
11. 「試合形式を入力してください。例:「日本フライ級ランキング」「バンタム級世界タイトルマッチ」etc:」と表示されるので、入力してください。
12. 試合形式まで入力を終えると自動的に試合が開始されます。経過は端末に文字列で表示されるほか、プログラム起動時に自動作成されるディレクトリ「fight_log」内に試合終了時にtxtファイルで出力されます。
13. 試合が終了したら「もう1試合やりますか？　続ける場合「q」以外のキーを、終了する場合「q」を入力してください。:」と表示されるため「q」以外のキーを入力すればもう1回試合ができます。「q」を入力したらプログラムが終了します。

## Instruction manual (English version)
### About this script
This is a game that pits two characters against each other using dice.

Each turn, both players roll a specified number of dice on a specified side, and the character with the larger die roll deals differential damage to the character with the smaller die roll.

When three turns have passed, one round has passed, and the game runs for the specified number of rounds.

The match ends when either character's HP (physical strength) drops below zero or the specified round is completed.

Victory or defeat is judged by KO (knockout) if either player's hp falls below 0, otherwise by the number of HP.

### Language used
Python 3 (tested with Python 3.8.10)

### How to play
1. Download the complete set of files by clicking "Code" on the page, then "Download Zip", and place them in a directory of your choice. If you have access to git, you can clone it.
2. How to execute
  1. For Mac or Linux
     1. Install Python 3. It is preferable to have the latest version.
     2. Start the terminal.
     3. In a terminal, use the cd command to navigate to the directory where you have placed dice_battle_machine.py.
     4. Type `python3 dice_battle_machine.py` and run it.
  2. If you are familiar with using the command prompt or PowerShell in Windows
     1. Install Python 3. It is preferable to have the latest version.
     2. Launch the command prompt or PowerShell.
     3. Use the cd command at the command prompt or in PowerShell to navigate to the directory where you have placed dice_battle_machine.py.
     4. Type `python dice_battle_machine.py` and run it.
  3. If you are not familiar with using command prompts, etc. in Windows
     1. Run "dice_battle_machine.exe" in the "for_windows" directory.
        * Caution:nuitka is used for exeing, but it may be falsely detected as malware by anti-malware software.In that case, sorry about that, but you will have to use method 2 to do it.
3. "表示言語を番号で選択してください。Please select the display language by number.　1:日本語(Japanese)　2:英語(English)" will be displayed, please select 1 or 2. Thereafter, it will be displayed in the language you have selected.
4. "Enter the value of the player's HP (a number greater than or equal to 1):" will be displayed, please enter the HP (Hit Points, Strength) value as an integer greater than or equal to 1.
5. "How many damage each do you want to take down? Please enter a number:" will be displayed, please enter a positive integer.
6. "How many dice do you want to use? Please enter a number. Example: 2d6 for '2' :" will be displayed, please enter a positive integer.
7. "How much size of the dice do you want to use? Please enter a number. For example: '6' for 2d6:" will be displayed, please enter a positive integer.
8. "Create a player in the red corner. Please enter name of player:" will be displayed, please decide on a name and enter it.
9. "Create a player in the blue corner. Please enter name of player:" will be displayed, please decide on a name and enter it.
10. "Enter a number greater than or equal to 1 for the maximum number of rounds. :" will be displayed, please enter a positive integer.
11. "Please enter the match format. Example: "Japanese Flyweight Ranking", "Bantamweight World Title Match", etc:" will be displayed, please enter.
12. When you finish entering the match format, the match will automatically start. The progress will be displayed as a string on the terminal, and will be output as a txt file at the end of the match in the directory "fight_log" that is automatically created when the program starts.
13. When the game is over, you will be asked "Do you want to play one more game?　Enter any key other than 'q' to continue, or 'q' to quit. :". You can play one more game by typing any key other than "q". If you enter "q", the program will end.
