#peça para o usuario escrever algo e disseque

p = input("Digite algo: ")

print(f"é uma string?{p.isalpha()}")
print(f"é um numero?{p.isnumeric()}")
print(f"é uma alfanumerico?{p.isalnum()}")
print(f"éstá em letras maiusculas?{p.isupper()}")
print(f"esta em letra minuscula? {p.islower()}")