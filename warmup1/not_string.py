def not_string(str):
    if str[:3].casefold() == "not":
        return str
    else:
        return "not " + str