@echo off
REM 仮想環境を有効にする（必要な場合）
call ./venv/scripts/activate
echo message: venv on


REM Python スクリプトを実行する
echo message: run whisper_transcription.py
python whisper_transcription.py


REM 実行が完了した後にウィンドウを保持する（任意）
REM echo message: done enter to escape
REM pause
