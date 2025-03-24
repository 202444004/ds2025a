cities = ['Incheon', 'Seoul', 'Incheon', 'Incheon', 'Gwangju']
cities = set(cities)    #set으로 중복 값 제거
cities.add('Incheon')
cities.add('Suwon')     #dictionary, set 순서 개념 없음
print(cities)