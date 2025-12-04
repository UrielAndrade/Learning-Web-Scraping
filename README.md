Web-scraping com cookies do Chrome

Este repositório contém dois scripts úteis para reutilizar a sessão do Chrome (cookies) em um WebDriver e assim realizar scraping em páginas que exigem login.

Arquivos principais

- `capturar_cookies.py` — abre uma janela do Chromium/Chrome usando um perfil temporário e permite que você faça login manualmente; ao confirmar salva os cookies para `cookies_suap.json` (filtrados para o domínio do SUAP).
- `V2.0SuapScaping.py` — carrega `cookies_suap.json`, injeta os cookies no WebDriver e navega até a página do aluno para extrair informações.

Requisitos

- Python 3.8+
- Google Chrome/Chromium instalado
- chromedriver compatível com a versão do seu Chrome no PATH, ou usar um gerenciador de driver (ex.: `webdriver-manager`).

Instalação recomendada (fish shell)

```fish
python -m venv venv
source venv/bin/activate.fish
pip install -r requirements.txt
```

Como usar

1) Capturar cookies

```fish
python capturar_cookies.py
```

- Será aberta uma janela do Chrome usando o perfil em `--user-data-dir=/home/uriel/.config/selenium-cookie-capture`.
- Acesse `https://suap.ifro.edu.br` e faça login manualmente.
- Depois volte ao terminal e aperte ENTER. O script salvará `cookies_suap.json` com os cookies do domínio.

Dicas: se o Chrome já estiver aberto com o mesmo perfil, feche-o antes de rodar o script ou mude o `--user-data-dir` para outra pasta temporária.

2) Rodar o scraping

```fish
python V2.0SuapScaping.py
```

- O script lê `cookies_suap.json`, injeta os cookies e tenta acessar a página do estudante.
- Se os cookies estiverem válidos, o script extrai Nome, Matrícula, E-mail e CPF.

Problemas comuns e soluções rápidas

- chromedriver não encontrado ou incompatível: instale um chromedriver compatível com o Chrome instalado. Alternativa: usar `webdriver-manager` e adaptar os scripts para usá-lo.
- Cookies expirados: repita `capturar_cookies.py` para gerar novos cookies.
- Erros ao adicionar cookies: verifique se o arquivo `cookies_suap.json` existe e contém cookies com `name` e `value`.

Privacidade

Os scripts lidam com cookies e sessões. Evite compartilhar `cookies_suap.json` e apague-o quando não for mais necessário.

Próximos passos sugeridos

- Adicionar `webdriver-manager` para evitar problemas com chromedriver.
- Opcional: tornar `capturar_cookies.py` interativo para escolher o `user-data-dir` e o domínio alvo.
