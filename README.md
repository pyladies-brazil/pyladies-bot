# pyladies-bot: PyLadiesBrasilBot
[![Python 3.8](https://img.shields.io/badge/python-3.8-green.svg)](https://www.python.org/downloads/release/python-380/) [![code-style-black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) [![mit-license](https://img.shields.io/github/license/naanadr/pyladies-bot)](https://img.shields.io/github/license/naanadr/pyladies-bot) [![build-action](https://img.shields.io/github/workflow/status/naanadr/pyladies-bot/Python%20Formatter%20Pipeline)](https://img.shields.io/github/workflow/status/naanadr/pyladies-bot/Python%20Formatter%20Pipeline)

> Esse projeto ainda está em construção!

Repositório com o código fonte do PyLadies Brasil Bot ([t.me/PyLadiesBrasilBot](t.me/PyLadiesBrasilBot)), desenvolvido com [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot).

Para ver os próximos passos desse projeto, veja as [issues](https://github.com/naanadr/ladies-bot/issues). Estamos aceitando contribuição :heart:, para saber mais como contribuir veja o nosso [guia de contribuição](CONTRIBUING.md).

## Dependências

Para gerenciar os pacotes eu utilizo o [Poetry](https://python-poetry.org/), mas como o Deploy é realizado no [Heroku](https://www.heroku.com) é preciso ter um arquivo `requirements.txt`.

Então caso você não tenha familiaridade com o Poetry e utiliza outro gerenciador de pacotes, você poderá utilizar o `requirements.txt`. Mas caso você prefira o Poetry ou deseja aprender mais sobre, nós temos um `pyproject.toml` também.

Se você ainda não tenha o Poetry instalado no seu computador, será preciso instala-lo, veja como instalar o Poetry [aqui](https://python-poetry.org/docs/#installation).

Após ter instalado o Poetry, vá para a raiz do projeto (`pyladies-bot/`) e execute no terminal:

```shell
$ poetry shell
$ poetry install
```

> Caso você não queira instalar as dependências de desenvolvimento, execute `poetry install --no-dev`.

Se esses comandos forem novos para você, recomendo você estudar a [documentação](https://python-poetry.org/docs/basic-usage/) do Poetry.

## Como executar esse projeto

Após ter instalado as dependências desse projeto e ativado o ambiente virtual. Você precisará ter a chave do bot em um arquivo `.env` persistido no diretório `pyladiesbrasilbot/conf/`.

> O `.env` terá apenas uma variável a `TELEGRAM_TOKEN` com o valor do chave do bot.

Após a chave do bot devidamente informada, execute:

```shell
$ python pyladiesbrasilbot/core.py
```

> Provavelmente, você não estará executando o @pyladiesbrasilbot porque o código dele não está disponível para consulta. Então você deverá está executando um bot de teste que você deve ter criado.

## Material de apoio

Caso você queira contribuir para esse repositório e não saiba muito bem como fazer um Bot no Telegram, te recomendamos alguns materiais que podem te ajudar:

* [O que é e o que pode fazer um bot do telegram](https://core.telegram.org/bots/)
* [Como fazer um chatbot em 1 dia](https://medium.com/como-programar-em-1-dia/como-fazer-um-chatbot-em-1-dia-bcb07c48ec5e)
* [Desenvolvendo o seu primeiro chatbot no telegram com python](https://medium.com/@mdcg.dev/desenvolvendo-o-seu-primeiro-chatbot-no-telegram-com-python-a9ad787bdf6)
* [Documentação do python-telegram-bot](https://python-telegram-bot.readthedocs.io/en/stable/index.html)
* [Documentação da API do Telegram](https://core.telegram.org/api)

Caso você tenha mais materiais de apoio, compartilhe com a gente.
