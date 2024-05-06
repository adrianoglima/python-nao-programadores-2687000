# Nesse exercício coletaremos dados de uma estudante, armazenaremos em um dicionário e imprimiremos na tela esse dados em um formato amigável.

# 1. Solicite a estudante os seguintes dados: nome, ano que conheceu o LinkedIn, ano atual e os cursos realizados no LinkedIn Learning separados por virgula em ordem cronológica
estudante = {}
estudante['nome'] = input("Seu nome: ")
estudante['ano_linkedin'] = int(input("Ano Linkedin: "))
estudante['ano_atual'] = int(input("Ano Atual: "))
cursos = input("Informe seus cursos realizados: ")
estudante['cursos_feitos'] = cursos.split(", ")

# 2. Armazene esses dados em um dicionário



# 3. Imprima na tela uma string com as informações de nome, ano_conheceu_linkedin, total de anos transcurridos, total de cursos realizados e (apenas) o primeiro e último curso.
print(f"O Aluno {estudante['nome']}, conhece o linkedin à {estudante['ano_atual']-estudante['ano_linkedin']} e realizou {len(estudante['cursos_feitos'])}. Seu primeiro curso foi de {estudante['cursos_feitos'][0]} e o último curso foi de {estudante['cursos_feitos'][-1]}")