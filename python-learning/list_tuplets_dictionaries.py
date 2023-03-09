#!/usr/bin/env python3

# required for get_functions function
import inspect

# defined lists, variables, dictionaries, tuples
lista = [12,15,2,3,4,5]
tup = ('barbara',"haslo15",16)
empty_tup = ()
filled_dictionary = {"sophisticated":"wyszukany", "bleak":"wyblakly", "Abel":"Przemek"}
empty_dict = {}
var_a, var_b, var_c = 21, 21, 53 

# playing with lists
def listy_listy():
    lista.append(121)
    lista.append("a")
    lista[6] = "adam"
    print(lista)
    lista.pop()
    print("popping",lista)
    print("lista[0]",lista[0])
    print("lista[-1]",lista[-1])
    print("len(lista)",len(lista))

# playing with tuples
def tup_tup():
    print(tup[-1])

# playing with for loop
def loop_for():
    tup_len = len(tup)
    # first loop over tupple
    for i in range(tup_len):
        print(tup[i])
    # loop over a range with step 10
    for i in range(0,1010,10):
        print(i/3)

# playing with dictionary
def play_dict(arg1):
    our_iterable = arg1.keys()
    print(our_iterable)

# playing with if condition
def if_condition(a,b):
    if a > b:
        print(a,">",b)
    elif a < b:
        print(a,"<",b)
    else:
        print(a,"=",b)

# list functions from a current modeule
def get_functions():
    functions = []
    for name, obj in inspect.getmembers(inspect.stack()[1][0]):
        if inspect.isfunction(obj):
            functions.append(name)
    return(functions)


# function execution

# if_condition(var_a,var_b)
# play_dict(filled_dictionary)
aaa = get_functions
print(aaa)