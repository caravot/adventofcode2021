data = []

pc = 0
gr = 0
er = 0
total = len(data)
half_total = round(total/2)
g_bits = []
e_bits = []

for x in range(0, 5):
  g_bits.append('1' if sum([int(d[x]) for d in data]) > half_total else '0')
  e_bits.append('0' if sum([int(d[x]) for d in data]) > half_total else '1')
  
print('gamma', ''.join(g_bits), int(''.join(g_bits), 2))
print('epsilon', ''.join(e_bits), int(''.join(e_bits), 2))
