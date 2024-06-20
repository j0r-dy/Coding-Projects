import random

words = [
    'python', 'javascript', 'kotlin', 'ruby', 'swift', 'algorithm',
    'compiler', 'database', 'encryption', 'firewall', 'hardware',
    'internet', 'java', 'kernel', 'malware', 'network', 'object',
    'protocol', 'query', 'router', 'security', 'token', 'url',
    'virtual', 'wireless', 'xml', 'yaml', 'zip', 'abstract', 'binary',
    'cache', 'developer', 'ethernet', 'framework', 'gateway', 'hexadecimal',
    'iteration', 'juxtapose', 'keystroke', 'lambda', 'metadata', 'node']

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

hangman_stages = ["""
   +---+
   O   |
  /|\\  |
  / \\  |
      ===""", '''
   +---+
   O   |
  /|\\  |
  /    |
      ===''', '''
   +---+
   O   |
  /|\\  |
       |
      ===''', '''
   +---+
   O   |
  /|   |
       |
      ===''', '''
   +---+
   O   |
   |   |
       |
      ===''', '''
   +---+
   O   |
       |
       |
      ===''', '''
   +---+
       |
       |
       |
      ===''',]

chosen_word = random.choice(words)

word_display = ['_' for _ in chosen_word]

attempts = 6

# Display dello stato dell'impiccato e della parola


def display_state():
    print(f'attempts = {attempts}')
    print(hangman_stages[attempts])
    print(' '.join(word_display))


def display_word():
    print(' '.join(word_display))


# loop principale di gioco

while attempts > 0 and '_' in word_display:
    display_state()
    guess = input('digita una lettera per giocare').lower()

    # check se la lettera immessa è corretta
    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                if word_display[index] == '_':
                    word_display[index] = guess
    else:
        print('incorrect. try again')
        attempts -= 1

    # check per vittoria
    if '_' not in word_display:
        print('Congratulazioni, hai vinto!')
        break

if attempts == 0:
    display_state()
    print('Mi spiace, hai perso. La prola era: ', chosen_word)
