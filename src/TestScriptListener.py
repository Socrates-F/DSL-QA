# Generated from TestScript.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .TestScriptParser import TestScriptParser
else:
    from TestScriptParser import TestScriptParser

# This class defines a complete listener for a parse tree produced by TestScriptParser.
class TestScriptListener(ParseTreeListener):

    # Enter a parse tree produced by TestScriptParser#script.
    def enterScript(self, ctx:TestScriptParser.ScriptContext):
        pass

    # Exit a parse tree produced by TestScriptParser#script.
    def exitScript(self, ctx:TestScriptParser.ScriptContext):
        pass


    # Enter a parse tree produced by TestScriptParser#testBlock.
    def enterTestBlock(self, ctx:TestScriptParser.TestBlockContext):
        pass

    # Exit a parse tree produced by TestScriptParser#testBlock.
    def exitTestBlock(self, ctx:TestScriptParser.TestBlockContext):
        pass


    # Enter a parse tree produced by TestScriptParser#commandBlock.
    def enterCommandBlock(self, ctx:TestScriptParser.CommandBlockContext):
        pass

    # Exit a parse tree produced by TestScriptParser#commandBlock.
    def exitCommandBlock(self, ctx:TestScriptParser.CommandBlockContext):
        pass


    # Enter a parse tree produced by TestScriptParser#command.
    def enterCommand(self, ctx:TestScriptParser.CommandContext):
        pass

    # Exit a parse tree produced by TestScriptParser#command.
    def exitCommand(self, ctx:TestScriptParser.CommandContext):
        pass


    # Enter a parse tree produced by TestScriptParser#openCmd.
    def enterOpenCmd(self, ctx:TestScriptParser.OpenCmdContext):
        pass

    # Exit a parse tree produced by TestScriptParser#openCmd.
    def exitOpenCmd(self, ctx:TestScriptParser.OpenCmdContext):
        pass


    # Enter a parse tree produced by TestScriptParser#clickCmd.
    def enterClickCmd(self, ctx:TestScriptParser.ClickCmdContext):
        pass

    # Exit a parse tree produced by TestScriptParser#clickCmd.
    def exitClickCmd(self, ctx:TestScriptParser.ClickCmdContext):
        pass


    # Enter a parse tree produced by TestScriptParser#clickTextCmd.
    def enterClickTextCmd(self, ctx:TestScriptParser.ClickTextCmdContext):
        pass

    # Exit a parse tree produced by TestScriptParser#clickTextCmd.
    def exitClickTextCmd(self, ctx:TestScriptParser.ClickTextCmdContext):
        pass


    # Enter a parse tree produced by TestScriptParser#typeCmd.
    def enterTypeCmd(self, ctx:TestScriptParser.TypeCmdContext):
        pass

    # Exit a parse tree produced by TestScriptParser#typeCmd.
    def exitTypeCmd(self, ctx:TestScriptParser.TypeCmdContext):
        pass


    # Enter a parse tree produced by TestScriptParser#uploadCmd.
    def enterUploadCmd(self, ctx:TestScriptParser.UploadCmdContext):
        pass

    # Exit a parse tree produced by TestScriptParser#uploadCmd.
    def exitUploadCmd(self, ctx:TestScriptParser.UploadCmdContext):
        pass


    # Enter a parse tree produced by TestScriptParser#submitCmd.
    def enterSubmitCmd(self, ctx:TestScriptParser.SubmitCmdContext):
        pass

    # Exit a parse tree produced by TestScriptParser#submitCmd.
    def exitSubmitCmd(self, ctx:TestScriptParser.SubmitCmdContext):
        pass


    # Enter a parse tree produced by TestScriptParser#expectCmd.
    def enterExpectCmd(self, ctx:TestScriptParser.ExpectCmdContext):
        pass

    # Exit a parse tree produced by TestScriptParser#expectCmd.
    def exitExpectCmd(self, ctx:TestScriptParser.ExpectCmdContext):
        pass


    # Enter a parse tree produced by TestScriptParser#expectTitleCmd.
    def enterExpectTitleCmd(self, ctx:TestScriptParser.ExpectTitleCmdContext):
        pass

    # Exit a parse tree produced by TestScriptParser#expectTitleCmd.
    def exitExpectTitleCmd(self, ctx:TestScriptParser.ExpectTitleCmdContext):
        pass


    # Enter a parse tree produced by TestScriptParser#waitCmd.
    def enterWaitCmd(self, ctx:TestScriptParser.WaitCmdContext):
        pass

    # Exit a parse tree produced by TestScriptParser#waitCmd.
    def exitWaitCmd(self, ctx:TestScriptParser.WaitCmdContext):
        pass


    # Enter a parse tree produced by TestScriptParser#waitVisibleCmd.
    def enterWaitVisibleCmd(self, ctx:TestScriptParser.WaitVisibleCmdContext):
        pass

    # Exit a parse tree produced by TestScriptParser#waitVisibleCmd.
    def exitWaitVisibleCmd(self, ctx:TestScriptParser.WaitVisibleCmdContext):
        pass


    # Enter a parse tree produced by TestScriptParser#scrollCmd.
    def enterScrollCmd(self, ctx:TestScriptParser.ScrollCmdContext):
        pass

    # Exit a parse tree produced by TestScriptParser#scrollCmd.
    def exitScrollCmd(self, ctx:TestScriptParser.ScrollCmdContext):
        pass


    # Enter a parse tree produced by TestScriptParser#screenshotCmd.
    def enterScreenshotCmd(self, ctx:TestScriptParser.ScreenshotCmdContext):
        pass

    # Exit a parse tree produced by TestScriptParser#screenshotCmd.
    def exitScreenshotCmd(self, ctx:TestScriptParser.ScreenshotCmdContext):
        pass


    # Enter a parse tree produced by TestScriptParser#pauseCmd.
    def enterPauseCmd(self, ctx:TestScriptParser.PauseCmdContext):
        pass

    # Exit a parse tree produced by TestScriptParser#pauseCmd.
    def exitPauseCmd(self, ctx:TestScriptParser.PauseCmdContext):
        pass



del TestScriptParser