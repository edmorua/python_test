import pygame
import pygame.camera
from pygame.locals import*

pygame.init()
pygame.camera.init()

size = (640,480)
display = pygame.display.set_mode(size,0)
pygame.display.set_caption("Mi_camara")
cams = pygame.camera.list_cameras()
cam_id = cams[0]
camera = pygame.camera.Camera(cam_id, size, "RGB")
camera.start()

snapshot = pygame.surface.Surface(size,0,display)
end = False

while not end:
	events = pygame.event.get()
	for e in events:
		if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
			end = True
	if camera.query_image():
		snapshot = camera.get_image(snapshot)
	else:
		snapshot = camera.get_image(display)
	pygame.display.flip()
