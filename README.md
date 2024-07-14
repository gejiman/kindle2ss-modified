daishir0/kindle2ssからフォークしたものです。
自分の環境で動かなかった箇所を直しています。

# スクリーンショット自動取得ツール

任意の画面領域を自動的にスクリーンショットし、ファイルとして保存するツールです。

## 必要なもの

- Python3
- pip
- 以下のPythonライブラリ
  - pyautogui
  - pywin32
  　- win32gui
  　- win32ui
  　- win32con
  　- win32api
  - PIL

## 使い方

1. 本リポジトリをクローンします。

```
git clone https://github.com/gejiman/kindle2ss-modified.git
```

2. 必要なPythonライブラリをインストールします。

```
pip install pyautogui pywin32 Pillow
```

3. ターミナルまたはコマンドプロンプトを開き、リポジトリのディレクトリに移動します。

```
cd kindle2ss-modified
```

4. スクリーンショットを取得したいKindleの画面に移動します。

5. 以下のコマンドを実行します。

```
python kindle2ss.py
```

5－1. リポジトリのディレクトリに５のコマンドをpause付きでbatファイルを作ると便利かも

```
chcp 65001
rem "キー押下後5秒でスタート"
pause
python kindle2ss.py
pause
```

6. スクリーンショットが取得され、`output_年月日時分秒`という名前のフォルダに保存されます。

7. 取得されたスクリーンショットを確認します。

## 設定

スクリーンショットを取得したい範囲の座標、スクショ間隔、出力フォルダ名、出力ファイル名の頭文字を変更することができます。

```python
# スクリーンショットを取得したい範囲の座標
left, top, width, height = (480, 120, 600, 870)
# スクショ間隔(秒)
span = 1
# 出力フォルダ頭文字
h_foldername = "output"
# 出力ファイル頭文字
h_filename = "picture"
```

また、3ページ連続で同じ画面が出現した場合に自動的にスクリーンショットを停止するようになっています。この回数を変更することができます。

```python
# 3回同じ画像が出現した場合は終了
if same_cnt >= 3:
    break
```

## 注意事項

- このツールはWindows環境でのみ動作します。
- このツールを使用する際には、利用規約や著作権に関する法律を遵守してください。
