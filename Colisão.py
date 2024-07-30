import pygame as py

#Tela
tela=py.display.set_mode((0,0))


Preto=(0,0,0)
Vermelho=(255,0,0)


altura=200
comprimento=200
y=600
x=600


cont=0
Clique=False
#Loop Infinito
while True:
	tela.fill((255,255,255))
	for event in py.event.get():
		if event.type==py.MOUSEBUTTONDOWN:
			Clique=True
			toquex,toquey=py.mouse.get_pos()
			
		if event.type==py.MOUSEBUTTONUP:
			Clique=False
	
	if Clique:
		x-=5
	
	
	
	
	
	cima=py.draw.rect(tela,Preto,(x,y-5,comprimento,5))
	baixo=py.draw.rect(tela,Preto,(x,y+201,comprimento,5))
	direita=py.draw.rect(tela,Preto,(x+201,y,5,altura))
	esquerda=py.draw.rect(tela,Preto,(x-5,y,5,altura))
	
	player=py.draw.rect(tela,Vermelho,(x,y,200,200))
	
	obj_ex=py.draw.rect(tela,Vermelho,(100,600,200,200))
	
	
	objetos=[obj_ex]
	while cont<=len(objetos):
			if cima.colliderect(obj_ex):
				y+=5
			if baixo.colliderect(obj_ex):
				y-=5
			if direita.colliderect(obj_ex):
				x-=5
			if esquerda.colliderect(obj_ex):
				x+=5
			cont+=1
	cont=0
			
			
					
	
	
	py.display.update()
			