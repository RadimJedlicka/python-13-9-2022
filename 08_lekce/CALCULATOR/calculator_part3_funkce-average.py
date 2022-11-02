# TODO importy


# TODO Main function
def calculator():
    """
    Main function
    """
    selection = ("+", "-", "*", "/", "avg", "pow", "quit")
    show_selection(selection)
    # power()
    count_average()


# TODO Selection listing
def show_selection(*args) -> None:
    """
    Description:
    Connects values from *args with .join method.
    Then adds separator before and after arguments.
    
    Example: 
    args = ("a", "b", "C")

    Result:
    ---------
    a | b | C
    ---------
    """    
    joined = ' | '.join(*args)
    separator = '-' * len(joined)
    print(separator, joined, separator, sep="\n")



# TODO Power
def power() -> None:
    """
    Description:
    Takes two inputs as parameters:
    1. input is base
    2. input is exponent
    
    Example:
    input1 = 5
    input2 = 2

    Result:
    5 ** 2 = 25
    """
    input1 = int(input('Base: '))
    input2 = int(input('Exponent: '))
    print(f'{input1} ** {input2} = {input1 ** input2}')


# TODO Average
def count_average() -> None:
    """
    Description:
    Takes values from input and stores them to list.
    Values must be numeric.
    If input '=', func calculates average as sum/lengh of list.
        
    Example:
    numbers = [1, 2, 3, 4, 5]

    Result:
    Average = 3
    """ 
    numbers = list()

    while (value := input('Number: ')) != '=':
        if value.isnumeric():
            numbers.append(int(value))

    result = sum(numbers) / len(numbers)

    print(f'Average is {result}')

# TODO Basic arithmetic operations



calculator()