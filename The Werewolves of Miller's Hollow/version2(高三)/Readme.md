#使用程式語言: py
#專案製作期間: 高三

## 主要檔案說明:
### [cmds]
>   #### [game_progress.py]
>   開始遊戲後會藉由此檔案內部函數執行遊戲流程
>   #### [set_role]
>   透過此檔案內部函數設定角色數量
>   #### [player_data.py]
>   供玩家加入或退出遊戲佇列，或還原成預設設定
>   #### [introduction.py]
>   介紹如何使用此機器人
### [menu]
>   #### [my_helpmenu.py]
>   提供"Help"指令
### [start.py]
運行此檔案便能啟動Bot
#### [data.json]
儲存遊戲內的所有資料
#### [setting.json]
儲存Bot的所有資料，包含版本等資訊，其中余"Developers"中才可執行部分指令