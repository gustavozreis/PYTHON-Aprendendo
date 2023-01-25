import random

def generate_cpf():
    
    cpf_nine_digits = ''
    
    for digit in range(9):
        cpf_nine_digits += str(random.randint(0,9))        
  
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
    
    # faz a multiplicação dos 10 digitos em ordem e depois os soma
    initial_mult_2 = 11
    final_digit_second = 0
    for digit in cpf_with_final_first_digit:
        result = int(digit) * initial_mult_2
        final_digit_second += result
        initial_mult_2 -= 1
        
    # multiplica a soma das multiplicações acima por 10
    final_digit_second *= 10
    
    # faz o módeulo por 11 do valor acima
    final_digit_second = 0 if final_digit_second % 11 > 9 else final_digit_second % 11
    
    generated_cpf = cpf_nine_digits + str(final_digit_first) + str(final_digit_second)
    
    print(generated_cpf)
        
generate_cpf()