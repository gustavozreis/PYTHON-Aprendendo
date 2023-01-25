"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11
Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14
Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for ma
"""

def get_last_digits(cpf):
    cpf_only_digits = ''
    
    # remove os pontos e os últimos 2 digitos do cpf
    for digit in cpf:
        if digit.isdigit():
            cpf_only_digits += digit
    
    cpf_nine_digits = cpf_only_digits[:9]
    
    # faz a multiplicação dos 9 digitos em ordem e depois os soma
    initial_mult_1 = 10
    final_digit_first = 0
    for digit in cpf_nine_digits:
        result = int(digit) * initial_mult_1
        final_digit_first += result
        initial_mult_1 -= 1 
    
    # multiplica a soma das multiplicações por 10
    final_digit_first *= 10
    
    # faz o módeulo por 11 do valor acima
    final_digit_first = 0 if final_digit_first % 11 > 9 else final_digit_first % 11
    
    cpf_with_final_first_digit = cpf_nine_digits + str(final_digit_first)
     
    print(cpf_with_final_first_digit)
    
    # faz a multiplicação dos 10 digitos em ordem e depois os soma
    initial_mult_2 = 11
    final_digit_second = 0
    for digit in cpf_with_final_first_digit:
        result = int(digit) * initial_mult_2
        final_digit_second += result
        initial_mult_2 -= 1
        
    # multiplica a soma das multiplicações acima por 10
    final_digit_second *= 10
    print(final_digit_second)
    
    # faz o módeulo por 11 do valor acima
    final_digit_second = 0 if final_digit_second % 11 > 9 else final_digit_second % 11
    
    print(final_digit_second)
        
get_last_digits('746.824.890-70')