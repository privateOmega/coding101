def permute(stringList, left, right):
    if left == right:
        print("".join(stringList))
    else:
        for i in range(left, right + 1):
            stringList[left], stringList[i] = stringList[i], stringList[left]
            permute(stringList, left+1, right)
            stringList[left], stringList[i] = stringList[i], stringList[left]


def main():
    string = "ABC"
    length = len(string)
    stringList = list(string)
    permute(stringList, 0, length-1)


if __name__ == '__main__':
    main()
