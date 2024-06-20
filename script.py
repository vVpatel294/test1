#!/usr/bin/env python3

"""
Script to prompt user for numbers and calculate the average.
Written by Vidhi K. Patel.
"""

def main():
    numbers = []
    while True:
        user_input = input("Enter a number (or press Enter to finish): ")
        if user_input == "":
            break
        if user_input.isnumeric():
            numbers.append(float(user_input))
    
    if numbers:
        average = sum(numbers) / len(numbers)
        print(f"The average is {average}")
    else:
        print("No valid numbers entered.")

if __name__ == "__main__":
    main()
