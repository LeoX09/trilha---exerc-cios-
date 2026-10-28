def calcular_salario():
    n_horas = int(input())
    valor_hora = float(input())
    valor_total_h = n_horas*valor_hora
    return valor_total_h
    
n_funcionario = int(input())
salario = calcular_salario()

print(f"NUMBER = {n_funcionario}")
print(f"SALARY = U$ {salario:.2f}")