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

```
## Windows
```
./env/Scripts/activate
```

# サーバ起動
```
export FLASK_APP=project
export FLASK_DEBUG=1
flask run
```
# DBスキーマの変更
```
flask-migration
```

# 開発作業終了
```
deactivete
```