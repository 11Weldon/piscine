d = [
    ('Hendrix', '1942'),
    ('Allman', '1946'),
    ('King', '1925'),
    ('Clapton', '1942'),
    ('Jonson', '1942'),
    ('Berry', '1942'),
    ('Vaughan', '1942'),
    ('Cooder', '1942'),
    ('Page', '1942'),
    ('Richards', '1942'),
    ('Hammett', '1942'),
    ('Cobain', '1942'),
    ('Garcia', '1942'),
    ('Beck', '1942'),
    ('Santana', '1942'),
    ('Ramone', '1942'),
    ('White', '1942'),
    ('Fruscianta', '1942'),
    ('Thompson', '1942'),
    ('Burton', '1942')
]

def dict_work(dict):
    i =1
    for item in dict:
        print(item[1],':',item[0])



if __name__=='__main__':
    dict_work(d)