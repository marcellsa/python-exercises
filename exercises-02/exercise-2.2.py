# Exercício 2.2: Jogo da palavra embaralhada. Desenvolva um jogo em que a
# pessoa usuária tenha que adivinhar uma palavra que será mostrada com as
# letras emaralhadas. O programa terá uma lista de palavras e escolherá uma
# aleatoriamente. O jogador terá 3 tentativas para adivinhar a palavra.
# Ao final, a apalavra deve ser mostrada na tela, informando se a pessoa ganhou
# ou perdeu o jogo.
import random

WORDS = ["banana", "carro", "computador", "urso", "caneca", "borracha"]
MAX_ATTEMPTS = 3


def get_secret_word(WORDS):
    secret_word = random.choice(WORDS)
    scrambled_word = "".join(random.sample(secret_word, len(secret_word)))
    return secret_word, scrambled_word


def store_guesses():
    guesses = []
    for attempt in range(MAX_ATTEMPTS):
        guess = input("Adivinha a palavra: ")
        guesses.append(guess)
    return guesses


def check_game_result(secret_word, guesses):
    print(f"Você acertou: {secret_word}") if secret_word in guesses else print(
        f"Você errou: {secret_word}"
    )


if __name__ == "__main__":
    secret_word, scrambled_word = get_secret_word(WORDS)
    print(f"Que palavra é essa: {scrambled_word}")
    guesses = store_guesses()
    check_game_result(secret_word, guesses)
