import pygame
print('=====DESAFIO 22=====')
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('ex022.mp3')
pygame.mixer.music.play()
pygame.event.wait()
#   pygame.init() ==> NÃO FUNCIONOU, PRECISOU INICIAR O MIXER TAMBÉM.
#   inicia o módulo.
#   Carrega o arquivo mp3.
#   Ativa o play.
#   Quando terminar, encerra a música.