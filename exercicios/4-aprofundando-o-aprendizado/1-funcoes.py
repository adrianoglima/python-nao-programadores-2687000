# Crie uma função para selecionar o curso desejado em uma trilha profissional
def seleciona_curso():
  curso = int(input(
    "Escolha o curso que deseja iniciar: 1- HTML5, 2- CSS3, 3- JAVASCRIPT, 4- SQL, 5- PYTHON : "
  ))
  return curso
# Crie uma função para percorrer todos os níveis de um curso e imprimir na tela a informação do nível atual
def busca_curso_selecionado(curso_selecionado):
  trilha = {
    1: {'titulo': 'Html 5', 'total_niveis': 5},
    2: {'titulo': 'Css 3', 'total_niveis': 7},
    3: {'titulo': 'Javascript', 'total_niveis': 15},
    4: {'titulo': 'Banco de Dados', 'total_niveis': 10},
    5: {'titulo': 'Programação', 'total_niveis': 20}
  }
  curso_atual = trilha[curso_selecionado]['titulo']
  curso_nivel_atual = 1
  curso_total_niveis = trilha[curso_selecionado]['total_niveis']

  print(
    f'Bem vindo ao curso: "{curso_atual}!. Voc está iniciando no nível {curso_nivel_atual}.\n.....'
  )

  while curso_nivel_atual <= curso_total_niveis:
    print(
      f'Parabéns! Você acaba de concluir a fase {curso_nivel_atual} do curso {curso_atual}.'
    )
    curso_nivel_atual += 1
  else:
    print(f'Você concluir o {curso_atual} com sucesso!')
4
# Execute as funções

curso = seleciona_curso()
busca_curso_selecionado(curso)