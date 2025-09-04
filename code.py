def write_name1(x, y):
    t1.write("t1", font=("Arial", 18))


def write_name2(x, y):
    t2.write("t2", font=("Arial", 18))


def write_name3(x, y):
    t3.write("t3", font=("Arial", 18))


t1.onclick(write_name1)
t2.onclick(write_name2)
t3.onclick(write_name3)
