# part 1
horizontal_position = 0
depth = 0

with open('input.txt') as f:
    for line in f.readlines():
        direction, num = line.split(' ')
        num = int(num)
        
        if direction == 'forward':
            horizontal_position += num
        elif direction == 'down':
            depth += num
        elif direction == 'up':
            depth -= num

print(horizontal_position * depth)
