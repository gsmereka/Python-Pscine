def NULL_not_found(object: any) -> int:
    recognized_null_types = [None, float("NaN"), 0, '', False]

    if object != object:
        print(f"Cheese: nan <class '{type(object).__name__}'>") 
        return 0  

    for recognized_null in recognized_null_types:
        if object == recognized_null:
            if object is None:
                name = "Nothing"
            elif object == 0:
                name = "Zero"
            elif object == '':
                name = "Empty"
            elif object == False:
                name = "Fake"
            
            print(f"{name} : {type(object).__name__}")
            return 0  

    print("Type not Found")
    return 1  