def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

# Testando a função
if __name__ == "__main__":
    num = int(input("Digite um número: "))
    print(f"O fatorial de {num} é {fatorial(num)}")
