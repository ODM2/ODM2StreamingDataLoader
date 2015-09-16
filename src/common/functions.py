
def searchDict(obj, key, lvl=0):
    # Base case: key is in the first level of dictionary.
    if key in obj:
        return obj[key]
    # Key is not in the first level of the dictionary.
    # Loop through keys to find nested dictionaries.
    for k,v in obj.items():
        # Recurse if a dictionary is found.
        if isinstance(v, dict):
            item = searchDict(v, key, lvl+1)
            if item is not None:
                return item
    # If we're done looking and key still has not
    # been found, then raise a KeyError
    if lvl == 0:
        raise KeyError(key)

