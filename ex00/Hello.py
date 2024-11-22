# -*- coding: utf-8 -*-

import sys
sys.stdout.reconfigure(encoding='utf-8')

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

ft_list[1] = "World"

ft_tuple = ("Hello", "Brazil")

ft_set.remove("tutu!")
city = str("S" + "\u00E3" + "o Paulo")
ft_set.add(city)

ft_dict["Hello"] = "42SP"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)