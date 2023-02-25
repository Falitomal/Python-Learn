print(f"\nExamples of list comprehension\n")

pies = [10, 20, 30, 40, 42, 46, 50]
metros = [p * 3.28 for p in pies]

print(f"From foots: {pies}\nto meter are: {metros}\n")

valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_cuadrado = [v **2 for v in valores]

print(f"From this values: {valores}\nto values squared are: {valores_cuadrado}")

valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_pares =[v for v in valores if v % 2== 0]
print(f"From this values: {valores}\nthe values pairs are: {valores_pares}")

temperatura_fahrenheit = [32, 212, 275]
grados_celsius = [(c -32) *(5/9) for c in temperatura_fahrenheit]
print(f"From this values: {temperatura_fahrenheit}\nto celsius are: {grados_celsius}")