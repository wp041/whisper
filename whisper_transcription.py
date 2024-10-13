import os
import whisper

# ファイルパスを定義
# fp = "C:/Users/okiko/Downloads/recording.mp3"
fp = input('ファイルパスを定義してください： ').strip('"').strip("'")
# ファイル名を取得
fn = os.path.splitext(os.path.basename(fp))[0]

# Whisperモデルをロード
model = whisper.load_model("turbo")

# 音声ファイルを処理して結果を取得
# verboseで進行状況を表示、trueにするとめちゃくちゃ出てくる
# 日本語固定したい時はlanguage="Japanese"を追加
result = model.transcribe(fp, language="Japanese", verbose=False)

# Markdown形式で書き込む
# ここで書き込み先を絶対パスで指定しちゃってるけど、なんかもっと賢い方法はあるっぽい
with open("C:/Users/okiko/Downloads/" + fn + ".md", mode="w", encoding="utf-8") as file:

    # 各セグメント（発話）をMarkdownに書き込む
    for segment in result["segments"]:
        # 秒を分と秒に変換
        start_time = segment["start"]
        end_time = segment["end"]

        start_minutes = int(start_time // 60)
        start_seconds = int(start_time % 60)
        end_minutes = int(end_time // 60)
        end_seconds = int(end_time % 60)

        # mm:ss形式で表示
        start_time_str = f"{start_minutes:02}:{start_seconds:02}"
        end_time_str = f"{end_minutes:02}:{end_seconds:02}"

        text = segment["text"].strip()  # 前後の空白を削除
        file.write("- " f"{start_time_str}  {text}\n")

        # 処理が終わったセグメントを表示
        # print(f"processed:{start_time_str}  {text}")


print("Markdownファイルを正常に書き出しました")