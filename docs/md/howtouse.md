# Procon30 Battle System ~How To Use~

## 目次

1. ダウンロード
1. 試合で遊ぶ

## 1. ダウンロード

### 1-1 対応OS

#### CUI-Client

UNIX実行ファイルが動作する環境

#### GUI-Client

- MacOS
- Linux (64bit)
- Linux Arm (64bit)

### 1-2 CUI-Clientダウンロード

　以下のURLよりCUI-Clientをダウンロードして下さい。  
　ダウンロード後は、任意のパスに解凍して下さい。

[CUI-Client(Google Drive](https://drive.google.com/open?id=1wnW0QmY9T0STfH7zcyKvlcYKuyPaPuyu)

### 1-3 GUI-Clientダウンロード

　以下のURLよりGUI-Clientをダウンロードして下さい。  
　ダウンロード後は、任意のパスに解凍して下さい。

[GUI-Client(Google Drive)](https://drive.google.com/open?id=149ygl5K_RXkOxxM8d54EAh2I7uDjUT5o)


## 2. 試合で遊ぶ

### 2-1 CUI-Client起動

　CUI-Clientを起動します。

```
> ./cui_client

Procon30 Battlle Syatem CUI Client ver0.0.1
Welcome user

Host URL: ******
Checking connection ... OK

>>
```

### 2-2 チーム登録

  CUI-Clientを使ってチームを登録します。
  既に登録を済ませている場合は必要ありません。1つのチームを同時に複数の試合に参加させることが出来ます。

```
>> register team
TeamName : TestTeamA
Token : TEAMA

register ok? y/N : y
register successed! ( TeamID: 7 )

>> register team
TeamName : TestTeamB
Token : TEAMB

register ok? y/N : y
register successed! ( TeamID: 8 )
```

### 2-3 試合を登録する

　CUI-Clientを使って試合を登録します。

```
>> register battle
BattleName : TestBattle
StartDateTime (Y) : 2019
StartDateTime (M) : 8
StartDateTime (D) : 1
StartDateTime (h) : 14
StartDateTime (m) : 0
StartDateTime (s) : 0
PlayerNum : 3
Turn : 30
TurnMillis (30000) : 30000
IntervalMillis (3000) : 3000
BoardWidth : 15
BoardHeight : 15
PointLower : -16
PointUpper : 16
TeamAID : 7
TeamBID : 8
GenerateBoardType (0) : 1

register ok? y/N : y
register successed! ( BattleID: 2 )
```

### 2-4 試合を起動する

　試合を起動します。  
　下コマンドでは、先ほど登録した試合「TestBattle」を起動しています。

```
>> start 22
battle started! ( battle_id: 22 }
```

### 2-5 GUI-Clientを起動する

　GUI-Clientを起動します。

```
// MacOS
> open gui_client.app
===================================================
   G4P V4.2.1 created by Peter Lager
===================================================
```

　起動するとトップ画面が表示されます。

![Imgur](https://i.imgur.com/rmvDh9S.png)

### 2-6 トークン入力

　トークンを入力します。  
　画像では先ほど登録した「TestTeamA」のトークンを入力しています。

![Imgur](https://i.imgur.com/8wNfuI9.png)

### 2-7 参加試合選択

　参加する試合を選択します。  
　画像では先ほど登録した「TestBattle」を選択しています。

![Imgur](https://i.imgur.com/5eIG6Oj.png)

### 2-8 エージェントを操作する

　エージェントをクリックして移動方向選択ボタンを表示させます。そして、方向を選択して行動情報をシステムに送信します。

![Imgur](https://i.imgur.com/jrJSPtP.png)
