import random

MAX_WRONG, VOWELS = 10, set("aeiou")
WORDS = {
    "Animals": ["elephant", "giraffe", "penguin", "dolphin"],
    "Jobs": ["dentist", "teacher", "engineer", "pilot"],
    "Countries": ["canada", "brazil", "germany", "japan"],
}



# انتخاب دسته با شماره
def choose_category():
    names = list(WORDS)
    for i, name in enumerate(names, 1):
        print(f"{i}. {name}")
    while True:
        choice = input("Category number: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(names):
            return names[int(choice) - 1]


# ساخت کلمه‌ی پنهان
def mask(word, guessed):
    return "".join(c if c in guessed else "-" for c in word)

# ورودی و اعتبارسنجی
def read_guess(guessed):
    while True:
        g = input("Guess a letter: ").strip().lower()
        if len(g) != 1 or not (g.isascii() and g.isalpha()):
            print("Enter exactly one English letter.")
        elif g in guessed:
            print("Already guessed (or a revealed vowel).")
        else:
            return g

# یک مرحله
def play_stage(word):
    guessed, wrong = set(VOWELS), []        # vowels are revealed from the start
    while len(wrong) < MAX_WRONG and mask(word, guessed) != word:
        print(f"\n{mask(word, guessed)}  wrong: {wrong}  left: {MAX_WRONG - len(wrong)}")
        g = read_guess(guessed)
        guessed.add(g)
        if g not in word:
            wrong.append(g)
    return len(wrong)

# کل بازی و امتیاز
def play_game():
    words = WORDS[choose_category()][:]
    random.shuffle(words)                   # no repeated words in a session
    score = 0
    for stage, word in enumerate(words, 1):
        wrong = play_stage(word)
        if wrong >= MAX_WRONG:
            print(f"Game over! The word was '{word}'.")
            break
        points = 100 + (MAX_WRONG - wrong) * 10
        score += points
        print(f"Stage {stage} won! +{points} points (total {score})")
    print(f"Final score: {score}")

if __name__ == "__main__":
    while input("\nPress Enter to play (q to quit): ").strip().lower() != "q":
        play_game()