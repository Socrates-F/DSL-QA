# Generated from TestScript.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .TestScriptParser import TestScriptParser
else:
    from TestScriptParser import TestScriptParser

# This class defines a complete generic visitor for a parse tree produced by TestScriptParser.

class TestScriptVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by TestScriptParser#script.
    def visitScript(self, ctx:TestScriptParser.ScriptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TestScriptParser#testBlock.
    def visitTestBlock(self, ctx:TestScriptParser.TestBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TestScriptParser#commandBlock.
    def visitCommandBlock(self, ctx:TestScriptParser.CommandBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TestScriptParser#command.
    def visitCommand(self, ctx:TestScriptParser.CommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TestScriptParser#openCmd.
    def visitOpenCmd(self, ctx:TestScriptParser.OpenCmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TestScriptParser#clickCmd.
    def visitClickCmd(self, ctx:TestScriptParser.ClickCmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TestScriptParser#clickTextCmd.
    def visitClickTextCmd(self, ctx:TestScriptParser.ClickTextCmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TestScriptParser#typeCmd.
    def visitTypeCmd(self, ctx:TestScriptParser.TypeCmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TestScriptParser#uploadCmd.
    def visitUploadCmd(self, ctx:TestScriptParser.UploadCmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TestScriptParser#submitCmd.
    def visitSubmitCmd(self, ctx:TestScriptParser.SubmitCmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TestScriptParser#expectCmd.
    def visitExpectCmd(self, ctx:TestScriptParser.ExpectCmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TestScriptParser#expectTitleCmd.
    def visitExpectTitleCmd(self, ctx:TestScriptParser.ExpectTitleCmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TestScriptParser#waitCmd.
    def visitWaitCmd(self, ctx:TestScriptParser.WaitCmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TestScriptParser#waitVisibleCmd.
    def visitWaitVisibleCmd(self, ctx:TestScriptParser.WaitVisibleCmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TestScriptParser#scrollCmd.
    def visitScrollCmd(self, ctx:TestScriptParser.ScrollCmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TestScriptParser#screenshotCmd.
    def visitScreenshotCmd(self, ctx:TestScriptParser.ScreenshotCmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TestScriptParser#pauseCmd.
    def visitPauseCmd(self, ctx:TestScriptParser.PauseCmdContext):
        return self.visitChildren(ctx)



del TestScriptParser