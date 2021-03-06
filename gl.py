"""
Paula Camila Gonzalez Ortega
18398
"""
import struct

def char(c):
	return struct.pack('=c', c.encode('ascii'))

def word(c):
	return struct.pack('=h', c)

def dword(c):
	return struct.pack('=l', c)

def changecolor(r, g, b):
	return bytes([b, g, r])

BLACK = changecolor(0,0,0)
WHITE = changecolor(255,255,255)
RED = changecolor(255, 0, 0)

class Render(object):
	def __init__(self, width, height):
		self.framebuffer = []
		self.clear_color = BLACK
		self.curr_color = RED
		self.glCreateWindow(width, height)
		#self.glClearColor(r, g, b)
		#self.glclear()

	def glInit():
		#Se inicializan variables
		pass

	def glCreateWindow(self, width, height):
		self.width = width
		self.height = height

	def glViewPort(self, x, y, width, height):
		self.vpWidth = width
		self.vpHeight = height
		self.vpx = x
		self.vpy = y

	def glclear(self):
		self.framebuffer = [
		[self.clear_color for x in range(self.width)]
		for y in range(self.height)
		]

	def glClearColor(self, r, g, b):
		red = round(r*255)
		green = round(g*255)
		blue = round(g*255)
		self.clear_color = changecolor(red, green, blue)

	def glVertex(self, x, y):
		new_x = round((x+1)*(self.vpWidth/2)+self.vpx)
		new_y = round((y+1)*(self.vpHeight/2)+self.vpy)
		#Linea 59 y 58 basadas en https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glViewport.xhtml
		self.framebuffer[new_y][new_x] = self.curr_color
	
	def glColor(self, r=1, g=1, b=1):
		red = round(r*255)
		green = round(g*255)
		blue = round(g*255)
		self.curr_color = changecolor(red, green, blue)

	def glLinePoint(self, x, y):
		self.framebuffer[y][x] = self.curr_color

	#Funciones para aplicar la ecuacion de la recta y dibujar lineas
	def glLine(self, x0, y0, x1, y1):
		dx = abs(x1 - x0)
		dy = abs(y1 - y0)

		steep = dy > dx

		if steep:
			x0, y0 = y0, x0
			x1, y1 = y1, x1
		if x0 > x1:
		 	x0, x1 = x1, x0
		 	y0, y1 = y1, y0

		dx = abs(x1 - x0)
		dy = abs(y1 - y0)

		offset = 0
		limit = dx
		
		y = y0
		for x in range(x0, x1):
			if steep:
				self.glLinePoint(y, x)
			else:
				self.glLinePoint(x, y)
			
			offset += dy*2
			if offset >= limit:
				y += 1 if y0 < y1 else -1
				limit += 2*dx
	
	def finish(self, filename):
		f = open(filename, 'bw')

		# file header
		f.write(char('B'))
		f.write(char('M'))
		f.write(dword(14 + 40 + self.width * self.height * 3))
		f.write(dword(0))
		f.write(dword(14 + 40))

		# image header
		f.write(dword(40))
		f.write(dword(self.width))
		f.write(dword(self.height))
		f.write(word(1))
		f.write(word(24))
		f.write(dword(0))
		f.write(dword(self.width * self.height * 3))
		f.write(dword(0))
		f.write(dword(0))
		f.write(dword(0))
		f.write(dword(0))

		# pixel data
		for x in range(self.height):
			for y in range(self.width):
				f.write(self.framebuffer[x][y])


		f.close()

	#Funcion para dibujar un poly de varios lados
	def drawPolygon(self, points):
		n = len(points)
		for i in range(n):
			v0 = points[i]
			v1 = points[(i+1)%n]
			self.glLine(v0[0], v0[1], v1[0], v1[1])

	#Funciones para checkear que un punto este dentro del poligono 
	def inside(self, poly, x, y):
		#Algoritmo Even–odd rule basado en https://en.wikipedia.org/wiki/Even%E2%80%93odd_rule
		# Primero se verifica que la Y del punto esté entre las y de cada par de vértices del poly
		# Luego se calcula la x con la coordenada y de la línea que se hace con cada par de vértices del poly
		# y verfica si esa x es mayor que la X del punto
		# Si cumple ambas condiciones cambia el valor boolean de c
		# Finalmente tal como lo dice el nombre del algoritmo "Even–odd rule", si se cumplen estas condiciones un número par de veces está afuera y si es impar está dentro del poly y se puede dibujar
		num = len(poly)
		i = 0
		j = num - 1
		c = False
		for i in range(num):
			if ((poly[i][1] > y) != (poly[j][1] > y)) and (x < poly[i][0] + (poly[j][0] - poly[i][0]) * (y - poly[i][1]) / (poly[j][1] - poly[i][1])):
				c = not c

			j = i

		return c

	def filling(self, poly):
	    arr_x = []
	    arr_y = []
	    puntos = []
	    n = len(poly)
	    for i in range(n):
	    	v0 = poly[i]
	    	v1 = poly[(i+1)%n]
	    	puntos.append(v0[0])
	    	puntos.append(v0[1])
	    	puntos.append(v1[0])
	    	puntos.append(v1[1])

	    for i in puntos:
	    	#se dividen las coordenadas de x y y segun la posicion en la lista
	    	position = puntos.index(i)
	    	if position%2 == 0:
	    		arr_x.append(i)
	    	else:
	    		arr_y.append(i)
	    xmax = max(arr_x) 
	    ymax = max(arr_y)
	    xmin = min(arr_x) 
	    ymin = min(arr_y)  
	    for x in range(xmin, xmax):
	    	for y in range(ymin, ymax):
	    		if self.inside(poly,x,y):
	    			#si el punto esta dentro del poligono se dibuja el punto
	    			self.glLinePoint(x,y)

