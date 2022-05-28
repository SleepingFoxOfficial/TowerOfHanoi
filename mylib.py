import pygame
import math
import random
import myclasses as cls


def countDisks(num, source, receiver, cache):  # Функция создания перемещения n дисков

    def play(num, source, receiver, cache):
        if num <= 0:
            return
        play(num - 1, source, cache, receiver)
        mtx.append([num, source, receiver])
        play(num - 1, cache, receiver, source)

    mtx = []
    play(num, source, receiver, cache)
    return mtx


def drawBackground(win):  # Функция прорисовки 3 башен и фона
    win.fill((200, 255, 200))
    cl_wood = (153, 98, 54)
    pygame.draw.rect(win, cl_wood, (85, 430, 160, 20))
    pygame.draw.rect(win, cl_wood, (320, 430, 160, 20))
    pygame.draw.rect(win, cl_wood, (555, 430, 160, 20))
    pygame.draw.rect(win, cl_wood, (160, 200, 10, 250))
    pygame.draw.rect(win, cl_wood, (395, 200, 10, 250))
    pygame.draw.rect(win, cl_wood, (630, 200, 10, 250))


def drawing(win, disks):  # Функция прорисовки всего
    drawBackground(win)
    drawDisks(win, disks)


def createDisks(maxN):  # Функция создания n дисков
    disks = []
    posY = 400
    rad = 70
    for i in range(maxN):
        disks.append(cls.Disk(165, posY, (random.uniform(0, 255), random.uniform(0, 255), random.uniform(0, 255)), rad))
        posY -= 20
        rad -= math.ceil(0.6861 * (maxN ** 2) - 6.8743 * maxN + 31.2937 - 0.0261 * (maxN ** 3))
    return disks


def drawDisks(window, disks):  # Функция Прорисовки n дисков
    for dk in disks:
        dk.draw(window)


def visualTower(totalN, mtx, win, speed):  # Функция перемещения дисков
    tower = [totalN, 0, 0]
    clock = pygame.time.Clock()
    pointer = 0
    lenList = len(mtx) - 1
    disks = createDisks(totalN)
    drawing(win, disks)
    while pointer <= lenList:
        numDisk = mtx[pointer][0]
        towerFrom = mtx[pointer][1] - 1
        towerTo = mtx[pointer][2] - 1
        print("Диск ", mtx[pointer][0], " с ", mtx[pointer][1], " на ", mtx[pointer][2], " башню")
        stop = False
        while not stop:
            clock.tick(speed)
            coord = disks[totalN - numDisk].coordY
            if coord <= 100:
                stop = True
            disks[totalN - numDisk].coordY -= 10
            drawing(win, disks)
            pygame.display.update()
        stop = False
        baseX = disks[totalN - numDisk].coordX + disks[totalN - numDisk].radius
        while not stop:
            clock.tick(speed / 2)
            coord = disks[totalN - numDisk].coordX + disks[totalN - numDisk].radius
            if towerTo > towerFrom:
                if coord >= ((towerTo - towerFrom) * 235 + baseX) - 5:
                    stop = True
                disks[totalN - numDisk].coordX += 5
            else:
                if coord <= ((towerTo - towerFrom) * 235 + baseX) + 5:
                    stop = True
                disks[totalN - numDisk].coordX -= 5
            drawing(win, disks)
            pygame.display.update()
        stop = False
        while not stop:
            clock.tick(speed)
            coord = disks[totalN - numDisk].coordY
            if coord >= (400 - tower[towerTo] * 20):
                stop = True
            disks[totalN - numDisk].coordY += 10
            drawing(win, disks)
            pygame.display.update()
        tower[towerTo] += 1
        tower[towerFrom] -= 1
        pointer += 1
