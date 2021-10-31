T = int(input())
for t in range(T):
    given_string = [x for x in input("Enter given string")]
    replace_string = [x for x in input("Enter replaced string")]
    given_len = len(given_string)
    replace_len = len(replace_string)
    result = []
    i = 0
    x = 0
    while i != given_len:
        if i + replace_len > given_len:
            for j in range(i, given_len):
                result.append(given_string[j])
            break

        else:
            r = given_string[i:i + replace_len]
            flag = True
            for j in range(replace_len):
                if r[j] != replace_string[j]:
                    flag = False
                    break
            if flag:
                if len(result) == 0:
                    result.append('X')
                elif result[len(result) - 1] != 'X':
                    result.append("X")

                i += replace_len
            else:
                result.append(given_string[i])
                i += 1

    print("".join(result))
