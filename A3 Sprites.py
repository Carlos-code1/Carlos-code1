import pygame as py

#Tela
tela=py.display.set_mode((0,0))


Preto=(0,0,0)
Vermelho=(255,0,0)



#Loop Infinito
while True:
	tela.fill((255,255,255))
	tela.blit(lista[cont5],(0,0))
	for event in py.event.get():
		if event.type==py.MOUSEBUTTONDOWN:
			Clique=True
			toquex,toquey=py.mouse.get_pos()
			
		if event.type==py.MOUSEBUTTONUP:
			Clique=False
			
			
					
	
	
	py.display.update()
			