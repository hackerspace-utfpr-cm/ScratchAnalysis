// Derived from http://json.org
grammar Antlr;

json
   : value
   ;

obj
   : '{' pair (',' pair)* '}'
   | '{' '}'
   ;

pair
   : SCRIPTS ':' scripts_array
   | SCRIPTCOMMENTS ':' comments_array
   | STRING ':' value
   | costumes
   | changename
   ;

scripts_array
   : '[' '[' value ',' value ',' blocks_array ']' (',' '[' value ',' value ',' blocks_array ']')* ']'
   ;


array
   : '[' cblock_value (',' cblock_value)* ']'
   | '[' value (',' value)* ']'
   | '[' ']'

   ;

blocks_array
   : '[' cblock_value (',' cblock_value)* ']'
   | '[' ']'
   ;

value
   : STRING
   | NUMBER
   | obj
   | array
   | 'true'
   | 'false'
   | 'null'
   ;

condition
   : array
   | 'false'
   ;

cblock_value
   :'[' WHENGREENFLAG ']'
   |cblock_doRepeat
   |cblock_doUntil
   |cblock_doIfElse
   |cblock_doIF
   |cblock_doWaitUntil
   |cblock_doForever
   |cblock_doBroadcast
   |cblock_whenIReceive
   |procDef
   |array
   |
   ;

cblock_doRepeat
   : '[' '"doRepeat"' ',' NUMBER ',' value ']'
   |'[' '"doRepeat"' ',' value ',' value ']'
   ;

cblock_doUntil
   : '[' '"doUntil"' ',' condition ','  content ']'
   ;

cblock_doIfElse
   : '[' '"doIfElse"' ',' condition ',' value ',' value ']'
   ;

cblock_doIF
   : '[' '"doIf"' ',' condition ',' value ']'
   ;

cblock_doWaitUntil
   : '[' '"doWaitUntil"' ',' condition ']'
   ;

cblock_doForever
   : '[' '"doForever"' ',' value ']'
   ;

cblock_doBroadcast
   : '[' '"broadcast:"' ',' array ']'
   |'[' '"broadcast:"' ',' STRING ']'
   |'[' '"doBroadcastAndWait"' ',' array ']'
   |'[' '"doBroadcastAndWait"' ',' STRING ']'
   ;

cblock_whenIReceive
   : '[' '"whenIReceive"' ',' STRING ']'
   ;

procDef
   : '[' '"procDef"' ',' value ',' value ',' value ',' value ']'(',' cblock_value)*
   ;

comments_array
   : '[' value (',' value)* ']'
   ;

costumes
   :'"costumes"' ':' '[' costume_content(',' costume_content)*']'
   ;
costume_content
   :'{' '"costumeName"' ':' value ',' '"baseLayerID": 'value',''"baseLayerMD5": 'value',''"bitmapResolution": 'value',''"rotationCenterX": 'value',''"rotationCenterY": 'value'}'
   ;


changename
   :'"changecos":' array
   |'"changespr":' array
   ;

content
   : STRING
   | NUMBER
   | obj
   | array
   | 'true'
   | 'false'
   | 'null'
   ;

SCRIPTCOMMENTS
   : '"scriptComments"'
   ;

SCRIPTS
   : '"scripts"'
   ;

WHENGREENFLAG
    : '"whenGreenFlag"'
    ;

STRING
   : '"' (ESC | ~ ["\\])* '"'
   ;

fragment ESC
   : '\\' (["\\/bfnrt] | UNICODE)
   ;
fragment UNICODE
   : 'u' HEX HEX HEX HEX
   ;
fragment HEX
   : [0-9a-fA-F]
   ;
NUMBER
   : '-'? INT ('.' [0-9] +)? EXP ?
   ;
fragment INT
   : '0' | [1-9] [0-9]*
   ;
// no leading zeros
fragment EXP
   : [Ee] [+\-]? INT+
   ;
// \- since - means "range" inside [...]
WS
   : [ \t\n\r] + -> skip
   ;