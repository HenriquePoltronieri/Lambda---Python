# lambda argumentos: expressão

## Essa função é para dobrar um número, mas ela é um pouco verbosa. Vamos reescrevê-la usando uma função lambda.
# refere-se a um trecho de código (função ou método) que utiliza uma quantidade excessiva de linhas, 
#símbolos ou palavras para realizar uma tarefa simples, tornando o código difícil de ler e manter
def dobrar(x):
    return x * 2


print(dobrar(5))  # 10
## Em lambda dobrar = lambda x: x * 2

dobrar_lambda = lambda x: x * 2
print(dobrar_lambda(5))  # 10



# O map(), uma função built in (veja no classroom em Dicas) aplica uma função em todos os elementos de uma lista.

numeros = [1, 2, 3, 4]

resultado = list(map(lambda x: x * 2, numeros))

print(resultado)  # [2, 4, 6, 8]

#O filter() filtra elementos com base em uma condição (True/False).

numeros = [1, 2, 3, 4, 5, 6]

pares = list(filter(lambda x: x % 2 == 0, numeros)) # Lembrem do operador de módulo (%) 
#que retorna o resto da divisão. Se o número for par, o resto da divisão por 2 será 0, ou seja, x % 2 == 0 é True para números pares.

print(pares)  # [2, 4, 6]


# O sorted() permite ordenar listas, inclusive com regras personalizadas.
numeros = [5, 2, 9, 1]

ordenado = sorted(numeros)

print(ordenado)  # [1, 2, 5, 9]

# Exemplo com um dicionário 
pessoas = [
    {"nome": "Ana", "idade": 25},
    {"nome": "Carlos", "idade": 20},
    {"nome": "Beatriz", "idade": 30}
]

ordenado = sorted(pessoas, key=lambda x: x["idade"]) # Aqui estou passando uma função lambda como argumento para a chave de ordenação (key).
 # A função lambda recebe um dicionário x e retorna o valor associado à chave "idade". Assim, a lista de pessoas será ordenada com base na idade.

print(ordenado)


#Map com lambda
nomes = ["ana", "carlos", "beatriz"]

maiusculos = list(map(lambda nome: nome.upper(), nomes))

print(maiusculos)  # ['ANA', 'CARLOS', 'BEATRIZ']

#Filter com lambda

nomes = ["ana", "carlos", "bia", "fernanda"]

longos = list(filter(lambda nome: len(nome) > 5, nomes))

print(longos)  # ['carlos', 'fernanda']


# Misturando oq que aprendemos
numeros = [1, 2, 3, 4, 5, 6]

resultado = list(
    map(
        lambda x: x * 2,
        filter(lambda x: x % 2 == 0, numeros)
    )
)

print(resultado)  # [4, 8, 12]



#Dada uma lista de dicionários, pegue apenas pessoas com idade > 18 e retorne os nomes em maiúsculo

pessoas = [
    {"nome": "Ana", "idade": 17},
    {"nome": "Carlos", "idade": 22},
    {"nome": "Beatriz", "idade": 19}
]

# Dica: use filter + map

resultado = list(
    map(
        lambda pessoa: pessoa["nome"].upper(),
        filter(lambda pessoa: pessoa["idade"] > 18, pessoas)
    )
)

print(resultado)

# ATIVIDADE

#1
# O avô de Ana tem o triplo de sua idade. Escreva uma função lambda para calcular a idade do avô, dado a idade de Ana..
# Ana tem 20 anos. Qual a idade do avô?

avo = lambda idade_ana: idade_ana * 3
print(avo(20))  # 60

#2
# Dada uma lista de números, use uma função lambda para filtrar apenas os números pares

numeros = [1, 2, 3, 4, 5, 6, 7, 8]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # [2, 4, 6, 8]

#3
# Dada uma lista de palavras, use uma função lambda para retornar apenas as palavras que começam com a letra "a"
# use o startswith() para verificar se a palavra começa com "a"

palavras = ["ana", "carlos", "amigo", "bia", "aviao"]
com_a = list(filter(lambda palavra: palavra.startswith("a"), palavras))
print(com_a)  # ['ana', 'amigo', 'aviao']
