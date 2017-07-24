# Generated from E:/new/antlrg/ScratchAnalysis\Antlr.g4 by ANTLR 4.7
# -*- coding: utf-8 -*-
from antlr4 import *


# This class defines a complete listener for a parse tree produced by AntlrParser.
class AntlrListener(ParseTreeListener):
    def __init__(self):
        self.max_depth = 0   #语法树的最大深度
        self.max_if_depth = 0#最大if语句的深度
        self.max_until_depth = 0#最大until语句的深度
        self.max_repeat_depth = 0#最大repeat语句的深度
        self.if_count = 0#if语句的数量
        self.until_count = 0#until语句的数量
        self.repeat_count = 0#repeat语句的数量
        self.scripts_count = 0#脚本语句scripts的数量
        self.depth = 0#总深度
        self.if_depth = 0#if语句的深度
        self.until_depth = 0#until语句的深度
        self.repeat_depth = 0#repeat语句的深度
        self.proj_count = 0#自定义函数proj的数目
        self.sprits_count = 0#角色sprits的数目
        self.wg_count = 0#小绿旗子的数目
        self.clone_count = 0#clone语句的数目
        self.whenclick_count = 0#鼠标点击事件的数目
        self.whenkey_count = 0#键盘输入事件的数目
        self.whdrop_count = 0#背景切换的数目
        self.whrecive_count = 0#接收信号模块的数目
        self.whsensor_count = 0#输入音频视频的数目
        self.deadcode_count = 0#死代码块的数目
        self.broadcastlist = []#广播发送的所有内容
        self.receivelist = []#广播接收的所有内容
        self.Meaningless_count = 0#无效命名数目
        self.initit = 0#是否初始化的标志
        self.Recursively = 0#递归的数目
        self.SayandSound=0#声画匹配的标志

        self.ap_score = 0  # Abstraction and problem decomposition 得分
        self.Parallelism_score = 0  # Parallelism得分
        self.Synchronization = 0  # Synchronization得分
        self.FlowControl_score = 0  # FlowControl得分
        self.UserInteractivity = 0  # UserInteractivity得分
        self.LogicalThinking = 0  # LogicalThinking得分
        self.DataRepresentation = 1  # 因为太多了，默认先直接给1分.....
        self.score = {}

    def create_score(self):
        self.score['Abstraction'] = self.ap_score
        self.score['Parallelism'] = self.Parallelism_score
        self.score['FlowControl'] = self.FlowControl_score
        self.score['UserInteractivity'] = self.UserInteractivity
        self.score['LogicalThinking'] = self.LogicalThinking
        self.score['DataRepresentation'] = self.DataRepresentation
        self.score['Synchronization'] = self.Synchronization

    def print_all(self):
        print("max_depth:", self.max_depth)
        print("max_if_depth:", self.max_if_depth)
        print("max_until_depth:", self.max_until_depth)
        print("max_repeat_depth:", self.max_repeat_depth)
        print("if_count:", self.if_count)
        print("until_count:", self.until_count)
        print("repeat_count:", self.repeat_count)
        print("scripts_count:", self.scripts_count)
        print("proj_count:", self.proj_count)
        print("sprits_count:", self.sprits_count)
        print("deadcode_count:", self.deadcode_count)
        self.create_score()
        print(self.score)

    # Enter a parse tree produced by AntlrParser#json.
    def enterJson(self, ctx):
        pass

    # Exit a parse tree produced by AntlrParser#json.
    def exitJson(self, ctx):
        # 是否有不匹配的广播
        if len(self.receivelist) != len(self.broadcastlist):
            print("广播不匹配")
        else:
            for r in self.receivelist:
                if self.broadcastlist.count(r) == 0:
                    print("广播不匹配")
                    self.deadcode_count += 1
        # 是否有无意义的角色命名
        if self.Meaningless_count > 0:
            print("有" + str(self.Meaningless_count) + "个角色存在无意义命名")
        # 是否进行初始化
        if self.initit > 0:
            print("可能未初始化")
        # 是否使用了递归
        if self.Recursively>0:
            print("使用了递归")
        # 是否声画同步
        if self.SayandSound>0:
            print("声画不同步")
        self.print_all()

        pass

    # Enter a parse tree produced by AntlrParser#obj.
    def enterObj(self, ctx):
        pass

    # Exit a parse tree produced by AntlrParser#obj.
    def exitObj(self, ctx):
        pass

    # Enter a parse tree produced by AntlrParser#pair.
    def enterPair(self, ctx):
        #判断有多少个角色和角色的命名判定
        ctx_STRING = ctx.STRING()
        if ctx_STRING:
            ctx_STRING_Text = ctx_STRING.getText()
            if ctx_STRING_Text == '"objName"':
                if ctx.value().STRING().getText() != '"Stage"':
                    self.sprits_count += 1
                    # 评分标准1-1
                    if self.sprits_count > 1 and self.scripts_count > 1 and self.ap_score == 0:
                        self.ap_score = 1
                #是否存在无意义命名
                if ctx.value().STRING().getText().find('Sprite') > 0 or ctx.value().STRING().getText().find('角色') > 0:
                    self.Meaningless_count += 1

            if ctx_STRING_Text == '"variables"':
                if self.DataRepresentation < 2:
                    self.DataRepresentation = 2

            if ctx_STRING_Text == '"lists"':
                if self.DataRepresentation < 3:
                    self.DataRepresentation = 3

    # Exit a parse tree produced by AntlrParser#pair.
    def exitPair(self, ctx):
        pass

    # Enter a parse tree produced by AntlrParser#scripts_array.
    def enterScripts_array(self, ctx):
        flag1 = 0
        flag2 = 0
        str2 = ctx.getText()
        str3 = str2
        # 关于初始化的几个方面
        #关于显示隐藏的初始化
        if str2.find('"hide"') > 0:
            if str2.find('"show"') < 0:
                self.initit = 1
        #关于角色造型的初始化
        if str2.find('"nextCostume"') > 0:
            if str2.find('"lookLike:"') < 0:
                self.initit = 1
        #关于角色大小的初始化
        if str2.find('"changeSizeBy:"') > 0:
            if str2.find('"setSizeTo:"') < 0:
                self.initit = 1
        #关于背景变化的初始化
        if str2.find('"nextScene"') > 0:
            if str2.find('"startScene"') < 0:
                self.initit = 1
        #关于角色方向的初始化
        if str2.find('"turnRight:"') > 0 or str2.find('"turnLeft:"') > 0 or str2.find('"pointTowards:"') > 0:
            if str2.find('"heading:"') < 0:
                self.initit = 1
        #关于角色位置的初始化
        if str2.find('"forward:"') > 0 or str2.find('"gotoSpriteOrMouse:"') > 0 or str2.find(
                '"glideSecs:toX:y:elapsed:from:"') > 0:
            if str2.find('"gotoX:y:"') < 0:
                self.initit = 1
        #关于x坐标的初始化
        if str2.find('"changeXposBy:"') > 0:
            if str2.find('"xpos:"') < 0 and str2.find('"gotoX:y:"') < 0:
                self.initit = 1
        # 关于y坐标的初始化
        if str2.find('"changeYposBy:"') > 0:
            if str2.find('"ypos:"') < 0 and str2.find('"gotoX:y:"') < 0:
                self.initit = 1
        # 处理音画同步，要求是画面必须出现在声音之前
        while str2.find("laySound") > 0 and flag2 == 0:
            soundstr = str2[str2.find("laySound"):str2.find("laySound") + 40]
            sc = ctx.getText().find(soundstr);
            str1 = str2[str2.find("laySound"):]
            s1 = str2.find("laySound")
            str1 = str1[:str1.find(']')]
            str1 = str1.split(',')
            str1 = str1[1].strip('"')
            while str3.find("say") > 0 and flag2 == 0:
                saystr = str3[str3.find("say"):str3.find("say") + 40]
                sy = ctx.getText().find(saystr)
                str4 = str3[str3.find("say"):]
                s2 = str3.find("say")
                str4 = str4[:str4.find(']')]
                str4 = str4.split(',')
                str4 = str4[1].strip('"')
                if str4 == str1 and sc < sy:
                    self.SayandSound+=1
                    flag2 = 1
                    break
                elif str4 == str1 and sc > sy:
                    str3 = str3[s2:]
                    flag1 = 1
                    break
                else:
                    str3 = str3[s2:]
            str2 = str2[s1:]
            if flag1 == 0:
                str3 = ctx.getText()
        # 评分标准1-1
        self.scripts_count += 1
        if self.sprits_count > 1 and self.scripts_count > 1 and self.ap_score < 1:
            self.ap_score = 1
        # 有scripts就给1分
        if self.FlowControl_score < 1:
            self.FlowControl_score = 1

    # Exit a parse tree produced by AntlrParser#scripts_array.
    def exitScripts_array(self, ctx):
        pass

    # Enter a parse tree produced by AntlrParser#array.
    def enterArray(self, ctx):
        pass

    # Exit a parse tree produced by AntlrParser#array.
    def exitArray(self, ctx):
        pass

    # Enter a parse tree produced by AntlrParser#blocks_array.
    def enterBlocks_array(self, ctx):
        #检测没有控制模块开始的代码块，认定为死代码
        if ctx.getText().find("when") == -1:
            self.deadcode_count += 1
        pass

    # Exit a parse tree produced by AntlrParser#blocks_array.
    def exitBlocks_array(self, ctx):
        pass

    # Enter a parse tree produced by AntlrParser#value.
    def enterValue(self, ctx):
        ctx_Text = ctx.getText()
        # 评分标准1-2
        if ctx_Text == '"procDef"':
            self.proj_count += 1
            if self.proj_count > 0 and self.ap_score < 2:
                self.ap_score = 2
        # 评分标准1-3
        if ctx_Text == '"whenCloned"':
            self.clone_count += 1
            if self.clone_count > 0 and self.ap_score < 3:
                self.ap_score = 3

        if '"whenKeyPressed"' == ctx_Text:
            self.whenkey_count += 1
            # 评分标准2-2
            if self.whenkey_count > 1 and self.whenclick_count > 1 and self.Parallelism_score < 2:
                self.Parallelism_score = 2
            if self.UserInteractivity < 2:
                self.UserInteractivity = 2
        if '"whenIReceive"' == ctx_Text:
            self.whrecive_count += 1
            # 评分标准2-3
            if self.whdrop_count > 1 or self.whrecive_count > 1 or self.whsensor_count > 1 and self.Parallelism_score < 3:
                self.Parallelism_score = 3

        if '"whenSensorGreaterThan"' == ctx_Text:
            self.whsensor_count += 1
            # 评分标准2-3
            if self.whdrop_count > 1 or self.whrecive_count > 1 or self.whsensor_count > 1 and self.Parallelism_score < 3:
                self.Parallelism_score = 3

        if '"whenClicked"' == ctx_Text:
            self.whenclick_count += 1
            # 评分标准2-2
            if self.whenkey_count > 1 and self.whenclick_count > 1 and self.Parallelism_score < 2:
                self.Parallelism_score = 2
            if self.UserInteractivity < 2:
                self.UserInteractivity = 2

        if '"doAsk"' == ctx_Text:
            if self.UserInteractivity < 2:
                self.UserInteractivity = 2

        if '"setVideoState"' == ctx_Text:
            if self.UserInteractivity < 3:
                self.UserInteractivity = 3

        if '"soundLevel"' == ctx_Text:
            if self.UserInteractivity < 3:
                self.UserInteractivity = 3

        logic_operator = ('"&"', '"|"', '"not"', '"<"', '">"', '"="')
        if (ctx_Text in logic_operator) and (self.LogicalThinking < 3):
            self.LogicalThinking = 3

        if '"wait:elapsed:from:"' == ctx_Text:
            if self.Synchronization < 1:
                self.Synchronization = 1

        if ctx_Text in ('"stopScripts"', '"broadcast"',):
            if self.Synchronization < 2:
                self.Synchronization = 2

        sync_3p = ('"whenSceneStarts"', '"doBroadcastAndWait"', '"doWaitUntil"')
        if ctx_Text in sync_3p:
            if self.Synchronization < 3:
                self.Synchronization = 3
        if ctx_Text == '"whenSceneStarts"':
            self.whdrop_count += 1
            # 评分标准2-3
            if self.whdrop_count > 1 or self.whrecive_count > 1 or self.whsensor_count > 1 and self.Parallelism_score < 3:
                self.Parallelism_score = 3

    # Exit a parse tree produced by AntlrParser#value.
    def exitValue(self, ctx):
        pass

    # Enter a parse tree produced by AntlrParser#cblock_value.
    def enterCblock_value(self, ctx):
        if ctx.WHENGREENFLAG():
            if self.UserInteractivity < 1:
                self.UserInteractivity = 1
            # 评分标准2-1
            self.wg_count += 1
            if self.wg_count > 1 and self.Parallelism_score == 0:
                self.Parallelism_score = 1
        pass

    # Exit a parse tree produced by AntlrParser#cblock_value.
    def exitCblock_value(self, ctx):
        pass

    # Enter a parse tree produced by AntlrParser#cblock_doRepeat.
    def enterCblock_doRepeat(self, ctx):
        if self.FlowControl_score < 2:
            self.FlowControl_score = 2
        pass

    # Exit a parse tree produced by AntlrParser#cblock_doRepeat.
    def exitCblock_doRepeat(self, ctx):
        pass

    # Enter a parse tree produced by AntlrParser#cblock_doUntil.
    def enterCblock_doUntil(self, ctx):
        if self.FlowControl_score < 3:
            self.FlowControl_score = 3
        pass

    # Exit a parse tree produced by AntlrParser#cblock_doUntil.
    def exitCblock_doUntil(self, ctx):
        pass

    # Enter a parse tree produced by AntlrParser#cblock_doIfElse.
    def enterCblock_doIfElse(self, ctx):
        if self.LogicalThinking < 2:
            self.UserInteractivity = 2
        pass

    # Exit a parse tree produced by AntlrParser#cblock_doIfElse.
    def exitCblock_doIfElse(self, ctx):
        pass

    # Enter a parse tree produced by AntlrParser#cblock_doIF.
    # 将if中比较静态的两部分进行比较,得到某部分是不是死代码
    def enterCblock_doIF(self, ctx):
        ctx_Text = ctx.getText()
        #去掉关于变量、列表和随机生成的内容
        if ctx.getText().find('readVariable') > 0 or ctx.getText().find('lineCountOfList') > 0 or ctx.getText().find(
                'randomFrom') > 0:
            return
        #判断“<”号左右两边是否能匹配
        elif ctx.getText().find('<') > 0:
            str1 = ctx_Text[ctx.getText().find('<'):ctx.getText().find(']')]
            str2 = str1.split(',')
            v1 = str2[1].strip('"')
            v2 = str2[2].strip('"')
            if int(v1) > int(v2):
                self.deadcode_count += 1
        # 判断“>”号左右两边是否能匹配
        elif ctx.getText().find('>') > 0:
            str1 = ctx_Text[ctx.getText().find('<'):ctx.getText().find(']')]
            str2 = str1.split(',')
            v1 = str2[1].strip('"')
            v2 = str2[2].strip('"')
            if int(v1) < int(v2):
                self.deadcode_count += 1
        # 判断“=”号左右两边是否能匹配
        elif ctx.getText().find('=') > 0:
            str1 = ctx_Text[ctx.getText().find('<'):ctx.getText().find(']')]
            str2 = str1.split(',')
            v1 = str2[1].strip('"')
            v2 = str2[2].strip('"')
            if int(v1) != int(v2):
                self.deadcode_count += 1
        #评分标准6-1
        if self.LogicalThinking < 1:
            self.UserInteractivity = 1
        pass

    # Exit a parse tree produced by AntlrParser#cblock_doIF.
    def exitCblock_doIF(self, ctx):
        pass

    # Enter a parse tree produced by AntlrParser#cblock_doWaitUntil.
    def enterCblock_doWaitUntil(self, ctx):
        pass

    # Exit a parse tree produced by AntlrParser#cblock_doWaitUntil.
    def exitCblock_doWaitUntil(self, ctx):
        pass

    # Enter a parse tree produced by AntlrParser#cblock_doForever.
    def enterCblock_doForever(self, ctx):
        if self.FlowControl_score < 2:
            self.FlowControl_score = 2
        pass

    # Exit a parse tree produced by AntlrParser#cblock_doForever.
    def exitCblock_doForever(self, ctx):
        pass

    # Enter a parse tree produced by AntlrParser#cblock_doBroadcast.
    # 发送广播模块发送的内容
    def enterCblock_doBroadcast(self, ctx):
        ctxText = ctx.getText()
        str1 = ctxText.split(",")
        str1 = str1[1][:-2]
        broadcastcontent = str1.strip('"')
        # 判断是否发送过该该内容
        if self.broadcastlist.count(broadcastcontent) == 0:
            self.broadcastlist.append(broadcastcontent)
        pass

    # Exit a parse tree produced by AntlrParser#cblock_doBroadcast.
    def exitCblock_doBroadcast(self, ctx):
        pass

    # Enter a parse tree produced by AntlrParser#cblock_whenIReceive.
    #得到接收广播得到的内容
    def enterCblock_whenIReceive(self, ctx):
        ctxText = ctx.getText()
        str1 = ctxText.split(",")
        str1 = str1[1][:-2]
        receivecontent = str1.strip('"')
        # 判断是是否已经收到过该内容
        if self.receivelist.count(receivecontent) == 0:
            self.receivelist.append(receivecontent)
        pass

    # Exit a parse tree produced by AntlrParser#cblock_whenIReceive.
    def exitCblock_whenIReceive(self, ctx):
        pass

    # Enter a parse tree produced by AntlrParser#procDef.

    #判断是否含有递归存在
    def enterProcDef(self, ctx):
        ctxText = ctx.getText()
        procname=ctx.value()[0].getText().strip('"')
        if ctxText.find('"call"')>0:
            str1=ctxText[ctxText.find('"call"'):]
            if str1.find(procname)>0:
                self.Recursively+=1;
        pass

    # Exit a parse tree produced by AntlrParser#procDef.
    def exitProcDef(self, ctx):
        pass

    # Enter a parse tree produced by AntlrParser#comments_array.
    def enterComments_array(self, ctx):
        pass

    # Exit a parse tree produced by AntlrParser#comments_array.
    def exitComments_array(self, ctx):
        pass


