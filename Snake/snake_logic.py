import simplegui
import random

w = 500
h = 500
food_size = 10
delay = 100

offsets = {
    "up": (0, -20),
    "down": (0, 20),
    "left": (-20, 0),
    "right": (20, 0)
}

def reset():
    global snake, snake_dir, food_position
    snake = [[0, 0], [0, 20], [0, 40], [0, 60], [0, 80]]
    snake_dir = "up"
    food_position = get_random_food_position()

def move_snake():
    global snake_dir

    new_head = snake[-1][:]
    new_head[0] += offsets[snake_dir][0]
    new_head[1] += offsets[snake_dir][1]

    if new_head in snake[:-1]:
        reset()
    else:
        snake.append(new_head)

        if not food_collision():
            snake.pop(0)

        # Wrap around the edges
        if snake[-1][0] < 0:
            snake[-1][0] = w - 20
        elif snake[-1][0] >= w:
            snake[-1][0] = 0
        elif snake[-1][1] < 0:
            snake[-1][1] = h - 20
        elif snake[-1][1] >= h:
            snake[-1][1] = 0

def food_collision():
    global food_position
    if get_distance(snake[-1], food_position) < 20:
        food_position = get_random_food_position()
        return True
    return False

def get_random_food_position():
    x = random.randint(0, w / 20 - 1) * 20
    y = random.randint(0, h / 20 - 1) * 20
    return [x, y]

def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
    return distance

def draw_handler(canvas):
    canvas.draw_polygon([(0, 0), (w, 0), (w, h), (0, h)], 1, "White", "White")
    for segment in snake:
        canvas.draw_circle(segment, 10, 1, 'CornflowerBlue', 'CornflowerBlue')
    canvas.draw_circle(food_position, 10, 1, 'CornflowerBlue', 'CornflowerBlue')

def key_handler(key):
    if key == simplegui.KEY_MAP["up"]:
        go_up()
    elif key == simplegui.KEY_MAP["right"]:
        go_right()
    elif key == simplegui.KEY_MAP["down"]:
        go_down()
    elif key == simplegui.KEY_MAP["left"]:
        go_left()

def go_up():
    global snake_dir
    if snake_dir != "down":
        snake_dir = "up"

def go_right():
    global snake_dir
    if snake_dir != "left":
        snake_dir = "right"

def go_down():
    global snake_dir
    if snake_dir!= "up":
        snake_dir = "down"

def go_left():
    global snake_dir
    if snake_dir != "right":
        snake_dir = "left"

frame = simplegui.create_frame("Snake", w, h)
frame.set_draw_handler(draw_handler)
frame.set_keydown_handler(key_handler)

frame.start()
reset()
timer = simplegui.create_timer(delay, move_snake)
timer.start()
