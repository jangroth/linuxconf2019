def faculty(n):
    if n == 1:
        return 1
    else:
        return n * faculty(n - 1)


print("Faculty of {} is {}".format(3, faculty(3)))
