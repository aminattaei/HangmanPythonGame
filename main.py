import os
os.system("clear")

from random import randint


WORDS = {
    "Animals": [
        "elephant", "giraffe", "penguin", "dolphin", "kangaroo",
        "crocodile", "butterfly", "squirrel", "leopard", "hamster",
    ],
    "Fruits & Vegetables": [
        "banana", "orange", "strawberry", "pineapple", "cucumber",
        "broccoli", "cabbage", "pumpkin", "tomato", "cherry",
    ],
    "Food & Drinks": [
        "pizza", "burger", "sandwich", "chocolate", "pancake",
        "spaghetti", "coffee", "lemonade", "omelette", "popcorn",
    ],
    "Jobs": [
        "dentist", "teacher", "engineer", "doctor", "farmer",
        "pilot", "plumber", "firefighter", "journalist", "architect",
    ],
    "Countries": [
        "canada", "brazil", "germany", "japan", "france",
        "mexico", "norway", "portugal", "australia", "argentina",
    ],
    "Sports": [
        "football", "tennis", "swimming", "volleyball", "cycling",
        "boxing", "archery", "wrestling", "baseball", "badminton",
    ],
    "Colors & Shapes": [
        "purple", "yellow", "orange", "circle", "triangle",
        "rectangle", "diamond", "crimson", "silver", "hexagon",
    ],
    "Household Items": [
        "pillow", "blanket", "kitchen", "curtain", "mirror",
        "window", "blender", "bookshelf", "carpet", "umbrella",
    ],
    "Nature": [
        "mountain", "river", "volcano", "forest", "desert",
        "waterfall", "rainbow", "thunder", "island", "glacier",
    ],
    "Technology": [
        "computer", "keyboard", "internet", "software", "battery",
        "monitor", "printer", "website", "program", "network",
    ],
}

# لیست نام دسته‌بندی‌ها (برای صفحه‌ی انتخاب دسته)
CATEGORIES = str(list(WORDS.keys())).lower()

def select_category():
    while True:
        user_category_choose =input(f"Please select one category from below:\n {CATEGORIES}\nEnter your choose: ")

        if user_category_choose in CATEGORIES:
            return user_category_choose
        else:
            print("Your should select one category!")

def select_word():
    category_obj = select_category().capitalize()
    return WORDS[category_obj][randint(0,9)] 


def validate_char_input_from_user():
    vowels = ['a','i','o','u','e']
    user_correct_guess_char = []

    word_seperated_char = [char for char in select_word()]
    user_char_input = input("Enter your guess character: ")

    for char in word_seperated_char:
        if user_char_input == char:
            user_correct_guess_char.append(char)
        elif user_char_input in vowels:
            return True
        else:
            return False

        return user_correct_guess_char
            


def check_guess_left():
    guess_left = 10
    pass


print(validate_char_input_from_user())

print(check_guess_left())