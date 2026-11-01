def calcular_area(raio):
    n = 3.14159
    resultado = n*(raio**2)
    return resultado
    
raio = float(input())
area = calcular_area(raio)

print(f"A = {area:.4f}")
