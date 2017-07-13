import sys
from antlr4 import *
from AntlrLexer import AntlrLexer
from AntlrParser import AntlrParser
from AntlrListener import AntlrListener

def main(argv):
    input = FileStream(argv[1], encoding='utf-8')
    lexer = AntlrLexer(input)
    stream = CommonTokenStream(lexer)
    parser = AntlrParser(stream)
    tree = parser.json()
    walker = ParseTreeWalker()
    walker.walk(AntlrListener(), tree)

 
if __name__ == '__main__':
    main(sys.argv)