chcp 65001
rem "キー押下後5秒でスタート"
pause
:saido
python kindle2ss-FHD.py
timeout 5
python onlyclick.py
timeout 5
goto :saido