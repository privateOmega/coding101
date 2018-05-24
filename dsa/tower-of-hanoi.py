def tower_of_hanoi(n, source, aux, sink):
    if(n == 1):
        print('Moved Ring %d from %c to %c' % (n, source, sink))
        return
    tower_of_hanoi(n-1, source, sink, aux)
    print('Moved Ring %d from %c to %c' % (n, source, sink))
    tower_of_hanoi(n-1, aux, source, sink)


NUMBER_OF_RINGS = int(input().strip())
tower_of_hanoi(NUMBER_OF_RINGS, 'A', 'B', 'C')
