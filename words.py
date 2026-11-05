"""دسته‌بندی‌ها و کلمات بازی Hangman."""

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
CATEGORIES = list(WORDS.keys())