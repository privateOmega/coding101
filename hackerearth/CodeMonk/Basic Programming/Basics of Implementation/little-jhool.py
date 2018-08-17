def main():
    binaryString = input().strip()
    luck = False
    count = 1
    for pos, char in enumerate(binaryString):
        if pos == 0 or char == binaryString[pos-1]:
            count += 1
            if count >= 6:
                print('Sorry, sorry!')
                return
        else:
            count = 1
    print('Good luck!')


if __name__ == '__main__':
    main()
