# command_line_functions.py
# @author Justin Noddell


# define CLI symbols for various messages
user_input_id = "> "                # user input identifier
info_msg_id = "-- "                 # info message identifier
list_id = " - "                     # list item symbol
warning_id = "*** WARNING *** "     # warning message 

# greet_user
# params        None
# returns:      None
# purpose:      greet the user with a message
def greet_user() -> None:

    print("\n\n*************************")
    print("******** WELCOME ********")
    print("*************************\n")

# api_error
# params        None
# returns:      None
# purpose:      alert user a fatal error has occured
def api_error() -> None:

    print(warning_id, "One of the following errors has occured:")
    print(info_msg_id, "The given API Key is either invalid or it has reached the daily limit of API calls.")
    print(info_msg_id, "There is no internet connection / Spoonacular is unavailable.")
    print("\nPlease fix the issue(s) before attempting to run the program again.")

# recipes_exhausted
# params        None
# returns:      None
# purpose:      alert user a fatal error has occured
def recipes_exhausted() -> None:

    print(info_msg_id, "Recipes have been exhausted...\n")

# confirm
# params:       msg: str -> the message to be displayed
# returns:      True/False
# purpose:      confirm user selection; return T/F based on action confirmed or not
def confirm(msg: str) -> bool:

    while True:

        response = input("\n" + msg + " (Y/N):\n" + user_input_id)
        response = str(response).lower()
        print()

        if response == "y" or response == "yes":
            return True
        elif response == "n" or response == "no":
            return False
        else:
            print("\nInvalid input, please re-enter.\n")

# pause
# params        None
# returns:      None
# purpose:      keep terminal open to allow time to view screen
def pause() -> None:

    input("\npress any key to continue...")