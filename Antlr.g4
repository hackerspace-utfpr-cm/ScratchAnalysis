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
   | STRING ':' value
   ;

scripts_array
   : '[' '[' value ',' value ',' blocks_array ']' (',' '[' value ',' value ',' blocks_array ']')* ']'
   ;


array
   : '[' value (',' value)* ']'
   | '[' cblock_value (',' cblock_value)* ']'
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

cblock_value
   :'[' '"whenGreenFlag"' ']'
   |cblock_doRepeat
   |cblock_doUntil
   |cblock_doIfElse
   |cblock_doIF
   |cblock_doWaitUntil
   |cblock_doForever
   |array
   ;

cblock_doRepeat
   : '[' '"doRepeat"' ',' NUMBER ',' value ']'
   ;

cblock_doUntil
   : '[' '"doUntil"' ',' value ',' value ']'
   ;

cblock_doIfElse
   : '[' '"doIfElse"' ',' value ',' value ',' value ']'
   ;

cblock_doIF
   : '[' '"doIf"' ',' value ',' value ']'
   ;

cblock_doWaitUntil
   : '[' '"doWaitUntil"' ',' value ']'
   ;

cblock_doForever
   : '[' '"doForever"' ',' value ']'
   ;

SCRIPTS
   : '"scripts"'
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
   : '-'? INT '.' [0-9] + EXP? | '-'? INT EXP | '-'? INT
   ;
fragment INT
   : '0' | [1-9] [0-9]*
   ;
// no leading zeros
fragment EXP
   : [Ee] [+\-]? INT
   ;
// \- since - means "range" inside [...]
WS
   : [ \t\n\r] + -> skip
   ;