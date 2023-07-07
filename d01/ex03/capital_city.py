import  sys
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
def magic(st,cc):
    string = sys.argv[1]
    try:
        print(cc[states[string]])
    except:
        print('Unknown state')

if __name__=='__main__':
    magic(states,capital_cities)