import time
import os

# my introduction again before the quiz starts so it's nothing actually
os.system('cls')
print("\n \n \nHi and WELCOME to my so called QUIZ GAME =.=")
time.sleep(3)
os.system('cls')
name = input("\n \n \nBefore we start... \n \n"
"Please enter your name here: ")
name = name.upper()
age = input("\nand your age is: ")
print()
print(f"Thank you {name}! you can start now after 3 seconds...")
time.sleep(3)
os.system('cls')

# the quiz game
print(f"\n \n \n    Name: {name}")
def quiz_game():
    
    guesses = []
    bonus_points_answer = []
    correct_guesses = 0
    question_num = 1
    print("____________________________________________________________________________")
    print(" \n \nI. MULTIPLE CHOICE: \n")
    
    # for loop for my outputs of QnA
    for key in questions:
        print()
        print(" ", key, "\n")
        
        for i in options[question_num - 1]:
            print("     ", i)
        
        guess = input("     Enter (A, B, C, or D): ")
        print()
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1
    
    print(" \n \nII. IDENTIFICATION(BONUS POINTS ONLY): \n \n")
    time.sleep(2)
    
    # this is for my riddle questions
    for key in riddles:    
        print()
        print(" ", key, "\n")
        
        guess = input("\n Answer: ")
        print()
        guess = guess.upper()
        bonus_points_answer.append(guess)
        
        correct_guesses += check_answer(riddles.get(key), guess)


    result(correct_guesses, guesses, bonus_points_answer)

def check_answer(answer, guess):

    if answer == guess:
        print(" CORRECT!")
        return 1
    else:
        print(" WRONG!")
        return 0
    
# results
def result(correct_guesses, guesses, bonus_points_answer):
    print("\n------------")
    print("RESULTS")
    print("vvvvvvvvv")

    print("\n \nAnswers: ", end ="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()
    print("\nGuesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()
    print("\nRiddles: ", end ="")
    for i in riddles:
        print(riddles.get(i), end=" ")
    print()
    print("\nBONUS POINTS: ", end="")
    for i in bonus_points_answer:
        print(i, end=" ")
    print()

    score = int((correct_guesses%(len(questions) + len(riddles) + 1)))
    print("\nYour score is: "+str(score))
    print()
    print("____________________________________________________________________________\n \n")


# check if still want another one quiz game or nah
def retake_or_not():
    
    response = input("Do you want to play again? (y/n): \n")
    response = response.lower()

    if response == 'y':
        os.system('cls')
        return True
    else:
        return False

# this is for my quiz QnAs
questions = {
"1. Which model doesnt allow defining requirements early in the cycle? ": "B",
"2. Waterfall model is not suitable for? ": "C",
"3. One of the developers myth is: ": "C",
"4. One can choose the Waterfall Model if the project development schedule is tight.": "B",
"5. Which of the following is not the characteristic of software? ": "D",
"6. What is the final result of the requirements analysis and specifications phase? ": "B",
"7. Which of the following is the most important phase of the Software Development Life Cycle (SDLC)? ": "A",
"8. What is a prototype? ": "B",
"9. Which of the following is not a named phase in the software development life cycle? ": "A",
"10. RAD Model was proposed by? ": "A"}
# riddle questions
riddles = {
"Q: The more you code, the more of me there is. I may be gone for now but you can't get rid of me forever. What am I? ": "BUG" ,
"Q: As a developer, you usually get mad at me because I complain a lot, although I'm usually right. What am I? ": "CoMPILER",
"Q: I have a pulse but no heart, a brain but can't think and while I can sleep, I usually don't stay asleep for long? What am I? ": "CPU"}
# quiz multiple choice
options = [
["A. Waterfall","B. Prototyping","C. Iterative waterfall","D. None of the above"],
["A. Small Projects","B. Complex Projects","C. Accommodating change","D. None of the above"],
["A. Changes are easy to accommodate","B. A general statement of objectives from the customer is all that is needed to begin a software project","C. Once a program is written, our work is finished","D. We have all the standards available, that will be sufficient to develop a program"],
["A. True","B. False"],
["A. Software does not wear out","B. Software is flexible","C. Software is not manufactured","D. Software is always correct"],
["A. Data flow diagram","B. SRS Document","C. Coding the project","D. User Manual"],
["A. Requirements analysis","B. Coding","C. Testing","D. Designing"],
["A. Mini model of existing system","B. Mini model of the proposed system","C. Working model of existing system.","D. None of the above"],
["A. Assessment","B. Maintenance","C. Development","D. Testing"],
["A. IBM","B. Motorola","C. Microsoft","D. Lucent Technologies"]]

# exit
quiz_game()

# re take of quiz game or not
while retake_or_not():
    quiz_game()
os.system('cls')
print(f" \n \n \n \n \nThank you! Byeeee {name}! \n \n \n \n \n")