import os
import requests
from bs4 import BeautifulSoup

class AdoroCinema:

    def extrairComentariosFilme(self, filme, n):
        comentarios = []
        for i in range(1, n + 1):
            url = 'http://www.adorocinema.com/filmes/' + filme + '/criticas/espectadores/?page=' + str(i)
            htmlComentarios = requests.get(url).text
            bsC = BeautifulSoup(htmlComentarios, 'html.parser')
            comentarios_com_tags = bsC.find_all('div', class_="content-txt review-card-content")
            for comentario_com_tag in comentarios_com_tags:
                comentarios.append(comentario_com_tag.get_text().strip())
        return comentarios

    def salvarComentariosFilme(self, filme, comentarios):
        diretorio = 'trabalho1'
        caminho_arquivo = os.path.join(diretorio, filme + '_comentarios.txt')
        
        with open(caminho_arquivo, 'w', encoding='utf-8') as arq_saida:
            for comentario in comentarios:
                arq_saida.write(comentario + '\n\n')


filme = input('Digite o código do filme, conforme listado na barra de endereço do site https://www.adorocinema.com/: ')
n = int(input('Digite quantas páginas de comentários você deseja consultar: '))
crawler = AdoroCinema()
comentarios = crawler.extrairComentariosFilme(filme, n)
crawler.salvarComentariosFilme(filme, comentarios)
print('Programa executado com sucesso. Consulte os arquivos gerados na pasta "trabalho1".')