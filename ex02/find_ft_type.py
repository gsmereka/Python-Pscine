def all_thing_is_obj(object: any) -> int:
    name = type(object).__name__
    print(name + " : " + str(type(object)))
    return 42