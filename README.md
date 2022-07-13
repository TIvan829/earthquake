<h1 align="center">Discord python 地震即時訊息</h1>
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
<h2 align="center">機器人環境建置（Python）</h2>

1. 到[官方網站](https://python.org)下載最新的 Python
2. 下載後開啟，**左下角的`Add Python *.**.** to PATH`一定要打開**
> ***很重要，沒開的話接下來可能會有問題***

![image](https://user-images.githubusercontent.com/72594971/178756663-7940d085-96a1-40f4-88c3-2c668e20409f.png)
3. 安裝必要套件
   1. 打開終端機
   2. 輸入```pip install discord.py requests```
![image](https://user-images.githubusercontent.com/72594971/178758823-8c69d82c-a613-423e-ab17-03d78448791c.png)

***
<h2 align="center">設定機器人</h2>

我們打開 config.json 把裡面的資訊填好<br>
![圖片](https://imgur.com/BcWqs8u.png)<br>
然後運行Bot,如果有測試訊息,你就成功了<br>
![圖片](https://i.imgur.com/DisIlHH.png)<br>
***
<h2 align="center">作者</h2>
<p align="center">早安，我是機車<br>
我不強求你們在Bot中標什麼`Make by 機車`，反正你們也不會聽拉哈<br>
但還是希望你們幫我宣傳下我的資訊（DC群之類的哈）<br>
<s>我發現打最久的不是code，是這該死的 MD 檔和 bot.py 裡的備註</s><br>
如果有沒說明到，或說錯的，歡迎來我群詢問或糾正<br>
以下是我的資訊，拜託幫我宣傳一下 DC 群哈<br></p>
<p align="center"><a href=""https://discord.gg/m9Z33wtHtK>Discord 群</a> | <a href="https://github.com/TIvan829">GitHub</a> | <a href="https://www.youtube.com/channel/UC-vgoLb7laDNvgH7w62Jxvg">YouTube</a></p>

***
> cFSovo：本 md 部分內容改進
> 因為突然發現有專案的 readme 有一個小小的格式問題就進來修改，結果順手大部分就修了一遍w

**感謝[FlySky](https://www.cfsovo.tk/)大佬花時間幫我修改README.md**
