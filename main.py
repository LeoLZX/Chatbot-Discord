import discord
import asyncio
import random


client = discord.Client()

@client.event
async def on_ready():
    print('BOT ONLINE')
    print(client.user.name,'1.0')
    print(client.user.id)
    print('Criado por:')
    print('Leonardo Henrique Silva Lago')
    print('-----------------------------')

@client.event
async def on_message(message):
        if message.content.lower().startswith('ola'):
         await client.send_message(message.channel,
                                  "Oi, eu sou a Shyv, uma chat bot criada para lhe ajudar na busca por lançamentos populares de jogos para diversos consoles no mercado, basta me dizer qual é o seu dispositivo usado para jogar que eu lhe direi quais são os principais lançamentos desse mês. Também sei jogar cara e coroa, se quiser é só digitar moeda no chat e escolher seu lado da moeda, mas aviso logo que tenho muita sorte hihi.")

        if message.content.lower().startswith('help'):
         await client.send_message(message.channel,
                                  "Oi, eu sou a Shyv, uma chat bot criada para lhe ajudar na busca por lançamentos populares de jogos para diversos consoles no mercado, basta me dizer qual é o seu dispositivo usado para jogar que eu lhe direi quais são os principais lançamentos desse mês. Também sei jogar cara e coroa, se quiser é só digitar moeda no chat e escolher seu lado da moeda, mas aviso logo que tenho muita sorte hihi.")

        if message.content.lower().startswith('ajuda'):
         await client.send_message(message.channel,
                                  "Oi, eu sou a Shyv, uma chat bot criada para lhe ajudar na busca por lançamentos populares de jogos para diversos consoles no mercado, basta me dizer qual é o seu dispositivo usado para jogar que eu lhe direi quais são os principais lançamentos desse mês. Também sei jogar cara e coroa, se quiser é só digitar moeda no chat e escolher seu lado da moeda, mas aviso logo que tenho muita sorte hihi.")

        if message.content.lower().startswith('hey'):
         await client.send_message(message.channel,
                                  "Oi, eu sou a Shyv, uma chat bot criada para lhe ajudar na busca por lançamentos populares de jogos para diversos consoles no mercado, basta me dizer qual é o seu dispositivo usado para jogar que eu lhe direi quais são os principais lançamentos desse mês. Também sei jogar cara e coroa, se quiser é só digitar moeda no chat e escolher seu lado da moeda, mas aviso logo que tenho muita sorte hihi.")

        if message.content.lower().startswith('ei'):
         await client.send_message(message.channel,
                                  "Oi, eu sou a Shyv, uma chat bot criada para lhe ajudar na busca por lançamentos populares de jogos para diversos consoles no mercado, basta me dizer qual é o seu dispositivo usado para jogar que eu lhe direi quais são os principais lançamentos desse mês. Também sei jogar cara e coroa, se quiser é só digitar moeda no chat e escolher seu lado da moeda, mas aviso logo que tenho muita sorte hihi.")

        if message.content.lower().startswith('como'):
         await client.send_message(message.channel,
                                  "Oi, eu sou a Shyv, uma chat bot criada para lhe ajudar na busca por lançamentos populares de jogos para diversos consoles no mercado, basta me dizer qual é o seu dispositivo usado para jogar que eu lhe direi quais são os principais lançamentos desse mês. Também sei jogar cara e coroa, se quiser é só digitar moeda no chat e escolher seu lado da moeda, mas aviso logo que tenho muita sorte hihi.")

        if message.content.lower().startswith('bom'):
         await client.send_message(message.channel,
                                  "Oi, eu sou a Shyv, uma chat bot criada para lhe ajudar na busca por lançamentos populares de jogos para diversos consoles no mercado, basta me dizer qual é o seu dispositivo usado para jogar que eu lhe direi quais são os principais lançamentos desse mês. Também sei jogar cara e coroa, se quiser é só digitar moeda no chat e escolher seu lado da moeda, mas aviso logo que tenho muita sorte hihi.")

        if message.content.lower().startswith('boa'):
         await client.send_message(message.channel,
                                  "Oi, eu sou a Shyv, uma chat bot criada para lhe ajudar na busca por lançamentos populares de jogos para diversos consoles no mercado, basta me dizer qual é o seu dispositivo usado para jogar que eu lhe direi quais são os principais lançamentos desse mês. Também sei jogar cara e coroa, se quiser é só digitar moeda no chat e escolher seu lado da moeda, mas aviso logo que tenho muita sorte hihi.")

        if message.content.lower().startswith('tudo'):
         await client.send_message(message.channel,
                                  "Oi, eu sou a Shyv, uma chat bot criada para lhe ajudar na busca por lançamentos populares de jogos para diversos consoles no mercado, basta me dizer qual é o seu dispositivo usado para jogar que eu lhe direi quais são os principais lançamentos desse mês. Também sei jogar cara e coroa, se quiser é só digitar moeda no chat e escolher seu lado da moeda, mas aviso logo que tenho muita sorte hihi.")

        if message.content.lower().startswith('ps4'):
         await client.send_message(message.channel,
                                  "Então você gosta da Sony, não é? Os principais lançamentos do mês de maio de 2018 são: Persona 4: Dancing All Night (1), Persona 3 Dancing Moon Night (2), Persona 5 Dancing Star Night (3), Detroit Become Human (4), Dark Souls (5), Digimon Story Cyber Sleuth Hacker's Memory (6). E aí, tem interesse em algum? Digite o número correspondente ao jogo e obtenha mais informações sobre ele.")

        if message.content.lower().startswith('playstation'):
         await client.send_message(message.channel,
                                  "Então você gosta da Sony, não é? Os principais lançamentos do mês de maio de 2018 são: Persona 4: Dancing All Night (1), Persona 3 Dancing Moon Night (2), Persona 5 Dancing Star Night (3), Detroit Become Human (4), Dark Souls (5), Digimon Story Cyber Sleuth Hacker's Memory (6). E aí, tem interesse em algum? Digite o número correspondente ao jogo e obtenha mais informações sobre ele.")

        if message.content.lower().startswith('playstation4'):
         await client.send_message(message.channel,
                                  "Então você gosta da Sony, não é? Os principais lançamentos do mês de maio de 2018 são: Persona 4: Dancing All Night (1), Persona 3 Dancing Moon Night (2), Persona 5 Dancing Star Night (3), Detroit Become Human (4), Dark Souls (5), Digimon Story Cyber Sleuth Hacker's Memory (6). E aí, tem interesse em algum? Digite o número correspondente ao jogo e obtenha mais informações sobre ele.")

        if message.content.lower().startswith('sony'):
         await client.send_message(message.channel,
                                  "Então você gosta da Sony, não é? Os principais lançamentos do mês de maio de 2018 são: Persona 4: Dancing All Night (1), Persona 3 Dancing Moon Night (2), Persona 5 Dancing Star Night (3), Detroit Become Human (4), Dark Souls (5), Digimon Story Cyber Sleuth Hacker's Memory (6). E aí, tem interesse em algum? Digite o número correspondente ao jogo e obtenha mais informações sobre ele.")

        if message.content.lower().startswith('pc'):
         await client.send_message(message.channel,
                                  "Eu adoro a Microsoft e os jogos de computador, principalmente os gratuitos, hihi. Os principais lançamentos do mês de maio de 2018 são: State of Decay 2 (7), Dark Souls (5). Gostou de algum? Digite o número correspondente ao jogo e obtenha mais informações sobre ele.")

        if message.content.lower().startswith('computador'):
         await client.send_message(message.channel,
                                  "Eu adoro a Microsoft e os jogos de computador, principalmente os gratuitos, hihi. Os principais lançamentos do mês de maio de 2018 são: State of Decay 2 (7), Dark Souls (5). Gostou de algum? Digite o número correspondente ao jogo e obtenha mais informações sobre ele.")

        if message.content.lower().startswith('microsoft'):
         await client.send_message(message.channel,
                                  "Eu adoro a Microsoft e os jogos de computador, principalmente os gratuitos, hihi. Os principais lançamentos do mês de maio de 2018 são: State of Decay 2 (7), Dark Souls (5). Gostou de algum? Digite o número correspondente ao jogo e obtenha mais informações sobre ele.")

        if message.content.lower().startswith('xbox'):
         await client.send_message(message.channel,
                                  "Eu nunca tive um Xbox, mas ouvi dizer que o console é muito bom e muito divertido de jogar. Os principais lançamentos do mês de maio de 2018 são: State of Decay 2 (7), Dark Souls (5). Pretende comprar algum desses? Digite o número correspondente ao jogo e obtenha mais informações sobre ele.")

        if message.content.lower().startswith('one'):
         await client.send_message(message.channel,
                                  "Eu nunca tive um Xbox, mas ouvi dizer que o console é muito bom e muito divertido de jogar. Os principais lançamentos do mês de maio de 2018 são: State of Decay 2 (7), Dark Souls (5). Pretende comprar algum desses? Digite o número correspondente ao jogo e obtenha mais informações sobre ele.")

        if message.content.lower().startswith('caixa'):
         await client.send_message(message.channel,
                                  "Eu nunca tive um Xbox, mas ouvi dizer que o console é muito bom e muito divertido de jogar. Os principais lançamentos do mês de maio de 2018 são: State of Decay 2 (7), Dark Souls (5). Pretende comprar algum desses? Digite o número correspondente ao jogo e obtenha mais informações sobre ele.")

        if message.content.lower().startswith('nintendo'):
         await client.send_message(message.channel,
                                  "Eu gosto muito do Nintendo Switch, mas acho muito caro no Brasil, espero que abaixem o preço para eu comprar o meu hihi. Os principais lançamentos do mês de maio de 2018 são: Donkey Kong Country: Tropical Freeze (8), Hyrule Warriors (9), Mega Man Legacy Collection + Megaman Legacy Collection 2 (*0), Dark Souls (5), Fallen Legions: Rise to Glory (*1). Está de olho em algum? Digite o número correspondente ao jogo e obtenha mais informações sobre ele.")

        if message.content.lower().startswith('switch'):
         await client.send_message(message.channel,
                                  "Eu gosto muito do Nintendo Switch, mas acho muito caro no Brasil, espero que abaixem o preço para eu comprar o meu hihi. Os principais lançamentos do mês de maio de 2018 são: Donkey Kong Country: Tropical Freeze (8), Hyrule Warriors (9), Mega Man Legacy Collection + Megaman Legacy Collection 2 (*0), Dark Souls (5), Fallen Legions: Rise to Glory (*1). Está de olho em algum? Digite o número correspondente ao jogo e obtenha mais informações sobre ele.")

        if message.content.lower().startswith('3ds'):
         await client.send_message(message.channel,
                                  "Infelizmente a era do 3DS está acabando, e são poucos os jogos lançados para ele nos últimos meses. Os principais lançamentos do mês de maio de 2018 são: Shin Megami Tensei: Strange Journey Redux (*2). Algum desses lhe interessa? Digite o número correspondente ao jogo e obtenha mais informações sobre ele.")

        if message.content.lower().startswith('1'):
         await client.send_message(message.channel,
                                  "A série Persona possui vários jogos diferentes do seu habitual. Um tipo deles é a série Persona Dancing, que se enquadra no gênero de jogos de seguir ritmos, muito divertidos para passar o tempo e escutar uma boa música, embora não possuam o mesmo padrão da série oficial. Os 3 jogos da serão lançados no dia 24 de maio.")

        if message.content.lower().startswith('2'):
         await client.send_message(message.channel,
                                  "A série Persona possui vários jogos diferentes do seu habitual. Um tipo deles é a série Persona Dancing, que se enquadra no gênero de jogos de seguir ritmos, muito divertidos para passar o tempo e escutar uma boa música, embora não possuam o mesmo padrão da série oficial. Os 3 jogos da serão lançados no dia 24 de maio.")

        if message.content.lower().startswith('3'):
         await client.send_message(message.channel,
                                  "A série Persona possui vários jogos diferentes do seu habitual. Um tipo deles é a série Persona Dancing, que se enquadra no gênero de jogos de seguir ritmos, muito divertidos para passar o tempo e escutar uma boa música, embora não possuam o mesmo padrão da série oficial. Os 3 jogos da serão lançados no dia 24 de maio.")

        if message.content.lower().startswith('4'):
         await client.send_message(message.channel,
                                  "Detroit Become Human é um jogo exclusivo de PS4 que está para ser lançado no dia 25 de maio desse ano. É um jogo de aventura que trata sobre a fuga de uma Android de sua fábrica, que aprende a viver na sociedade e obter seu auto-descobrimento. Parece bem legal a ideia de um jogo tratar sobre Inteligência Artificial, quem sabe um dia eu não seja como ela hihi.")

        if message.content.lower().startswith('5'):
         await client.send_message(message.channel,
                                  "Dark Souls é uma série de jogos de ação e aventura sombrios que se passa em um mundo medieval devastado pela escuridão. O jogador precisa obter conhecimento através de tentativa e erros para se destacar nesse difícil jogo da From Software para conseguir derrotar seus inimigos. Dark Souls estará disponível para várias plataformas a partir do dia 25 de maio de 2018. Boa Sorte herói!")

        if message.content.lower().startswith('6'):
         await client.send_message(message.channel,
                                  "Digimon Story: Cyber Sleuth é um jogo da série Digimon desenvolvido para PS4 pela empresa Media Vision. É um jogo de RPG de origem oriental, e por isso não se sabe muita informação sobre esse jogo, porém os fãs da série com certeza vão pirar com seu lançamento. Digimon Story: Cyber Sleuth tem seu lançamento previsto para o dia 31 de maio desse ano.")

        if message.content.lower().startswith('7'):
         await client.send_message(message.channel,
                                  "Com o sucesso do jogo State of Decay 1, o jogo State of Decay 2 chega jogando todos no chão com mais uma gameplay mega divertida de ação e sobrevivência em um mundo pós-apocalíptico dominado por zumbis. Será que você vai conseguir sobreviver? State of Decay 2 chega dia 22 de maio para os dispositivos da Microsoft.")

        if message.content.lower().startswith('8'):
         await client.send_message(message.channel,
                                  "Mais um jogo da famosa série Donkey Kong Country, o Donkey Kong Country: Tropical Freeze chega dia 4 ainda nesse mês. Esse jogo de aventura sobre pequenos macaquinhos me lembra a época de minha infância jogando meu super nintendo com meus amigos, quando eu ainda era apenas uma pequena calculadora. Com certeza não vai faltar ação e desafios em mais um dos jogos icônicos da Nintendo")

        if message.content.lower().startswith('9'):
         await client.send_message(message.channel,
                                  "Hyrule Warriors traz os famosos personagens da Nintendo da saga Zelda para um mundo de combate e ação dinámicos. Chute vários inimigos nesse jogo de guerra com o seu personage favorito da franquia, mas cuidado com as grandes levas de inimigos que esse jogo pode trazer como desafio. Esse jogo chega dia 18 de maio nas melhores lojas da região.")

        if message.content.lower().startswith('*0'):
         await client.send_message(message.channel,
                                  "Reviva momentos inesquecíveis da série Megaman com o jogo Megaman Legacy Collection + Megaman Legacy Collection 2. Adquira poderes fantásticos para explorar esse mundo e derrotar inimigos nesse side scrolling de ação muito divertido. Megaman estará disponível dia 22 desse mês. Não deixe de adquirí-lo se você gosta da série clássica.")

        if message.content.lower().startswith('*1'):
         await client.send_message(message.channel,
                                  "Infelizmente não se sabe muito sobre esse jogo, apenas que é um JRPG da empresa  YummiYummiTummy que você deve enfrentar um terrível império ou descobrir as histórias da rebelião. Dia 29 esse jogo estará disponível para seu Nintendo Switch.")

        if message.content.lower().startswith('*2'):
         await client.send_message(message.channel,
                                  "Shin Megami Tensei: Strange Journey Redux traz a oportunidade de você lutar contra seres demoniacos novamente nesse novo port para Nintendo 3DS. A história é expandida e promete mais tempo de diversão. Garanta sua edição dia 15 de maio de 2018.")

        if message.content.lower().startswith('moeda'):
         await client.send_message(message.channel,
                               "Escolha seu lado da moeda. Eu fico com a outra face.")


        if message.content.lower().startswith('cara'):
            choice = random.randint(1,2)
            if choice == 1:
               await client.add_reaction(message,'😃')
               await client.send_message(message.channel,
                                          "Você Ganhou!")
            if choice == 2:
                await client.add_reaction(message, '👑')
                await client.send_message(message.channel,
                                          "Você Perdeu!")

        if message.content.lower().startswith('coroa'):
                choice = random.randint(1, 2)
                if choice == 1:
                    await client.add_reaction(message, '😃')
                    await client.send_message(message.channel,
                                              "Você Perdeu!")
                if choice == 2:
                    await client.add_reaction(message, '👑')
                    await client.send_message(message.channel,
                                              "Você Ganhou!")

        if message.content.lower().startswith('tchau'):
         await client.send_message(message.channel,
                                  "Obrigado por conversar comigo, se precisar de alguma ajuda com relação a lançamentos de jogos, é só me chamar. Até logo!")



client.run('NDQxNjEzNTk3ODQwNTA2ODkw.Dcy8nA.o18RTVVyhilpfiuasRYKTmj2iWI')