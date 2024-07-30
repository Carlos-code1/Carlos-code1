import pygame as py

#Tela
tela=py.display.set_mode((0,0))


Preto=(0,0,0)
Vermelho=(255,0,0)


Clique=False


joystick_x=500

joystick_y=500

toquex=500
toquey=500

x=350
y=900
#Loop Infinito
while True:
	tela.fill((255,255,255))
	for event in py.event.get():
		if event.type==py.MOUSEBUTTONDOWN:
			Clique=True
			toquex,toquey=py.mouse.get_pos()
			
		if event.type==py.MOUSEBUTTONUP:
			Clique=False
			
					
	if Clique and toquex<=650 and toquex>=300 and toquey<=650 and  toquey>=300:
				toquex,toquey=py.mouse.get_pos()
				joystick_x=toquex
				joystick_y=toquey
				
				
	if Clique==False:
			joystick_x=500
			joystick_y=500
						
			
	py.draw.circle(tela,Preto,(500,500),150)
	py.draw.circle(tela,(255,255,255),(500,500),80)
	joystick=py.draw.circle(tela,Vermelho,(joystick_x,joystick_y),80)
	
	
	
	
	esquerda=py.draw.circle(tela,(255,255,255),(500,360),10)
	direita=py.draw.circle(tela,(255,255,255),(500,640),10)
	cima=py.draw.circle(tela,(255,255,255),(640,500),10)
	baixo=py.draw.circle(tela,(255,255,255),(360,500),10)
	
	player=py.draw.rect(tela,(0,0,0),(x,y,200,200))
	
	if direita.colliderect(joystick):
		y+=1
	if cima.colliderect(joystick):
		x+=1
	if esquerda.colliderect(joystick):
		y-=1
	if baixo.colliderect(joystick):
		x-=1
	py.display.update()
			