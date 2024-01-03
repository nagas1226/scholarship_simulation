# 資産運用シミュレーションアプリ
このアプリケーションは、奨学金の返済と同時に資産運用を行った場合の資産推移をモンテカルロ・シミュレーションして可視化するための Streamlit アプリです。
![スクリーンショット](./img/screenshot.png "サンプル")
## 使用法
1. GitHub リポジトリのクローン
ターミナルを開き、以下のコマンドを実行して、GitHub リポジトリをローカルにクローンします。
```bash
git clone git@github.com:nagas1226/scholarship_simulation.git
```

2. クローンしたディレクトリに移動
```bash
cd schalarship_simulation
```

3. Docker イメージのビルド
以下のコマンドを使用して、Docker イメージをビルドします。
```bash
docker build -t schalarship_simulation .
```

4. Docker コンテナの実行
ビルドした Docker イメージを使用して、コンテナを実行します。
```bash
docker run -p 8501:8501 schalarship_simulation
```