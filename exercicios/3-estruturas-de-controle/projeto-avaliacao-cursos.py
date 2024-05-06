# Nesse desafio você verificará dentro de uma lista se o item estar contido nela, caso verdadeiro deverá imprimir na tela essa informação, além disso deverá solicitar avaliação para o item e armazená-la em um dicionário.
# 1. Crie uma lista com 5 diferentes cursos do LinkedIn Learning
lista_cursos = ['javascript','html5','css3','python','sql']

# 2. Crie 3 variáveis do tipo string e associe 1 curso a cada uma delas
curso1 = 'html5'
curso2 = 'css3'
curso3 = 'javascript5'
# 3. Crie um dicionário vazio para armazenar a nota do curso
avaliacoes = {}

# 4. Crie uma estrutura condicional para verificar se cada variável está contida na lista
if curso1 in lista_cursos:
  print(f'Curso {curso1} no catálogo')
  avaliacoes[curso1] = int(input(f"Informe a nota do curso {curso1}: 0 a 5 "))
if curso2 in lista_cursos:
  print(f'Curso {curso2} no catálogo')
  avaliacoes[curso2] = int(input(f"Informe a nota do curso {curso2}: 0 a 5 "))
if curso3 in lista_cursos:
  print(f'Curso {curso3} no catálogo')
  avaliacoes[curso3] = int(input(f"Informe a nota do curso {curso3}: 0 a 5 "))
else:
  print("Curso não existe no catálogo!")

print(avaliacoes)

# 5. Se o curso estiver na lista, solicite uma nota para avaliação
# 6. Armazene essa nota no dicionário, sendo a chave o título do curso e o valor a nota
