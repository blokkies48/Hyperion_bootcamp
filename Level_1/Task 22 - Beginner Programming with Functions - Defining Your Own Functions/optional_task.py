# Asking user for input of 2 numbers then the operator
number_1 = float(input("Enter you're first number: "))
number_2 = float(input("Enter you're second number: "))
operator_input = input("Please choose by selecting a number.\n1. add\n2. subtract\n3. multiply\n4. divide\n--")

# https://www.w3schools.com/python/python_lambda.asp got lambda
# lambdas used instead of making a function for each option
# Though I might as well practice my lambdas because they are technically one use functions
if operator_input == "1":
    # x will be the func name and number_1 in the variable passed then the operation on the right is returned 
    add_num_func = lambda number_1 : number_1 + number_2
    print(add_num_func(number_1))

if operator_input == "2":
    subtract_num_func = lambda number_1 : number_1 - number_2
    print(subtract_num_func(number_1))

if operator_input == "3":
    multiply_num_func = lambda number_1 : number_1 * number_2
    print(multiply_num_func(number_1))

if operator_input == "4":
    divide_num_func = lambda number_1 : number_1 / number_2
    print(divide_num_func(number_1))
