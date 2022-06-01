from colors import *
class Picture:
  def __init__(self, img):
    self.img = img;

  def __eq__(self, other):
    return self.img == other.img

  def _invColor(self, color):
    if color not in inverter:
      return color
    return inverter[color]

  def verticalMirror(self):
    figure = self.img
    lines = len(figure) -1 
    pictureVM = [figure[a-1] for a in range(lines,-1,-1)];

    return Picture(pictureVM)

  def horizontalMirror(self):
    figure = self.img
    lines = len(figure)

    pictureHM = [];

    for i in range(0,lines):
      line = [figure[i][a-1] for a in range(lines,-1,-1)];
      newLine = "".join(line)
      pictureHM.append(newLine)

    return Picture(pictureHM)

  def negative(self):
    figure = self.img
    lines = len(figure)
    pictureHM = [];
    
    for i in range(0,lines):
      line = [self._invColor(a) for a in figure[i]];
      newLine = "".join(line)
      pictureHM.append(newLine)

    return Picture(pictureHM)

  def join(self, p):
    if(self.img == None):
      return p
    else:
      x = lambda a, b: a + b
      y = map(x,self.img,p.img)

      return Picture(list(y))

  def up(self, p):
    if(self.img == None):
      return p
    else:
      img = p.img
      y = self.img

      return Picture(img+y)

  def under(self, p):
    debajo = self.img
    encima = p.img
    picture = [];

    lines = len(debajo)
    
    for i in range(0,lines):
      line = '';
      for j in range(0,len(debajo[i])):
        if(encima[i][j] == ' '):
          line += debajo[i][j]
        else:
          line += encima[i][j]

      picture.append(line)

    return Picture(picture)
  
  def horizontalRepeat(self, n):
    picture = self
    pictureNew = Picture(None);

    for i in range(0,n):
      pictureNew = pictureNew.join(picture)

    return pictureNew

  def verticalRepeat(self, n):
    picture = self
    pictureNew = Picture(None);

    for j in range(0,n):
      pictureNew = pictureNew.up(picture)

    return pictureNew

  def rotate(self):
    figure = self.img
    picture = [];

    lines = len(figure)
    
    for i in range(0,len(figure[0])):
      line = '';
      for j in range(0,lines):
        line += figure[j][i]

      picture.append(line)

    return Picture(picture)

