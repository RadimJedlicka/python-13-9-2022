# TODO importy


# TODO Main function
def calculator():
    """
    Main function
    """
    selection = ("+", "-", "*", "/", "avg", "pow", "quit")
    show_selection(selection)
    power()


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


# TODO Basic arithmetic operations



calculator()