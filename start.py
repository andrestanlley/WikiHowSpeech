import requests
from bs4 import BeautifulSoup
from gtts import gTTS
criados = 0

while True:
    while True:
        random = requests.get("https://www.wikihow.com/Special:Randomizer")
        url = requests.get(f'{random.url}')
        content = url.content
        site = BeautifulSoup(content, 'html.parser')
        titulo = site.find('h1', attrs={'class': 'title_md'})
        if titulo != None:
            print(f'TITULO: {titulo.text}\n')
            break
    print(f'Videos criados: {criados}')
    print('\n[ INICIANDO NOVA BUSCA ]\n')
    conteudo = site.find('div', attrs={'class': 'mf-section-1 collapsible-block'})
    steps = conteudo.find_all('div', attrs={'class': f'step'})
    for i, t in enumerate(steps):
        texto = f'{i+1}st - {t.text}'
        print(texto)
        print(f'\n [ Criando arquivo de audio {i+1}.mp3 ]\n')
        tts = gTTS(texto, lang='en', tld='com')
        tts.save(f'{i+1}.mp3')
    print('\n [ Criação de arquivos finalizada. ] \n')
    criados += 1
