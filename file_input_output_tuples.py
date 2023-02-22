import os as os

"""
Program: file_input_output_tuples.py
Author: Tony Ehlert
Last date modified: 2/22/2023

The purpose of this program is to accept a user's test scores and then write them to a .txt file.  After accepting
multiple users' scores the file that was created is read and printed to the console line by line

The input is a series of test scores
The output is a print-out to the console of the contents of the created .txt file
"""


def write_to_file(student_info_tuple):
    """
    This function accepts a tuple containing a student's name and scores and writes the tuple to the end of a .txt file
    on one line
    :param student_info: tuple containing the student's name and scores
    :return: none
    """

    # open/create the file
    file = open("student_info.txt", "a")

    # write to file
    file.write(str(student_info_tuple) + "\n")

    # close the file
    file.close


def get_student_info(student_name):
    """
    This function accepts a students name as an argument and then prompts the user to input test scores.  It then
    creates a tuple containing the student's name and scores and calls the write_to_file function to write the tuple to
    the end of a .txt file

    :param student_name: string value representing a student's name
    :return: none
    """

    # creation of empty list to hold scores
    user_scores = []

    # creation of sentinel variable
    SENTINEL_VALUE = "stop"

    # creation of variable for user input
    user_input = ""

    # while loop and try/except block used to check for valid number entry
    while (user_input != SENTINEL_VALUE):

        # prompt the user for input (indicating the sentinel value to stop)
        user_input = input(
            f"{student_name}, Please enter a score between 0 and 100. Enter \"{SENTINEL_VALUE}\" to stop.").lower()

        # if statement to check if sentinel value has been entered and break if it has
        if (user_input == SENTINEL_VALUE):
            break

        try:
            # convert user input to float data type
            user_input_as_int = int(user_input)

            # while loop checks for valid range
            while ((user_input_as_int < 0) or (user_input_as_int > 100) and user_input != SENTINEL_VALUE):
                print("Entry out of range! Score must be between 0 and 100")
                user_input = input(
                    f"{student_name}, Please enter a score between 0 and 100. Enter \"{SENTINEL_VALUE}\" to stop.").lower()

                # if statement to check if sentinel value has been entered and break if it has
                if (user_input == SENTINEL_VALUE):
                    break
                user_input_as_int = float(user_input)

            # if statement to check if sentinel value has been entered and break if it has
            if (user_input == SENTINEL_VALUE):
                break

            # add user input to list
            user_scores.append(user_input_as_int)

        except:
            print(f"Cannot convert input to integer. Must be a whole number: \"{user_input}\"")

    # creation of tuple to be appended to file
    student_info_tuple = (student_name, user_scores)

    # call write_to_file function to append tuple to file
    write_to_file(student_info_tuple)


def read_from_file():
    """
    This function reads a .txt file and prints the contents to the console line by line

    :return: none
    """

    # open file for read mode
    with open("student_info.txt", "r") as file:
        # for loop to read file
        # for line in file:
        #     line = line.strip()
        #     print(line)

        # file.read() to read contents of file
        line_read = file.read()
        print(line_read)

    # close the file
    file.close()


if __name__ == "__main__":
    open("student_info.txt", "w").close()
    get_student_info("Tony")
    get_student_info("Steve")
    get_student_info("Bruce")
    get_student_info("Scott")
    read_from_file()
