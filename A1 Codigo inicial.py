import pygame as py

#Tela
tela=py.display.set_mode((0,0))

Clique=False

#Loop Infinito
while True:
	for event in py.event.get():
		if event.type==py.MOUSEBUTTONDOWN:
			Clique=True
		if event.type==py.MOUSEBUTTONUP:
			Clique=False
			
	py.draw.rect(tela,(255,0,0),())
			
	py.display.update()
			