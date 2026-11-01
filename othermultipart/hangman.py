def hangmanthegame():
  import random
  # List of words to choose from
  words = ["python", "hangman", "challenge", "programming", "code"]

  def choose_word():
      return random.choice(words)

  def display_progress(word, guessed_letters):
      return " ".join([letter if letter in guessed_letters else "_" for letter in word])

  def hangman():
      word = choose_word()
      guessed_letters = set()
      attempts = 6

      print("Welcome to Hangman!")
      print("Guess the word:")

      while attempts > 0:
          print(display_progress(word, guessed_letters))
          print(f"Attempts remaining: {attempts}")
          guess = input("Guess a letter: ").lower()

          if len(guess) != 1 or not guess.isalpha():
              print("Please guess a single letter.")
              continue

          if guess in guessed_letters:
              print("You already guessed that letter!")
              continue

          guessed_letters.add(guess)

          if guess in word:
              print("Good guess!")
              if all(letter in guessed_letters for letter in word):
                  print(f"Congratulations, you guessed the word: {word}!")
                  break
          else:
              attempts -= 1
              print("Incorrect guess.")

          if attempts == 0:
              print(f"Game over! The word was: {word}")

  # Run the game
  hangman()
