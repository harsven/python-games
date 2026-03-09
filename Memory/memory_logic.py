import simplegui
import random
chances = 0

# helper function to initialize globals
def new_game():
    global cardsListing
    global revealed
    global cardOpened
    global countedClicks
    global chances
    cardsListing =[i for i in range(8)]+[i for i in range(8)]
    random.shuffle(cardsListing)
    revealed = [not True for i in range(16)]
    cardOpened = []
    countedClicks = 0
    chances = 0

     
# define event handlers
def mouseclick(pos):
    global chances
    global countedClicks
    if countedClicks == 0:
        cardOpened.append(pos[0]//50)
        revealed[pos[0] // 50] = True
        countedClicks += 1
        chances = 1
        
    elif countedClicks == 1:
        if not(pos[0] // 50 in cardOpened):
            cardOpened.append(pos[0] // 50)
            countedClicks = countedClicks + 1
        revealed[pos[0] // 50] = True
            
    else:	
         if not (pos[0] // 50 in cardOpened):
            if cardsListing[cardOpened[-1]]!=cardsListing[cardOpened[-2]]:
                revealed[cardOpened[-1]] = False
                revealed[cardOpened[-2]] = False
                cardOpened.pop(), cardOpened.pop()
                
            countedClicks = 1
            chances += 1
            revealed[pos[0] // 50] = True
            cardOpened.append(pos[0] // 50)
                
               
    
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for i in range(16):
        canvas.draw_line([50 *(i % 16),0],[50 * (i % 16), 100], 2, "cornflowerblue")
        if revealed[i]:
            canvas.draw_text(str(cardsListing[i]), [15 + 50 * i, 70], 40, "cornflowerblue")


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = ("Turns = " +str(chances))
frame.set_canvas_background('White')

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
