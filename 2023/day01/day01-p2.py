line = input()
ans = 0
digits = {"one": 1, 
          "two": 2,
          "three": 3,
          "four": 4,
          "five": 5,
          "six": 6,
          "seven": 7,
          "eight": 8,
          "nine": 9,
          }
while line:
    prev = [] # to store previous characters
    for c in line: # find first digit
        prev.append(c)
        if c.isdigit():
            first = int(c)
            break
        else:
            for d in digits:
                if d in ''.join(prev):
                    first = digits[d]
                    break
            else: # if no digit found, continue
                continue
            break # otherwise, break
    prev = []
    for c in line[::-1]: # find last digit (search in reverse)
        prev.insert(0, c) # insert at start of list to ensure correct order
        if c.isdigit():
            last = int(c)
            break
        else:
            for d in digits:
                if d in ''.join(prev):
                    last = digits[d]
                    break
            else:
                continue
            break
    ans += 10 * first + last
    line = input()
print(ans)