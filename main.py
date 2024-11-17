import pygame
import time

pygame.init()

WIDTH = 600
HEIGHT = 600

display_surface= pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Birthday Greetings Card")

img=pygame.image.load("bday.jpg")
image = pygame.transform.scale(img,(WIDTH,HEIGHT))

while(True):
    font=pygame.font.SysFont("Times New Roman",72)
    text=font.render("Happy",True,(0,0,0))
    text2=font.render("Birthday",True,(0,0,0))
    display_surface.fill((255,255,255))
    display_surface.blit(image,(0,0))
    display_surface.blit(text,(210,180))
    display_surface.blit(text2,(180,264))
    pygame.display.update()
    time.sleep(2)

    img2=pygame.image.load("Cake.jpg")
    font2=pygame.font.SysFont("Arial",50)
    text3=font2.render("I wish you a good year",True,(0,0,0))
    display_surface.fill((255,255,255))
    display_surface.blit(img2,(0,0))
    display_surface.blit(text3,(210,180))
    pygame.display.update()
    time.sleep(2)
    
    img3=pygame.image.load("Final.jpg")
    font3=pygame.font.SysFont("Arial",30)
    text4=font3.render("Have a nice day",True,(0,0,0))
    display_surface.fill((255,255,255))
    display_surface.blit(img3,(0,0))
    display_surface.blit(text4,(210,210))
    pygame.display.update()
    time.sleep(2)


   


