import pygame as py
from random import randint

tela=py.display.set_mode((0,0))

py.init()
tecla=py.image.load('ima/tecla.png')
tecla2=py.transform.scale(tecla,(400,600))




posx2=[3]
posy2=[-800]
time=0
cont=0
tx=-1000
cont2=0
ty=-1000
velocidade=40
objects=[]
cont3=0
limite=20
vai=0
cont5=0
font=py.font.SysFont('arial',70,True,True)

fundo=py.image.load('fundo.jpg')
fundo2=py.transform.scale(fundo,(1200,2200))

music=py.mixer.music.load('Naruto Shippuden - Opening 9.mp3')
py.mixer.music.play(-1)
pontos=0
timer=0
remover=0
velocidade2=1

while True:
	mensagem=f'Pontuação: {pontos}'
	texto=font.render(mensagem,(255,255,255),False)
	tela.fill((255,255,255))
	tela.blit(fundo2,(0,0))
	for event in py.event.get():
		if event.type==py.MOUSEBUTTONDOWN:
			tx,ty=py.mouse.get_pos()
		if event.type==py.MOUSEBUTTONDOWN and velocidade<=0:
			pontos=0
			velocidade=30
			velocidade2=1
			
			
	vai+=0.4
	if vai<1:
		cont5=0
	if vai>=1 and vai<2:
		cont5=1
	if vai>=2 and vai<3:
		cont5=2
	if vai>=3 and vai<4:
		cont5=3
	if vai>=4 and vai<5:
		cont5=4
	if vai>=5 and vai<6:
		cont5=5
	if vai>=6 and vai<7:
		cont5=6
	if vai>=7 and vai<8:
		cont5=7
	if vai>=9 and vai<10:
		cont5=8
	if vai>=10 and vai<11:
		cont5=10
	if vai>=11 and vai<12:
		cont5=11
	if vai>=12 and vai<13:
		cont5=13
	if vai>=13:
		cont5=0
		vai=0
	
	
	
	
	py.draw.rect(tela,(255,255,255),(330,0,3,2400))
	py.draw.rect(tela,(255,255,255),(680,0,3,2400))
	
	
	
	remover+=1
	timer+=1
	time+=velocidade2
	if time>=limite:
		escolha=randint(1,3)
		if escolha==1:
			posx=1
		if escolha==2:
			posx=300
		if escolha==3:
			posx=700
		
		posy=-800
		posx2.append(posx)
		posy2.append(posy)
		time=0
	
	linha=py.draw.rect(tela,(0,255,255),(0,1900,1200,3))
	
	while cont<len(posx2):
		if posy2[cont]>-800 and posy2[cont]<2200:
			obj=tela.blit(tecla2,(posx2[cont],posy2[cont]))
			
			objects.append(obj)
			
		while cont2<len(posx2):
							if ty>=posy2[cont2] and ty<=posy2[cont2]+600 and tx>=posx2[cont2] and tx<=posx2[cont2]+400:
								pontos+=1
								posy2[cont2]=6000
								ty=-1000
								
							cont2+=1		
		if posy2[cont]<=2400:
			posy2[cont]+=velocidade
			
		while cont3<len(objects):
			if linha.colliderect(objects[cont3]):
				velocidade=0
				velocidade2=1
				del objects[cont3]
			cont3+=1
		cont3=0
		cont+=1
		cont2=0
		
	if remover>=500:
			del objects[0:20]
			
			
	if timer>=100:
		velocidade+=15
		limite=15
		timer=0
		
	
	cont=0
	cont4=0
	
			
	tela.blit(texto,(50,0))
	py.display.update()