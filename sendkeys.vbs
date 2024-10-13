set OBJECT=WScript.CreateObject("WScript.Shell")
WScript.sleep 1000
OBJECT.SendKeys "whisper --model turbo --language Japanese --verbose False "