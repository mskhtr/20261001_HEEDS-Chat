# HEEDS チャット（水準をそろえずに実行）

スタディごとに入力水準をそろえない版です。CSV の下限・上限・刻みは各 Study に渡しますが、水準の中身は Study 側の HEEDS が作るので、crash の水準1と固有値の水準1が同じ板厚・同じ幅とは限りません。入力の組が違う行は、横断表で片方の出力が「—」になります。決め方は [docs/04_SPEC.md](docs/04_SPEC.md) の「水準はスタディごと」にあります。

ブラウザのチャットに設計要件を書くと、実行する試験と変数を確認したうえで、HEEDS|MDO のスタディを実行し、結果を返します。計算そのものは HEEDS が行います。同意があるまで HEEDS は動きません。

言葉と試験の対応は [heeds/catalog.yaml](heeds/catalog.yaml) だけに書いてあります。開始画面の表も、確認文も、実際に実行する試験も、そこから作ります。

```mermaid
flowchart LR
  words["チャットの文"] --> catalog["catalog.yaml"]
  catalog --> ask["確認文"]
  ask --> yes["はい"]
  yes --> heeds["HEEDS"]
```

## 人が編集するもの

| 変えたいこと | 編集する場所 |
| --- | --- |
| チャットの言葉、実行する試験の組み合わせ、HEEDS 画面の Study 名 | `heeds/catalog.yaml`。編集後にチャットを起動し直す |
| この PC だけ Study 名がカタログと違う | `.env` に `HEEDS_STUDY_<試験IDの大文字>` を1行 |
| API キーと HEEDS のパス | `.env` |
| 振る変数 | チャットに添付する CSV |

使う `.heeds` ファイルは、同梱の
[`HEEDS_PROJECT/`](HEEDS_PROJECT/README.md)へ置けます。別の場所でも構いませんが、
`.env` の `HEEDS_PROJECT_PATH` は実際のフルパスに合わせます。

## 必要なもの

| 項目 | 要件 |
| --- | --- |
| OS | Windows |
| Python | 3.12 |
| AI | Azure OpenAI（実行後の要約。試験の選択には使いません） |
| HEEDS | HEEDS\|MDO と、`.heeds` プロジェクト |

## 文書

実務は次の2つです。仕組みを知るときは、そのあと `docs/` をファイル名の番号順（01 → 09）で読んでください。

| 知りたいこと | 文書 |
| --- | --- |
| インストールと `.env` | [docs/セットアップ.md](docs/セットアップ.md) |
| 起動と確認 | [docs/動かし方.md](docs/動かし方.md) |
| 全体像・用語 | [docs/01_はじめに.md](docs/01_はじめに.md) |
| ファイルのつながり | [docs/02_ファイルの関連.md](docs/02_ファイルの関連.md) |
| 設定変数の意味 | [docs/03_変数と設定.md](docs/03_変数と設定.md) |
| 仕様・スタディごとの水準・会話の例・限界 | [docs/04_SPEC.md](docs/04_SPEC.md) |
| HEEDS 実機への接続 | [docs/05_HEEDS接続.md](docs/05_HEEDS接続.md) |
| HEEDS プロジェクトを作るときの名前 | [docs/06_HEEDSファイルを作るとき.md](docs/06_HEEDSファイルを作るとき.md) |
| プログラム設定と HEEDS の突き合わせ | [docs/07_設定チェック.md](docs/07_設定チェック.md) |
| チャットの要件や解析を変える | [docs/08_試験の種類を変える.md](docs/08_試験の種類を変える.md) |
| 起動から終了まで、ファイルごとの入出力 | [docs/09_起動から終了までの流れ.md](docs/09_起動から終了までの流れ.md) |

エディタは Visual Studio Code を推奨します。Markdown の図（mermaid）を見るときは、拡張機能 Markdown Preview Mermaid Support を入れるか、GitHub 上で開いてください。
