import random

def random_int_between_interval(min:int, max:int):
    """
    Provides a random integer between the numbers 
    provided as parameter (upper and lower limits included).

    Parameters
    ----------

    min : int
        Lower end of the interval

    max : int
        Upper end of the interval

    Returns
    -------
    int
        Random integer between min and max (included).
    """
    try:
        return random.randint(min, max)
    except TypeError:
        print ("Please make sure the provided input numbers are integers")




def random_operand():
    """
    Provides a random operand between addition (+), 
    subtraction (-) and multiplication (*) as a string.

    Returns
    -------
    str
        Random operand from a list of [+, -, *] as a string
    """
    return random.choice(['+', '-', '*'])


def perform_operation(first_number:int, second_number:int, operand:str):
    """
    Will perform the operation between first_number and second_number 
    using the provided operand. 
    If the operand is "+" -> Addition.
    If the operand is "-" -> Subtraction.
    If the operand is "*  -> Multiplication.
    
    Parameters
    ----------
    first_number : int
        First integer of the operation
    
    second_number : int
        Second integer of the operation

    operand : str
        Can only be the characters +, - or *

    Returns
    -------
    string, int
        Performed operation as a string, operation result as an integer

    """

    operation_as_string = f"{first_number} {operand} {second_number}"
    
    if operand == '+':
        answer = first_number + second_number

    elif operand == '-':
        answer = first_number - second_number

    elif operand == "*":
        answer = first_number * second_number

    return operation_as_string, answer

def math_quiz():
    """
    Creates a math quiz made up of 3 questions for the user, based on randomly generated 
    integers and random operands from a list of addition, subtraction and multiplication.
    \n
    The method prompts the user with a mathematical operation and the user must input the 
    correct answer. 
    \n
    At the end of the quiz, prints the total score as the number of correct answers over 
    the total number of questions.
    """
    current_score = 0
    total_number_of_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for questions in range(total_number_of_questions):

        random_number_1 = random_int_between_interval(1, 10)
        random_number_2 = random_int_between_interval(1, 5)
        operand = random_operand()

        problem, answer = perform_operation(random_number_1, random_number_2, operand)

        print(f"\nQuestion: {problem}")

        useranswer = input("Your answer: ")
        try:
            useranswer = int(useranswer)
        except:
            print("Please make sure to input an integer.")

        if useranswer == answer:
            print("Correct! You earned a point.")
            current_score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {current_score}/{total_number_of_questions}")


if __name__ == "__main__":
    math_quiz()
