from interpreter import draw
from chessPictures import *

picture = knight

picture = picture.join(picture.negative())
picture = picture.horizontalMirror().up(picture)

draw(picture)