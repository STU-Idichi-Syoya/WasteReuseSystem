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

# 初回設定
**ここではユーザのホームディレクトリで実行することを前提にします。**
```
cd ~
git clone https://github.com/STU-Idichi-Syoya/WasteReuseSystem/
cd  ~/WasteReuseSystem/ # 各自DLしたディレクトリまで移動しよう。
```
## Mac or Linux
```
python3 -m venv env
source env/bin/activate
pip3 install  -r requrements.txt
flask db init 
```
## Windows
```
python3 -m venv env
pip3 install -r requrements.txt　## うまくいかない場合、「開発を行うときにやる設定(毎回やること)」のwindowsの項を参照
flask db init 
```

# 開発を行うときにやる設定(毎回やること)
```
cd ~/WasteReuseSystem/
```
## Mac or Linux
```
source env/bin/activate
```
## windows
### コマンドプロンプトの場合
```
env\Scripts\activate.bat ## コマンドプロンプトの場合
```
### PowerShellの場合
```
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser -Force # 初回だけ実行
.env/Scripts/activate.ps1 # 毎回実行
```

# サーバ起動
## Mac or Linux
```
export FLASK_APP=project
export FLASK_DEBUG=1
flask run
```

## Windows
```
set FLASK_APP=project
set FLASK_DEBUG=1
flask run
```

# 開発作業終了
```
deactivete
```

# DBスキーマの変更
参考：https://flask-migrate.readthedocs.io/en/latest/
```
flask db migrate -m "msg..."
flask db upgrade
```
