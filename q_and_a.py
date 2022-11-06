questions = [
    "We don't serve strings around here. Are you a string?",
    "What is said on Father's day in the forest?",
    "What makes the sound 'Sis! Boom! Bah!'?"
]

answers = [
    "An exploding sheep.",
    "No, I'm a frayed knot.",
    "Pop! goes the weasel."
]

# So when looking at offsets -1 is the last item in a list
# Notice the pattern the answer to the first one is the last answer
# Then the answer to the next question is the next answer
# Formula Q[i] : A[i + 1]

i = -1
while i < len(questions) - 1:
    print(f'Q: {questions[i]}')
    print(f'A: {answers[i + 1]}\n')
    i += 1
