ano_nascimento = 1989
ano_formatura = 2010

# Considerando que as variáveis acima correspondem a 'Darlene', descubra a idade dela no ano da sua formatura
print(ano_formatura-ano_nascimento)

# Escreva expressões comparativas usando os operadores relacionais >, <= e ==. Imprima na tela as respostas
maior = ano_nascimento > ano_formatura
menor = ano_nascimento <= ano_formatura
diferenca = ano_formatura == ano_nascimento

print(f"O ano de nascimento da 'Darlene' é maior que o ano de formatura? {maior}")
print(f"O ano de nascimento da 'Darlene' é menor ou igual que o ano de formatura? {menor}")
print(f"A 'Gerlaine se formou no mesmo ano que nasceu? {diferenca}")
# Crie expressões comparativas mais complexas utilizando operadores lógicos and, or e not. Imprima na tela as respostas
print((ano_formatura < ano_nascimento) and (ano_formatura < ano_nascimento))
print((ano_formatura >= ano_nascimento) or (ano_nascimento != ano_formatura))
print(not(ano_nascimento == ano_formatura))

print('Adriano' != 'Lima')
print(1958 == 2023 and 2==2)
print('Adriano' != 'Lima' or 'Python' == 'Python')
print(not ano_formatura == ano_nascimento)