import random

words = ["python", "computer", "mobile", "keyboard", "monitor"]

word = random.choice(words)
guessed = []
attempts = 6

print("Welcome to Hangman!")
print("Word: " + "_ " * len(word))

while attempts > 0:
    guess = input("\nEnter a letter: ").lower()
    
    if guess in guessed:
        print("Already guessed this letter!")
        continue
    
    guessed.append(guess)
    
    if guess in word:
        print("Correct!")
    else:
        attempts -= 1
        print("Wrong! Attempts left: " + str(attempts))
    
    display = ""
    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "
    print("Word: " + display)
    
    if all(letter in guessed for letter in word):
        print("\nYou WIN! The word was: " + word)
        break
else:
    print("\nGame Over! The word was: " + word)