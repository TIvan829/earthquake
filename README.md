<h1 align="center">Discord python 台灣地震報告</h1>
<h2 align="center">氣象資料開放平台</h2>

1. 首先，你要創建一個[氣象資料開放平台](https://opendata.cwb.gov.tw/user/authkey)的帳號<br>
2. 然後取得 [API 授權碼](https://opendata.cwb.gov.tw/user/authkey)<br>
![圖片](https://imgur.com/WKf1DOr.png)<br>
> **切記，此授權碼不要共用，給任何人，他的使用是有限制的**<br>
3. 拿到授權碼後，[到這裡](https://opendata.cwb.gov.tw/dataset/forecast/E-A0015-001)選擇API<br>
![圖片](https://imgur.com/JyIOJ3C.png)<br>
4. 點選「Try it out」後開始選擇選項<br>
![圖片](https://imgur.com/cEXuYnR.png)<br>
我只填選了這兩樣，避免其他干擾到，建議和我填一樣<br>
![圖片](https://imgur.com/nMYXhsh.png)<br>
5. 然後滑到下面，按「Execute」<br>
![圖片](https://imgur.com/PV6j7G6.png)<br>
> **然後我們就可以拿到一串網址，這一串可以連到 API，一樣不要給人**

![圖片](https://imgur.com/gjfDCDZ.png)<br>
***
<h2 align="center">設定機器人</h2>

我們打開 config.json 把裡面的資訊填好<br>
![圖片](https://imgur.com/BcWqs8u.png)<br>
然後運行Bot,如果有測試訊息,你就成功了<br>
![圖片](https://i.imgur.com/DisIlHH.png)<br>
***

<h2 align="center">機器人環境建置&啟動</h2>

1. 到[官方網站](https://python.org)下載最新的 Python
2. 下載後開啟，**左下角的`Add Python *.**.** to PATH`一定要打開**
> ***很重要，沒開的話接下來可能會有問題***

![image](https://user-images.githubusercontent.com/72594971/178756663-7940d085-96a1-40f4-88c3-2c668e20409f.png)

3. 以下步驟分 **Windows 系統** 和 **非 Windows 系統**
   1. Windows
      1. 打開 `windows_run.bat`
      2. 等待自動安裝和啟動機器人
      3. 完成！
   2. 非 Windows 系統
      1. 打開終端機
      2. 輸入 `pip install pycord requests`
      3. 接著輸入 `python ./bot.py`
      4. 完成！

***

<h2 align="center">作者</h2>
<p align="center">早安，我是機車<br>
我不強求你們在 Bot 中標什麼 Made by 機車 ，反正你們也不會聽拉哈<br>
但還是希望你們幫我宣傳下我的資訊（DC群之類的哈）<br>
如果有沒說明到或說錯的，歡迎來我群詢問或糾正<br>
以下是我的資訊</p><br>
<p align="center"><a href="https://discord.gg/KQufgaCxAM">Discord 群</a> | <a href="https://github.com/TIvan829">GitHub</a> | <a href="https://www.youtube.com/channel/UC-vgoLb7laDNvgH7w62Jxvg">YouTube</a></p>

***
**感謝 [cFSovo](https://www.cfsovo.tk/) 大佬花時間幫我修改README.md**
