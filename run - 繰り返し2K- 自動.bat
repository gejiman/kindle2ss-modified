chcp 65001
rem "キー押下後5秒でスタート"
pause
:saido
python kindle2ss-2K.py
timeout 5
python onlyclick.py
timeout 5
goto :saido