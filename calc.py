def calculate(s: str) -> int:
    marks = {"+", "-", "*"}
    stack = []                      # stack
    now_num = ""                    # current
    last_mark = "+"                 # set default 
    for ch in s + "+":              # append a meaning-less mark in the end to calculate the last number with last_mark
        if ch.isdigit():
            now_num += ch
        elif ch in marks:
            num = int(now_num)      # calculate the current number read in with last operation mark
            if last_mark == "+":
                stack.append(num)   # if the last operation mark is +, we add the number into stack
            elif last_mark == "-":
                stack.append(-num)  # if the last operation mark is -, we add the negated number into stack
            elif last_mark == "*":  # only push number into stack when meeting + or - for final addition
                stack[-1] *= num    # if * is the last operand, multiply the last element in stack with the current number immediately
            now_num = ""
            last_mark = ch
    return sum(stack)               # do final addition

# Main function that continues to prompt the user to enter a mathematical equation until they wish to exit the program
if __name__ == '__main__':
    programRunning = True
    while programRunning:
        print("Please enter a string corresponding to a mathematical equation: ")
        equation = input()
        if type(equation) == str:
            if equation.lower() == "exit" or equation.lower() == "quit":
                programRunning = False
                print("See you again.")
            else:
                acceptableDigits = [' ', '+', '-', '*', '1', '2', '3', '4', '5', '6', '7', '8', '9']
                validEquation = True
                for index in range(0, len(equation)):
                    if(not equation[index] in acceptableDigits):
                        validEquation = False
                if validEquation:
                    print(f"The result of {equation} is {calculate(equation)}")
                else:
                    print(f"Error: The equation {equation} is not valid.")
        else:
            print("Error: The equation you wish to have computed must be entered in the form of a string.")