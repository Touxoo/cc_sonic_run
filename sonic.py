import pygame

class Personnage(pygame.sprite.Sprite):
	
	spriteSheet = pygame.image.load("sprites-sonic.png").convert_alpha()
	
	sequences = [(0,1,False),(24,32,True),(32,24,False)]
	
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
	
		self.image = Personnage.spriteSheet.subsurface(pygame.Rect(0,0,32,64))
		self.rect = pygame.Rect(0,0,44,46)
		self.rect.bottom = HEIGHT

		self.numeroSequence = 0
		self.numeroImage = 0
		self.flip = False

		self.deltaTime = 0
		self.vitesse = int(round(100/FPS))
			
	def update(self,time):
		self.deltaTime = self.deltaTime + time
		
		if self.deltaTime>=150:
			self.deltaTime = 0
			
			n = Personnage.sequences[self.numeroSequence][0]+self.numeroImage
			self.image = Personnage.spriteSheet.subsurface(pygame.Rect(n%10*44,n//10*46,44,46))
			if self.flip:
				self.image = pygame.transform.flip(self.image,True,False)
			
			self.numeroImage = self.numeroImage+1
			
			if self.numeroImage == Personnage.sequences[self.numeroSequence][1]:
				if Personnage.sequences[self.numeroSequence][2]:
					self.numeroImage = 0
				else:
					self.numeroImage = self.numeroImage-1
	
	
	def goRight(self):
		self.rect = self.rect.move(self.vitesse,0).clamp(rectScreen)
		self.flip = False
		self.setSequence(1)
	
	def goLeft(self):
		self.rect = self.rect.move(-self.vitesse,0).clamp(rectScreen)
		self.flip = True
		self.setSequence(1)