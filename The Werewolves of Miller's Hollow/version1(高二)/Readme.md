#使用程式語言: py  
#使用資源: Discord.py/ Youtube/ [Discord.py API](https://discordpy.readthedocs.io/en/stable/api.html)  
#專案製作期間: 高二

## 主要檔案說明:  
### [cmds](https://github.com/fortest-C/My_code/tree/main/The%20Werewolves%20of%20Miller's%20Hollow/version1(%E9%AB%98%E4%BA%8C)/cmds)
包含各種使用者指令
>   #### [main_game](https://github.com/fortest-C/My_code/blob/main/The%20Werewolves%20of%20Miller's%20Hollow/version1(%E9%AB%98%E4%BA%8C)/cmds/main_game.py)
>   此為遊戲最主要的執行檔，內容包含遊戲規則判斷、遊戲執行主函式等等
>   #### [set_role](https://github.com/fortest-C/My_code/blob/main/The%20Werewolves%20of%20Miller's%20Hollow/version1(%E9%AB%98%E4%BA%8C)/cmds/set_role.py)
>   此為角色數量設定指令
>   #### [game](https://github.com/fortest-C/My_code/blob/main/The%20Werewolves%20of%20Miller's%20Hollow/version1(%E9%AB%98%E4%BA%8C)/cmds/set_role.py)
>   此檔案提供玩家加入或退出遊戲佇列
### [core](https://github.com/fortest-C/My_code/tree/main/The%20Werewolves%20of%20Miller's%20Hollow/version1(%E9%AB%98%E4%BA%8C)/core)
為此discord bot的啟動檔，執行其中```classes.py```便能啟動機器人
### [data.json](https://github.com/fortest-C/My_code/blob/main/The%20Werewolves%20of%20Miller's%20Hollow/version1(%E9%AB%98%E4%BA%8C)/data.json)
此為json資料庫，儲存遊戲的所有資料
