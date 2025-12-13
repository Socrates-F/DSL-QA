from TestScriptVisitor import TestScriptVisitor
from TestScriptParser import TestScriptParser
from selenium.webdriver.common.by import By
import time

class SeleniumGenerator(TestScriptVisitor):
    def __init__(self):
        self.functions = []   # cada teste vira uma função python
        self.test_names = []  # lista dos nomes

    def generate(self):
        header = [
            "import sys",
            "from selenium import webdriver",
            "from selenium.webdriver.common.by import By",
            "from selenium.webdriver.support.ui import WebDriverWait",
            "from selenium.webdriver.support import expected_conditions as EC",
            "",
            "driver = webdriver.Chrome()",
            ""
        ]

        footer = [
            "",
            "if __name__ == '__main__':",
            "    if len(sys.argv) == 1:",
            "        print('Uso: python saida_selenium.py <nome_do_teste> | all')",
            "        driver.quit()",
            "        sys.exit()",
            "",
            "    arg = sys.argv[1]",
            "",
            "    if arg == 'all':",
            ] + [f"        test_{name}()" for name in self.test_names] + [
            "    else:",
            "        try:",
            "            globals()[f'test_{arg}']()",
            "        except KeyError:",
            "            print(f'Teste {arg} não existe!')",
            "",
            "    driver.quit()"
        ]

        return "\n".join(header + self.functions + footer)

  
    # Blocos de testes:
    def visitTestBlock(self, ctx):
        name = ctx.IDENT().getText()
        self.test_names.append(name)

        self.functions.append(f"def test_{name}():")
        self.visit(ctx.commandBlock())
        self.functions.append("") 
        return None

   
    # Coomandos da DSL
    def visitOpenCmd(self, ctx):
        self.functions.append(f"    driver.get({ctx.STRING().getText()})")

    def visitClickCmd(self, ctx):
        sel = ctx.STRING().getText()
        self.functions.append(f"    driver.find_element(By.CSS_SELECTOR, {sel}).click()")
        

    def visitClickTextCmd(self, ctx):
        txt = ctx.STRING().getText()
        self.functions.append(f"    driver.find_element(By.LINK_TEXT, {txt}).click()")
        

    def visitTypeCmd(self, ctx):
        sel = ctx.STRING(0).getText()
        txt = ctx.STRING(1).getText()
        self.functions.append(f"    driver.find_element(By.CSS_SELECTOR, {sel}).send_keys({txt})")
        

    def visitUploadCmd(self, ctx):
        sel = ctx.STRING(0).getText()
        file = ctx.STRING(1).getText()
        self.functions.append(f"    driver.find_element(By.CSS_SELECTOR, {sel}).send_keys({file})")

    def visitSubmitCmd(self, ctx):
        sel = ctx.STRING().getText()
        self.functions.append(f"    driver.find_element(By.CSS_SELECTOR, {sel}).submit()")
        

    def visitExpectCmd(self, ctx):
        txt = ctx.STRING().getText()
        self.functions.append(f"    assert {txt} in driver.page_source")
        

    def visitExpectTitleCmd(self, ctx):
        txt = ctx.STRING().getText()
        self.functions.append(f"    assert {txt} in driver.title")
        

    def visitWaitCmd(self, ctx):
        sel = ctx.STRING().getText()
        t = int(ctx.INT().getText())
        self.functions.append(
            f"    WebDriverWait(driver, {t}).until(EC.presence_of_element_located((By.CSS_SELECTOR, {sel})))"
        )

    def visitWaitVisibleCmd(self, ctx):
        
        sel = ctx.STRING().getText()
        t = int(ctx.INT().getText()) / 1000
        self.functions.append(
            f"    WebDriverWait(driver, {t}).until(EC.visibility_of_element_located((By.CSS_SELECTOR, {sel})))"
        )

    def visitScrollCmd(self, ctx):
        direction = ctx.STRING().getText().strip('"')
        if direction == "down":
            self.functions.append('    driver.execute_script("window.scrollBy(0, 600);")')
        else:
            self.functions.append('    driver.execute_script("window.scrollBy(0, -600);")')

    def visitScreenshotCmd(self, ctx):
        file = ctx.STRING().getText()
        self.functions.append(f"    driver.save_screenshot({file})")

    def visitPauseCmd(self, ctx):
        seconds = int(ctx.INT().getText())
        self.functions.append("    import time")
        self.functions.append(f"    time.sleep({seconds})")