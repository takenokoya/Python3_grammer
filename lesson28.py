# pythonでは関数のドキュメントは関数内に"""に書く
def example_func(param1, param2):
    """Example function with types documented in the docstring.
    :param param1: The First Params (int)
    :param param2: The Second Params (str)
    :return: The Return Value (bool). True for success. False otherwise.
    """
    print(param1)
    print(param2)
    return True


# documentの内容を表示
print(example_func.__doc__)
help(example_func)

