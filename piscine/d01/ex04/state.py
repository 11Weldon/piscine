import sys

states = {
    "Oregon" : "OR",
    "Alabama" : "Al",
    "New Jersey" : "NJ",
    "Colorado" : "CO"
}

capital_cities = {
    "OR" : "Salem",
    "Al" : "Mont",
    "NJ" : "TRenton",
    "CO" : "Denver"
}
def dicts(dict,need):
    for key, value in dict.items():
        if value == need:
            return(key)
def magic(st,cc):
    user_input=sys.argv[1]


    try:
        print(dicts(st,dicts(cc, user_input)))
    except:
        print('Unknown state')

if __name__=='__main__':
    magic(states,capital_cities)
