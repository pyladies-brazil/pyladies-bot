# ladies-bot
[![Python 3.8](https://img.shields.io/badge/python-3.8-green.svg)](https://www.python.org/downloads/release/python-380/)
[![code-style-black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

> Esse projeto ainda está em construção!

Repositório com o código fonte do PyLadies Brasil Bot ([t.me/PyLadiesBrasilBot](t.me/PyLadiesBrasilBot)), desenvolvido com [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot).

Para ver os próximos passos desse projeto, veja as [issues](https://github.com/naanadr/ladies-bot/issues). Estamos aceitando contribuição :heart:

## Dependências

Para gerenciar os pacotes eu utilizo o [Poetry](https://python-poetry.org/), então caso você não tenha o Poetry instalado no seu computador, será preciso instala-lo, veja como instalar o Poetry [aqui](https://python-poetry.org/docs/#installation).

Após ter instalado o Poetry, execute no terminal:

```shell
$ poetry shell
$ poetry install
```

> Caso você não queira instalar as dependências de desenvolvimento, execute `poetry install --no-dev`.

## Como executar esse projeto

Antes de mais nada, você precisará ter a chave do bot em um arquivo `.env` persistido no diretório `pyladiesbrasilbot/conf`.

> O `.env` terá apenas uma variável a `TELEGRAM_TOKEN` com o valor do chave do bot.

Após a chave do bot devidamente informada, execute:

```shell
$ python pyladiesbrasilbot/core.py
```

> Provavelmente, você não estará executando o @pyladiesbrasilbot porque o código dele não está disponível para consulta. Então você deverá está executando um bot de teste que você deve ter criado (ainda não sei como é para fazer teste em bots).

## Material de apoio

Caso você queira contribuir para esse repositório e não saiba muito bem como fazer um Bot, te recomendamos alguns materiais que podem te ajudar:

* [O que é e o que pode fazer um bot do telegram](https://core.telegram.org/bots/)
* [Como fazer um chatbot em 1 dia](https://medium.com/como-programar-em-1-dia/como-fazer-um-chatbot-em-1-dia-bcb07c48ec5e)
* [Desenvolvendo o seu primeiro chatbot no telegram com python](https://medium.com/@mdcg.dev/desenvolvendo-o-seu-primeiro-chatbot-no-telegram-com-python-a9ad787bdf6)
* [Documentação do python-telegram-bot](https://python-telegram-bot.readthedocs.io/en/stable/index.html)
* [Documentação da API do Telegram](https://core.telegram.org/api)
