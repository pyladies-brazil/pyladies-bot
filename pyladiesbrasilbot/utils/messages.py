START_MESSAGE = (
    "Olá, eu sou a PyLadies Brasil Bot! \n"
    "Sou um Bot focado em moderação de grupo, principalmente os"
    " grupos dos PyLadies no Telegram :).\n"
    "Ainda estou em construção, mas espero poder te ajudar.\n\n"
    "Para ver a lista de comandos execute /help"
)

WELCOME_NEW_MEMBER_MESSAGE = (
    "Seja bem vinda, {first_name} {las_name} (@{username}) ao {chat_title}!"
)

HELP_MESSAGE = (
    "/conf_boas_vindas -> "
    "Configurar mensagem de boas vindas para o grupo (apenas mensagem)\n"
    "/conf_boas_vindas_foto -> "
    "Configurar mensagem de boas vindas para o grupo (foto com mensagem)\n"
    "/help -> Lista de comandos"
)

HELLO_MESSAGE = (
    "Obrigada por me colocar no grupo {chat_title}! \n"
    "Espero poder ajudar vocês na moderação do grupo ❤️ \n\n"
    "Para que eu possa começar o meu trabalho, por favor, "
    "configure algumas funcionalidades minhas: \n" + HELP_MESSAGE
)

UNKNOWN_MESSAGE = "Comando inválido! Insira /help para ver a lista de comandos"
