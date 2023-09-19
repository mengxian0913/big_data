import pandas

grades = {
    "name" : ["AA", "BB", "CC"],
    "math" : [1, 2, 3],
    "chinese" : [1, 2, 3],
}

grades = pandas.DataFrame(grades)

print(grades)
