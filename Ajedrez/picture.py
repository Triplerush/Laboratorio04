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
    """ Devuelve una nueva figura poniendo la figura p sobre la
        figura actual """
    return Picture(None)
  
  def horizontalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual al costado
        la cantidad de veces que indique el valor de n """
    return Picture(None)

  def verticalRepeat(self, n):
    return Picture(None)

  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    return Picture(None)

