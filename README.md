# LINEチャットデータのファインチューニング用データセット化ツール

このリポジトリは、LINEのチャットデータをファインチューニング用のデータセットに変換するためのツールです。LINEから書き出したチャット履歴を読み込み、ユーザー・アシスタントの会話形式に適切に整形し、モデルのファインチューニングに利用できるデータセットを生成します。

## 機能

- LINEのチャット履歴を読み込み、指定したユーザーを`user`、他の会話相手を`assistant`として扱うデータセットを作成
- `datasets/` ディレクトリにファインチューニング用のJSONデータとして保存
- プロンプト（`user`の発言）と応答（`assistant`の返答）のペアを自動で生成

## 実行方法

### 1. リポジトリをクローンします
```bash
git clone git@github.com:Kida-Takuma/create-datasets-frome-line-app.git
cd create-datasets-frome-line-app
```

### 2. 実行コマンド
以下のコマンドでスクリプトを実行し、LINEのチャットデータをファインチューニング用データセットに変換します。

```bash
python app.py <path_to_line_chat_data>
```

#### 例:
```bash
python app.py ./data/line_chat.txt
```

### 3. 出力
実行が完了すると、指定したLINEのチャットデータがファインチューニング用のデータセット形式に変換されます。変換されたデータセットは、`datasets/` ディレクトリ内にタイムスタンプ付きのファイル名で保存されます。

出力ファイル例:
```
datasets/finetune_dataset_`日時`.json
```


