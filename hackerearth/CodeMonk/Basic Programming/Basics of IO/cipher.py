def main():
    unencrypedString = input().strip()
    encryptionKey = int(input())
    encrypedString = ''
    for char in unencrypedString:
        if char.isalnum():
            if char.isdigit():
                encrypedString += str((int(char) + encryptionKey) % 10)
            elif char.isupper():
                encrypedString += chr(((ord(char) - ord('A') +
                                        encryptionKey) % 26) + ord('A'))
            elif char.islower():
                encrypedString += chr(((ord(char) - ord('a') +
                                        encryptionKey) % 26) + ord('a'))
        else:
            encrypedString += char
    print(encrypedString)


if __name__ == '__main__':
    main()
