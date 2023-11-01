import random

def adivinhador_numero():
    print("Pense em um número de 1 a 100 e eu vou tentar adivinhá-lo.")

    limite_inferior = 1
    limite_superior = 100
    tentativas = 0
    numero_adivinhado = None

    while True:
        numero_adivinhado = random.randint(limite_inferior, limite_superior)
        tentativas += 1
        print(f"Minha tentativa {tentativas}: {numero_adivinhado}")

        resposta = input("O número adivinhado é (Digite 'M' para Menor, 'P' para Maior ou 'C' para Correto): ").upper()

        if resposta == 'C':
            print(f"Eu acertei! Seu número é {numero_adivinhado}.")
            break
        elif resposta == 'M':
            limite_superior = numero_adivinhado - 1
        elif resposta == 'P':
            limite_inferior = numero_adivinhado + 1
        else:
            print("Por favor, digite 'M' para Menor, 'P' para Maior ou 'C' para Correto.")

    print(f"Levou {tentativas} tentativas para adivinhar o seu número.")

if __name__ == "__main__":
    adivinhador_numero()
