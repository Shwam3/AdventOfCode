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

import collections
def day4():
    inp = []
    with open('day4.txt','r') as f:
        for line in f:
            line = line.rstrip()
            inp.append(line.replace('-','$',line.count('-')-1).split('-'))

    count = 0
    for line in inp:
        common = collections.Counter(''.join(sorted(line[0].replace('$','')))).most_common()
        common = list(sorted(common, key=lambda x: (-x[1], x[0])))[:5]
        common = ''.join([x[0] for x in common])

        if common in line[1]:
            num = int(line[1][0:line[1].find('[')])
            count += num

            name = line[0]
            for i in range(num):
                name = ''.join([(' ' if x == '$' or x == ' ' else ('a' if x == 'z' else chr(ord(x)+1))) for x in name])
            if 'northpole' in name:
                print('Storage room sector ID: ' + str(num))

    print('The arbitrarily required sum is ' + str(count))

import hashlib
def day5():
    inp = 'ffykfhsq'
    index = 0
    hash = inp
    password = ''

    while len(password) < 8:
        while hash[:5] != '00000':
            hash = hashlib.md5((inp + str(index)).encode('utf-8')).hexdigest()
            index += 1

        password += hash[5]
        index += 1
        hash = inp

    print('Password 1: ' + password)

    password = ['_','_','_','_','_','_','_','_']
    index = 0
    hash = inp
    while '_' in password:
        while hash[:5] != '00000':
            hash = hashlib.md5((inp + str(index)).encode('utf-8')).hexdigest()
            index += 1

        if int(hash[5],16) < 8:
            if password[int(hash[5],16)] == '_':
                password[int(hash[5],16)] = hash[6]

        hash = inp
        index += 1

    print('Password 2: ' + ''.join(password))

def day6():
    inp = ['','','','','','','','']
    with open('day6.txt','r') as f:
        for line in f:
            line = line.rstrip()
            for i in range(len(line)):
                inp[i] = (inp[i] if len(inp) > i else '') + line[i]

    code1 = ''.join([collections.Counter(x).most_common()[0][0] for x in inp])
    code2 = ''.join([collections.Counter(x).most_common()[-1][0] for x in inp])

    print('Message 1: ' + code1)
    print('Message 2: ' + code2)

def day7():
    inp = []
    with open('day7.txt','r') as f:
        for line in f:
            inp.append(line.rstrip().replace(']','[').split('['))

    tls = 0
    ssl = 0
    for line in inp:
        hyperABBA = False
        hyperABA = False
        superABBA = False
        superABA = False
        ABA = []

        for i in line[::2]:
            if len(i) > 3:
                for offset in range(len(i)-3):
                    if i[offset] == i[offset+3] and i[offset+1] == i[offset+2] and i[offset] != i[offset+1]:
                        superABBA = True
                        break

            if len(i) > 2:
                for offset in range(len(i)-2):
                    if i[offset] == i[offset+2] and i[offset] != i[offset+1]:
                        ABA.append((i[offset],i[offset+1]))
                        superABA = True

        for i in line[1::2]:
            if len(i) > 3:
                for offset in range(len(i)-3):
                    if i[offset] == i[offset+3] and i[offset+1] == i[offset+2] and i[offset] != i[offset+1]:
                        hyperABBA = True
                        break

            if len(i) > 2:
                for offset in range(len(i)-2):
                    if i[offset] == i[offset+2] and i[offset] != i[offset+1]:
                        if (i[offset+1],i[offset]) in ABA:
                            hyperABA = True
                            break

        if not hyperABBA and superABBA:
            tls += 1
        if hyperABA:
            ssl += 1

    print('TLS supporting addresses: ' + str(tls))
    print('SSL supporting addresses: ' + str(ssl))

def day8():
    inp = []
    with open('day8.txt','r') as f:
        for line in f:
            inp.append(line.rstrip())

    screen = []
    for y in range(6):
        screen.append(' '*50)

    for line in inp:
        if line[:4] == 'rect':
            w = int(line[5:line.find('x')])
            h = int(line[line.find('x')+1:])

            for y in range(h):
                screen[y] = screen[y].replace(' ','#',w)

        elif line[:13] == 'rotate row y=':
            nums = line[13:].split(' by ')
            row = int(nums[0])
            shift = int(nums[1])

            screen[row] = (screen[row][-shift:] + screen[row])[:50]

        elif line[:16] == 'rotate column x=':
            nums = line[16:].split(' by ')
            col = int(nums[0])
            shift = int(nums[1])

            dat = ''
            for y in range(6):
                dat += screen[y][col]

            dat = (dat[-shift:] + dat)[:50]

            for y in range(6):
                screen[y] = screen[y][:col] + dat[y] + screen[y][col+1:]

    lit = 0
    for x in screen:
        lit += len(x.replace(' ',''))

    print(str(lit) + ' pixels are lit')
    print('The screen:')
    [print('>  ' + x) for x in screen]

day1()
day2()
day3()
day4()
#day5()
day6()
day7()
day8()
