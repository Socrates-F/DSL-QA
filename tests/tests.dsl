test login_valido:
    open "https://the-internet.herokuapp.com/login"
    type "#username" "tomsmith"
    type "#password" "SuperSecretPassword!"
    click "button[type=submit]"
    wait ".flash" 5000
    expect "You logged"
    pause 5


test formulario:
    open "https://demoqa.com/automation-practice-form"
    type "#firstName" "Carlos"
    type "#lastName" "Lira"
    click "label[for='gender-radio-1']"
    scroll "down"
    submit "#submit"
    wait ".modal-content" 5000
    expect "Thanks"
    pause 10


test upload_arquivo:
    open "https://the-internet.herokuapp.com/upload"
    upload "#file-upload" "../tests/upload_teste.txt"
    click "label[for='gender-radio-1']"
    wait "h3" 5000
    expect "File Uploaded!"
    pause 10
    

test carregamento_lento:
    open "https://the-internet.herokuapp.com/dynamic_loading/1"
    click "#start button"
    wait_visible "#finish" 15000
    expect "Hello World"
    

test maps_localizacao:
    open "https://www.google.com/maps"
    wait_visible "input#searchboxinput" 15000
    type "input#searchboxinput" "Escola Politécnica de Pernambuco"
    wait_visible "button[aria-label='Pesquisar']" 10000
    click "button[aria-label='Pesquisar']"
    pause 10
    wait_visible "input#searchboxinput" 15000
    expect "Recife"
    pause 8

test github_search:
    open "https://github.com/search?q=antlr+python"
    wait_visible "div[data-testid='results-list']" 10000
    expect "antlr"
    pause 6