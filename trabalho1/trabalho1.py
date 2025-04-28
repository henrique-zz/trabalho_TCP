import os
import re

diretorio = 'trabalho1'

# \b: significa que estaremos analisando apenas palavras completas, e não subpalavras
palavras_positivas = [
    re.compile(r"\bbom\b", re.IGNORECASE), # \w: permite qualquer coisa após o divert, para contar divertido e divertida
    re.compile(r"\blegal\w+\b", re.IGNORECASE),
    re.compile(r"\binteressante\b", re.IGNORECASE),
    re.compile(r"\bdivertid\w+\b", re.IGNORECASE),
    re.compile(r"\bincrível\b", re.IGNORECASE),
    re.compile(r"\bimpressionante\b", re.IGNORECASE),
    re.compile(r"\brecomendo\b", re.IGNORECASE),
    re.compile(r"\bexcelente\b", re.IGNORECASE),
    re.compile(r"\bmaravilhoso\b", re.IGNORECASE),
    re.compile(r"\bespetacular\b", re.IGNORECASE),
    re.compile(r"\bcativante\b", re.IGNORECASE),
    re.compile(r"\benvolvente\b", re.IGNORECASE),
    re.compile(r"\btocante\b", re.IGNORECASE),
    re.compile(r"\bemocionante\b", re.IGNORECASE),
    re.compile(r"\bgenial\b", re.IGNORECASE),
    re.compile(r"\bsurpreendente\b", re.IGNORECASE),
    re.compile(r"\bsensivel\b", re.IGNORECASE),
    re.compile(r"\bintenso\b", re.IGNORECASE),
    re.compile(r"\bobra-prima\b", re.IGNORECASE),
    re.compile(r"\bempolgante\b", re.IGNORECASE),
    re.compile(r"\bcimpactante\b", re.IGNORECASE),
    re.compile(r"\bsensível\b", re.IGNORECASE),
    re.compile(r"\bfenomenal\b", re.IGNORECASE),
    re.compile(r"\bbrilhante\b", re.IGNORECASE),
    re.compile(r"\bfascinante\b", re.IGNORECASE),
    re.compile(r"\bbem contruído\b", re.IGNORECASE),
    re.compile(r"\batuações incríveis\b", re.IGNORECASE),
    re.compile(r"\btrama envolvente\b", re.IGNORECASE),
    re.compile(r"\bdireção impecável\b", re.IGNORECASE),
    re.compile(r"\bvale a pena\b", re.IGNORECASE),
    re.compile(r"\bfotografia linda\b", re.IGNORECASE),
    re.compile(r"\bprodução de alto nível\b", re.IGNORECASE),
    re.compile(r"\bprofundo e tocante\b", re.IGNORECASE),
]

palavras_negativas = [
    re.compile(r"\bruim\b", re.IGNORECASE),
    re.compile(r"\bpessim\w+\b", re.IGNORECASE),
    re.compile(r"\bchat\w+\b", re.IGNORECASE),
    re.compile(r"\bterrível\b", re.IGNORECASE),
    re.compile(r"\bsem graça\b", re.IGNORECASE),
    re.compile(r"\bfraco\b", re.IGNORECASE),
    re.compile(r"\bmau\b", re.IGNORECASE),
    re.compile(r"\birritante\b", re.IGNORECASE),
    re.compile(r"\bdá raiva\b", re.IGNORECASE),
    re.compile(r"\bfrustrante\b", re.IGNORECASE),
    re.compile(r"\bdecepcionante\b", re.IGNORECASE),
    re.compile(r"\bredundância\b", re.IGNORECASE),
    re.compile(r"\bcansativ\w+\b", re.IGNORECASE),
    re.compile(r"\bexagerado\b", re.IGNORECASE),
    re.compile(r"\bforçado\b", re.IGNORECASE),
    re.compile(r"\broteiro ruim\b", re.IGNORECASE),
    re.compile(r"\bmedian\b", re.IGNORECASE),
    re.compile(r"\bdecepção\b", re.IGNORECASE),
    re.compile(r"\bsuperficial\b", re.IGNORECASE),
    re.compile(r"\bentedianteb", re.IGNORECASE),
    re.compile(r"\bdeixa a desejar\b", re.IGNORECASE),
    re.compile(r"\bnão percam tempo\b", re.IGNORECASE),
    re.compile(r"\bridiculo\b", re.IGNORECASE),
    re.compile(r"\bbagunçado\b", re.IGNORECASE),
    re.compile(r"\bmonótono\b", re.IGNORECASE),
    re.compile(r"\bcansativo\b", re.IGNORECASE),
    re.compile(r"\bsem sentido\b", re.IGNORECASE),
    re.compile(r"\bexagerado\b", re.IGNORECASE),
    re.compile(r"\broteiro fraco\b", re.IGNORECASE),
    re.compile(r"\bconfuso demais\b", re.IGNORECASE),
    re.compile(r"\bdeperdício de tempo\b", re.IGNORECASE),
    re.compile(r"\bnão recomendo\b", re.IGNORECASE),
    re.compile(r"\besperava mais\b", re.IGNORECASE),
    re.compile(r"\bdiálogos fracos\b", re.IGNORECASE),
    re.compile(r"\befeitos ruins\b", re.IGNORECASE),
    re.compile(r"\bhistória mal contada\b", re.IGNORECASE),
]

for arquivo in os.listdir(diretorio):
    if arquivo.endswith('comentarios.txt'):
        caminho_completo = os.path.join(diretorio, arquivo)

        # define o nome do arquivo de saída com base no nome do arquivo de entrada (nome do filme)
        nome_arquivo_saida = arquivo.replace(
            'comentarios.txt', '_comentarios_classificados.txt')
        caminho_saida = os.path.join(diretorio, nome_arquivo_saida)

        reviews_positivas = 0
        reviews_negativas = 0
        reviews_neutras = 0

        with open(caminho_saida, "w", encoding="utf-8") as saida:
            with open(caminho_completo, 'r', encoding="utf-8") as f:
                conteudo = f.read()
                comentarios = [linha.strip() for linha in conteudo.splitlines() 
                               if linha.strip()]  # divide o texto por linhas
                total_comentarios = len(comentarios)

                print(f'Comentários no arquivo {arquivo}:')
                saida.write(f'Comentários no arquivo {arquivo}:\n')

                for comentario in comentarios:
                    print(f'\n- {comentario}')

                    positiva = any(positivas.search(comentario)
                                   for positivas in palavras_positivas)
                    negativa = any(negativas.search(comentario)
                                   for negativas in palavras_negativas)

                    if positiva and not negativa:
                        categoria = "Positiva"
                        reviews_positivas += 1
                        print("  -> Review Positiva.")
                    elif negativa and not positiva:
                        categoria = "Negativa"
                        reviews_negativas += 1
                        print("  -> Review Negativa.")
                    else:
                        categoria = "Neutra"
                        reviews_neutras += 1
                        print("  -> Review Neutra.")

                    saida.write(
                        f"- {comentario}\nClassificação: {categoria}\n\n")

        porcentagem_positivos = (reviews_positivas / total_comentarios) * 100
        porcentagem_negativos = (reviews_negativas / total_comentarios) * 100
        porcentagem_neutros = (reviews_neutras / total_comentarios) * 100

        saida_comentarios = (
            "\n==============================\n"
            f"Total de comentários: {total_comentarios}\n\n"
            f"Total de comentários positivos: {reviews_positivas}\n"
            f"Com {porcentagem_positivos:.1f}% dos comentários.\n\n"
            f"Total de comentários negativos: {reviews_negativas}\n"
            f"Com {porcentagem_negativos:.1f}% dos comentários.\n\n"
            f"Total de comentários neutros: {reviews_neutras}\n"
            f"Com {porcentagem_neutros:.1f}% dos comentários.\n"
            "==============================\n"
        )
        # Salva comentários classificados separadamente
arquivo_positivos = os.path.join(diretorio, f'{arquivo[:-15]}_positivos.txt')
arquivo_negativos = os.path.join(diretorio, f'{arquivo[:-15]}_negativos.txt')
arquivo_neutros = os.path.join(diretorio, f'{arquivo[:-15]}_neutros.txt')

print(saida_comentarios)
with open(caminho_saida, "a", encoding="utf-8") as saida:
    saida.write(saida_comentarios)

with open(arquivo_positivos, 'w', encoding='utf-8') as pos, \
        open(arquivo_negativos, 'w', encoding='utf-8') as neg, \
        open(arquivo_neutros, 'w', encoding='utf-8') as neu:
    for comentario in comentarios:
        positiva = any(p.search(comentario) for p in palavras_positivas)
        negativa = any(n.search(comentario) for n in palavras_negativas)

        if positiva and not negativa:
            pos.write(comentario + '\n\n')
        elif negativa and not positiva:
            neg.write(comentario + '\n\n')
        else:
            neu.write(comentario + '\n\n')

        
