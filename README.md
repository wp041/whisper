## 概要
基本的にやってることは
[Whisperをローカル環境で使用する方法について #Python - Qiita](https://qiita.com/ussoewwin/items/37a464cd0baebb195275)
を参考に構築した環境を
pythonで動かすことによってmdを得る、ということをしている

元ネタがかなりシンプルなので、obsidianで使いやすい形に調整したファイルをdownloadフォルダに吐き出してくれるようにした

## 導入方法
（自分用メモ：2024-10-12-📝Whisper導入する.mdを参照する）

> [!WARNING]
> 出力先のファイルパスが適当に決めた絶対値になってるので必要に応じて修正する

1. [Whisperをローカル環境で使用する方法について #Python - Qiita](https://qiita.com/ussoewwin/items/37a464cd0baebb195275) を全部やる
2. vbsファイル,batファイルを削除する
3. 変わりにここにおいてある`whisper_transcription.py`と`whisper-start.bat`を同じ場所に置く
4. whisper-start.batを実行する
5. 言われた通りに文字起こししたい音声ファイルのパスをコピペする（ダブルクオーテーションがついてても処理してくれる）
