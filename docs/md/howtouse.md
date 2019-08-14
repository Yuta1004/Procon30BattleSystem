# Procon30 Battle System ~How To Use~

## 目次

1. 試合で遊ぶ

## 1. 試合で遊ぶ

### 1-1 CUI-Client起動

　CUI-Clientを起動します。

```
> make cui-client

Procon30 Battlle Syatem CUI Client ver0.0.1
Welcome user

Host URL: ******
Checking connection ... OK

>>
```

### 1-2 チーム登録

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

### 1-3 試合を登録する

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

### 1-4 試合を起動する

　試合を起動します。  
　下コマンドでは、先ほど登録した試合「TestBattle」を起動しています。

```
>> start 22
battle started! ( battle_id: 22 }
```

### 1-5 GUI-Clientを起動する

　GUI-Clientを起動します。

```
> make gui-client
===================================================
   G4P V4.2.1 created by Peter Lager
===================================================
```

　起動するとトップ画面が表示されます。

![Imgur](https://i.imgur.com/rmvDh9S.png)

### 1-6 トークン入力

　トークンを入力します。  
　画像では先ほど登録した「TestTeamA」のトークンを入力しています。

![Imgur](https://i.imgur.com/8wNfuI9.png)

### 1-7 参加試合選択

　参加する試合を選択します。  
　画像では先ほど登録した「TestBattle」を選択しています。

![Imgur](https://i.imgur.com/5eIG6Oj.png)

### 1-8 エージェントを操作する

　エージェントをクリックして移動方向選択ボタンを表示させます。そして、方向を選択して行動情報をシステムに送信します。

![Imgur](https://i.imgur.com/jrJSPtP.png)
