#使用程式語言: py  
#使用資源: Discord.py/ Youtube/ [Discord.py API](https://discordpy.readthedocs.io/en/stable/api.html)  
#專案製作期間: 高二上+高二下(111年)  

# 狼人殺
## 簡介:
這是我的第一個製作的中小型專案。想透過所學之程式能力改善大家遊玩體驗，歷時7個月完成，但未進行debug及gui優化。

## 動機:
總是作為旁觀者的我，發覺大家在玩這款桌時，必須有人需自稱"上帝"，無法參與遊戲。於是思考有沒有辦法解決這個問題，讓上帝這角色由電腦扮演，如此一來大家便都能參與到遊戲。

## 過程:
曾想過以JAVA進行Windows GUI介面開發，但後來想到Discord bot，便決定改以Discord作為開發工具。
最初透過Youtuber Proladon學習基礎知識，後來利用[Discord.py API](https://discordpy.readthedocs.io/en/stable/api.html)尋找需要的功能，有問題時便透過[discord](https://discord.com/)群組討論區或論壇[Stack Overflow](https://stackoverflow.com/)詢問其他前輩。最終歷時約七個月後大致完成這項專案。

## 自評建議:
1. 除蟲改善(debug): 完成基本功能後，尋找朋友進行執行測試時，才知道已有人製作出手機應用程式，也因此失去尚未找到機會進行這部分。
2. ```指令/功能說明互動介面```以及```程式碼優化```: 由於時間上的限制，這部分還沒有完成。預計未來有空時會再補上。

## 主要檔案說明:  
### [cmds](https://github.com/fortest-C/Repository-1/tree/main/The%20Werewolves%20of%20Miller's%20Hollow/werewolf/cmds)
包含各種使用者指令
>   #### [main_game](https://github.com/fortest-C/Repository-1/blob/main/The%20Werewolves%20of%20Miller's%20Hollow/werewolf/cmds/main_game.py)
>   此為遊戲最主要的執行檔，內容包含遊戲規則判斷、遊戲執行主函式等等
>   #### [set_role](https://github.com/fortest-C/Repository-1/blob/main/The%20Werewolves%20of%20Miller's%20Hollow/werewolf/cmds/set_role.py)
>   此為角色數量設定指令
>   #### [game](https://github.com/fortest-C/Repository-1/blob/main/The%20Werewolves%20of%20Miller's%20Hollow/werewolf/cmds/game.py)
>   此檔案提供玩家加入或退出遊戲佇列
### [core](https://github.com/fortest-C/Repository-1/tree/main/The%20Werewolves%20of%20Miller's%20Hollow/werewolf/core)
為此discord bot的啟動檔，執行其中```classes.py```便能啟動機器人
### [data.json](https://github.com/fortest-C/Repository-1/blob/main/The%20Werewolves%20of%20Miller's%20Hollow/werewolf/data.json)
此為json資料庫，儲存遊戲的所有資料
