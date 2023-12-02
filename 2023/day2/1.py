def possible(records):
    for record in records.split(';'):
        for color_count in record.strip().split(','):
            split = color_count.strip().split(' ')
            count, color = int(split[0]), split[1]
            if color == 'red' and count > 12:
                return False
            if color == 'green' and count > 13:
                return False
            if color == 'blue' and count > 14:
                return False
    return True

def solve():
    f = open('in.txt', 'r')
    res = 0
    for l in f:
        split = l.split(':')
        game_id, records = split[0].split(' ')[1], split[1]
        if possible(records):
           res += int(game_id)
    return res

print(solve())
