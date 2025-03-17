import random

class NumberGuessingGame:
    def __init__(self):
        self.number = random.randint(1, 100)
        self.guesses = 0
        self.high_score = float('inf')

    def play(self):
        self.displayWelcomeMessage()
        self.guessingLoop()
        self.updateHighScore()

    def guessingLoop(self):
        while True:
            self.guesses += 1
            guess = self.getUserInput()
            if self.checkGuess(guess):
                break

    def getUserInput(self):
        while True:
            try:
                return int(input("🎯 Enter your guess: "))
            except ValueError:
                print("❌ Invalid Input! Please enter a valid number.")

    def checkGuess(self, guess):
        if guess > self.number:
            print("👇 Lower Number Please")
        elif guess < self.number:
            print("👆 Higher Number Please")
        else:
            print(f"\n✅ You guessed the number {self.number} correctly in {self.guesses} attempts!")
            return True
        return False

    def updateHighScore(self):
        if self.guesses < self.high_score:
            self.high_score = self.guesses
            print("🏁 New High Score Achieved!")
        print(f"🥇 Your Best Score: {self.high_score} attempts")

    def restart(self):
        self.number = random.randint(1, 100)
        self.guesses = 0

    def playAgain(self):
        while True:
            choice = input("\n🔁 Do you want to play again? (yes/no): ").lower()
            if choice == 'yes':
                self.restart()
                self.play()
            elif choice == 'no':
                print("\n🎮 Thanks for Playing! 😊")
                break
            else:
                print("❌ Invalid Option! Please enter 'yes' or 'no'.")

    def displayWelcomeMessage(self):
        print("\n🎮 Welcome to the Number Guessing Game!")
        print("Guess the number between 1 to 100")
        print("---------------------------------------------------")


if __name__ == "__main__":
    game = NumberGuessingGame()
    game.play()
    game.playAgain()
