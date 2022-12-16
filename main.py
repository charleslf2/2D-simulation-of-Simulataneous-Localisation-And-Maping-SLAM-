import sensor,env
import pygame
import math 



environment=env.Buildenv((800,1200))


environment.originalMap=environment.map.copy()

laser=sensor.LaserSensor(200, environment.originalMap, uncertentity=(0.5,0.01))
environment.map.fill((0,0,0))
environment.infomap=environment.map.copy()


running=True


while running:
    sensorON=False
    for envent in pygame.event.get():
        if envent.type==pygame.QUIT:
            running=False
        if pygame.mouse.get_focused():
            sensorON=True
        elif not pygame.mouse.get_focused():
            sensorON=False
    if sensorON:
        position=pygame.mouse.get_pos()
        laser.position=position
        sensor_data=laser.sense_obstacles()
        environment.datastorage(sensor_data)
        environment.show_sonsorData()
    environment.map.blit(environment.infomap, (0,0))
    pygame.display.update()
