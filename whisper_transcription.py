import os
import whisper

# ファイルパスを定義
# fp = "C:/Users/okiko/Downloads/recording.mp3"
fp = input('ファイルパスを定義してください（D&D可）： ').strip('"').strip("'")
# 後にエクスポートファイルに使うため、ファイル名（拡張子なし）、ファイルパスを取得
fn = os.path.splitext(os.path.basename(fp))[0]
dp = os.path.dirname(fp)

# Whisperモデルをロード
model = whisper.load_model("turbo")

# 音声ファイルを処理して結果を取得
# verboseで進行状況を表示、trueにするとめちゃくちゃ出てくる
# 日本語固定したい時はlanguage="Japanese"を追加
result = model.transcribe(fp, language="Japanese", verbose=False)

# Markdown形式での出力先
md_path = dp  +"/"+ fn + ".md"

# SRT形式での出力先
srt_path = dp +"/"+ fn + ".srt"

# Markdownファイルを書き込み
with open(md_path, mode="w", encoding="utf-8") as md_file,open(srt_path, mode="w", encoding="utf-8") as srt_file:

    # 各セグメント（発話）をMarkdownテーブルとSRTに書き込む
    for i, segment in enumerate(result["segments"], start=1):
        # 秒を分と秒に変換
        start_time = segment["start"]
        end_time = segment["end"]

        start_minutes = int(start_time // 60)
        start_seconds = int(start_time % 60)
        end_minutes = int(end_time // 60)
        end_seconds = int(end_time % 60)

        # mm:ss形式で表示 (Markdown用)
        start_time_str = f"{start_minutes:02}:{start_seconds:02}"
        end_time_str = f"{end_minutes:02}:{end_seconds:02}"

        # Markdownテーブルに書き込む
        text = segment["text"].strip()  # 前後の空白を削除
        md_file.write("- " f"{start_time_str}  {text}\n")

        # hh:mm:ss,ms 形式に変換 (SRT用)
        start_hours = int(start_time // 3600)
        end_hours = int(end_time // 3600)

        start_time_srt = f"{start_hours:02}:{start_minutes:02}:{start_seconds:02},{int((start_time % 1) * 1000):03}"
        end_time_srt = f"{end_hours:02}:{end_minutes:02}:{end_seconds:02},{int((end_time % 1) * 1000):03}"

        # SRT形式に書き込む
        srt_file.write(f"{i}\n")
        srt_file.write(f"{start_time_srt} --> {end_time_srt}\n")
        srt_file.write(f"{text}\n\n")

print(f"Markdownファイルが {md_path} に、SRTファイルが {srt_path} に書き出されました。")