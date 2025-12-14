# TestScript DSL - Automação de Testes Web

Este projeto implementa uma Linguagem de Domínio Específico (DSL) projetada para simplificar a criação de scripts de automação e testes para navegadores web. O compilador traduz comandos de alto nível da DSL para código Python utilizando a biblioteca **Playwright/Selenium**.

## 👥 Equipe

* **[Eduardo José Ferreira de Souza]**
* **[Mateus Gonçalves Cunha]**
* **[Sócrates Farias de Oliveira]**

-----

## 🚀 Motivação e Descrição Informal

### O Problema
Escrever scripts de teste de automação web diretamente em código pode ser uma tarefa repetitiva e verbosa. O testador precisa lidar constantemente com configurações de drivers, importações complexas, esperas explícitas e seletores longos.

### A Solução
A **TestScript DSL** foi criada para abstrair essa complexidade. Ela permite descrever cenários de teste de forma declarativa e legível, focando na **intenção** do usuário (ex: "abra este site", "clique ali", "espere ver tal texto") em vez da implementação técnica.

### Exemplo de Código DSL
```text
test busca_google:
    open "[https://google.com](https://google.com)"
    type "textarea[name=q]" "Compiladores"
    click "input[name=btnK]"
    expect_title "Compiladores"
````

-----

## 🛠️ Estrutura do Compilador

O projeto utiliza a ferramenta **ANTLR4** para análise léxica e sintática.

1.  **Gramática (`TestScript.g4`):** Define as regras da linguagem.
2.  **Parser/Lexer:** Gerados automaticamente pelo ANTLR em Python.
3.  **Gerador (Visitor):** Percorre a árvore sintática e traduz os comandos DSL para script Python final.

-----

## 📦 Como Executar

### Pré-requisitos Gerais

  * **Python 3.11+** instalado.

### 1\. Instalação das Dependências Básicas

No terminal, execute:

```bash
pip install -r requirements.txt
```

### 2\. Compilando a DSL

O arquivo principal de entrada é o `src/mainTests.py`. Ele lê o arquivo de teste (padrão: `tests/tests.dsl`) e gera o script de saída.

```bash
python src/mainTests.py
```

-----

## 🚀 Execução no GitHub Codespaces (Playwright)

O ambiente do Codespaces utiliza um contêiner Linux leve. Para garantir que o navegador abra corretamente e você consiga visualizar os testes, siga rigorosamente os passos abaixo:

### 1\. Instalação de Dependências do Sistema

O Codespaces não possui bibliotecas gráficas (como `libatk`, `libgtk`, etc.) instaladas por padrão. Sem elas, o navegador fecha imediatamente.

Execute no terminal **uma única vez**:

```bash
# Instala os binários do navegador
playwright install

# (CRÍTICO) Instala as dependências de sistema do Linux para rodar navegadores
# Isso corrige o erro: "error while loading shared libraries: libatk-1.0.so.0"
sudo playwright install-deps
```

### 2\. Executando os Testes

Após gerar o script (passo de compilação acima), execute:

```bash
python src/saida_playwright.py all
```

*Isso gerará um arquivo `trace.zip` contendo a gravação da execução.*

### 3\. 🔎 Visualizando a Execução (Trace Viewer)

Como o Codespaces roda em modo *headless* (sem monitor), você não verá o navegador abrindo. Para visualizar o passo a passo (telas, cliques e logs), utilize o **Trace Viewer** com uma porta específica:

```bash
playwright show-trace trace.zip --port 9323
```

> **Nota Importante:** A flag `--port 9323` é essencial no Codespaces. Ela evita erros de protocolo ("Internal server error, session closed") e garante que o VS Code faça o redirecionamento de porta corretamente. Após rodar o comando, clique no link `http://localhost:9323` que aparecerá no terminal.

-----

## ⚠️ Limitações e Notas Técnicas

1.  **Execução Headless:** Por padrão, em ambientes CI/CD ou Codespaces, os testes rodam sem interface gráfica para economizar recursos.
2.  **Arquivos de Trace:** Em caso de falha ou para auditoria, verifique sempre o arquivo `trace.zip` gerado. Ele contém snapshots do DOM, screenshots e timeline da execução.
3.  **Ambiente Local:** Se estiver rodando em sua máquina local (Windows/Linux/Mac) com interface gráfica, o comando `install-deps` geralmente não é necessário, e o Trace Viewer pode ser aberto sem especificar a porta.

-----

## 📚 Comandos da Linguagem

| Comando | Sintaxe | Descrição |
| :--- | :--- | :--- |
| **test** | `test nome:` | Define um bloco de teste. |
| **open** | `open "URL"` | Abre uma URL no navegador. |
| **click** | `click "seletor"` | Clica em um elemento CSS. |
| **type** | `type "seletor" "texto"` | Digita texto em um input. |
| **wait** | `wait "seletor" MS` | Espera até X ms pela presença do elemento. |
| **expect** | `expect "texto"` | Asserta que o texto existe no código fonte. |
| **screenshot** | `screenshot "nome.png"` | Tira um print da tela. |

```
