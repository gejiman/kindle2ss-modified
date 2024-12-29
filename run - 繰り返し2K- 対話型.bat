chcp 65001
rem "キー押下後5秒でスタート"
pause
:saido
python kindle2ss-2K.py

set /p yn_check="作業を続けますか？ (y/n)"
IF %yn_check:Y=Y%==Y (
goto :saido
) ELSE (
echo 終わります
)