import random
print('开始石头剪刀布游戏喽！')
print("请注意规则：1是石头，2是剪刀，三是布")
playergrade=0
rivalgrade=0
b=0
s=0
while s==0:
    i=0
    f=random.randint(1,3)
    rival=f
    player=int(input("我已经想好要出什么了，该你啦！:"))
    while (player<=0 or player>3):
        print("请重新输入：")
        player=int(input())
    if(rival==1 and player==1):
        playergrade=playergrade+0
        rivalgrade=rivalgrade+0
        print('实力相当，我们打成了平局！')
    elif(rival==1 and player==2):
        rivalgrade=rivalgrade+1
        print('哈哈，你输了，简直弱爆了')
    elif(rival==1 and player==3):
        playergrade=playergrade+1
        print('恭喜，你赢啦！')
    elif(rival==2 and player==3):
        rivalgrade=rivalgrade+1
        print('哈哈，你输了，简直弱爆了')
    elif(rival==2 and player==2):
        playergrade=playergrade+0
        rivalgrade=rivalgrade+0
        print('实力相当，我们打成了平局！')
    elif(rival==2 and player==1):
        playergrade=playergrade+1
        print('恭喜，你赢啦！')
    elif(rival==3 and player==1):
        rivalgrade=rivalgrade+1
        print('哈哈，你输了，简直弱爆了')
    elif(rival==3 and player==2):
        playergrade=playergrade+1
        print('恭喜，你赢啦！')
    elif(rival==3 and player==3):
        playergrade=playergrade+0
        rivalgrade=rivalgrade+0
        print('实力相当，我们打成了平局！')
    print('请选择继续游戏或退出游戏，继续请输入0，退出请输入其他任意键')
    print(playergrade,rivalgrade)
    s=int(input())
    if s==0:
        print('游戏继续！')
    else:
        print('结束游戏！')
        break
    
    
   
        
