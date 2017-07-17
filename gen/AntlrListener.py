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
        self.scrips_count=0
        self.depth = 0
        self.if_depth = 0
        self.until_depth = 0
        self.repeat_depth = 0
        self.proj_count=0
        self.sprits_count=0
        self.wg_count=0
        self.whenclick_count=0
        self.whenkey_count=0
        self.whdrop_count=0
        self.whrecive_count=0
        self.whsensor_count=0


        self.A&p_score=0 #Abstraction and problem decomposition 得分
        self.Parallelism_score=0 #Parallelism得分
        self.Synchronization = 0 #Synchronization得分
        self.FlowControl_score = 0 #FlowControl得分
        self.UserInteractivity = 0 #UserInteractivity得分
        self.LogicalThinking = 0 #LogicalThinking得分
        self.DataRepresentation = 1 #因为太多了，默认先直接给1分.....
        self.score = {}

    def create_score(self):
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
        print("scrips_count:",self.scrips_count)
        print("proj_count:",self.proj_count)
        print("sprits_count:",self.sprits_count)
        self.create_score()
        print( self.score)


    # Enter a parse tree produced by AntlrParser#json.
    def enterJson(self, ctx):
        pass

    # Exit a parse tree produced by AntlrParser#json.
    def exitJson(self, ctx):
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
                    if self.sprits_count>1 and self.scripts<1 and self.A&p_score==0:
                        self.A&p_score=1

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
        self.scrips_count+=1

        # 有scripts就给1分?
        if self.FlowControl_score < 1:
            self.FlowControl_score = 1

        gen = ctx.getChildren()
        print(gen.next())
        print(gen.next())
        print(gen.next())


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
        pass

    # Exit a parse tree produced by AntlrParser#blocks_array.
    def exitBlocks_array(self, ctx):
        pass


    # Enter a parse tree produced by AntlrParser#value.
    def enterValue(self, ctx):
        print(ctx.getText())
        ctx_Text = ctx.getText()
        if ctx.value():
            if ctx.value()[0].getText()=='"procDef"':
                self.proj_count+=1
                if self.proj_count>0 and self.A&p_score=1:
                    self.A&p_score=2
            if ctx.value()[0].getText()=='"whenCloned"':
                self.clone_count+=1
                if self.clone_count>0 and self.A&p_score==2:
                    self.A&p_score=3

        if '"whenKeyPressed"' == ctx_Text:
            self.whenkry_count+=1
            if self.whenkey_count>1 and self.whenclick_count>1 and self.Parallelism_score==1:
                self.Parallelism_score=2
            if self.UserInteractivity < 2:
                self.UserInteractivity = 2
        if '"whenIReceive"'==ctx_Text:
            self.whrecive_count+=1
            if self.whdrop_count>1  or self.whrecive_count>1 or self.whsensor_count>1 and self.Parallelism_score==2:
                self.Parallelism_score=3

        if '"whenSensorGreaterThan"'==ctx_Text:
            self.whsensor_count+=1
            if self.whdrop_count>1  or self.whrecive_count>1 or self.whsensor_count>1 and self.Parallelism_score==2:
                self.Parallelism_score=3



        if '"whenClicked"' == ctx_Text:
            self.whenclick_count+=1
            if self.whenkey_count>1 and self.whenclick_count>1 and self.Parallelism_score==1:
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
            if self.whdrop_count>1  or self.whrecive_count>1 or self.whsensor_count>1 and self.Parallelism_score==2:
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
            if self.wg_count>1 and self.Parallelism_score==0:
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
    def enterCblock_doIF(self, ctx):
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


