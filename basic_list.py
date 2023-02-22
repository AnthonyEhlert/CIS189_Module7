"""
Program: basic_list.py
Author: Tony Ehlert
Last date modified: 2/22/2023

The purpose of this program is to have the driver call a function that firsts creates an empty list,
and then calls an inner function the number of times that was passed into the main function.
After getting user input the correct number of times, the list is returned from the function and printed in the driver

The input is a series of numbers provided by the user
The output is a print-out to the console of the list of numbers the user input
"""
def make_list(size_of_list):
    """
    This function accepts an integer number and creates a list containing numbers that were obtained by calling an
    inner function to get user input.  The call to the inner function is made the number of times equal to the integer
    passed in.  Once the correct number of inputs have been obtained and place in the list, the entire list is returned.

    :param size_of_list: integer number indicating not only the size of the list, but also the number of times the
            inner function is to be called
    :return: the list containing the numeric values entered by the user
    """

    def get_input():
        """
        This inner function is called to prompt a user to input a numeric value and then return that value as a string

        :return: string data type representing a numeric value
        """

        # prompt user for input
        user_input = input("Please enter a numeric value between 0-100: ")

        #return user_input to calling function
        return user_input

    # create an empty list
    user_input_list = []

    # create a counter variable to control while loop
    loop_count = 0

    # while loop to call inner function until the correct number of inputs is equal to the number passed in
    while (loop_count < size_of_list):

        # try/except block to catch non-numeric input
        try:
            # convert user input to float type
            user_input_as_float = float(get_input())

            # if in correct range append to list and increment loop count by one, else output incorrect range message
            if (0 <= user_input_as_float <= 100):
                user_input_list.append(user_input_as_float)
                loop_count += 1
            else:
                print("Input out of range!")
        except ValueError:
            print("Invalid input!")

    return user_input_list

if __name__ == '__main__':
    print(make_list(1))
    print(make_list(2))
    print(make_list(3))
    print(make_list(10))
