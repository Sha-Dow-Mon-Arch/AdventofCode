from regex import * # need to pip install this library

d = {
    'one': 1,
    '1': 1,
    'two': 2,
    '2': 2,
    'three': 3,
    '3': 3,
    'four': 4,
    '4': 4,
    'five': 5,
    '5': 5,
    'six': 6,
    '6': 6,
    'seven': 7,
    '7': 7,
    'eight': 8,
    '8': 8,
    'nine': 9,
    '9': 9
    }

sam = 0
for i in range(1000):
    w = input()
    pattern = 'one|two|three|four|five|six|seven|eight|nine|1|2|3|4|5|6|7|8|9'
    nums = findall(pattern, w, overlapped = True)
    sam += int(str(d[nums[0]]) + str(d[nums[-1]]))
print(sam)

