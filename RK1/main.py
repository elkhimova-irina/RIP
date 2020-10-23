from operator import itemgetter

class street:
    """Улица"""
    def __init__(self, id, name):
        self.id = id
        self.name = name


class house:
    """Дом"""
    def __init__(self,id,number,owner, salary, street_id):
        self.id = id
        self.number = number
        self.owner = owner
        self.salary = salary
        self.street_id = street_id

class streho:
    """'Дома улицы' для реализации связи многие-ко-многим"""
    def __init__(self, house_id,street_id):
        self.house_id = house_id
        self.street_id = street_id

#Улицы
str =[
    street(1,'Александры Монаховой'),
    street(2,'Чертановская'),
    street(3,'Лунных кошек'),
    street(4,'Дорожная'),
    street(5,'Привольная'),
]


#Дома
hss =[
    house(1,94,'Елизарова',190000,1),
    house(2,13,'Арустнова',25000,1),
    house(3,26,'Шумилина',13000,2),
    house(4,7,'Алинова',100000,2),
    house(5,65,'Гончаров',189000,4),
]

str_hss =[
    streho(1,1),
    streho(1,2),
    streho(2,5),
    streho(3,2),
    streho(3,3),
    streho(4,1),
    streho(4,2),
    streho(4,4),
    streho(5,1),
    streho(5,2),
    streho(5,5),
]

def main():
    """Основная функция"""

    #Соединение данных  один-ко-многим
    one_to_many =[(h.owner, h.salary, s.name)
                  for s in str
                  for h in hss
                  if h.street_id == s.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(s.name, sh.house_id, sh.street_id)
                         for s in str
                         for sh in str_hss
                         if s.id == sh.street_id]

    many_to_many = [(h.owner, h.salary, street_name)
                    for street_name, street_id, house_id in many_to_many_temp
                    for h in hss if h.id == house_id]

    print('Задание В1')
    res_11 = list(filter(lambda x: x[0].startswith('А'),one_to_many))
    print(res_11)

    print('\nЗадание B2')
    res_12_unsorted = []

    for s in str:

        s_house = list(filter(lambda i: i[2]==s.name, one_to_many))
        if len(s_house) > 0:
            s_salary = [salary for _,salary,_ in s_house]
            s_salary_min = min(s_salary)
            res_12_unsorted.append((s.name, s_salary_min))


    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=False)
    print(res_12)

    print('\nЗадание B3')
    res_13 = sorted(many_to_many, key=itemgetter(0))
    print(res_13)

if __name__ == '__main__':
    main()



