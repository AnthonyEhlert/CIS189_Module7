"""
Program: sort_and_search_list.py
Author: Tony Ehlert
Last date modified: 2/22/2023

The purpose of this program is to pass a list to a function that sorts the list and to a function the searches the list
The input is a list of numbers obtained from user input
The output is a print out of the sorted list and if the value was found
"""


def sort_list(list_to_sort):
    """
    This function simply calls python's built in sort() function using dot notation on the list passed in

    There is no return statement as this function sorts the list that already exists in memory
    and does not create a new list variable to store the sorted list

    :param list_to_sort: list to be sorted
    :return: none
    """
    list_to_sort.sort()


def search_list(list_to_search):
    """
    This function searches the passed in list for the number "17"

    A boolean return variable was used to indicate if the number 17 was found because then the function could
    be used as a control in a loop. Plus if the number was not found a ValueError is raised and is not as easy
    to understand as true/false.

    :param list_to_search: list of numbers to be searched to see if it contains "17"
    :return: Boolean value representing if the value was found or not
    """

    try:
        list_to_search.index(17)
        found = True
    except ValueError:
        found = False
    return found


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

        # return user_input to calling function
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
    user_list = make_list(3)
    sort_list(user_list)
    print(user_list)
    print("17 found? " + str(search_list(user_list)))
