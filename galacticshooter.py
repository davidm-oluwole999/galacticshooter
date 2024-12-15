import pgzrun
import random

WIDTH= 700
HEIGHT= 600

ship= Actor("ship.png")


ship.pos= (WIDTH//2, HEIGHT- 60)
speed= 5
enemies= []
bullets= []
score= 0
direction= 1

for e in range(8):
    op= Actor("enemies.png")
    enemies.append(op)
    enemies[-1].x = 100+ 50* e
    enemies[-1].y = 100

def draw():
    screen.clear()
    screen.fill("royal blue")
    ship.draw()
    screen.draw.text("Score = "+ str(score), (50,50))
    for e in enemies:
        e.draw()
    for b in bullets:
        b.draw(      )

def update():
    global score, direction, bullets
    if keyboard.left:
        ship.x -= speed
        if ship.x <= 40:
            ship.x= 40
    elif keyboard.right:
        ship.x += speed
        if ship.x >= WIDTH- 40:
            ship.x= WIDTH - 40
    for b in bullets:
        if b.y <= 0:
            bullets.remove(b)
        else:
            b.y-= 10
        
    if len(enemies)> 0 and (enemies[-1].x > WIDTH- 80 or enemies[0].x < 80):
        direction= direction *-1

    for e in enemies:
        e.y += 0.5
        e.x += 5* direction
        if e.y >= HEIGHT:
            e.y= -100
            e.x = random.randint(40, WIDTH- 40)
        for b in bullets:
            if e.colliderect(b):
                '''sounds.eep.play()'''
                score+= 100 
                bullets.remove(b)
                enemies.remove(e)    


def on_key_down(key):
    global bullets
    if key == keys.SPACE:
        bullets.append(Actor("bullet.png"))
        bullets[-1].x= ship.x
        bullets[-1].y= ship.y- 50



pgzrun.go()