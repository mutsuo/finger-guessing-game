#玩家先出
import random 
playergrade=0
rivalgrade=0
s=0
while s==0:
    player=int(input("玩家的手势:"))
    while (player<=0 or player>3):
        print("请重新输入:")
        player=int(input())
    f=random.randint(1,3)
    rival=f
    if(player==1 and rival==2):
        print("恭喜，你赢了!")
        rivalgrade+=1
    elif (player==1 and rival==3):
        print("悲催，你输了!")
        rivalgrade+=1
    elif (player==2 and rival==1):
        pri0nt("悲催，你输了!")
        rivalgrade+=1
    elif (player==2 and rival==3):
        print("恭喜，你赢了!")
        playergrade+=1   
    elif (player==3 and rival==1):
        print("恭喜，你赢了!")
        playergrade+=1   
    elif (player==3 and rival==2):
        print("悲催，你输了!")
        rivalgrade+=1
    else:
        print("呵呵，我们打了平局.")
        playergrade+=1
        rivalgrade+=1

        print("请选择继续游戏或结束游戏,继续请输入0，结束游戏请输入任意数字键")
    
    s=int(input())
  
    if s==0:
        print("游戏继续")
        continue

    else:
        print("结束游戏!")
print(playergrade)
print(rivalgrade)           

