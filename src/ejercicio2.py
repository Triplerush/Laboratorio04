matriz = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]

#Con dos funciones
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
  
def esUnitaria(m):
  return m[0][0] == 1 and esEscalar(m)

#Con una funcion
def esUnitaria2(m):
  for i in range(len(m)):
    for j in range(len(m[i])):
      if i != j:
        if m[i][j] != 0:
          print(m[i][j])
          return False
      elif m[i][j] != 1:
        print(m[i][j])
        return False
  return True


print(esUnitaria(matriz))
print(esUnitaria2(matriz))