def duplicate_city(cities):
    result_city = []
    s = set()

    for city in cities:
        l1 = len(s)
        s.add(city)
        l2 = len(s)
        if l1 == l2:
            result_city.append(city)
    return result_city




cities = ['Incheon', 'Seoul', 'Incheon', 'Incheon', 'Gwangju']
#cities = set(cities)    #set으로 중복 값 제거
#cities.add('Incheon')
#cities.add('Suwon')     #dictionary, set 순서 개념 없음
cities.append('Incheon')
cities.append('Suwon')
cities.append('Seoul')
print(set(duplicate_city(cities)))