d = {
    'Hendrix'   : '1942',
    'Allman'    : '1946',
    'King'      : '1925',
    'Clapton'   : '1945',
    'Jonson'    : '1911',
    'Berry'     : '1926',
    'Vaughan'   : '1954',
    'Cooder'    : '1947',
    'Page'      : '1942',
    'Richards'  : '1944',
    'Hammett'   : '1943',
    'Cobain'    : '1962',
    'Garcia'    : '1967',
    'Beck'      : '1942',
    'Santana'   : '1944',
    'Ramone'    : '1947',
    'White'     : '1948',
    'Fruscianta': '1975',
    'Thompson'  : '1970',
    'Burton'    : '1949'
}

def my_sort(families: dict):

    d=[v[0] for v in sorted(families.items(), key=lambda k_v: (k_v[1], k_v[0]))]

    for name in d:
        print(name)


if __name__=='__main__':
    my_sort(d)
