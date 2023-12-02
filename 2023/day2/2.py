def power(records):
    red_max, green_max, blue_max = 0, 0, 0
    for record in records.split(';'):
        for color_count in record.strip().split(','):
            split = color_count.strip().split(' ')
            count, color = int(split[0]), split[1]
            if color == 'red':
                red_max = max(red_max, count)
            if color == 'green':
                green_max = max(green_max, count)
            if color == 'blue':
                blue_max = max(blue_max, count)
    return red_max * green_max * blue_max

def solve():
    f = open('in.txt', 'r')
    res = 0
    for l in f:
        split = l.split(':')
        game_id, records = split[0].split(' ')[1], split[1]
        res += power(records)   
    return res

print(solve())
