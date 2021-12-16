from itertools import zip_longest

# Source: https://stackoverflow.com/questions/4998427/how-to-group-elements-in-python-by-n-elements

def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)