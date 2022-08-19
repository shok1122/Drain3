# 環境構築

anacondaで作る．

```bash
(base) kakei@kakei-1912-d01:~$ conda create -n drain3 python=3.6
```

drain3のインストール

```bash
(drain3) kakei@kakei-1912-d01:~$ pip install drain3
```

永続化するためにredisをインストール

```bash
(drain3) kakei@kakei-1912-d01:~$ pip install redis
```

drain3のリポジトリ（shok1122版）をpullする

```bash
(drain3) kakei@kakei-1912-d01:~/dev$ git clone https://github.com/shok1122/Drain3.git
(drain3) kakei@kakei-1912-d01:~/dev$ git checkout v0.9.11-dev
```

pipenvでパッケージをインストールするためにpipenvをインストール

```bash
(drain3) kakei@kakei-1912-d01:~/dev/Drain3$ pip install pipenv
```

pipenvでパッケージをインストール（drain3のディレクトリの中で）

```bash
(drain3) kakei@kakei-1912-d01:~/dev$ cd Drain3/
(drain3) kakei@kakei-1912-d01:~/dev/Drain3$ python -m pipenv sync
```

ログのグラフを作成するためにパッケージをインストール

```bash
conda install matplotlib
conda install networkx
conda install pygraphviz
```

# テスト

## ログの解析

リポジトリのディレクトリに入って，以下を実行．

```bash
(drain3) kakei@kakei-1912-d01:~/dev/Drain3$ python -m pipenv run python -m examples.drain_bigfile_demo-train
(drain3) kakei@kakei-1912-d01:~/dev/Drain3$ python -m pipenv run python -m examples.drain_bigfile_demo-test
```

## ロググラフの作成

```bash
(drain3) kakei@kakei-1912-d01:~/dev/Drain3$ python -m analysis.make_graph
```

/tmpディレクトリにグラフが出力される．
