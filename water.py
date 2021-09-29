import pygame

pygame.init()
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Plant Water')


#Font Settings
WHITE = (255,255,255)
YELLOW = (0,0,0)
BLUEBACKGROUND = (41,221,247)
FONT = pygame.font.SysFont('comicsansms', 36)
SMALLFONT = pygame.font.SysFont('comicsansms', 12)



def draw(status, remaining):
	background(remaining)
	drawPlant(status)
	drawButtons()


	pygame.display.flip()


def background(remaining):
	win.fill(WHITE)

	text = FONT.render(f'You have {remaining} minutes remaining!', 1, YELLOW)
	win.blit(text, (140,25))

def drawButtons():
	button = pygame.image.load('Assets/WaterButton.png')
	win.blit(button, (WIDTH*.3 - 200, HEIGHT*.66))

	button = pygame.image.load('Assets/QuitButton.png')
	win.blit(button, (WIDTH*.6, HEIGHT*.66))

#Draws the plant sprite
#@status is the current plant state
def drawPlant(status):
	if status < 0:
		plant = pygame.image.load('Assets/DeadPlant' + str(status*-1) +'.png')
	else:
		plant = pygame.image.load('Assets/plant' + str(status) +'.png')
	
	win.blit(plant, (int((WIDTH/2)-(256/2)), int((HEIGHT/2)-(256/2))))

def click(pos):
	waterBox = [(WIDTH*.3 - 184), (WIDTH*.3 + 44), (HEIGHT*.66+70), (HEIGHT*.66+170)]
	quitBox = [(WIDTH*.6+16), (WIDTH*.6 + 243), (HEIGHT*.66+70), (HEIGHT*.66+170)]

	if waterBox[0] < pos[0] <waterBox[1]:
		if waterBox[2] < pos[1] < waterBox[3]:
			return 1
	elif quitBox[0] < pos[0] < quitBox[1]:
		if quitBox[2] < pos[1] < quitBox[3]:
			return 2
	else:
		return 0





def main():
	clock = pygame.time.Clock()
	run = True
	FPS = 60

	#Plant Status
	status = 0
	waterTimer = 3600

	#20 minutes (54000) max without water
	timerMax = 72000


	while run:
		clock.tick(FPS)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()

			if event.type == pygame.MOUSEBUTTONDOWN:
				pos = pygame.mouse.get_pos()
				#print(pos)

				clicked = click(pos)

				#1 = Water
				#2 = Quit
				if clicked == 1:

					#If the user hasn't clicked in a minute, prevents overwatering
					if waterTimer > 3600:
						waterTimer = 0

						if status < 4:
							status += 1

				elif clicked == 2:
					run = False
					pygame.quit()

		if waterTimer >= timerMax:
			if status >= 2:
				status = -2
			else:
				status = -1

			waterTimer = 0

		remaining = int(round(((timerMax - waterTimer)/60)/60))

		draw(status, remaining)

		waterTimer += 1



while True:
	main()

pygame.quit()
system.exit()
