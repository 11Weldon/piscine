import sys

states = {
    "Oregon" : "OR",
    "Alabama" : "Al",
    "New Jersey" : "NJ",
    "Colorado" : "CO"
}

capital_cities = {
    "OR" : "Salem",
    "Al" : "Montgomery",
    "NJ" : "Trenton",
    "CO" : "Denver"
}
a1="New jersey, Tren ton, NewJersey, Trenton, sAlem, oregon, denver"
# a1='Trenton'
# Ключ нужного значения
def dicts(dict,need):
    for key, value in dict.items():
        if value.lower() == need.lower():
            return(key)

def capital_or_not(st,cc,string):
    a=0
    for key,value in cc.items():
        if string.lower() == value.lower():
            for k,v in st.items():
                if key == v:

                    print(k,"is capital of",value)
                    a+=1

    for key in st.keys():
        if string.lower() == key.lower():
            print(key,"is capital of",cc[st[key]])
            a+=1
    if a == 0:
        print(string,"is neither a capital city nor a state")

def all_in(string):

    for words in string:
        print(words)
        capital_or_not(states,capital_cities,words)


if __name__=='__main__':
    print(sys.argv[1:])
    all_in(sys.argv[1:])

