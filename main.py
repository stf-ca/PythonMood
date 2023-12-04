# Stefan Boudriau, December 2023.
import random

# Bank of words with corresponding scores
# Example: great is +0.8, amazing is +1.0, bad is -0.8, terrible is -1.0!

bank = {"great": 0.8, "amazing": 1.0, "bad": -0.8, "terrible": -1.0, "happy": 0.6, "wonderful": 0.9, "awful": -0.9,
        "good": 0.7, "fantastic": 0.9, "horrible": -0.9, "sad": -0.6, "excellent": 0.8, "lovely": 0.7, "pretty": 0.3,
        "unpleasant": -0.7, "miserable": -0.7, "positive": 0.6, "delightful": 0.8, "disappointing": -0.7, "amused": 0.6,
        "satisfied": 0.7, "disgusting": -0.8, "content": 0.5, "enjoyable": 0.7, "dreadful": -0.9, "excited": 0.7,
        "moderate": -0.1, "nightmare": -1.0, "peaceful": 0.6, "exciting": 0.7, "repulsive": -0.8, "pleasant": 0.6,
        "alright": 0.2, "relaxed": 0.6, "down": -0.6, "up": 0.4, "beautiful": 0.8, "uplifting": 0.8, "calm": 0.6,
        "repelling": -0.8, "average": 0.2, "upset": -0.6, "n't": -0.1, "hard": -0.3, "easy": 0.4, "strong": 0.2,
        "unhappy": -0.6, "thrilled": 0.8, "relaxing": 0.6, "displeasing": -0.7, "glad": 0.7, "fascinating": 0.8,
        "uninterested": -0.5, "okay": 0.1, "fun": 0.7, "unenthusiastic": -0.5, "merry": 0.7, "joyful": 0.8,
        "boring": -0.6, "cheerful": 0.8, "enchanting": 0.8, "unexciting": -0.5, "stupid": -0.5, "smart": 0.5}
examples = ["Today was okay, I went to work and it was calm. Not too many customers, time passed by slow but it was enjoyable.",
            "Oh goodness, where to start! My car broke down, and I couldn't fix it. What a nightmare!",
            "I went to the waterpark, I hung out with my friends and splashed around, I had so much fun.",
            "I have a lot of things on my mind right now, I've been having a hard time. ",
            "Today I tried painting. I didn't know something could be so fun! It was exciting to see what the other students had created."]

def calculate_score(sentence, word_scores):
    words = sentence.lower().split()
    x = 0.0
    y = 0
    avg2 = 0
    for word in words:
        for match in word_scores:
            if match in word:  # prevent . or , after word removing it from overall score
                x += word_scores[match]
                y += 1
    if len(words) > 0:
        avg = x / len(words)
        if y > 0:
            avg2 = x / y
    else:
        avg = 0.0
    return x, avg, avg2


sentence = ""
while not sentence == "q":
    # kindly greet user and input
    print("Welcome to Emotion Analyzer!"
          "\nThis program puts your thoughts into an algorithm to help you decide if you are feeling happy or not :)\n---")
    print("How is your day going? Please tell me about it, or anything that interests/annoys you."
          "\nPS: be serious! I'm not good with sarcasm, I'm just an algorithm. Please include details!\n")
    print('Example input: "', random.choice(examples), '"')
    sentence = input("Enter a sentence to analyze, or Q to quit: ")

    total_score, average, positivity = calculate_score(sentence, bank)

    if total_score > 0:
        sentiment = "positive"
        if positivity > 0.75:
            sentiment = "deeply positive"
    elif total_score < 0:
        sentiment = "negative"
        if positivity < -0.75:
            sentiment = "deeply negative"
    else:
        sentiment = "neutral"

    confidence = abs(average)  # Confidence is the absolute value of the average score
    z = "neutral :|"
    if positivity > 0:
        z = "happy :) !"
    elif positivity < 0:
        z = "sad :( ..."

    if not sentence == "q":
        print("\nYour sentence sounds", sentiment, "with a confidence of", confidence)
        print("For mood words, the sentence is ", positivity * 100, "% ", z)
        sentence = input("Press enter to continue or type q to quit...")