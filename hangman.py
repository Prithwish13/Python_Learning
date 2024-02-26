import random

word_list = ["ardvark", "baboon", "camel"]
hangman_stages = [
    """
     ------
    |    |
    |
    |
    |
    |
    -
    """,
    """
     ------
    |    |
    |    O
    |
    |
    |
    -
    """,
    """
     ------
    |    |
    |    O
    |    |
    |
    |
    -
    """,
    """
     ------
    |    |
    |    O
    |   /|
    |
    |
    -
    """,
    """
     ------
    |    |
    |    O
    |   /|\\
    |
    |
    -
    """,
    """
     ------
    |    |
    |    O
    |   /|\\
    |   /
    |
    -
    """,
    """
     ------
    |    |
    |    O
    |   /|\\
    |   / \\
    |
    -
    """
]
hangman_stage = 0
matched_count = 0
chosen_word = random.choice(word_list)
implementing_word = list( "_" * len(chosen_word) )


while matched_count < len(chosen_word) and hangman_stage < len(hangman_stages):
    chosen_letter = str(input("chose a character: ")).lower()
    is_match = False
    for index, char in enumerate(chosen_word):
        if chosen_letter == char and implementing_word[index] == "_":
             is_match = True
             implementing_word[index] = char
             matched_count += 1
    
    if is_match:
        print(implementing_word)         
    if not is_match:
        print(hangman_stages[hangman_stage])
        hangman_stage += 1
if "".join(implementing_word) == chosen_word:
    print("Game oven you have won the match")
elif hangman_stage == len(hangman_stages):
    print("Game oven you have lost the match")
else:
    print("Game over match draw")            