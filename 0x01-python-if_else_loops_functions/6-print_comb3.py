#!/usr/bin/python3
for i in range(i, 10):
    for j in range(1, 10):
        if i < j:
            print("{:d}{:d}".format(i, j),
                    end="\n" if i == 0 and j == 9 else ", ")
