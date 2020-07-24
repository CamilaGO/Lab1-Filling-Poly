"""
Paula Camila Gonzalez Ortega
18398
"""
from gl import Render

width = 1000
height = 1000

bitmap = Render(width, height) 

bitmap.glClearColor(0, 0, 0) #este es background color
bitmap.glclear()
bitmap.glColor(1, 0.5, 0) #estos colores son los que se usaran para pintar 

#POLY 1
poly = [(165, 380), (185, 360), 
(185, 360), (180, 330),
(180, 330), (207, 345),
(207, 345), (233, 330), 
(233, 330), (230, 360),
(230, 360), (250, 380),
(250, 380), (220, 385),
(220, 385), (205, 410),
(205, 410), (193, 383),
(193, 383), (165, 380)]
bitmap.drawPolygon(poly)
bitmap.filling(poly)

#POLY 2
bitmap.glColor(0.5, 0, 1)
poly = [(321, 335), (288, 286),
(288, 286), (339, 251),
(339, 251), (374, 302),
(374, 302), (321, 335)]
bitmap.drawPolygon(poly)
bitmap.filling(poly)

#POLY 3
bitmap.glColor(0, 0.5, 0.5)
poly = [(377, 249), (411, 197),
(411, 197), (436, 249),
(436, 249), (377, 249)]
bitmap.drawPolygon(poly)
bitmap.filling(poly)

#POLY 4
bitmap.glColor(1, 1, 1)
poly = [(413, 177), (448, 159),
(448, 159), (502, 88),
(502, 88), (553, 53),
(553, 53), (535, 36),
(535, 36), (676, 37),
(676, 37), (660, 52),
(660, 52), (750, 145),
(750, 145), (761, 179),
(761, 179), (672, 192),
(672, 192), (659, 214),
(659, 214), (615, 214),
(615, 214), (632, 230),
(632, 230), (580, 230),
(580, 230), (597, 215),
(597, 215), (552, 214),
(552, 214), (517, 144),
(517, 144), (466, 180),
(413, 177), (466, 180)]
bitmap.drawPolygon(poly)
bitmap.filling(poly)

#POLY 5
bitmap.glColor(0, 0, 0)
poly = [(682, 175), (708, 120),
(708, 120), (735, 148),
(735, 148), (739, 170),
(739, 170), (682, 175)]
bitmap.drawPolygon(poly)
bitmap.filling(poly)


bitmap.finish('outfilled.bmp')