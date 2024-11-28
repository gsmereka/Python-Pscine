def NULL_not_found(object: any):
    recognized_null_types = [None, float("NaN"), 0, '', False]

    if object != object:
        print(f"Cheese: nan <class '{type(object).__name__}'>")
        return "1\n"

    for recognized_null in recognized_null_types:
        if object == recognized_null:
            if object is None:
                name = "Nothing"
            elif object is False:
                name = "Fake"
            elif object == 0:
                name = "Zero"
            elif object == '':
                name = "Empty"
            print(f"{name} : {object} {type(object)}")
            return "1\n"

    print("Type not Found")
    return "1\n"
