import unittest
from math_quiz import random_int_between_interval, random_operand, perform_operation


class TestMathGame(unittest.TestCase):

    def test_function_random_int_between_interval(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_int_between_interval(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_function_random_operand_generation(self):
        operand = random_operand()
        self.assertTrue(operand in ["+","-","*"])

    def test_function_perform_operation(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (3, 1, '-', '3 - 1', 2),
                (-1, -1, '-', '-1 - -1', 0),
                (-1, -1, '+', '-1 + -1', -2), 
                (0, 3, '*', '0 * 3', 0),
                (-1, -3, '*', '-1 * -3', 3),
                (2, 3, '*', '2 * 3', 6)
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:

                problem, answer = perform_operation(num1,num2,operator)
                self.assertTrue(problem == expected_problem,f"Problem does not correspond, got {problem}, expected {expected_problem}")
                self.assertTrue(answer == expected_answer, f"Answer does not correspond, got {answer}, expected {expected_answer}")
                pass

    

if __name__ == "__main__":
    unittest.main()
