
lst =[['HAS',23.43],['HIM',54.23],['SHE',23.43],['HE',31],['HER',31]]
# for _ in range(int(input())):
#     name = input()
#     score = float(input())
#     lst.append([name ,score])
sorted_score=sorted(list(set(i[1] for i in lst)))

second_lowest=sorted_score[1]
lst1=[]
for i in lst:
    if i[1]==second_lowest:
      lst1.append(i[0])
for j in sorted(lst1):
    print(j)
    #
    # n = int(input())
    # student_marks = {}
    # for _ in range(n):
    #     name, *line = input().split()
    #     scores = list(map(float, line))
    #     student_marks[name] = scores
    # query_name = input()
    #
    # for i, j in student_marks.items():
    #     if (i == query_name):
    #         s = 0
    #         for x in j:
    #             s = s + x
    #         avg = s / len(j)
    #         print("%.2f" % avg)

    # select
    # distinct
    # city
    # from station
    #
    # where
    # mod(id, 2) = 0;

    # select
    # city, length(city)
    # from station order
    #
    # by
    # length(city)
    # asc, city
    # limit
    # 1;
    # select
    # city, length(city)
    # from station order
    #
    # by
    # length(city)
    # desc, city
    # limit
    # 1;

    # select
    # city
    # from station
    #
    # where
    # left(city, 1) in ('a', 'i', 'e', 'o', 'u');