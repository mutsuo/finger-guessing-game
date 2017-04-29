# 说明文档（游戏：猜拳大比拼）

## 小组成员列表

1. 小组名称：实在想不出组名

2. 成员

组长：邓旸

组员：侯存巧 王娟 甄攀星

3. 分工

| 成员 | 邓 旸 | 侯存巧 | 王 娟 | 甄攀星 |

| -----|:-----:|:------:|:------:|:------:|

|分工 |	操作界面/计时系统/统筹|	电脑先手|计分系统|玩家先手|

## 程序功能说明

### 介绍

我们小组制作的是一款叫做“猜拳大比拼”的游戏，相类似于传统意义上的“石头、剪子、布”游戏。

### 游戏机制

玩家通过输入特定指令完成和电脑的交互。

玩家可以按照喜好选择自己喜欢的游戏方式——“电脑先手”或者“玩家先手”：让玩家选择是电脑先出还是自己先出。

赢的一方获得一分，平局时两方都不得分。

玩家的决策时间不得超过60秒，若超过60秒，判断自动输掉该局。

玩家可以和电脑进行任意有限局游戏，直到玩家自主选择退出游戏——此时会将已玩局数、玩家和电脑分别的得分以及最终输赢反馈给玩家。

### 亮点&难点

1. （伪）可视化界面：我们用python写这个游戏的时候没有借助pygame跨平台模块，但为了让游戏更具有可视性、提高其游戏性，我们尝试用ASCII符号制作“字符画”——将“石头、剪子、布”的图像制作成“字符画”打印在界面上。同时我们为游戏设计了界面。用于打印游戏操作界面的函数就有21个，达到总函数使用量的70%之多。

2. 计时系统：在设计游戏机制的时候，成员甄攀星同学提出了“给玩家（做选择）一个限制时间”的想法，这是本游戏的一个亮点，也是这次课设的一个难点。

3. 完整性：上述提到的（伪）操作界面使游戏看起来有始有终，从最开始的（伪）加载画面，到退出游戏后制作成员列表的打印，我们几乎考虑到了能考虑到的所有细节。游戏会对用户输入的所有指令进行正确性检查和输入时间检查，保证游戏的有效进行。

## 函数表

1.主要函数

main()								主函数

rival_first(runc,playergrade,rivalgrade)		电脑先手

player_first(runc,playergrade,rivalgrade)	玩家先手

2.打印

print_line_1()	print_line_2()				打印分割线

print_order_zone()						打印指令区

print_loading()						打印游戏载入界面

print_start()							打印游戏开始界面

print_way()							打印选择游戏方式界面

print_rule()							打印游戏规则界面

print_rock()							打印拳头字符画

print_scissor()							打印剪子字符画

print_paper()							打印布字符画

print_result(runc,playergrade,rivalgrade)	打印游戏结束界面

print_start_rival_first()					打印电脑先手画面

print_start_player_first1()				打印玩家先手画面1

print_start_player_first2()				打印玩家先手画面2

print_start_rival_first3()					打印玩家先手画面3

print_end()							打印结束界面

print_win()							打印玩家赢时引导语

print_lose()							打印玩家输时引导语

print_draw()							打印平局时引导语

print_timeout_lose()					打印因超时输掉比赛时引导语

print_producer()						打印制作者列表

3.其它

initialise()								初始化

win_or_lose_all(playergrade,rivalgrade)	判断赢家（返回序号 1-玩家赢 2-电脑赢 3-平局）

rival_do()								产生电脑出类型

count(w,playergrade,rivalgrade)			计分

timeout()								返回当前时间戳

timeout_lose(playergrade,rivalgrade,w)	超时动作






