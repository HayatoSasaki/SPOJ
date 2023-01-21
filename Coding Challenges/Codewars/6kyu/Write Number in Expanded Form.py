def expanded_form(num):
    return " + ".join([f'{number}{"0" * (len(str(num))-index-1)}' for index,number in enumerate(str(num)) if number != "0"])
