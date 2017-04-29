import random
import time
import sys
#def player_do():
"""
playergrade=0
rivalgrade=0
w=0
runc=0
def initialise_v():
    global playergrade,rivalgrade,w,runc
if __name__=='__main__':
    initialise_v()
    print(playergrade,rivalgrade,w,runc)
"""
"""
def __init__(self,parent=None):
    self.showMaximized()
    """
def print_line_1():
    print("############################################################")
def print_line_2():
    print("------------------------------------------------------------")
def print_order_zone():
    print("	--------------------------------------------\n        |    指令区：",end='')
def print_start():
    print_line_1()
    print_line_2()
    print("\n\n		        -----------\n		      （猜拳大比拼 ）\n		        -----------\n\n		          1->开始\n\n\n\n")
    print_line_2()
    print_order_zone()
def print_way():
    print_line_1()
    print_line_2()
    print("\n\n		      --请选择游戏方式--\n\n	  		 1->电脑先手\n\n			 2->玩家先手\n\n\n")
    print_line_2()
    print_order_zone()
def print_rule():
    print_line_1()
    print_line_2()
    print("		        --游戏规则--")
    print("	我们将开始猜拳游戏！从现在开始，你唯一要做的事就是")
    print("    思考如何赢过我！你可以和我进行任意有限局的猜拳游戏，赢")
    print("    的一方能够获得一分，若和我打成平手，两方都不计分哦。值")
    print("    得注意的是，猜拳时你只有60秒的时间做决策，如果超时将会")
    print("    默认输掉当前局哦。")
    print("\n\n\n\n\n\n		          1->继续\n")
    print_line_2()
    print_order_zone()
def print_rock():
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%]]]]]]@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@]];>\/(:[]&@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@&@@@[]]}\......_*?]]]@&]]]]]&@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@]];}+;;}>!..........,):+++{*>>{=]]@@@@@@\n@@@@@@@@@@@&]]]]]]]=:/..............................)[[@@@@@\n@@@@@@@@]];{::*>)\!^.................................(][@@@@\n@@@@@@@]+/....................^..............,^.......;]@@@@\n@@@@@@]{...................(\((........../.!*)^.......*]@@@@\n@@@@]]>....................)]\...........)++!.........*][@@@\n@@]]+!..........._(........{{............/],..........;]]?@@\n@[?(........../(/},.......^;,............{*........../](}][@\n[[!.^..........([_........**............\[^..........*=.,[]@\n]?\_:^.........(>........^?!............?:...........+:._[]@\n?]*(?_.........}_........([............\],...........;=\(];@\n@]?^{\........!}.........}?............:+............=:._]]@\n@@]>*<........**........^[=............+}..........._]!..)[[\n@@&?;*........+)........!][,...........}?/.........^;{....{[\n@@@]]+........[(........,?]+,..........;]];:<(\\():{)..^..;]\n@@@@[[\......<]*........._{[?*\,^^^...)++;=[[?=;++;*...()<][\n@@@@@][<,...\[][\..........+]]][?;(,!!!^...........^..._]][@\n@@@@@@&]?+};]][]]}*)(\//(>;][[[]]!_}))))(<!............:][@@\n@@@@@@@@@]]]][[[]]]]]]]]]]][[[[]=.;/.....,{/.........)*][@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@[[){/......>).........:][@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@][*:><<<<</.........!?]@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@]]?[[[[=}*>)\/!!/){[]?@@@@@")
def print_scissor():
    print("~~~~~~~~~~.?<~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*;~~~~~~~~~~\n~~~~~~~~~,?@$*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~.{#@=.~~~~~~~~\n~~~~~~~~~;@@@@$>~~~~~~~~~~~~~~~~~~~~~~~~~~~~.:#@@@@:~~~~~~~~\n~~~~~~~~~^+@@@@@&(~~~~~~~~~~~~~~~~~~~~~~~~~<%@@@@@{.~~~~~~~~\n~~~~~~~~~~~\]@@@@@?!~~~~~~~~~~~~~~~~~~~~~\[@@@@@[!~~~~~~~~~~\n~~~~~~~~~~~~~:@@@@@@+,~~~~~~~~~~~~~~~~~_;@@@@@$>~~~~~~~~~~~~\n~~~~~~~~~~~~~~_?@@@@@#*.~~~~~~~~~~~~~^{@@@@@@;,~~~~~~~~~~~~~\n~~~~~~~~~~~~~~~~<$@@@@@&)~~~~~~~~~~~>$@@@@@%(~~~~~~~~~~~~~~~\n~~~~~~~~~~~~~~~~~^;@@@@@@[/~~~~~~~(]@@@@@@}.~~~~~~~~~~~~~~~~\n~~~~~~~~~~~~~~~~~~~(%@@@@@@;,~~~!=@@@@@@&/~~~~~~~~~~~~~~~~~~\n~~~~~~~~~~~~~~~~~~~~.}@@@@@@#:_}@@@@@@@:~~~~~~~~~~~~~~~~~~~~\n~~~~~~~~~~~~~~~~~~~~~~\&@@@@@@@@@@@@@[!~~~~~~~~~~~~~~~~~~~~~\n~~~~~~~~~~~~~~~~~~~~~~~~:#@@@@@@@@@$*~~~~~~~~~~~~~~~~~~~~~~~\n~~~~~~~~~~~~~~~~~~~~~~~~~>@@@@@@@@@(~~~~~~~~~~~~~~~~~~~~~~~~\n~~~~~~~~~~~~~~~~~~~~~~~,+#@@@@@@@@@#}^~~~~~~~~~~~~~~~~~~~~~~\n~~~~~~~~~~~~~~~~~~~~~.:#@@@@@$=#@@@@@$>~~~~~~~~~~~~~~~~~~~~~\n~~~~~~~~~~~~~~~~~~~~<%@@@@@@{^~,+@@@@@@&(~~~~~~~~~~~~~~~~~~~\n~~~~~~^/>}=[&%%&[=}[@@@@@@%/~~~~~(#@@@@@@?}=]&%%&[={</.~~~~~\n~~~^<?#@@@@@@@@@@@@@@@@@@%,~~~~~~~!#@@@@@@@@@@@@@@@@@@$=).~~\n~~:$@@@@@?*(_,,_)[@@@@@@@_~~~~~~~~~\@@@@@@@=(_,,!(:[@@@@@%>~\n^=@@@@@;_~~~~~~~~~$@@@@@*~~~~~~~~~~~+@@@@@&~~~~~~~~~!?@@@@@}\n%@@@@@;~~~~~~~~~~<@@@@@%~~~~~~~~~~~~^#@@@@#\~~~~~~~~~~[@@@@@\n[@@@@@?^~~~~~~.(=@@@@@]_~~~~~~~~~~~~~/%@@@@@;\.~~~~~~,&@@@@@\n~*@@@@@$={:{+[$@@@@@&>~~~~~~~~~~~~~~~~.*%@@@@@$?+::{=#@@@@#<\n~~^>?%#@@@@@@@@$];>,~~~~~~~~~~~~~~~~~~~~~_>=&$@@@@@@@@#&=<.~")
def print_paper():
    print("~~~~~~~~~~~~~~~~~~~~~~~<t&fst*~~.rs%%fc/~~<jx%%s+~~~~~~~~~~~\n~~~~~~~~~~~~~~~~~~~~~~]s=:>*;&i*&c{<<:rf}]e=:<>+te/~~~~~~~~~\n~~~~~~~~~~~~~~~~~~~~~fq)/\\\/\w@;!/\\\!}@w\/\\\/!u@>:+;+{\~~\n~~~~~~~~~~~~~~~~~~~~(@r!(((((/;@+/((((\}@=/(((((/:@$]+{}rs&!\n~~~~~~~~~~~~~~~~~~~~>@=/(((((\}@r/((((/=@+/((((((bx\/\\\//ad\n~~~~~~~~~~~~~~~~~~~~<@=/(((((\}@?/((((/=@;/((((/;@=/(((((\*@\n~~~~~~~~~~~~~~~~~~~~<@=/(((((\}@?/((((/=@;/((((/?@}\(((((\*@\n~~~~~~~~~~~~~~~~~~~~<@=/(((((\}@?/((((/=@;/((((/r@}\(((((\{@\n~~~~~~~~~~~~~~~~~~~~<@=/(((((\}@?/((((/=@;/((((/[@{\(((((\{@\n~/?[[[[r?;(~~~~~~~~~<@=/(((((\}@?/((((/=@;/((((/]@:\(((((\}@\ns@[><)<>{[jsi^~~~~~~<@=/(((((\}@=!//\\!+@+!\\\\_i@>/\\\\\!}@\n>xf\/(((\//*&xr,~~~~<@=/(((((\+@z;====;j@c+;;;;}&@?}++++}{i@\n~~&b{!(((((\/*tfc\~~<@=/(((((()};;;=====;=????????rrrrrrr?z@\n~~~=qc/((((((\/)ifz<)@=/(((((((\\\\\\\\//////////////////!;@\n~~~~\qs/((((((((/\?&%@r()(\//\\((((((((((((((((((((((((((/?@\n~~~~~\@j!(((((((((//}uzicccir=}*)\//\((((((((((((((((((((/=@\n~~~~~~}@;/((((((((((\/\\()>{+?]cjji=:\/\(((((((((((((((((/?@\n~~~~~~~c@{!\(((((((((((((((\\//\(>+[uec*!((((((((((((((((/jm\n~~~~~~~~?su=(/\(((((((((((((((((((\/\>cwe)(((((((((((((((!fy\n~~~~~~~~~~*jsj://((((((((((((((((((((\!:f+\(((((((((((\//?@}\n~~~~~~~~~~~~_=e&r<\/\((((((((((((((((((\/\(((((((((\/>}[ua:~\n~~~~~~~~~~~~~~~)izci;(/(((((((((((((((((((((((((((/{fj?{\~~~\n~~~~~~~~~~~~~~~~~~_*txr/\((((((((((((((((((((((((\<me~~~~~~~\n~~~~~~~~~~~~~~~~~~~~~)ya\\\\\\\\\\\\\\\\\\\\\\\\\!u@.~~~~~~~\n~~~~~~~~~~~~~~~~~~~~~~~ba()))))))))))))))))))))))(ba~~~~~~~~")
def initialise():
    print_start()
    #initialise_v()
def win_or_lose_all(playergrade,rivalgrade):
    if (playergrade>rivalgrade):
        return 1
    elif (playergrade<rivalgrade):
        return 2
    else:
        return 3
def print_result(runc,playergrade,rivalgrade):
    print_line_1()
    print_line_2()
    print("\n\n		      	 --游戏结束--\n")
    print("	          共进行了%d局游戏，得分如下：" %runc)
    print("\n\n	  		 玩家：%d分" %playergrade)
    print("\n\n			 电脑：%d分\n" %rivalgrade)

    winner=win_or_lose_all(playergrade,rivalgrade)
    if (winner==1):
        print("		  玩家胜出！")
    elif(winner==2):
        print("		  电脑胜出！")
    else:
        print("		  平局！")

    print_line_2()
    print("\n\n			1->重新开始\n\n			2->退出\n")
    print_line_2()
    print_order_zone()
def rival_do():
    return(random.randint(0,2))
#def right_or_false():
def count(w,playergrade,rivalgrade):
    if (w!=-1):
        return(playergrade+w,rivalgrade+(1-w))
    else:
        return(playergrade,rivalgrade)
#def win_or_lose_now():
def timeout():
    return time.time()
def print_start_rival_first():
    print_line_1()
    print_line_2()
    print("\n\n	“游戏开始。我想好要出什么啦，但我不告诉你。”\n			“到你啦！”\n\n\n	  		 1->拳头\n\n			 2->剪子\n\n			 3->布\n\n\n")
    print_line_2()
    print_order_zone()
def print_start_player_first1():
    print_line_1()
    print_line_2()
    print("\n\n		“游戏开始。那么你先出吧！”\n			“想好了吗？”\n\n\n	  		 1->想好了\n\n\n\n\n\n\n")
    print_line_2()
    print_order_zone()
def print_start_player_first2():
    print_line_1()
    print_line_2()
    print("\n\n\n\n\n\n	  		 1->想好了\n\n\n\n\n\n\n")
def print_start_rival_first3():
    print_line_1()
    print_line_2()
    print("\n\n		  “告诉我你出的是什么？”\n\n\n\n	  		 1->拳头\n\n			 2->剪子\n\n			 3->布\n\n\n")
    print_line_2()
    print_order_zone()    
def print_end():
    print_line_1()
    print_line_2()
    print("\n\n		      	 --请选择--\n\n\n\n	  		 1->再来一局\n\n			 2->结束游戏\n\n\n\n\n")
    print_line_2()
    print_order_zone()
def print_win():
    print_line_2()
    print('“恭喜，你赢啦！”\n')
def print_lose():
    print_line_2()
    print('“你输了，哈哈，简直弱爆了”\n')
def print_draw():
    print_line_2()
    print('“实力相当，我们打成了平局！”\n')
def print_timeout_lose():
    print_line_2()
    print("！！！！！！！！！！")
    print("！！！！！！！！！！")
    print('“超时啦！当前局算你输！”\n')
def timeout_lose(playergrade,rivalgrade,w):
    print_timeout_lose()
    w=-1
    playergrade,rivalgrade=count(w,playergrade,rivalgrade)
def rival_first(func,playergrade,rivalgrade):
    turn=1
    runc=0
    t1,t2=0,0
    w=0
    while turn:
        runc+=1
        print_start_rival_first()
        rival_style=rival_do()

        t1=timeout()
        player_style=int(input())
        f=2
        t2=timeout()
        if (t2-t1<=5):
            while (player_style<=0 or player_style>3):
                print("指令有误，请重新输入：")
                player_style=int(input())
                t2=timeout()
                if(t2-t1>5):
                    break
            print_line_1()
            if(t2-t1<=5):
                if(rival_style==0):
                    print_rock()
                    print("\n")
                    print_line_2()
                    print("“我出的是拳头。”\n")
                elif(rival_style==1):
                    print_scissor()
                    print("\n")
                    print_line_2()
                    print("“我出的是剪刀。”\n")
                elif(rival_style==2):
                    print_paper()
                    print("\n")
                    print_line_2()
                    print("“我出的是布。”\n")
                            
                if(rival_style==0 and player_style==1):
                    w=-1
                    playergrade,rivalgrade=count(w,playergrade,rivalgrade)

                elif(rival_style==0 and player_style==2):
                    w=0
                    playergrade,rivalgrade=count(w,playergrade,rivalgrade)
                elif(rival_style==0 and player_style==3):
                    w=1
                    playergrade,rivalgrade=count(w,playergrade,rivalgrade)
                    print_win()
                elif(rival_style==1 and player_style==3):
                    w=0
                    playergrade,rivalgrade=count(w,playergrade,rivalgrade)
                    print_lose()
                elif(rival_style==1 and player_style==2):
                    w=-1
                    playergrade,rivalgrade=count(w,playergrade,rivalgrade)
                    print_draw()
                elif(rival_style==1 and player_style==1):
                    w=1
                    playergrade,rivalgrade=count(w,playergrade,rivalgrade)
                    print_win()
                elif(rival_style==2 and player_style==1):
                    w=0
                    playergrade,rivalgrade=count(w,playergrade,rivalgrade)
                    print_lose()
                elif(rival_style==2 and player_style==2):
                    w=1
                    playergrade,rivalgrade=count(w,playergrade,rivalgrade)
                    print_win()
                elif(rival_style==2 and player_style==3):
                    w=-1
                    playergrade,rivalgrade=count(w,playergrade,rivalgrade)
                    print_draw()
            else:
                timeout_lose(playergrade,rivalgrade,w)
        else:
            timeout_lose(playergrade,rivalgrade,w)

        print_line_1()
        print_end()
        order=int(input())
        while(order!=1 and order!=2):
            order=int(input("指令有误，请重新输入："))
        print_line_1()
        
        if (order==1):
            print_line_1()
            print_line_1()
            print("\n\n		      “游戏继续！”\n")
        else:
            print_result(runc,playergrade,rivalgrade)
            turn=0

def player_first(func,playergrade,rivalgrade):
    turn=1
    runc=0
    t1,t2=0,0
    w=0
    while turn:
        runc+=1
        print_start_player_first1()
        
        order=int(input())

        while(order!=1):
            order=int(input("指令有误，请重新输入："))
        print_line_1()

        print_start_player_first2()
        rival_style=rival_do()
        if(rival_style==0):
            print_rock()
            print("\n")
            print_line_2()
            print("\n\n“我出的是拳头”\n")
        elif(rival_style==1):
            print_scissor()
            print("\n")
            print_line_2()
            print("\n\n“我出的是剪刀。”\n")
        elif(rival_style==2):
            print_paper()
            print("\n")
            print_line_2()
            print("\n\n“我出的是布。”\n")

        print_start_rival_first3()
        t1=timeout()
        player_style=int(input())
        t2=timeout()
        if (t2-t1<=5):
            while (player_style<=0 or player_style>3):
                print("指令有误，请重新输入：")
                player_style=int(input())
                t2=timeout()
                if (t2-t1>5):
                    break
            print_line_1()
            if (t2-t1<=5):
                if(rival_style==0 and player_style==1):
                    w=-1
                    playergrade,rivalgrade=count(w,playergrade,rivalgrade)
                    print_draw()
                elif(rival_style==0 and player_style==2):
                    w=0
                    playergrade,rivalgrade=count(w,playergrade,rivalgrade)
                    print_lose()
                elif(rival_style==0 and player_style==3):
                    w=1
                    playergrade,rivalgrade=count(w,playergrade,rivalgrade)
                    print_win()
                elif(rival_style==1 and player_style==3):
                    w=0
                    playergrade,rivalgrade=count(w,playergrade,rivalgrade)
                    print_lose()
                elif(rival_style==1 and player_style==2):
                    w=-1
                    playergrade,rivalgrade=count(w,playergrade,rivalgrade)
                    print_draw()
                elif(rival_style==1 and player_style==1):
                    w=1
                    playergrade,rivalgrade=count(w,playergrade,rivalgrade)
                    print_win()
                elif(rival_style==2 and player_style==1):
                    w=0
                    playergrade,rivalgrade=count(w,playergrade,rivalgrade)
                    print_lose()
                elif(rival_style==2 and player_style==2):
                    w=1
                    playergrade,rivalgrade=count(w,playergrade,rivalgrade)
                    print_win()
                elif(rival_style==2 and player_style==3):
                    w=-1
                    playergrade,rivalgrade=count(w,playergrade,rivalgrade)
                    print_draw()
            else:
                timeout_lose(playergrade,rivalgrade,w)
        else:
            timeout_lose(playergrade,rivalgrade,w)
        print_end()
        order=int(input())
        while(order!=1 and order!=2):
            order=int(input("指令有误，请重新输入："))
        print_line_1()
        
        if (order==1):
            print("\n\n		      “游戏继续！”\n")
        else:
            print_result(runc,playergrade,rivalgrade)
            turn=0

##################主函数部分##################
##################变量初始化##################
func=0
##################界面初始化##################
initialise()
order=int(input())
while(order!=1):
    order=int(input("指令有误，请重新输入："))
print_rule()
order=int(input())
while(order!=1):
    order=int(input("指令有误，请重新输入："))
##############################################
run=1
while run:
    print_way()
    order=int(input())
    while(order!=1 and order!=2):
        order=int(input("指令有误，请重新输入："))
        
    playergrade=0
    rivalgrade=0
    runc=0

    if(order==1):
        rival_first(func,playergrade,rivalgrade)
        order=int(input())
        while(order!=1 and order!=2):
            order=int(input("指令有误，请重新输入："))
        if (order==1):
            print("\n\n")
            print_line_1()
            print("                   “开始新一局游戏！”\n\n")
            print_line_1()
            print("\n\n")
        else:
            run=0
    else:
        player_first(func,playergrade,rivalgrade)
        order=int(input())
        while(order!=1 and order!=2):
            order=int(input("指令有误，请重新输入："))
        if (order==1):
            print("\n\n")
            print_line_1()
            print("                   “开始新一局游戏！”\n\n")
            print_line_1()
            print("\n\n")
        else:
            run=0
