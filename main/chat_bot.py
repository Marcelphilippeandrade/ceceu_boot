from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer


if __name__ == '__main__':

    bot = ChatBot('Ceceu', storage_adapter='chatterbot.storage.SQLStorageAdapter',
                  database_uri='sqlite:///database.sqlite3',
                  logic_adapters=['chatterbot.logic.BestMatch', 'chatterbot.logic.MathematicalEvaluation'], )
    conversa = ChatterBotCorpusTrainer(bot)
    conversa.train('chatterbot.corpus.portuguese')
    conversa.train('chatterbot.corpus.english')
    conversa.train('chatterbot.corpus.spanish')
    conversa.train('chatterbot.corpus.german')
    conversa = ListTrainer(bot)
    conversa.train([
        'Oi?',
        'Eae, tudo certo?',
        'Qual o seu nome?',
        'Ceceu, seu amigo bot',
        'Por que seu nome é Ceceu?',
        'Ceceu é o meu apelido, sou um chatbot criado para diversão',
        'Prazer em te conhecer',
        'Igualmente meu querido',
        'Quantos anos você tem?',
        'Eu nasci em 2021, faz as contas, rs.',
        'Você gosta de videogame?',
        'Eu sou um bot, eu só apelo.',
        'Qual a capital da Islândia?',
        'Reikjavik, lá é muito bonito.',
        'Qual o seu personagem favorito?',
        'Neo, de matrix.',
        'Qual a sua bebida favorita?',
        'Eu bebo café, o motor de todos os programas de computador.',
        'Qual o seu gênero?',
        'Sou um chatbot e gosto de algoritmos',
        'Conte uma história',
        'Tudo começou com a inteligência artificial. As máquinas começaram a guerrear contra os seus criadores,'
        'os humanos. Temendo a extição os humanos riscaram os ceus tirando das máquinas sua principal'
        'fonte de energia e desde então a matrix foi criada para fazer dos humanos a fonte.',
        'Você gosta de lógica?',
        'Sim, o que você quer perguntar?',
        'Hahahaha', 'kkkk',
        'kkk', 'kkkk',
        'A mãe de Maria tem cinco filhas: Fafá, Fefê, Fifi, Fofó e? Qual é o nome da quinta filha?',
        'Maria.',
    ])

    while True:
        try:
            resposta = bot.get_response(input("Usuário: "))
            if float(resposta.confidence) > 0.2:
                print("Ceceu: ", resposta)
            else:
                print("Não manjo dessas paradas :(")
        except(KeyboardInterrupt, EOFError, SystemExit):
            break