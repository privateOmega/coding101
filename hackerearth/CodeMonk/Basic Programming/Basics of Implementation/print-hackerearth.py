def main():
    length = int(input())
    string = input().strip()
    dictHackerEarth = {char: 'hackerearth'.count(
        char) for char in set('hackerearth')}
    dictString = {char: string.count(char) for char in set(string)}
    countArray = []
    for key in dictHackerEarth:
        if key in dictString.keys():
            countArray.append(dictString[key] // dictHackerEarth[key])
        else:
            print(0)
            return
    print(min(countArray))


if __name__ == '__main__':
    main()
