import pyautogui
import win32gui
import win32ui
import win32con
import win32api
import time
import os
import datetime
import random
from PIL import Image


# スクリーンショットを取得したい範囲の座標
left, top, width, height = (200, 120, 2160, 1318)
# スクショ間隔(秒)
span = 10
spanran = [1.5, 2, 2.5]
# 出力フォルダ頭文字
h_foldername = "output"
# 出力ファイル頭文字
h_filename = "picture"

# ５秒の間に、スクショしたいkindleの画面に移動
time.sleep(5)

        # 次のページ
pyautogui.click() #元はKeyDown
        # 画面の動作待ち
time.sleep(span)
