import pygame,time,os

pygame.init()
#初始化pygame

#img = pygame.image.load("rect/icon.ico")
#pygame.display.set_icon(img)

size = (1000,700)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Rect")
#初始化窗口

fps = pygame.time.Clock()
fps.tick(60)
#设置帧率

start_time = time.time()
left_time = 60
#设置计时器

rect_x_p1 = 50
rect_y_p1 = 600
rect_x_p2 = 900
rect_y_p2 = 600
rect_height = 50
rect_width = 50
#对象的初始数据


white = (255, 255, 255)
#定义颜色

done = True

catch = False

font = pygame.font.SysFont('Arial', 24)

bouncy = False
#设成True有彩蛋

y_speed_p1 = 0
x_speed_p1 = 0
y_speed_p2 = 0
x_speed_p2 = 0
bounce_height_p1 = 0
bounce_height_p2 = 0
#速度初始化

while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
        #退出事件检测
    
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_d]:
        if x_speed_p1 < 0.5:
            x_speed_p1 += 0.0005
    elif pressed[pygame.K_a]:
        if x_speed_p1 > -0.5:
            x_speed_p1 -= 0.0005
    elif x_speed_p1 < -0.001 or x_speed_p1 > 0.001:
        if x_speed_p1 > 0:
            x_speed_p1 -= 0.0005
        if x_speed_p1 < 0:
            x_speed_p1 += 0.0005 
    else:
        x_speed_p1 = 0
    #P1的横向移动
    
    if pressed[pygame.K_w] and y_speed_p1 == 0:
        y_speed_p1 = -0.8
        rect_y_p1 -= 0.1
        if bouncy:
            bounce_height_p1 = -0.8
    #P1的跳跃
    
    if pressed[pygame.K_s]:
        rect_y_p1=625
    #P1的潜行
    
    if pressed[pygame.K_SPACE] and catch:
        rect_y_p1=rect_y_p2-300
        rect_x_p1=rect_x_p2
    #P1的传送技能(没加CD)
    
    if pressed[pygame.K_RIGHT]:
        if x_speed_p2 < 0.5:
            x_speed_p2 += 0.0005
    elif pressed[pygame.K_LEFT]:
        if x_speed_p2 > -0.5:
            x_speed_p2 -= 0.0005
    elif x_speed_p2 < -0.001 or x_speed_p2 > 0.001:
        if x_speed_p2 > 0:
            x_speed_p2 -= 0.0005
        if x_speed_p2 < 0:
            x_speed_p2 += 0.0005 
    else:
        x_speed_p2 = 0
    #P2的横向移动
    
    if pressed[pygame.K_UP] and y_speed_p2 == 0:
        y_speed_p2 = -0.8
        rect_y_p2 -= 0.1 
        if bouncy:
            bounce_height_p2 = -0.8
    #P2的跳跃
    
    if pressed[pygame.K_DOWN]:
        rect_y_p2=625
    #P2的潜行

    if pressed[pygame.K_SPACE] and (not catch):
        rect_y_p2=rect_y_p1-300
        rect_x_p2=rect_x_p1
    #P2的传送技能(没加CD)

    if rect_y_p1 >= 625:
        if bounce_height_p1 > -0.2:
            y_speed_p1 = 0
            rect_y_p1 = 625
        elif bouncy:
            bounce_height_p1 = bounce_height_p1 * 0.8
            rect_y_p1 -= 0.1
            y_speed_p1 = bounce_height_p1
    else:
        y_speed_p1 += 0.001

    if rect_y_p2 >= 625:
        if bounce_height_p2 > -0.2:
            y_speed_p2 = 0
            rect_y_p2 = 625
        elif bouncy:
            bounce_height_p2 = bounce_height_p2 * 0.8
            rect_y_p2 -= 0.1
            y_speed_p2 = bounce_height_p2
    else:
        y_speed_p2 += 0.001
    #重力模拟
        
    
    if rect_x_p1 >= 925:
        x_speed_p1 = 0
        rect_x_p1 = 924.999
    elif rect_x_p1 <= 25:
        x_speed_p1 = 0
        rect_x_p1 = 25.001

    if rect_x_p2 >= 925:
        x_speed_p2 = 0
        rect_x_p2 = 924.999
    elif rect_x_p2 <= 25:
        x_speed_p2 = 0
        rect_x_p2 = 25.001
    #惯性模拟 边缘检测

    rect_y_p1 += y_speed_p1
    rect_x_p1 += x_speed_p1

    rect_y_p2 += y_speed_p2
    rect_x_p2 += x_speed_p2
    #移动执行

    if rect_x_p1 <= rect_x_p2+50 and rect_x_p1 >= rect_x_p2-50 and rect_y_p1 <= rect_y_p2+50 and rect_y_p1 >= rect_y_p2-50:
        catch = not catch
        rect_x_p1 = 50
        rect_y_p1 = 600
        rect_x_p2 = 900
        rect_y_p2 = 600
    #碰撞检测
    
    if catch:
        text1 = font.render("Black's turn", True, white)
    else:
        text1 = font.render("White's turn", True, white)
    #设置抓逃轮次文字
    
    this_time=left_time - (time.time() - start_time)
    str_time=str(round(this_time))
    text2 = font.render(str_time, True, white)
    #计时器

    if this_time <= 0:
        break
    #时长判断(是否结束)
    
    screen.fill((0, 0, 0))
    screen.blit(text1, (450, 10))
    screen.blit(text2, (450, 30))
    pygame.draw.rect(screen, white, [rect_x_p1, rect_y_p1, rect_width, rect_height], 2, 10)
    pygame.draw.rect(screen, white, [rect_x_p2, rect_y_p2, rect_width, rect_height], 0, 10)
    #书写文字
    pygame.display.update()#刷新界面

while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
    #退出事件检测
    pressed = pygame.key.get_pressed()
    if catch:
        text1 = font.render("Loser:Black", True, white)
    else:
        text1 = font.render("Loser:White", True, white)

    text2 = font.render("Press R to restart", True, white)
    if pressed[pygame.K_r]:
        os.system('start '+__file__)
        pygame.quit()
        quit()
    screen.fill((0, 0, 0))
    screen.blit(text1, (450, 300))
    screen.blit(text2, (450, 400))
    pygame.display.update()
