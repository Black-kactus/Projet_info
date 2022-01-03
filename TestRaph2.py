
from piece import Cavalier, Dame, Fou, Pion, Roi, Tour




a="e2-e4 e7-e5 d1-h5 b8-c6 f1-c4 g8-f6 h5-f7" #echec et mat
b="g2-g4 g7-g5 h2-h4 b7-b5 h4-g5 g8-f6 g5-g6 b5-b4 g6-g7 b4-b3 g7-g8" #promo pion


from time import *
minute=strftime('%H %M %S', gmtime(4242))
duree_minute=minute[:3] + 'h ' + minute[3:6] +'mn ' + minute[6:] + ' s'
print(duree_minute)