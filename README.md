
# TestScript DSL - Automação de Testes Web com Selenium

Este projeto implementa uma Linguagem de Domínio Específico (DSL) projetada para simplificar a criação de scripts de automação e testes para navegadores web. O compilador traduz comandos de alto nível da DSL para código Python utilizando a biblioteca **Selenium**.

## 👥 Equipe

* **[Eduardo José Ferreira de Souza]**
* **[Mateus Gonçalves Cunha]**
* **[Sócrates Farias de Oliveira]**

-----

## 🚀 Motivação e Descrição Informal

### O Problema
Escrever scripts de teste em **Selenium** diretamente em Python (ou Java) pode ser uma tarefa repetitiva e verbosa. O testador precisa lidar constantemente com configurações de drivers, importações complexas, esperas explícitas (`WebDriverWait`) e seletores CSS longos, o que dificulta a leitura e a manutenção dos testes por pessoas que não são desenvolvedoras sêniores.

### A Solução
A **TestScript DSL** foi criada para abstrair a complexidade do Selenium. Ela permite descrever cenários de teste de forma declarativa e legível, focando na **intenção** do usuário (ex: "abra este site", "clique ali", "espere ver tal texto") em vez da **implementação**.

### Estrutura da Linguagem
A linguagem é imperativa e estruturada em blocos de teste. Cada teste possui um nome único e uma sequência de comandos.

Exemplo informal:
> "Abra o Google, digite 'Compiladores' na barra de busca, clique em pesquisar e garanta que o título da página mudou."

Na DSL:
```text
test busca_google:
    open "[https://google.com](https://google.com)"
    type "textarea[name=q]" "Compiladores"
    click "input[name=btnK]"
    expect_title "Compiladores"
````

-----

## 🛠️ Estrutura do Compilador

O projeto foi implementado seguindo a estrutura clássica de compiladores, utilizando a ferramenta **ANTLR4**:

1.  **Análise Léxica e Sintática:** Definidas formalmente no arquivo `TestScript.g4`. O ANTLR gera os lexers e parsers em Python.
2.  **Árvore Sintática (Parse Tree):** O parser gera uma árvore que representa a estrutura gramatical do script de entrada.
3.  **Geração de Código (Visitor):** Utilizamos o padrão **Visitor** (classe `SeleniumGenerator.py`) para percorrer a árvore sintática.
      * Cada nó da árvore (comando da DSL) é visitado e traduzido para seu equivalente em Python + Selenium.
      * O compilador gerencia automaticamente os `imports`, a instanciação híbrida do `webdriver` (Chrome ou Firefox) e o tratamento de argumentos.

-----

## 📦 Como Executar

### Pré-requisitos

  * **Python 3.11+** instalado.
  * **Navegadores Suportados (Sistema Híbrido):**
      * **Google Chrome / Chromium:** Necessário para rodar em ambientes Docker ou GitHub Codespaces.
      * **Mozilla Firefox:** Suportado para execução local (Linux), caso o Chrome não esteja disponível.

### Instalação das Dependências

Execute o comando abaixo para instalar o runtime do ANTLR e o Selenium:

```bash
pip install -r requirements.txt
```

### Compilando e Gerando o Código

O arquivo principal de entrada é o `src/mainTests.py`. Ele lê o arquivo de teste (padrão: `tests/tests.dsl`) e gera o arquivo `src/saida_selenium.py`.

1.  Navegue até a pasta do projeto.
2.  Execute o compilador:

<!-- end list -->

```bash
python src/mainTests.py
```

*Saída esperada:* `Código Selenium gerado em: .../src/saida_selenium.py`

### Executando o Teste Gerado

O arquivo gerado (`saida_selenium.py`) é um script Python autônomo. Ele permite rodar todos os testes ou um teste específico via linha de comando.

Para rodar **todos** os testes definidos na DSL:

```bash
python src/saida_selenium.py all
```

Para rodar **um teste específico** (pelo nome definido na DSL):

```bash
python src/saida_selenium.py login_valido
```

-----

## ⚠️ Limitações e Ambientes (Codespaces vs Local)

Este projeto foi otimizado para rodar tanto localmente quanto em contêineres, mas existem diferenças importantes de comportamento:

### 1\. Execução "Headless" no GitHub Codespaces

O GitHub Codespaces não possui monitor (interface gráfica). O script detecta isso e força o navegador a rodar em modo **`--headless`** (invisível).

  * **Impacto:** Você não verá o navegador abrindo.
  * **Confirmação:** A validação deve ser feita pelos logs do terminal ("AssertionError" ou sucesso) ou utilizando o comando `screenshot` da DSL para gerar uma evidência visual.

### 2\. Erro de Visualização de Porta

Ao rodar no Codespaces, tentar clicar em links ou abrir portas de debug (ex: 9222) resultará em erro ou página em branco. Isso ocorre porque o teste é executado rapidamente e o processo do navegador é encerrado (`driver.quit()`) antes que seja possível conectar uma ferramenta de visualização.

### 3\. Suporte ao Nobara/Fedora

Para facilitar o desenvolvimento local em sistemas como o Linux (onde o Chrome pode não ser o padrão), o gerador possui um **fallback automático**. Se ele não encontrar o Chrome, tentará utilizar o driver do **Firefox**.

-----

## 📝 Exemplos de Programas

Abaixo estão exemplos da sintaxe suportada pela linguagem (baseados no arquivo `tests/tests.dsl`).

### 1\. Teste de Login Simples

Verifica se o login ocorre com sucesso e se a mensagem de boas-vindas aparece.

```text
test login_valido:
    open "[https://the-internet.herokuapp.com/login](https://the-internet.herokuapp.com/login)"
    type "#username" "tomsmith"
    type "#password" "SuperSecretPassword!"
    click "button[type=submit]"
    wait ".flash" 5000
    expect "You logged"
```

### 2\. Preenchimento de Formulário e Scroll

Demonstra o uso de scroll e interação com diferentes inputs.

```text
test formulario:
    open "[https://demoqa.com/automation-practice-form](https://demoqa.com/automation-practice-form)"
    type "#firstName" "Carlos"
    type "#lastName" "Silva"
    click "label[for='gender-radio-1']"
    scroll "down"
    submit "#submit"
    wait ".modal-content" 5000
    expect "Thanks"
```

### 3\. Upload de Arquivos

A DSL simplifica drasticamente o comando de upload de arquivos.

```text
test upload_arquivo:
    open "[https://the-internet.herokuapp.com/upload](https://the-internet.herokuapp.com/upload)"
    upload "#file-upload" "../tests/upload_teste.txt"
    click "#file-submit"
    wait "h3" 5000
    expect "File Uploaded!"
```

-----

## 📚 Comandos da Linguagem

| Comando | Sintaxe | Descrição |
| :--- | :--- | :--- |
| **test** | `test nome:` | Define um bloco de teste. |
| **open** | `open "URL"` | Abre uma URL no navegador. |
| **click** | `click "seletor"` | Clica em um elemento CSS. |
| **type** | `type "seletor" "texto"` | Digita texto em um input. |
| **upload** | `upload "seletor" "caminho"` | Faz upload de um arquivo local. |
| **submit** | `submit "seletor"` | Submete um formulário. |
| **scroll** | `scroll "down"` | Rola a página para baixo (ou para cima). |
| **wait** | `wait "seletor" MS` | Espera até X ms pela presença do elemento. |
| **wait\_visible**| `wait_visible "seletor" MS`| Espera até X ms pela visibilidade do elemento. |
| **expect** | `expect "texto"` | Asserta que o texto existe no código fonte da página. |
| **expect\_title**| `expect_title "texto"` | Asserta que o texto está no título da aba. |
| **screenshot** | `screenshot "nome.png"` | Tira um print da tela. |
| **pause** | `pause SEGUNDOS` | Pausa a execução por X segundos. |

```
```
