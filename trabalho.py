class Automato:
    def __init__(self, es_inicial, es_finais = [], estados = [], transicoes = []):
        self.es_inicial = es_inicial
        self.es_finais = es_finais
        self.estados = estados
        self.transicoes = transicoes

def reconhecer(palavra, index, estado, automato):
    if index == len(string) - 1:
        return estado in automato.es_finais
    


arq_entrada = []                    # Cria uma lista para armazenar as linhas do arquivo
file = open("entrada.txt", "r")     # Abre o arquivo de entrada em modo leitura
for line in file:                   # Pega as linhas do arquivo
    arq_entrada.append(line.replace('\n', ''))  # Armazena a linha do arquivo na lista, removendo '\n' se houver
file.close()                        # Fecha o arquivo

for i in range(2, len(arq_entrada)):    # Transforma as strings dos estados finais e das transições em listas
    arq_entrada[i] = arq_entrada[i].split()

# Cria o objeto automato nao deterministico com os dados do arquivo de entrada
afnd = Automato(arq_entrada[1], arq_entrada[2], arq_entrada[0], arq_entrada[3:])

palavras = []                       # Cria uma lista para armazenar as palavras
file = open("saida.txt", "r")       # Abre o arquivo de saida em modo leitura
for line in file:                   # Percorre as linhas do arquivo
    palavras.append(line.replace('\n', ''))  # Armazena as linhas do arquivo na lista de palavras, removendo '\n' se houver
file.close()                        # Fecha o arquivo

aceito = []                         # Cria uma lista para armazenar se as palavras são aceitas pelo automato
for palavra in palavras:            # Percorre a lista de palavras
    