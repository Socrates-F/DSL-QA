# TestScript DSL - Automação de Testes Web com Selenium

Este projeto implementa uma Linguagem de Domínio Específico (DSL) projetada para simplificar a criação de scripts de automação e testes para navegadores web. O compilador traduz comandos de alto nível da DSL para código Python utilizando a biblioteca **Selenium**.

## 👥 Equipe

  * **[Eduardo José Ferreira de Souza]**
  * **[NOME DO INTEGRANTE 2]**
  * **[NOME DO INTEGRANTE 3]**

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
    open "https://google.com"
    type "textarea[name=q]" "Compiladores"
    click "input[name=btnK]"
    expect_title "Compiladores"
```

-----

## 🛠️ Estrutura do Compilador

O projeto foi implementado seguindo a estrutura clássica de compiladores, utilizando a ferramenta **ANTLR4**:

1.  **Análise Léxica e Sintática:** Definidas formalmente no arquivo `TestScript.g4`. O ANTLR gera os lexers e parsers em Python.
2.  **Árvore Sintática (Parse Tree):** O parser gera uma árvore que representa a estrutura gramatical do script de entrada.
3.  **Geração de Código (Visitor):** Utilizamos o padrão **Visitor** (classe `SeleniumGenerator.py`) para percorrer a árvore sintática.
      * Cada nó da árvore (comando da DSL) é visitado e traduzido para seu equivalente em Python + Selenium.
      * O compilador gerencia automaticamente os `imports`, a instanciação do `webdriver` e o tratamento de argumentos de linha de comando no arquivo de saída.

-----

## 📦 Como Executar

### Pré-requisitos

  * **Python 3.x** instalado.
  * **Google Chrome** instalado.

### Instalação das Dependências

Execute o comando abaixo para instalar o runtime do ANTLR e o Selenium:

```bash
pip install antlr4-python3-runtime selenium
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

## 📝 Exemplos de Programas

Abaixo estão exemplos da sintaxe suportada pela linguagem (baseados no arquivo `tests/tests.dsl`).

### 1\. Teste de Login Simples

Verifica se o login ocorre com sucesso e se a mensagem de boas-vindas aparece.

```text
test login_valido:
    open "https://the-internet.herokuapp.com/login"
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
    open "https://demoqa.com/automation-practice-form"
    type "#firstName" "Carlos"
    type "#lastName" "Silva"
    click "#gender-radio-1"
    scroll "down"
    submit "#submit"
    wait ".modal-content" 5000
    expect "Thanks"
```

### 3\. Upload de Arquivos

A DSL simplifica drasticamente o comando de upload de arquivos.

```text
test upload_arquivo:
    open "https://the-internet.herokuapp.com/upload"
    upload "#file-upload" "../tests/upload_test.txt"
    click "#file-submit"
    wait "h3" 5000
    expect "File Uploaded!"
```

### 4\. Busca no Github (Wait Explícito)

Uso de espera explicita para elementos dinâmicos.

```text
test github_search:
    open "https://github.com/search?q=antlr+python"
    wait_visible "div[data-testid='results-list']" 10000
    expect "antlr"
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
