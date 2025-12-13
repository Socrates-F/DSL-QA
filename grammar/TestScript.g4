grammar TestScript;

script: (testBlock)+ EOF;

testBlock: 'test' IDENT ':' commandBlock;

commandBlock: (command)+;

command:
      openCmd
    | clickCmd
    | clickTextCmd
    | typeCmd
    | expectCmd
    | expectTitleCmd
    | waitCmd
    | waitVisibleCmd
    | scrollCmd
    | screenshotCmd
    | uploadCmd
    | submitCmd
    | pauseCmd
    ;

openCmd: 'open' STRING ;
clickCmd: 'click' STRING ;
clickTextCmd: 'click_text' STRING ;
typeCmd: 'type' STRING STRING ;
uploadCmd: 'upload' STRING STRING ;
submitCmd: 'submit' STRING ; 
expectCmd: 'expect' STRING ;
expectTitleCmd: 'expect_title' STRING ;
waitCmd: 'wait' STRING INT ;
waitVisibleCmd: 'wait_visible' STRING INT ;
scrollCmd: 'scroll' STRING ;
screenshotCmd: 'screenshot' STRING ;
pauseCmd: 'pause' INT;

IDENT: [a-zA-Z_][a-zA-Z0-9_]* ;
INT: [0-9]+ ;
STRING: '"' (~["\r\n])* '"' ;
WS: [ \t\r\n]+ -> skip ;
