# Discord python 地震即時訊息
## 氣象資料開放平台
首先,你要創建一個[氣象資料開放平台](https://opendata.cwb.gov.tw/user/authkey)的帳號<br>
然後拿到API授權碼:**[點我](https://opendata.cwb.gov.tw/user/authkey)**<br>
![圖片](https://imgur.com/WKf1DOr.png)<br>
**切記,此授權碼不要共用,給任何人,他的使用是有限制的**<br>
拿到授權碼後,[到這裡])(https://opendata.cwb.gov.tw/dataset/forecast/E-A0015-001)選擇API<br>
![圖片](https://imgur.com/JyIOJ3C.png)<br>
點選「Try out」後開始選擇選項<br>
![圖片](https://imgur.com/cEXuYnR.png)<br>
我只填選了這兩樣,避免其他干擾到,建議和我填一樣<br>
![圖片](https://imgur.com/nMYXhsh.png)<br>
然後滑到下面,按Execute<br>
![圖片](https://imgur.com/PV6j7G6.png)<br>
**然後我們就可以拿到一串網址,這一串可以連到api,一樣不要給人<br>**
![圖片](https://imgur.com/gjfDCDZ.png)<br>
***
## 安裝python模組
基本的discord.py之類的你們應該都安裝過了,但現在我們要安裝另一個,才有辦法用URL讀取api<br>
在終端機上輸入 `pip install requests` , 正常來說就可以安裝成功了
***
## 設置Bot
我們打開 config.json 把裡面的資訊填好<br>
![圖片](https://imgur.com/BcWqs8u.png)<br>
然後運行Bot,如果有測試訊息,你就成功了<br>
![圖片](https://i.imgur.com/DisIlHH.png)<br>
***
## 作者
早安,我是機車<br>
我不強求你們在Bot中標什麼`Make by 機車`,反正你們也不會聽拉哈<br>
但還是希望你們幫我宣傳下我的資訊(DC群之類的哈)<br>
~~我發現打最久的不是code,是這該死的MD檔和bot.py裡的備註~~<br>
如果有沒說明到,或說錯的,歡迎來我群詢問或糾正<br>
以下是我的資訊,拜託幫我宣傳一下DC群哈<br>
[Discord群](https://discord.gg/m9Z33wtHtK) | [Github](https://github.com/TIvan829) | [Youtube](https://www.youtube.com/channel/UC-vgoLb7laDNvgH7w62Jxvg)
***
