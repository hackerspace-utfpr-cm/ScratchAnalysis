# Generated from E:/new/antlrg/ScratchAnalysis\Antlr.g4 by ANTLR 4.7
# -*- coding: utf-8 -*-
from antlr4 import *

# This class defines a complete listener for a parse tree produced by AntlrParser.
class AntlrListener(ParseTreeListener):
    def __init__(self):
        self.max_depth = 0
        self.max_if_depth = 0
        self.max_until_depth = 0
        self.max_repeat_depth = 0
        self.if_count = 0
        self.until_count = 0
        self.repeat_count = 0
        self.scripts_count=0
        self.depth = 0
        self.if_depth = 0
        self.until_depth = 0
        self.repeat_depth = 0
        self.proj_count=0
        self.sprits_count=0
        self.wg_count=0
        self.clone_count=0
        self.whenclick_count=0
        self.whenkey_count=0
        self.whdrop_count=0
        self.whrecive_count=0
        self.whsensor_count=0
        self.deadcode_count=0
        self.broadcastlist=[]
        self.receivelist=[]
        self.Meaningless_count=0
        self.initit=0


        self.ap_score=0 #Abstraction and problem decomposition 得分
        self.Parallelism_score=0 #Parallelism得分
        self.Synchronization = 0 #Synchronization得分
        self.FlowControl_score = 0 #FlowControl得分
        self.UserInteractivity = 0 #UserInteractivity得分
        self.LogicalThinking = 0 #LogicalThinking得分
        self.DataRepresentation = 1 #因为太多了，默认先直接给1分.....
        self.score = {}

    def create_score(self):
        self.score['Abstraction']=self.ap_score
        self.score['Parallelism']=self.Parallelism_score
        self.score['FlowControl'] = self.FlowControl_score
        self.score['UserInteractivity'] = self.UserInteractivity
        self.score['LogicalThinking'] = self.LogicalThinking
        self.score['DataRepresentation'] = self.DataRepresentation
        self.score['Synchronization'] = self.Synchronization

    def print_all(self):
        print ("max_depth:", self.max_depth)
        print ("max_if_depth:", self.max_if_depth)
        print ("max_until_depth:", self.max_until_depth)
        print ("max_repeat_depth:", self.max_repeat_depth)
        print ("if_count:", self.if_count)
        print ("until_count:", self.until_count)
        print ("repeat_count:", self.repeat_count)
        print("scripts_count:",self.scripts_count)
        print("proj_count:",self.proj_count)
        print("sprits_count:",self.sprits_count)
        print("deadcode_count:", self.deadcode_count)
        self.create_score()
        print( self.score)


    # Enter a parse tree produced by AntlrParser#json.
    def enterJson(self, ctx):
        pass

    # Exit a parse tree produced by AntlrParser#json.
    def exitJson(self, ctx):
        if len(self.receivelist)!=len(self.broadcastlist):
            print("广播不匹配")
        else:
            for r in self.receivelist:
                if self.broadcastlist.count(r)==0:
                    print("广播不匹配")
                    self.deadcode_count+=1
        if self.Meaningless_count>0:
            print("有"+str(self.Meaningless_count)+"个角色存在无意义命名")
        if self.initit>0:
            print("可能未同步")
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
        ctx_STRING = ctx.STRING()
        if ctx_STRING:
            ctx_STRING_Text = ctx_STRING.getText()
            if ctx_STRING_Text == '"objName"':
                if ctx.value().STRING().getText()!='"Stage"':
                    #print(ctx.value().STRING().getText())
                    self.sprits_count+=1
                    if self.sprits_count>1 and self.scripts_count>1 and self.ap_score==0:#标准1-1
                        self.ap_score=1
                if ctx.value().STRING().getText().find('Sprite')>0:
                    self.Meaningless_count +=1

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
        flag1=0
        flag2=0
        str2 = ctx.getText()
        str3=str2
        if str2.find('"hide"')>0:#关于初始化的几个方面
            if str2.find('"show"')<0:
                self.initit=1
        if str2.find('"nextCostume"')>0:
            if str2.find('"lookLike:"')<0:
                self.initit = 1
        if str2.find('"changeGraphicEffect:by:"')>0:
            if str2.find('"setGraphicEffect:to:"')<0:
                self.initit=1
        if str2.find('"changeSizeBy:"')>0:
            if str2.find('"setSizeTo:"')<0:
                self.initit=1
        if str2.find('"nextScene"') > 0:
            if str2.find('"startScene"') < 0:
                self.initit = 1
        if str2.find('"turnRight:"') > 0 or  str2.find('"turnLeft:"') > 0 or  str2.find('"pointTowards:"') > 0 :
            if str2.find('"heading:"') < 0:
                self.initit = 1
        if str2.find('"forward:"') > 0 or str2.find('"gotoSpriteOrMouse:"') > 0 or str2.find('"glideSecs:toX:y:elapsed:from:"')  > 0:
            if str2.find('"gotoX:y:"') < 0:
                self.initit = 1
        if str2.find('"changeXposBy:"') > 0:
            if str2.find('"xpos:"') < 0 and str2.find('"gotoX:y:"') < 0:
                self.initit = 1
        if str2.find('"changeYposBy:"') > 0:
            if str2.find('"ypos:"') < 0 and str2.find('"gotoX:y:"') < 0:
                self.initit = 1

        # print(str2)
        while str2.find("laySound")>0 and flag2==0:#处理音画同步
            soundstr=str2[str2.find("laySound"):str2.find("laySound")+40]
            sc=ctx.getText().find(soundstr);
            str1=str2[str2.find("laySound"):]
            s1 =str2.find("laySound")
            str1=str1[:str1.find(']')]
            str1 = str1.split(',')
            str1=str1[1].strip('"')
            #print(str1+"声音")
            # dictsay.append(str1)
            while str3.find("say")>0 and flag2==0:
                saystr=str3[str3.find("say"):str3.find("say")+40]
                sy=ctx.getText().find(saystr)
                str4 = str3[str3.find("say"):]
                # print(str4)
                s2=str3.find("say")
                str4 = str4[:str4.find(']')]
                # print(str4)
                str4 = str4.split(',')
                str4 = str4[1].strip('"')
                # print(str3)
                if str4==str1 and sc<sy:
                    print("声画不同步错误")
                    flag2=1
                    break
                elif str4==str1 and sc>sy:
                    str3=str3[s2:]
                    # print(str3)
                    # print("找到一个生化匹配")
                    flag1=1
                    break
                else:
                    str3 = str3[s2:]
            str2 = str2[s1:]
            if flag1==0:
                str3=ctx.getText()
            #print(str3)
        # str3=str2[str2.find("playsound"):str2.find("]")]
        # print(str1,str3)
        self.scripts_count+=1#标准1-1
        if self.sprits_count > 1 and self.scripts_count > 1 and self.ap_score <1:
            self.ap_score = 1
        # 有scripts就给1分?
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
        # print(ctx.getText().find("when"))
        if ctx.getText().find("when")==-1:
            self.deadcode_count+=1
        pass

    # Exit a parse tree produced by AntlrParser#blocks_array.
    def exitBlocks_array(self, ctx):
        pass


    # Enter a parse tree produced by AntlrParser#value.
    def enterValue(self, ctx):
        # print(ctx.getText())
        ctx_Text = ctx.getText()
        if ctx_Text=='"procDef"':#标准1-2
          #  if ctx.value()[0].getText()=='"procDef"':
            self.proj_count+=1
            if self.proj_count>0 and self.ap_score<2:
                self.ap_score=2
        if ctx_Text=='"whenCloned"':#标准1-3
            self.clone_count+=1
            if self.clone_count>0 and self.ap_score<3:
                self.ap_score=3

        if '"whenKeyPressed"' == ctx_Text:
            self.whenkey_count+=1
            if self.whenkey_count>1 and self.whenclick_count>1 and self.Parallelism_score<2:#标准2-2
                self.Parallelism_score=2
            if self.UserInteractivity < 2:
                self.UserInteractivity = 2
        if '"whenIReceive"'==ctx_Text:
            self.whrecive_count+=1
            if self.whdrop_count>1  or self.whrecive_count>1 or self.whsensor_count>1 and self.Parallelism_score<3:#标准2-3
                self.Parallelism_score=3

        if '"whenSensorGreaterThan"'==ctx_Text:
            self.whsensor_count+=1
            if self.whdrop_count>1  or self.whrecive_count>1 or self.whsensor_count>1 and self.Parallelism_score<3:#标准2-3
                self.Parallelism_score=3



        if '"whenClicked"' == ctx_Text:
            self.whenclick_count+=1
            if self.whenkey_count>1 and self.whenclick_count>1 and self.Parallelism_score<2:#标准2-2
                self.Parallelism_score=2
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
        if ctx_Text =='"whenSceneStarts"':
            self.whdrop_count+=1
            if self.whdrop_count>1  or self.whrecive_count>1 or self.whsensor_count>1 and self.Parallelism_score<3:#标准2-3
                self.Parallelism_score=3


    # Exit a parse tree produced by AntlrParser#value.
    def exitValue(self, ctx):
        pass


    # Enter a parse tree produced by AntlrParser#cblock_value.
    def enterCblock_value(self, ctx):
        if ctx.WHENGREENFLAG():
            if self.UserInteractivity < 1:
                self.UserInteractivity = 1
            self.wg_count+=1
            if self.wg_count>1 and self.Parallelism_score==0:#标准2-1
                self.Parallelism_score=1
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
    def enterCblock_doIF(self, ctx):#将if中比较的两部分
        ctx_Text=ctx.getText()
        # print(ctx_Text)
        # Varlist=['readVariable','lineCountOfList','randomFrom']
        if ctx.getText().find('readVariable')>0 or ctx.getText().find('lineCountOfList')>0 or ctx.getText().find('randomFrom')>0:
            return
        elif ctx.getText().find('<')>0:
            str1=ctx_Text[ctx.getText().find('<'):ctx.getText().find(']')]
            str2=str1.split(',')
            v1=str2[1].strip('"')
            v2=str2[2].strip('"')
            # print(int(v1),int(v2))
            if int(v1)>int(v2):
                self.deadcode_count+=1
        elif ctx.getText().find('>')>0:
            str1=ctx_Text[ctx.getText().find('<'):ctx.getText().find(']')]
            str2=str1.split(',')
            v1=str2[1].strip('"')
            v2=str2[2].strip('"')
            # print(int(v1),int(v2))
            if int(v1)<int(v2):
                self.deadcode_count+=1
        elif ctx.getText().find('=')>0:
            str1=ctx_Text[ctx.getText().find('<'):ctx.getText().find(']')]
            str2=str1.split(',')
            v1=str2[1].strip('"')
            v2=str2[2].strip('"')
            # print(int(v1),int(v2))
            if int(v1)!=int(v2):
                self.deadcode_count+=1

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
    def enterCblock_doBroadcast(self, ctx):
        ctxText=ctx.getText()
        # print(ctxText)
        str1=ctxText.split(",")
        str1=str1[1][:-2]
        broadcastcontent=str1.strip('"')
        if self.broadcastlist.count(broadcastcontent)==0:
            self.broadcastlist.append(broadcastcontent)
        # print(broadcastcontent+"发送")
        pass

    # Exit a parse tree produced by AntlrParser#cblock_doBroadcast.
    def exitCblock_doBroadcast(self, ctx):
        pass


    # Enter a parse tree produced by AntlrParser#cblock_whenIReceive.
    def enterCblock_whenIReceive(self, ctx):
        ctxText = ctx.getText()
        # print(ctxText)
        str1 = ctxText.split(",")
        str1 = str1[1][:-2]
        receivecontent = str1.strip('"')
        if self.receivelist.count(receivecontent) == 0:
            self.receivelist.append(receivecontent)
        # print(receivecontent+"接收")
        pass

    # Exit a parse tree produced by AntlrParser#cblock_whenIReceive.
    def exitCblock_whenIReceive(self, ctx):
        pass



