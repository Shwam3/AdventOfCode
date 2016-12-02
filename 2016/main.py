def day1():
    inp = ''
    with open('day1.txt','r') as f:
        inp = f[0].split(', ')

    locs = []
    part2loc = None

    x = 0
    y = 0
    dir = 0 #0 north, 1 e, 2 s, 3 w

    for i in inp:
        if i[0] == 'R':
            dir += 1
        elif i[0] == 'L':
            dir -= 1

        if dir < 0:
            dir = 3
        else:
            dir = dir % 4

        dist = int(i[1:])
        if dir == 0:
            if not part2loc:
                for ys in range(0, dist):
                    if (x,y+ys) in locs:
                        part2loc = (x,y+ys)
                        break
                    locs.append((x,y+ys))
            y += dist
        elif dir == 1:
            if not part2loc:
                for xs in range(0, dist):
                    if (x+xs,y) in locs:
                        part2loc = (x+xs,y)
                        break
                    locs.append((x+xs,y))
            x += dist
        elif dir == 2:
            if not part2loc:
                for ys in range(0, dist):
                    if (x,y-ys) in locs:
                        part2loc = (x,y-ys)
                        break
                    locs.append((x,y-ys))
            y -= dist
        elif dir == 3:
            if not part2loc:
                for xs in range(0, dist):
                    if (x-xs,y) in locs:
                        part2loc = (x-xs,y)
                        break
                    locs.append((x-xs,y))
            x -= dist

    print('Bunny HQ is ' + str(abs(x) + abs(y)) + ' blocks away')

    print('Bunny HQ is ' + str(abs(part2loc[0]) + abs(part2loc[1])) + ' blocks away')

day1()
