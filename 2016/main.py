def day1():
    inp = ''
    with open('day1.txt','r') as f:
        inp = f.readline().split(', ')

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

def day2():
    inp = []
    with open('day2.txt','r') as f:
        for line in f:
            inp.append(list(line))

    x = 1
    y = 1
    keypad = [['1', '2', '3'],
              ['4', '5', '6'],
              ['7', '8', '9']]
    code = ''

    for instructs in inp:
        for i in instructs:
            if i == 'U':
                y -= 1
            elif i == 'D':
                y += 1
            elif i == 'L':
                x -= 1
            elif i == 'R':
                x += 1

            x = max(0, min(2, x))
            y = max(0, min(2, y))

        code += keypad[y][x]

    print('Bathroom code: ' + code)

    x = 0
    y = 2
    keypad = [[None, None, '1', None, None],
              [None, '2',  '3', '4',  None],
              ['5',  '6',  '7', '8',  '9' ],
              [None, 'A',  'B', 'C',  None],
              [None, None, 'D', None, None]]
    code = ''

    for instructs in inp:
        for i in instructs:
            if i == 'U':
                if y > 0:
                    if keypad[y-1][x] != None:
                        y -= 1
            elif i == 'D':
                if y < 4:
                    if keypad[y+1][x] != None:
                        y += 1
            elif i == 'L':
                if x > 0:
                    if keypad[y][x-1] != None:
                        x -= 1
            elif i == 'R':
                if x < 4:
                    if keypad[y][x+1] != None:
                        x += 1

        code += keypad[y][x]

    print('Bathroom code: ' + code)
    
def day3():
    inp = []
    inp2 = []
    with open('day3.txt','r') as f:
        inp2 = [[],[],[]]
        
        for line in f:
            spl = line.split()
            inp.append([int(x) for x in spl])
            inp2[0].append(int(spl[0]))
            inp2[1].append(int(spl[1]))
            inp2[2].append(int(spl[2]))
            
        inp2 = inp2[0] + inp2[1] + inp2[2]
    
    bork = len([None for x in inp if x[0] + x[1] > x[2] and x[1] + x[2] > x[0] and x[0] + x[2] > x[1]])
    print(str(bork) + ' triangles out of ' + str(len(inp)) + ' are possible')
    
    bork = len([None for x in range(0, len(inp2), 3) if inp2[x] + inp2[x+1] > inp2[x+2] and inp2[x+1] + inp2[x+2] > inp2[x+0] and inp2[x+0] + inp2[x+2] > inp2[x+1]])
    print(str(bork) + ' triangles out of ' + str(len(inp)) + ' are possible')

day1()
day2()
day3()
