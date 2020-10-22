START_MESSAGE = (
    "Olá, eu sou a PyLadies Brasil Bot! \n"
    "Sou um Bot focado em moderação de grupo, principalmente os"
    " grupos dos PyLadies no Telegram :).\n"
    "Ainda estou em construção, mas espero poder te ajudar.\n\n"
    "Você pode me adicionar ao seu grupo e me configurar lá mesmo, "
    "não precisa me colocar como administradora.\n\n"
    "Para ver a lista de comandos execute /help"
)

WELCOME_NEW_MEMBER_MESSAGE = (
    "Seja bem vinda, {first_name} {last_name} (@{username}) ao {chat_title}!"
)

HELP_MESSAGE = (
    "/boas_vindas -> "
    "Configurar mensagem de boas vindas para o grupo. "
    "Essa mensagem será mostrada a novos membros do grupo.\n"
    "/boas_vindas_foto -> "
    "Configurar nova imagem de boas vindas do grupo.\n"
    "/imagem_boas_vindas -> Para ver a imagem que será mostrada na mensagem "
    "de boas vindas.\n"
    "/desativar_imagem_boas_vindas -> "
    "Desativar envio de imagem na mensagem de boas vindas. "
    "Caso esteja desativada, o resultado será o de ativação.\n"
    "/desativar_boas_vindas -> "
    "Desativar envio de mensagem de boas vindas.\n"
    "/status_boas_vindas -> "
    "Para ver o status da mensagem de boas vindas.\n"
    "/help -> Lista de comandos"
)

HELLO_MESSAGE = (
    "Obrigada por me colocar no grupo {chat_title}! \n"
    "Espero poder ajudar vocês na moderação do grupo ❤️ \n\n"
    "Para que eu possa começar o meu trabalho, por favor, "
    "configure algumas funcionalidades minhas: \n" + HELP_MESSAGE
)

UNKNOWN_MESSAGE = "Comando inválido! Insira /help para ver a lista de comandos"

CONF_BOAS_VINDAS_PHOTO_INFO = (
    "Comando utilizado de forma incorreta!\n"
    "Por favor, envie uma foto com a legenda /conf_boas_vindas_foto."
)

CONF_BOAS_VINDAS_PHOTO_INFO_CHECK = "Foto enviada com sucesso!"
