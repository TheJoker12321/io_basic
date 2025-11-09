with open("mixed_stories.txt", "r") as file:
    lst = []
    for line in file:
        lst.append(line)

    story1 = [i for i in lst if lst.index(i) % 2 == 0]
    story2 = [i for i in lst if lst.index(i) % 2 != 0]
    with open("story1.txt", "a") as f1:
        for i in story1:
            f1.write(i)

    with open("story2.txt", "a") as f2:
        for i in story2:
            f2.write(i)