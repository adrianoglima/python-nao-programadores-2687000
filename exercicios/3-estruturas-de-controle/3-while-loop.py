# Crie duas variáveis do tipo numérica, uma sinalizando a fase atual do curso e outra o nível final
nivel_atual = 1
nivel_final = 4

# Crie um while loop que imprima na tela o nível atual
while nivel_atual <= nivel_final:
  print(f'Você avançou um nível do curso. Nivel atual: {nivel_atual}')
  nivel_atual += 1

# Insira "else" no while loop anterior.
else:
  print('Parabéns, você concluiu o curso!')