@echo off
start Powershell.exe -noexit -Command "& {. .\venv\Scripts\Activate}"
cscript //nologo sendkeys.vbs