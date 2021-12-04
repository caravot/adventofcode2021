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

print('gamma:', gr)
print('epsilon:', er)
print('power consumption:', pc)

# part 2
print('----------')

odata = data

for x in range(0, first_line_size - 1):
  current_bits = list(int(d[x]) for d in odata)
  most_common = int(sum(current_bits) >= round(len(odata)/2))
  odata = list(f for f in odata if int(f[x]) == most_common)

  #print(x+1, current_bits, most_common)
  #print(odata)

cdata = data

for x in range(0, first_line_size - 1):
  current_bits = list(int(d[x]) for d in cdata)
  one_cnt = current_bits.count(1)
  zero_cnt = current_bits.count(0)
  least_common = 1 if one_cnt < zero_cnt else 0
  cdata = list(f for f in cdata if int(f[x]) == least_common)

  #print(x+1, current_bits, one_cnt, zero_cnt, least_common)
  #print(cdata)
  #print('-----')

  if len(cdata) == 1:
    break

ogr = int(''.join(odata), 2) # oxygen generator rating
csr = int(''.join(cdata), 2)  # CO2 scrubber rating
ls = ogr * csr

print('oxygen generator rating: ', ogr)
print('CO2 scrubber rating: ', csr)
print('life support rating: ', ls)