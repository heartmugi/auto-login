とある大学のポータルサイトに自動ログインするためのプログラム

必要な変数は別ファイルconfig.pyに格納（個人情報を非公開にするため）

以下，変数の説明:
- driver_path:
  - 自身のローカルでwebdriverを設置した場所(path)
- url:
  - 初めのログインページ
  - 具体的にはIDとパスワードを要求するページ
- id:
  - student ID
- password:
  - パスワード
- xpaths1:
  - idとpasswordを入力するフォームのpath
- xpaths2:
  - 3つのmatrixの英語を入力するフォームのpath
- matrix:
  - マトリックス表

以下のようなシェルスクリプトをホームディレクトリに置いておくと便利
```
python3 [..]/auto_login/main.py
```
