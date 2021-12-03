data = []
first_line_size = 0

with open('3.txt') as f:
  data = f.readlines()
  f.close()

first_line_size = len(data[0])

pc = 0
gr = 0
er = 0
total = len(data)
half_total = round(total/2)
g_bits = []
e_bits = []

for x in range(0, first_line_size - 1):
  g_bits.append('1' if sum([int(d[x]) for d in data]) > half_total else '0')
  e_bits.append('0' if sum([int(d[x]) for d in data]) > half_total else '1')

gr = int(''.join(g_bits), 2)
er = int(''.join(e_bits), 2)
pc = gr * er

print('gamma', gr)
print('epsilon', er)
print('power consumption', pc)

# part 2
print('----------')