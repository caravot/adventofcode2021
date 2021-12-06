data = []
file_name = 'input.txt'
maxX1 = 0
maxY1 = 0
maxX2 = 0
maxY2 = 0

with open(file_name) as f:
  for line in f.readlines():
      splits = [l.split(',') for l in line.split(' -> ')]

      print(splits, '====', splits[0])
  f.close()

#print(list(data))