# \#procon30 Battle System

## 概要

　第30回高等専門学校プログラミングコンテスト（以下、高専プロコン）競技部門「踊って舞って回って」で使用される競技システムを再現したものです。


## 仕様

　基本的な部分は、高専プロコン公式HPに掲載されている仕様に基づいて実装されています。なお、公開されていない内容については独自仕様としました。

- [競技ルール](http://www.procon.gr.jp/wp-content/uploads//2019/04/e3ca8e6e8c8d8ab1062729e66a711fea.pdf)
- [システム仕様](https://procon30resources.s3-ap-northeast-1.amazonaws.com/index.html#null%2Fpaths%2F~1ping%2Fget)


## システム構成

　本システムは 競技サーバ/CUIクライアント/GUIクライアント により構成されています。これらは独立して動作し、同環境で同時に動かした場合でも干渉し合いません。  
　その他、詳細な実装についてソースコードを参照してください。===


## ディレクトリ構成

- cui_client : CUIクライアント
- gui_client : GUIクライアント
- env : 環境変数ファイル
- server : 競技サーバソース
    - api_func : API向け処理プログラム
    - battle : 競技進行処理プログラム
    - common : 独立した関数群
    - db : DB操作系
    - simulator : ゲームシミュレータ
    - views : Flaskルート


## 使用方法

### Server

```
// 起動
make
make run

// テスト環境での起動
make run-test
```

ポート変更は `server/__init__.py`を編集して下さい。


### CUIClient

```
// 起動
make cui-client
```

### GUIClient

```
// 起動
make gui-client
```

ホストURLの変更は `cui_client/cui_client.py` の編集、もしくはプログラム内で行ってください。

## LICENCE

MIT  
Copyright (c) 2019 NakagamiYuta
