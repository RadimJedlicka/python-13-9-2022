# TODO importy


# TODO Main function
def calculator():
    """
    Main function
    """
    selection = ("+", "-", "*", "/", "avg", "pow", "quit")
    show_selection(selection)


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


# TODO Average


# TODO Basic arithmetic operations



calculator()