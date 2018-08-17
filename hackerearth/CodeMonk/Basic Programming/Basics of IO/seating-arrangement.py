def calculate_seat(addOperation, seatNumber, operand, seatType):
    if addOperation:
        return '{} {}'.format(seatNumber + operand, seatType)
    else:
        return '{} {}'.format(seatNumber - operand, seatType)


def get_seating_arrangement(seatNumber):
    workableValue = seatNumber % 12
    switcher = {
        0: calculate_seat(False, seatNumber, 11, 'WS'),
        1: calculate_seat(True, seatNumber, 11, 'WS'),
        2: calculate_seat(True, seatNumber, 9, 'MS'),
        3: calculate_seat(True, seatNumber, 7, 'AS'),
        4: calculate_seat(True, seatNumber, 5, 'AS'),
        5: calculate_seat(True, seatNumber, 3, 'MS'),
        6: calculate_seat(True, seatNumber, 1, 'WS'),
        7: calculate_seat(False, seatNumber, 1, 'WS'),
        8: calculate_seat(False, seatNumber, 3, 'MS'),
        9: calculate_seat(False, seatNumber, 5, 'AS'),
        10: calculate_seat(False, seatNumber, 7, 'AS'),
        11: calculate_seat(False, seatNumber, 9, 'MS')
    }
    return switcher.get(workableValue, lambda: 'Invalid')


def main():
    noOfTestCases = int(input())
    testCases = []
    if noOfTestCases < 1:
        return
    for iterator in range(noOfTestCases):
        testCases.append(int(input()))
    for iterator in range(noOfTestCases):
        print(get_seating_arrangement(testCases[iterator]))


if __name__ == '__main__':
    main()

""" 
Akash and Vishal are quite fond of travelling. They mostly travel by railways. They were travelling in a train one day and they got interested in the seating arrangement of their compartment. The compartment looked something like 

So they got interested to know the seat number facing them and the seat type facing them. The seats are denoted as follows : 

Window Seat : WS
Middle Seat : MS
Aisle Seat : AS

You will be given a seat number, find out the seat number facing you and the seat type, i.e. WS, MS or AS.

INPUT
First line of input will consist of a single integer T denoting number of test-cases. Each test-case consists of a single integer N denoting the seat-number.

OUTPUT
For each test case, print the facing seat-number and the seat-type, separated by a single space in a new line. """