# Procon30 Battle System API

## Version

v1.1.2

## 公式API

　本システムはプロコン運営が公式に発表しているAPIを全て実装しています。API仕様は公式ページを確認して下さい。

[ProconAPI (v0.0.1)](https://procon30resources.s3-ap-northeast-1.amazonaws.com/index.html#)

## システム独自API

　試合の管理を行う本システム独自のAPIです。このAPIは公式の試合では使用出来ません。

### 開催中試合一覧取得(GET)

　現在開催中の試合データ一覧を返します。

```
/battle
```

#### 返される値

　以下の要素からなる配列が返されます。

- 試合ID
- 試合名
- 試合開始時刻(UNIX時間)
- 試合のターン数
- 試合1ターンあたりの時間(ミリ秒)
- 試合のターンととターンの間の時間(ミリ秒)
- 試合参加チームID A
- 試合参加チームID B

　データ例を以下に示します。

```
// 0        -> integer
// "string" -> string

{
    [
        "battleID": 0,
        "name": "string",
        "startAtUnixTime": 0,
        "turn": 0,
        "turnMillis": 0,
        "intervalMillis": 0,
        "teamA": 0,
        "teamB": 0
    ]
}
```

#### HTTPステータスコード

- 200 : 正常に処理されました

---

### 試合情報取得(GET)

　指定された試合IDの情報を、開催中かどうかに関わらず返します。

```
/battle/{battleID}
```

#### 返される値

　以下の要素が返されます。

- 試合ID
- 試合名
- 試合開始時刻(UNIX時間)
- 試合のターン数
- 試合1ターンあたりの時間(ミリ秒)
- 試合のターンととターンの間の時間(ミリ秒)
- 試合参加チームID A
- 試合参加チームID B

　データ例を以下に示します。

```
// 0        -> integer
// "string" -> string

{
    "battleID": 0,
    "name": "string",
    "startAtUnixTime": 0,
    "turn": 0,
    "turnMillis": 0,
    "intervalMillis": 0,
    "teamA": 0,
    "teamB": 0
}
```

#### HTTPステータスコード

- 200 : 正常に処理されました
- 401 : 試合IDが不正です

---

### 試合登録(POST)

　試合を新規登録します。

```
/battle/register
```

#### POSTデータ

　以下の要素からなるJSONオブジェクトをPOSTして下さい。

　(注意)公開盤面を使用する場合、以下の値は**無視**されます。

```
- プレイヤー人数
- 盤面サイズ(幅)
- 盤面サイズ(縦)
- 配置得点下限値
- 配置得点上限値
- 盤面生成パターン
```

- 試合名
- 試合開始時刻(UNIX時間)
- 試合のターン数
- 試合1ターンあたりの時間(ミリ秒)
- 試合のターンととターンの間の時間(ミリ秒)
- 試合参加チームID A
- 試合参加チームID B
- プレイヤー人数
  - 1チームの人数
- 盤面サイズ(幅)
- 盤面サイズ(縦)
- 配置得点下限値
- 配置得点上限値
- 公開盤面を使用する場合、その名前
- 盤面生成パターン
  - 0 : 左右・上下のどちらかに線対称
  - 1 : 左右・上下のどちらにも線対称
  - 2 : 点対称

　データ例を以下に示します。

```
// 0        -> integer
// "string" -> string

{
    "name": "string",
    "startAtUnixTime": 0,
    "turn": 0,
    "turnMillis": 0,
    "intervalMillis": 0,
    "teamA": 0,
    "teamB": 0,
    "playerNum: 0,
    "width": 0,
    "height": 0,
    "pointLower": 0,
    "pointUpper": 0,
    "use_exist_board": "",
    "generateBoardType": 0
}
```

#### HTTPステータスコード

- 200 : 正常に処理されました

---

### 試合起動

　指定された試合IDの試合を起動します。

```
/battle/start/{battleID}
```

#### HTTPステータスコード

- 200 : 試合が正常に起動しました
- 400 : 指定された試合IDの試合は既に起動されています

---

### 試合終了

　指定された試合を終了させます。

```
/battle/finish/{battleID}
```

#### HTTPステータスコード

- 200 : 試合は正常に終了しました
- 400 : 試合IDが不正です
