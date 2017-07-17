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

        self.FlowControl_score = 0 #FlowControl得分
        self.UserInteractivity = 0 #UserInteractivity得分

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
        if ctx.STRING():
            if ctx.STRING().getText()== '"objName"':
                if ctx.value().STRING().getText()!='"Stage"':
                    #print(ctx.value().STRING().getText())
                    self.sprits_count+=1
        pass

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
        pass

    # Exit a parse tree produced by AntlrParser#value.
    def exitValue(self, ctx):
        pass


    # Enter a parse tree produced by AntlrParser#cblock_value.
    def enterCblock_value(self, ctx):
        if ctx.WHENGREENFLAG():
            if self.UserInteractivity < 1:
                self.UserInteractivity = 1
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
        pass

    # Exit a parse tree produced by AntlrParser#cblock_doIfElse.
    def exitCblock_doIfElse(self, ctx):
        pass


    # Enter a parse tree produced by AntlrParser#cblock_doIF.
    def enterCblock_doIF(self, ctx):
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


