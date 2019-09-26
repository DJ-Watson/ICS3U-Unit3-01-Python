#!/usr/bin/env python3

# Created by: DJ Watson
# Created on: September 2019
# This program adds two numbers together


def main():
    # input
    number1 = int(input("type first number (integer): "))
    number2 = int(input("type second number (integer): "))
    # process
    answer = number1 + number2
    # output
    print("")
    print("{} + {} = {}".format(number1, number2, answer))


if __name__ == "__main__":
    main()
