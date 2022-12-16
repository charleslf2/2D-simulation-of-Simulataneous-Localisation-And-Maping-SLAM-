import math 
import pygame

class Buildenv:
    def __init__(self, MapDimensions):
        pygame.init()
        self.pointcloud=[]
        self.externalMap=pygame.image.load("map.jpg")
        self.maph, self.mapw=MapDimensions
        self.MapwindowsName="RRT path Planing"
        pygame.display.set_caption(self.MapwindowsName)
        self.map=pygame.display.set_mode((self.mapw, self.maph), pygame.RESIZABLE)
        self.map.blit(self.externalMap, (0,0))

        # colors
        self.black=(0,0,0)
        self.grey=(70,70,70)
        self.blue=(0,0,255)
        self.green=(0,255,0)
        self.red=(255,0,0)
        self.white=(255,255,255)
    
    def AD2pos (self, distance, angle, robotposition):
        x=distance * math.cos(angle)+robotposition[0]
        y=-distance * math.sin(angle)+robotposition[1]
        return (int(x), int(y))
    
    def datastorage(self,data):
        print(len(self.pointcloud))
        for element in data:
            point=self.AD2pos(element[0], element[1], element[2])
            if point not in self.pointcloud:
                self.pointcloud.append(point)
    
    def show_sonsorData(self):
        self.infomap=self.map.copy()
        for point in self.pointcloud:
            self.infomap.set_at((int(point[0]), int(point[1])), (255,0,0))
