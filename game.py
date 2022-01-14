#Stacy Meng, swm8xb

import pygame
import gamebox
import random


#CREATE GAME
camera = gamebox.Camera(800, 600)
ground = gamebox.from_color(400,600,"green", 800, 50)
game_on = False

#TREES
tree1 = gamebox.from_color(160,300,"tan", 100, 16000)
tree2 = gamebox.from_color(640,300,"tan", 100, 16000)
top1 = gamebox.from_color(160, -7700, "green", 300, 300)
top2 = gamebox.from_color(640, -7700, "green", 300, 300)

#HEALTH BAR
health_p1 = 100
health_p2 = 100
health_b1 = gamebox.from_color(410, 200, "red", health_p1, 30)
health_b2 = gamebox.from_color(410, 400, "blue", health_p2, 30)
p1_text = gamebox.from_text(340, 200, 'P1', 30, 'black', bold=True, italic=False)
p2_text = gamebox.from_text(340, 200, 'P2', 30, 'black', bold=True, italic=False)

#CLIMBER

climber1 = gamebox.from_image(229,300,'ladybug1.png')
climber1.scale_by(0.115)
climber2 = gamebox.from_image(709,300,'ladybug1.png')
climber2.scale_by(0.115)

#CLIMBER SPEED
v1 = -10
v2 = -10
climber1.yspeed = v1
climber2.yspeed = v2

#LEAF POWERUPS

leafp1_1 = gamebox.from_image(100, random.randint(-2000,-1000), "leaf.png")
leafp1_1.scale_by(0.1)
leafp1_2 = gamebox.from_image(210, random.randint(-5000,-4000), "leaf.png")
leafp1_2.scale_by(0.1)
leafp1_3 = gamebox.from_image(100, random.randint(-7000,-6000), "leaf.png")
leafp1_3.scale_by(0.1)
leafp2_1 = gamebox.from_image(580, random.randint(-2000,-1000), "leaf.png")
leafp2_1.scale_by(0.1)
leafp2_2 = gamebox.from_image(700, random.randint(-5000,-4000), "leaf.png")
leafp2_2.scale_by(0.1)
leafp2_3 = gamebox.from_image(580, random.randint(-7000,-6000), "leaf.png")
leafp2_3.scale_by(0.1)

########## Counter
counter = 0

###### TREE BRANCHES OBSTACLE
branches = []

#START SCREEN

name = gamebox.from_text(180, 40, 'Name: Stacy Meng // Computing ID: swm8xb', 20, 'black', bold=False, italic=False)
game_name = gamebox.from_text(400, 150, 'The Tree Race', 60, 'black', bold=True, italic=False)
i1 = gamebox.from_text(400, 200, 'INSTRUCTIONS: Each player climbs up the tree and races to reach the top.', 20, 'black', bold=False, italic=False)
i2 = gamebox.from_text(400, 220, 'Along the way, there will be branches on the sides that must be avoided.', 20, 'black', bold=False, italic=False)
i3 = gamebox.from_text(400, 240, 'To dodge the branches, p1 uses the "A" and "D" keys and p2 uses left and right arrows.', 20, 'black', bold=False, italic=False)
i4 = gamebox.from_text(400, 260, 'If the player fails to dodge the obstacle, their health bar will decrease.', 20, 'black', bold=False, italic=False)
i5 = gamebox.from_text(400, 280, 'Players can gain speed by collecting the leaf powerups along the way.', 20, 'black', bold=False, italic=False)
i6 = gamebox.from_text(400, 300, 'GOAL: Get to the top of the tree the fastest. If a player\'s health bar hits zero, the other player wins.', 20, 'black', bold=False, italic=False)
i7 = gamebox.from_text(400, 400, 'PRESS SPACE TO START', 40, 'black', bold=True, italic=False)


def tick(keys):
    global game_on
    global health_p1, health_b1
    global health_p2, health_b2
    global leafp1_1, leafp1_2, leafp1_3, leafp2_1, leafp2_2, leafp2_3
    global climber1, climber2, v1, v2, tree1, tree2, p1_text, p2_text, counter

#################################### START SCREEN ######################################

    camera.clear('white')
    camera.draw(name)
    camera.draw(game_name)
    camera.draw(i1)
    camera.draw(i2)
    camera.draw(i3)
    camera.draw(i4)
    camera.draw(i5)
    camera.draw(i6)
    camera.draw(i7)
    camera.display()

#################################### GAMEPLAY ######################################

    if pygame.K_SPACE in keys:
        game_on = True


    if game_on:
        camera.clear("cyan")

        #### DRAW GAME BACKGROUND
        camera.draw(climber1)
        camera.draw(climber2)
        camera.draw(tree1)
        camera.draw(tree2)
        camera.draw(leafp1_1)
        camera.draw(leafp1_2)
        camera.draw(leafp1_3)
        camera.draw(leafp2_1)
        camera.draw(leafp2_2)
        camera.draw(leafp2_3)
        camera.draw(health_b1)
        camera.draw(health_b2)
        camera.draw(ground)
        camera.draw(p1_text)
        camera.draw(p2_text)
        camera.display()

       ########### MOVING SETTINGS
        camera.y = (climber1.y + climber2.y)/2  #update camera to follow player movement
        climber1.move_speed()
        climber2.move_speed()
        health_b1.y = camera.y - 80
        health_b2.y = camera.y + 100
        p1_text.y = camera.y - 80
        p2_text.y = camera.y + 100


        #### PLAYER 1 CONTROLS
        if pygame.K_a in keys:
            climber1.right = 110

        if pygame.K_d in keys:
            climber1.left = 210

        #### PLAYER 2 CONTROLS
        if pygame.K_LEFT in keys:
            climber2.right = 590

        if pygame.K_RIGHT in keys:
            climber2.left = 690

        ### OBSTACLES MOVEMENT

        counter += 1

        if counter % 30 == 0:
            branches.append(gamebox.from_color(85, camera.y - random.randint(300,350),"tan", 50, 20)) #first tree left branch
            branches.append(gamebox.from_color(235, camera.y - random.randint(400, 500), "tan", 50, 20)) #first tree right branch
            branches.append(gamebox.from_color(565, camera.y - random.randint(300, 350), "tan", 50, 20))  #second tree left branch
            branches.append(gamebox.from_color(715, camera.y - random.randint(400, 500), "tan", 50, 20))  #second tree right branch

        for item in branches:
            # leaves don't show up on branches
            if item.y != leafp1_1 and item.y != leafp1_2 and item.y != leafp1_3 and item.y != leafp2_1 and item.y != leafp2_2 and item.y != leafp2_3:
                camera.draw(item)

        #tops cover extra branches at top
        camera.draw(top1)
        camera.draw(top2)
        camera.display()

        #### POWERUPS

        #PLAYER 1
        #powerups increase climbing speed of player

        if climber1.touches(leafp1_1):
            leafp1_1.x = -50  #remove powerup by moving leaf off screen
            climber1.yspeed = -10.6
            climber1.move_speed()

        if climber1.touches(leafp1_2):
            leafp1_2.x = -50 #remove powerup by moving leaf off screen
            climber1.yspeed = -11.1
            climber1.move_speed()

        if climber1.touches(leafp1_3):
            leafp1_3.x = -50  # remove powerup by moving leaf off screen
            climber1.yspeed = -11.7
            climber1.move_speed()

        #PLAYER 2

        if climber2.touches(leafp2_1):
            leafp2_1.x = -50  # remove powerup by moving leaf off screen
            climber2.yspeed = -10.6
            climber2.move_speed()

        if climber2.touches(leafp2_2):
            leafp2_2.x = -50  # remove powerup by moving leaf off screen
            climber2.yspeed = -11.1
            climber2.move_speed()

        if climber2.touches(leafp2_3):
            leafp2_3.x = -50  # remove powerup by moving leaf off screen
            climber2.yspeed = -11.7
            climber2.move_speed()


        ############################### COLLISIONS ################################################


                                                                #PLAYER 1

        ### CLIMBER 1 TOUCH BRANCH
        for item in branches:
            if climber1.touches(item):
                if health_p1 > 0:
                    health_p1 -= 3
                    health_b1 = gamebox.from_color(410, camera.y-80 , "red", health_p1, 30)

        if health_p1 <= 0:
            gamebox.pause()
            camera.clear('white')
            camera.draw(gamebox.from_text(400, camera.y, "GAME OVER! PLAYER 2 WINS!", 60, "black"))
        camera.display()

        ### CLIMBER 1 TOUCH TREE TO WIN AND HIGHER POSITION THAN CLIMBER 2
        if top1.bottom_touches(climber1) and climber1.y < climber2.y:
            camera.clear("white")
            camera.draw(gamebox.from_text(400, camera.y, "GAME OVER! PLAYER 1 WINS!", 60, "black"))
            gamebox.pause()
        camera.display()

                                                                 #PLAYER 2

        # CLIMBER 2 TOUCH BRANCH

        for item in branches:
            if climber2.touches(item):
                if health_p2 > 0:
                    health_p2 -= 3
                    health_b2 = gamebox.from_color(410, camera.y+100 , "blue", health_p2, 30)

        if health_p2 <= 0:
            # player 2 health bar hits 0
            camera.clear('white')
            camera.draw(gamebox.from_text(400, camera.y, "GAME OVER! PLAYER 1 WINS!", 60, "black"))
            gamebox.pause()
        camera.display()

        ### CLIMBER 2 TOUCH TREE TO WIN AND HIGHER POSITION THAN CLIMBER 1
        if top2.bottom_touches(climber2) and climber2.y < climber1.y:
            camera.clear("white")
            camera.draw(gamebox.from_text(400, camera.y, "GAME OVER! PLAYER 2 WINS!", 60, "black"))
            gamebox.pause()
        camera.display()

        ################# TIE GAME ##################

        if top2.bottom_touches(climber2) and top1.bottom_touches(climber1) and climber1.y == climber2.y:
            camera.clear("white")
            camera.draw(gamebox.from_text(400, camera.y, "GAME OVER! YOU TIED!", 60, "black"))
            gamebox.pause()
        camera.display()


gamebox.timer_loop(30, tick)





