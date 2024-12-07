import random

def escolher_palavra():
    # Lista de palavras em português
    palavras = ["computador", "desenvolvimento", "qualidade", "software", "programacao", 
                "educacao", "colaboracao", "algoritmo", "tecnologia", "internet"]
    return random.choice(palavras)

def exibir_progresso(palavra, letras_corretas):
    # Mostra o progresso do jogador
    return " ".join([letra if letra in letras_corretas else "_" for letra in palavra])

def jogo_da_forca():
    palavra = escolher_palavra()
    letras_corretas = set()
    letras_erradas = set()
    tentativas = 6

    print("Bem-vindo ao Jogo da Forca!")
    print("Adivinhe a palavra: ", exibir_progresso(palavra, letras_corretas))

    while tentativas > 0:
        print("\nLetras já tentadas:", ", ".join(sorted(letras_erradas | letras_corretas)))
        letra = input("Digite uma letra: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, insira apenas uma letra válida.")
            continue

        if letra in letras_corretas | letras_erradas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        if letra in palavra:
            letras_corretas.add(letra)
            print("Boa! ", exibir_progresso(palavra, letras_corretas))
        else:
            letras_erradas.add(letra)
            tentativas -= 1
            print(f"Errou! Você tem {tentativas} tentativas restantes.")

        if set(palavra).issubset(letras_corretas):
            print(f"Parabéns! Você adivinhou a palavra: {palavra}")
            break
    else:
        print(f"Você perdeu! A palavra era: {palavra}")

if __name__ == "__main__":
    jogo_da_forca()
