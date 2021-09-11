# WasteReuseSystem（仮）  
CCC2021-NoobFighterReturnsの作品です.  

テスト状況：
![ branch parameter](https://github.com/STU-Idichi-Syoya/WasteReuseSystem/actions/workflows/main.yml/badge.svg?branch=main)

メンバーは
* 伊地知翔也 STU-Idichi-Syoya
* パニアグアカルロス https://github.com/carlos-paniagua
* すやま ゆいこ https://github.com/mt-sumikko
* 福田信斗 https://github.com/fukudanobuto
* Masashi Hashiguchi https://github.com/MasashiHashiguchi

# プロジェクトのDL
** ここではユーザのホームディレクトリで実行することを前提にします。
```
cd ~
git clone https://github.com/STU-Idichi-Syoya/WasteReuseSystem/
```

# 環境設定
PCを再起動したり、初めてプロジェクトを立ち上げるときに実行しましょう
```
cd ~ # 各自DLしたディレクトリまで移動しよう。
```
## Mac or Linux
```
source env/bin/activate
pip install -r requrements.txt
flask db init # 毎回しなくていい
```
## Windows
```
./env/Scripts/activate
pip install -r requrements.txt
flask db init # 毎回しなくていい
```

# サーバ起動
```
set FLASK_APP=project
set FLASK_DEBUG=1
flask run
```
# DBスキーマの変更
参考：https://flask-migrate.readthedocs.io/en/latest/
```
flask db upgrade
```

# 開発作業終了
```
deactivete
```
