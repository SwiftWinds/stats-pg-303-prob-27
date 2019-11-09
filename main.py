import random


def rand(start, end, count):
    res = []

    for _ in range(count):
        res.append(random.randint(start, end))

    return res


count = 0
countList = []
randList = rand(0, 99, 100000)
for num in randList:
    count += 1
    if num < 7:
        print(f"Took {count} to get red-green color blindness")
        countList.append(count)
        count = 0
atLeast20 = sum(count >= 20 for count in countList)
print(f"{atLeast20} times of {len(countList)}, took at least 20 times to get red-green blindness")
print(f"So {atLeast20 / len(countList) * 100}%")
