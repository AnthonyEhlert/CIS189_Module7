"""
Program: keyword_and_arbitrary_args.py
Author: Tony Ehlert
Last date modified: 2/22/2023

The purpose of this program is call a function that accepts arbitrary arguments of scores as well as keyword arguments
and output a new string containing the keyword argument values and a calculated average of the scores
The input is a series of scores, followed by a first name, last name, and course
The output is a string starting with the full name, then the average score/gps, and finally the course name
"""


def average_scores(*args, **kwargs):
    """
    This function accepts an unknown numbers of GPS scores and calculates the average.
    It also accepts three keyword arguments used to create variables used in a final return string

    :param args: gps scores
    :param kwargs: keyword arguments of first_name, last_name, major
    :return: f string with the calculated average and full name and major/course
    """
    # Use *args for average calculation
    total_of_scores = 0
    num_of_scores = 0
    for num in args:
        total_of_scores += num
        num_of_scores += 1
    average_of_scores = total_of_scores / num_of_scores

    # Use **kwargs to create variables for return string
    for key, value in kwargs.items():
        if (key == "first_name"):
            f_name = value
        if (key == "last_name"):
            l_name = value
        if (key == "major"):
            course = value
    return (f"RESULT= Name: {f_name} {l_name}, Average GPA: {average_of_scores: 3.2f}, Course/Major: {course}")


if __name__ == '__main__':
    print(average_scores(4, 3, 2, 4, first_name='Michelle', last_name='Ruse', major='World_domination'))
    print(average_scores(4, 4, 4, 4, 2, 4, last_name="Ehlert", first_name="Tony", major="Physics"))
    print(average_scores(1, 2, 3, 4, 3, 2, 1, major="Music", first_name="Bruce", last_name="Banner"))
    print(average_scores(4, 4, 3, first_name="Steve", last_name="Rodgers", major="US History"))
