def audit(placing, value, C):
    counter = 1
    element = placing[0]
    for i in range(len(placing)):
        if placing[i] - element >= value:
            counter += 1
            element = placing[i]
            if counter >= C:
                return True
    return False


def farm():
    angry_cow = 3
    placing = [1, 2, 8, 4, 9]
    placing.sort()
    right = placing[len(placing) - 1]
    left = 1
    ans = 0
    while left < right:
        result = left + (right - left) // 2
        if audit(placing, result, angry_cow):
            ans = result
            left = result + 1
        else:
            right = result
    print("Min: " + str(ans))



if __name__ == "__main__":
    farm()
