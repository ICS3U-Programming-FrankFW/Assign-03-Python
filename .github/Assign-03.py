#!/usr/bin/env python3
# Created by: Frankie fox
# Created on: Oct 20, 2022
# This program tells wether or not it is a square or rectangle and does area

import math
import numbers


def main():

    user_width_as_string = input("Enter your width ")
    user_length_as_string = input("Enter your length ")
    print()

    try:
        # This casts a user string to an int
        user_width = int(user_width_as_string)
        user_length = int(user_length_as_string)

        # This checks if it is a rectangle or square
        if user_width == user_length:
            print("This is not a rectangle")
        # This shows it is a rectangle
        elif user_width != user_length:
            print("It is a rectangle ")
            # The exception error
    except Exception:
        print("This is not an integer ")
    finally:
        print("Thanks for playing ")


if __name__ == "__main__":
    main()
