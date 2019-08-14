# Procon30 Battle System CUI-Client

## version

v1.1.2

## コマンド

### status

　サーバアドレスを表示します。

### set host

　サーバアドレスを設定します。

### check connection

　サーバとの接続確認をします。

### check token {TOKEN}

　引数で与えれたTOKENが正常なものか確認します。

### show battle {BattleID}

　引数で与えられたBattleIDの試合情報を表示します。
　BattleIDを指定しなかった場合、開催中の試合全ての情報を表示します。

### show team {TeamID}

　引数で与えられたTeamIDのチーム情報を表示します。
　TeamIDを指定しなかった場合、登録されているチーム全ての情報を表示します。

### register battle

　試合を新規登録します。ナビゲーションに従って必要情報を入力して下さい。
　登録が成功すると試合IDが表示されます。

### register team

　チームを新規登録します。ナビゲーションに従って必要情報を入力して下さい。
　登録が成功するとチームIDが表示されます。

### help

　コマンド一覧を表示します。

### exit

　CUI-Clientを終了します。