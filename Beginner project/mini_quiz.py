
quiz ={
    1: {
        "question": "What is the smallest planet in the Solar System?",
        "answer": "mercury"
        },
    2: {
        "question": "What planet is closest in size to Earth?",
        "answer": "venus"
    },
    3: {
        "question": "What is the brightest planet in the night sky?",
        "answer": "venus"
        },
    4: {
        "question": "Triton is the largest moon of what planet?",
        "answer": "neptune" 
    },
    5: {
        "question": "True or false? Neptune is larger than Saturn.",
        "answer": "false"
    }
}
def intro():
    print("Lets start quiz on planets!!\nYou will face 5 questions, if the answer is wrong you have 3 tries to clear it.\nSO, are you ready? Lets go!!")
    input("Press any key to start :)\n") # Returns true regardless of any key pressed
    return True

def check_ans(score, tries, choice, guess):
    if quiz[choice]["answer"].lower() == guess.lower():
        print(f"Correct answer!\nYour score is {score+1}\n")
        return True
    else:
        print(f"Wrong answer!\nYour score is {score}")
        print(f"You have {tries-1} tries left.\nLet's try again!!\n")
        return False
intro = intro()
while True:
    score = 0
    for choice in quiz:
        tries = 3
        while (tries > 0):
            question = quiz[choice]["question"]
            print(question)
            guess = input("Enter your answer: ")
            result = check_ans(score, tries, choice, guess)
            if result:
                score += 1
                break
            else:
                tries -= 1
    break
if score == 5:
    print("\n-----------------------------------------------------------------------------------------------")
    print(f"Your score is {score}\nYou answered all the questions correctly, YAAYY!! you got the full scores.")
else:
    print(f"Your final score is {score}")
print("Thanks for playing :)")



