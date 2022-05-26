
matriz1 = [[4,0,0,0],[0,4,0,0],[0,0,4,0],[0,0,0,4]]
matriz2 = [[4,0,2,0],[0,4,0,0],[0,0,4,0],[0,0,0,4]]

def esEscalar(m):
  d = m[0][0]
  for i in range(len(m)):
    for j in range(len(m[i])):
      if i != j:
        if m[i][j] != 0:
          print(m[i][j])
          return False
      elif m[i][j] != d:
        print(m[i][j])
        return False
  return True

print(esEscalar(matriz1))
print(esEscalar(matriz2))

