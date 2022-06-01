from interpreter import draw
from chessPictures import *

picture = square.join(square.negative())

picture = picture.horizontalRepeat(4)

picture = picture.negative().up(picture)

picture = picture.verticalRepeat(2)

draw(picture)