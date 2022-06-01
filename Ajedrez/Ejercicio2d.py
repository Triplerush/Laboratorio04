from interpreter import draw
from chessPictures import *

picture = square.join(square.negative())

picture = picture.horizontalRepeat(4)

draw(picture)