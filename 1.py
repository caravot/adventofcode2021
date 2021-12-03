#part 1

last_depth = 0
depth_increased = 0

with open('1_example.txt') as f:
    for line in f:
        current_depth = int(line)
        if last_depth <= current_depth and last_depth > 0:
            depth_increased += 1
        last_depth = current_depth
    f.close()

print("part1: ", depth_increased)
print("------------------")

# part 2
# I cheated :(
last_measure_count = 0
depth_increased = 0

with open('1.txt') as f:
    nums = f.readlines()
    n = list(map(int, nums))
    print(sum(a < b for a, b in zip(n, n[3:])))

    f.close()