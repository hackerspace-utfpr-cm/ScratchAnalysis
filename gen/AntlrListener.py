from antlr4 import *

class AntlrListener(ParseTreeListener):

    def __init__(self):
        self.max_depth = 0
        self.max_if_depth = 0
        self.max_until_depth = 0
        self.max_repeat_depth = 0
        self.if_count = 0
        self.until_count = 0
        self.repeat_count = 0

        self.depth = 0
        self.if_depth = 0
        self.until_depth = 0
        self.repeat_depth = 0

    def print_all(self):
        print "max_depth:", self.max_depth
        print "max_if_depth:", self.max_if_depth
        print "max_until_depth:", self.max_until_depth
        print "max_repeat_depth:", self.max_repeat_depth
        print "if_count:", self.if_count
        print "until_count:", self.until_count
        print "repeat_count:", self.repeat_count

    # Enter a parse tree produced by JSONParser#json.
    def enterJson(self, ctx):
        pass

    # Exit a parse tree produced by JSONParser#json.
    def exitJson(self, ctx):
        self.print_all()



    # Enter a parse tree produced by JSONParser#obj.
    def enterObj(self, ctx):
        pass

    # Exit a parse tree produced by JSONParser#obj.
    def exitObj(self, ctx):
        pass


    # Enter a parse tree produced by JSONParser#pair.
    def enterPair(self, ctx):
        pass

    # Exit a parse tree produced by JSONParser#pair.
    def exitPair(self, ctx):
        pass


    # Enter a parse tree produced by JSONParser#scripts_array.
    def enterScripts_array(self, ctx):
        pass

    # Exit a parse tree produced by JSONParser#scripts_array.
    def exitScripts_array(self, ctx):
        pass


    # Enter a parse tree produced by JSONParser#array.
    def enterArray(self, ctx):
        pass

    # Exit a parse tree produced by JSONParser#array.
    def exitArray(self, ctx):
        pass


    # Enter a parse tree produced by JSONParser#blocks_array.
    def enterBlocks_array(self, ctx):
        pass

    # Exit a parse tree produced by JSONParser#blocks_array.
    def exitBlocks_array(self, ctx):
        pass


    # Enter a parse tree produced by JSONParser#value.
    def enterValue(self, ctx):
        pass

    # Exit a parse tree produced by JSONParser#value.
    def exitValue(self, ctx):
        pass


    # Enter a parse tree produced by JSONParser#cblock_value.
    def enterCblock_value(self, ctx):
        pass

    # Exit a parse tree produced by JSONParser#cblock_value.
    def exitCblock_value(self, ctx):
        pass


    # Enter a parse tree produced by JSONParser#cblock_doRepeat.
    def enterCblock_doRepeat(self, ctx):
        self.depth += 1
        self.repeat_count += 1
        self.repeat_depth += 1

        if self.depth > self.max_depth:
            self.max_depth = self.depth
        if self.repeat_depth > self.max_repeat_depth:
            self.max_repeat_depth = self.repeat_depth
        pass

    # Exit a parse tree produced by JSONParser#cblock_doRepeat.
    def exitCblock_doRepeat(self, ctx):
        self.depth -= 1
        self.repeat_depth += 1

        pass


    # Enter a parse tree produced by JSONParser#cblock_doUntil.
    def enterCblock_doUntil(self, ctx):
        self.depth += 1
        self.until_count += 1
        self.until_depth += 1

        if self.depth > self.max_depth:
            self.max_depth = self.depth
        if self.until_depth > self.max_until_depth:
            self.max_until_depth = self.until_depth
        pass

    # Exit a parse tree produced by JSONParser#cblock_doUntil.
    def exitCblock_doUntil(self, ctx):
        self.depth -= 1
        self.until_depth -= 1
        pass


    # Enter a parse tree produced by JSONParser#cblock_doIfElse.
    def enterCblock_doIfElse(self, ctx):
        self.depth += 1
        self.if_count += 1
        self.if_depth += 1

        if self.depth > self.max_depth:
            self.max_depth = self.depth
        if self.if_depth > self.max_if_depth:
            self.max_if_depth = self.if_depth
        pass

    # Exit a parse tree produced by JSONParser#cblock_doIfElse.
    def exitCblock_doIfElse(self, ctx):
        self.depth -= 1
        self.if_depth -= 1
        pass


    # Enter a parse tree produced by JSONParser#cblock_doIF.
    def enterCblock_doIF(self, ctx):
        self.depth += 1
        self.if_count += 1
        self.if_depth += 1

        if self.depth > self.max_depth:
            self.max_depth = self.depth
        if self.if_depth > self.max_if_depth:
            self.max_if_depth = self.if_depth
        pass

    # Exit a parse tree produced by JSONParser#cblock_doIF.
    def exitCblock_doIF(self, ctx):
        self.depth -= 1
        self.if_depth -= 1
        pass


    # Enter a parse tree produced by JSONParser#cblock_doWaitUntil.
    def enterCblock_doWaitUntil(self, ctx):
        self.depth += 1
        self.until_count += 1
        self.until_depth += 1

        if self.depth > self.max_depth:
            self.max_depth = self.depth
        if self.until_depth > self.max_until_depth:
            self.max_until_depth = self.until_depth
        pass

    # Exit a parse tree produced by JSONParser#cblock_doWaitUntil.
    def exitCblock_doWaitUntil(self, ctx):
        self.depth -= 1
        self.until_depth -= 1
        pass


    # Enter a parse tree produced by JSONParser#cblock_doForever.
    def enterCblock_doForever(self, ctx):
        pass

    # Exit a parse tree produced by JSONParser#cblock_doForever.
    def exitCblock_doForever(self, ctx):
        pass


