# Generated from TestScript.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,19,110,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,1,0,4,0,36,8,0,11,0,12,0,37,1,0,1,
        0,1,1,1,1,1,1,1,1,1,1,1,2,4,2,48,8,2,11,2,12,2,49,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,65,8,3,1,4,1,4,1,4,1,5,
        1,5,1,5,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,9,1,9,1,9,
        1,10,1,10,1,10,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,13,1,13,1,13,
        1,13,1,14,1,14,1,14,1,15,1,15,1,15,1,16,1,16,1,16,1,16,0,0,17,0,
        2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,0,0,106,0,35,1,0,0,0,
        2,41,1,0,0,0,4,47,1,0,0,0,6,64,1,0,0,0,8,66,1,0,0,0,10,69,1,0,0,
        0,12,72,1,0,0,0,14,75,1,0,0,0,16,79,1,0,0,0,18,83,1,0,0,0,20,86,
        1,0,0,0,22,89,1,0,0,0,24,92,1,0,0,0,26,96,1,0,0,0,28,100,1,0,0,0,
        30,103,1,0,0,0,32,106,1,0,0,0,34,36,3,2,1,0,35,34,1,0,0,0,36,37,
        1,0,0,0,37,35,1,0,0,0,37,38,1,0,0,0,38,39,1,0,0,0,39,40,5,0,0,1,
        40,1,1,0,0,0,41,42,5,1,0,0,42,43,5,16,0,0,43,44,5,2,0,0,44,45,3,
        4,2,0,45,3,1,0,0,0,46,48,3,6,3,0,47,46,1,0,0,0,48,49,1,0,0,0,49,
        47,1,0,0,0,49,50,1,0,0,0,50,5,1,0,0,0,51,65,3,8,4,0,52,65,3,10,5,
        0,53,65,3,12,6,0,54,65,3,14,7,0,55,65,3,20,10,0,56,65,3,22,11,0,
        57,65,3,24,12,0,58,65,3,26,13,0,59,65,3,28,14,0,60,65,3,30,15,0,
        61,65,3,16,8,0,62,65,3,18,9,0,63,65,3,32,16,0,64,51,1,0,0,0,64,52,
        1,0,0,0,64,53,1,0,0,0,64,54,1,0,0,0,64,55,1,0,0,0,64,56,1,0,0,0,
        64,57,1,0,0,0,64,58,1,0,0,0,64,59,1,0,0,0,64,60,1,0,0,0,64,61,1,
        0,0,0,64,62,1,0,0,0,64,63,1,0,0,0,65,7,1,0,0,0,66,67,5,3,0,0,67,
        68,5,18,0,0,68,9,1,0,0,0,69,70,5,4,0,0,70,71,5,18,0,0,71,11,1,0,
        0,0,72,73,5,5,0,0,73,74,5,18,0,0,74,13,1,0,0,0,75,76,5,6,0,0,76,
        77,5,18,0,0,77,78,5,18,0,0,78,15,1,0,0,0,79,80,5,7,0,0,80,81,5,18,
        0,0,81,82,5,18,0,0,82,17,1,0,0,0,83,84,5,8,0,0,84,85,5,18,0,0,85,
        19,1,0,0,0,86,87,5,9,0,0,87,88,5,18,0,0,88,21,1,0,0,0,89,90,5,10,
        0,0,90,91,5,18,0,0,91,23,1,0,0,0,92,93,5,11,0,0,93,94,5,18,0,0,94,
        95,5,17,0,0,95,25,1,0,0,0,96,97,5,12,0,0,97,98,5,18,0,0,98,99,5,
        17,0,0,99,27,1,0,0,0,100,101,5,13,0,0,101,102,5,18,0,0,102,29,1,
        0,0,0,103,104,5,14,0,0,104,105,5,18,0,0,105,31,1,0,0,0,106,107,5,
        15,0,0,107,108,5,17,0,0,108,33,1,0,0,0,3,37,49,64
    ]

class TestScriptParser ( Parser ):

    grammarFileName = "TestScript.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'test'", "':'", "'open'", "'click'", 
                     "'click_text'", "'type'", "'upload'", "'submit'", "'expect'", 
                     "'expect_title'", "'wait'", "'wait_visible'", "'scroll'", 
                     "'screenshot'", "'pause'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "IDENT", "INT", "STRING", "WS" ]

    RULE_script = 0
    RULE_testBlock = 1
    RULE_commandBlock = 2
    RULE_command = 3
    RULE_openCmd = 4
    RULE_clickCmd = 5
    RULE_clickTextCmd = 6
    RULE_typeCmd = 7
    RULE_uploadCmd = 8
    RULE_submitCmd = 9
    RULE_expectCmd = 10
    RULE_expectTitleCmd = 11
    RULE_waitCmd = 12
    RULE_waitVisibleCmd = 13
    RULE_scrollCmd = 14
    RULE_screenshotCmd = 15
    RULE_pauseCmd = 16

    ruleNames =  [ "script", "testBlock", "commandBlock", "command", "openCmd", 
                   "clickCmd", "clickTextCmd", "typeCmd", "uploadCmd", "submitCmd", 
                   "expectCmd", "expectTitleCmd", "waitCmd", "waitVisibleCmd", 
                   "scrollCmd", "screenshotCmd", "pauseCmd" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    IDENT=16
    INT=17
    STRING=18
    WS=19

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ScriptContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(TestScriptParser.EOF, 0)

        def testBlock(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TestScriptParser.TestBlockContext)
            else:
                return self.getTypedRuleContext(TestScriptParser.TestBlockContext,i)


        def getRuleIndex(self):
            return TestScriptParser.RULE_script

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScript" ):
                listener.enterScript(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScript" ):
                listener.exitScript(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScript" ):
                return visitor.visitScript(self)
            else:
                return visitor.visitChildren(self)




    def script(self):

        localctx = TestScriptParser.ScriptContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_script)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 34
                self.testBlock()
                self.state = 37 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1):
                    break

            self.state = 39
            self.match(TestScriptParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TestBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(TestScriptParser.IDENT, 0)

        def commandBlock(self):
            return self.getTypedRuleContext(TestScriptParser.CommandBlockContext,0)


        def getRuleIndex(self):
            return TestScriptParser.RULE_testBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTestBlock" ):
                listener.enterTestBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTestBlock" ):
                listener.exitTestBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTestBlock" ):
                return visitor.visitTestBlock(self)
            else:
                return visitor.visitChildren(self)




    def testBlock(self):

        localctx = TestScriptParser.TestBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_testBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(TestScriptParser.T__0)
            self.state = 42
            self.match(TestScriptParser.IDENT)
            self.state = 43
            self.match(TestScriptParser.T__1)
            self.state = 44
            self.commandBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def command(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TestScriptParser.CommandContext)
            else:
                return self.getTypedRuleContext(TestScriptParser.CommandContext,i)


        def getRuleIndex(self):
            return TestScriptParser.RULE_commandBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommandBlock" ):
                listener.enterCommandBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommandBlock" ):
                listener.exitCommandBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommandBlock" ):
                return visitor.visitCommandBlock(self)
            else:
                return visitor.visitChildren(self)




    def commandBlock(self):

        localctx = TestScriptParser.CommandBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_commandBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 46
                self.command()
                self.state = 49 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 65528) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def openCmd(self):
            return self.getTypedRuleContext(TestScriptParser.OpenCmdContext,0)


        def clickCmd(self):
            return self.getTypedRuleContext(TestScriptParser.ClickCmdContext,0)


        def clickTextCmd(self):
            return self.getTypedRuleContext(TestScriptParser.ClickTextCmdContext,0)


        def typeCmd(self):
            return self.getTypedRuleContext(TestScriptParser.TypeCmdContext,0)


        def expectCmd(self):
            return self.getTypedRuleContext(TestScriptParser.ExpectCmdContext,0)


        def expectTitleCmd(self):
            return self.getTypedRuleContext(TestScriptParser.ExpectTitleCmdContext,0)


        def waitCmd(self):
            return self.getTypedRuleContext(TestScriptParser.WaitCmdContext,0)


        def waitVisibleCmd(self):
            return self.getTypedRuleContext(TestScriptParser.WaitVisibleCmdContext,0)


        def scrollCmd(self):
            return self.getTypedRuleContext(TestScriptParser.ScrollCmdContext,0)


        def screenshotCmd(self):
            return self.getTypedRuleContext(TestScriptParser.ScreenshotCmdContext,0)


        def uploadCmd(self):
            return self.getTypedRuleContext(TestScriptParser.UploadCmdContext,0)


        def submitCmd(self):
            return self.getTypedRuleContext(TestScriptParser.SubmitCmdContext,0)


        def pauseCmd(self):
            return self.getTypedRuleContext(TestScriptParser.PauseCmdContext,0)


        def getRuleIndex(self):
            return TestScriptParser.RULE_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommand" ):
                listener.enterCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommand" ):
                listener.exitCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommand" ):
                return visitor.visitCommand(self)
            else:
                return visitor.visitChildren(self)




    def command(self):

        localctx = TestScriptParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_command)
        try:
            self.state = 64
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 51
                self.openCmd()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 52
                self.clickCmd()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 53
                self.clickTextCmd()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 4)
                self.state = 54
                self.typeCmd()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 5)
                self.state = 55
                self.expectCmd()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 6)
                self.state = 56
                self.expectTitleCmd()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 7)
                self.state = 57
                self.waitCmd()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 8)
                self.state = 58
                self.waitVisibleCmd()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 9)
                self.state = 59
                self.scrollCmd()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 10)
                self.state = 60
                self.screenshotCmd()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 11)
                self.state = 61
                self.uploadCmd()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 12)
                self.state = 62
                self.submitCmd()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 13)
                self.state = 63
                self.pauseCmd()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpenCmdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(TestScriptParser.STRING, 0)

        def getRuleIndex(self):
            return TestScriptParser.RULE_openCmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpenCmd" ):
                listener.enterOpenCmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpenCmd" ):
                listener.exitOpenCmd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpenCmd" ):
                return visitor.visitOpenCmd(self)
            else:
                return visitor.visitChildren(self)




    def openCmd(self):

        localctx = TestScriptParser.OpenCmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_openCmd)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(TestScriptParser.T__2)
            self.state = 67
            self.match(TestScriptParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClickCmdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(TestScriptParser.STRING, 0)

        def getRuleIndex(self):
            return TestScriptParser.RULE_clickCmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClickCmd" ):
                listener.enterClickCmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClickCmd" ):
                listener.exitClickCmd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClickCmd" ):
                return visitor.visitClickCmd(self)
            else:
                return visitor.visitChildren(self)




    def clickCmd(self):

        localctx = TestScriptParser.ClickCmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_clickCmd)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(TestScriptParser.T__3)
            self.state = 70
            self.match(TestScriptParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClickTextCmdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(TestScriptParser.STRING, 0)

        def getRuleIndex(self):
            return TestScriptParser.RULE_clickTextCmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClickTextCmd" ):
                listener.enterClickTextCmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClickTextCmd" ):
                listener.exitClickTextCmd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClickTextCmd" ):
                return visitor.visitClickTextCmd(self)
            else:
                return visitor.visitChildren(self)




    def clickTextCmd(self):

        localctx = TestScriptParser.ClickTextCmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_clickTextCmd)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(TestScriptParser.T__4)
            self.state = 73
            self.match(TestScriptParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeCmdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(TestScriptParser.STRING)
            else:
                return self.getToken(TestScriptParser.STRING, i)

        def getRuleIndex(self):
            return TestScriptParser.RULE_typeCmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeCmd" ):
                listener.enterTypeCmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeCmd" ):
                listener.exitTypeCmd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeCmd" ):
                return visitor.visitTypeCmd(self)
            else:
                return visitor.visitChildren(self)




    def typeCmd(self):

        localctx = TestScriptParser.TypeCmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_typeCmd)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(TestScriptParser.T__5)
            self.state = 76
            self.match(TestScriptParser.STRING)
            self.state = 77
            self.match(TestScriptParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UploadCmdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(TestScriptParser.STRING)
            else:
                return self.getToken(TestScriptParser.STRING, i)

        def getRuleIndex(self):
            return TestScriptParser.RULE_uploadCmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUploadCmd" ):
                listener.enterUploadCmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUploadCmd" ):
                listener.exitUploadCmd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUploadCmd" ):
                return visitor.visitUploadCmd(self)
            else:
                return visitor.visitChildren(self)




    def uploadCmd(self):

        localctx = TestScriptParser.UploadCmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_uploadCmd)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(TestScriptParser.T__6)
            self.state = 80
            self.match(TestScriptParser.STRING)
            self.state = 81
            self.match(TestScriptParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubmitCmdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(TestScriptParser.STRING, 0)

        def getRuleIndex(self):
            return TestScriptParser.RULE_submitCmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubmitCmd" ):
                listener.enterSubmitCmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubmitCmd" ):
                listener.exitSubmitCmd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubmitCmd" ):
                return visitor.visitSubmitCmd(self)
            else:
                return visitor.visitChildren(self)




    def submitCmd(self):

        localctx = TestScriptParser.SubmitCmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_submitCmd)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(TestScriptParser.T__7)
            self.state = 84
            self.match(TestScriptParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpectCmdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(TestScriptParser.STRING, 0)

        def getRuleIndex(self):
            return TestScriptParser.RULE_expectCmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpectCmd" ):
                listener.enterExpectCmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpectCmd" ):
                listener.exitExpectCmd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpectCmd" ):
                return visitor.visitExpectCmd(self)
            else:
                return visitor.visitChildren(self)




    def expectCmd(self):

        localctx = TestScriptParser.ExpectCmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_expectCmd)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(TestScriptParser.T__8)
            self.state = 87
            self.match(TestScriptParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpectTitleCmdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(TestScriptParser.STRING, 0)

        def getRuleIndex(self):
            return TestScriptParser.RULE_expectTitleCmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpectTitleCmd" ):
                listener.enterExpectTitleCmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpectTitleCmd" ):
                listener.exitExpectTitleCmd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpectTitleCmd" ):
                return visitor.visitExpectTitleCmd(self)
            else:
                return visitor.visitChildren(self)




    def expectTitleCmd(self):

        localctx = TestScriptParser.ExpectTitleCmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_expectTitleCmd)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(TestScriptParser.T__9)
            self.state = 90
            self.match(TestScriptParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WaitCmdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(TestScriptParser.STRING, 0)

        def INT(self):
            return self.getToken(TestScriptParser.INT, 0)

        def getRuleIndex(self):
            return TestScriptParser.RULE_waitCmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWaitCmd" ):
                listener.enterWaitCmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWaitCmd" ):
                listener.exitWaitCmd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWaitCmd" ):
                return visitor.visitWaitCmd(self)
            else:
                return visitor.visitChildren(self)




    def waitCmd(self):

        localctx = TestScriptParser.WaitCmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_waitCmd)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(TestScriptParser.T__10)
            self.state = 93
            self.match(TestScriptParser.STRING)
            self.state = 94
            self.match(TestScriptParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WaitVisibleCmdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(TestScriptParser.STRING, 0)

        def INT(self):
            return self.getToken(TestScriptParser.INT, 0)

        def getRuleIndex(self):
            return TestScriptParser.RULE_waitVisibleCmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWaitVisibleCmd" ):
                listener.enterWaitVisibleCmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWaitVisibleCmd" ):
                listener.exitWaitVisibleCmd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWaitVisibleCmd" ):
                return visitor.visitWaitVisibleCmd(self)
            else:
                return visitor.visitChildren(self)




    def waitVisibleCmd(self):

        localctx = TestScriptParser.WaitVisibleCmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_waitVisibleCmd)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(TestScriptParser.T__11)
            self.state = 97
            self.match(TestScriptParser.STRING)
            self.state = 98
            self.match(TestScriptParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScrollCmdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(TestScriptParser.STRING, 0)

        def getRuleIndex(self):
            return TestScriptParser.RULE_scrollCmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScrollCmd" ):
                listener.enterScrollCmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScrollCmd" ):
                listener.exitScrollCmd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScrollCmd" ):
                return visitor.visitScrollCmd(self)
            else:
                return visitor.visitChildren(self)




    def scrollCmd(self):

        localctx = TestScriptParser.ScrollCmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_scrollCmd)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(TestScriptParser.T__12)
            self.state = 101
            self.match(TestScriptParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScreenshotCmdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(TestScriptParser.STRING, 0)

        def getRuleIndex(self):
            return TestScriptParser.RULE_screenshotCmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScreenshotCmd" ):
                listener.enterScreenshotCmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScreenshotCmd" ):
                listener.exitScreenshotCmd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScreenshotCmd" ):
                return visitor.visitScreenshotCmd(self)
            else:
                return visitor.visitChildren(self)




    def screenshotCmd(self):

        localctx = TestScriptParser.ScreenshotCmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_screenshotCmd)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(TestScriptParser.T__13)
            self.state = 104
            self.match(TestScriptParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PauseCmdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(TestScriptParser.INT, 0)

        def getRuleIndex(self):
            return TestScriptParser.RULE_pauseCmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPauseCmd" ):
                listener.enterPauseCmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPauseCmd" ):
                listener.exitPauseCmd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPauseCmd" ):
                return visitor.visitPauseCmd(self)
            else:
                return visitor.visitChildren(self)




    def pauseCmd(self):

        localctx = TestScriptParser.PauseCmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_pauseCmd)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(TestScriptParser.T__14)
            self.state = 107
            self.match(TestScriptParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





