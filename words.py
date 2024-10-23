words = [
    "apple",
    "banana",
    "cherry",
    "date",
    "elderberry",
    "fig",
    "grape",
    "honeydew",
    "kiwi",
    "lemon",
    "mango",
    "nectarine",
    "orange",
    "papaya",
    "quince",
    "raspberry",
    "strawberry",
    "tangerine",
    "watermelon",
    "zucchini",
    "avocado",
    "blackberry",
    "blueberry",
    "cantaloupe",
    "coconut",
    "cranberry",
    "dragonfruit",
    "grapefruit",
    "guava",
    "jackfruit",
    "lychee",
    "mandarin",
    "mulberry",
    "olive",
    "peach",
    "pear",
    "plum",
    "pomegranate",
    "pineapple",
    "persimmon",
    "apricot",
    "passionfruit",
    "rhubarb",
]


easy = [word for word in words if 3 <= len(word) <= 5]
medium = [word for word in words if 6 <= len(word) <= 8]
hard = [word for word in words if len(word) >= 9]

# easy = ["Easy"]
# medium = ["Medium"]
# hard = ["hard"]
