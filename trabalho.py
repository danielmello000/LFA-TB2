class Automato:
    def __init__(self, es_inicial, es_finais = [], estados = [], transicoes = []):
        self.es_inicial = es_inicial
        self.es_finais = es_finais
        self.estados = estados
        self.transicoes = transicoes

# Função que recebe um automato, uma palavra, o estado atual (opcional) e o indice do símbolo na palavra (opcional)
# Retorna True se a palavra for reconhecida pelo automato, caso contrário retorna Falso
def reconhecerPalavra(automato, palavra, estado = "", indice = 0):
    if estado == "":    # Se o estado não for passado, seu valor é setado para o estado inicial do autômato
        estado = automato.es_inicial

    if indice == len(palavra):  # Verifica se chegou no final da palavra, se não há mais símbolo para ler; Ponto de parada
        return estado in automato.es_finais     # Checa se o estado atual é um estado final

    aceito = False  # Inicializa a variável de aceite como falso
    for transicao in automato.transicoes:   # Percorre a lista de transições do autômato
        if transicao[0] == estado and transicao[1] == palavra[indice]:  # Pega a transição correspondente ao estado e símbolo atual
            # Chama a função recursivamente para o próximo caminho, avançando o símbolo na palavra e o estado
            if reconhecerPalavra(automato, palavra, transicao[2], indice + 1):
                return True;    # retorna verdadeiro se a instância da função acima for true
    return False;   # Retorna nenhum dos caminhos acima der verdadeiro

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
file = open("palavras.txt", "r")       # Abre o arquivo de palavras em modo leitura
for line in file:                   # Percorre as linhas do arquivo
    palavras.append(line.replace('\n', ''))  # Armazena as linhas do arquivo na lista de palavras, removendo '\n' se houver
file.close()                        # Fecha o arquivo

palavrasAceitas = []                         # Cria uma lista para armazenar se as palavras são aceitas pelo automato
for palavra in palavras:            # Percorre a lista de palavras
    palavrasAceitas.append(reconhecerPalavra(afnd, palavra)) # Armazena na lista palavrasAceitas o resultado da função

file = open('saida.txt', "w") # Abre o arquivo de saida em modo gravacao
for i in range(len(palavras)): # Loop que executa a quantidade de palavras na lista de palavras
    if(palavrasAceitas[i]): # Define o valor da string aceito de acordo com o valor da posição atual da lista palavrasAceitas
        aceito = "aceito"
    else:
        aceito = "não aceito"
    file.write(palavras[i] + " " + aceito + "\n") # Grava a linha no arquivo de saída
    print(palavras[i] + " " + aceito)   # Imprime o resultado no console
file.close()    # Fecha o arquivo de saída