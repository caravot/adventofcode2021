last_depth = 0
depth_increased = 0

with open('1.txt') as f:
    for line in f:
        current_depth = int(line)
        if last_depth <= current_depth and last_depth > 0:
            depth_increased += 1
        last_depth = current_depth

print(depth_increased)