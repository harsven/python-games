# CodeSkulptor runs Python programs in your browser.
# Click the upper left button to run this simple demo.

# CodeSkulptor is tested to run in recent versions of
# Chrome, Firefox, Safari, and Edge.

import simplegui
import random

width = 650
height = 400       
ball_radius = 20
PAD_WIDTH = 8
PAD_HEIGHT = 85
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

# Key identifiers: W=87, S=83, UP=38, DOWN=40

# initialize ball_pos and ball_vel for new ball in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos=[width/2,height/2]
    ball_vel=[0,0]
    ball_vel[1]=-random.randrange(60, 180)/60
    if direction:
        ball_vel[0]=random.randrange(120, 240)/60
    else:
        ball_vel[0]=-random.randrange(120, 240)/60
       
     
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    paddle1_pos=height/2
    paddle2_pos=height/2
    paddle1_vel=0
    paddle2_vel=0
    global score1, score2  # these are ints
    score1=0
    score2=0
    spawn_ball(random.randrange(0,2))

def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    
        
    # draw mid line and gutters
    c.draw_line([width / 2, 0],[width / 2, height], 1, "cornflowerblue")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, height], 1, "cornflowerblue")
    c.draw_line([width - PAD_WIDTH, 0],[width - PAD_WIDTH, height], 1, "cornflowerblue")
       
    # update ball
    ball_pos[0]+=ball_vel[0]
    ball_pos[1]+=ball_vel[1]
    
    if (ball_pos[0]+ball_radius)>=width-PAD_WIDTH:
        if ball_pos[1]>paddle2_pos - HALF_PAD_HEIGHT and ball_pos[1]<paddle2_pos + HALF_PAD_HEIGHT:
            ball_vel[0]=-ball_vel[0]
            ball_vel[0]=1.1*ball_vel[0]
            ball_vel[1]=1.1*ball_vel[1]
        else:
            score1+=1
            spawn_ball(LEFT)
        
    elif (ball_pos[0]-ball_radius)<=PAD_WIDTH:
        if ball_pos[1]>paddle1_pos - HALF_PAD_HEIGHT and ball_pos[1]<paddle1_pos + HALF_PAD_HEIGHT:
            ball_vel[0]=-ball_vel[0]
            ball_vel[0]=1.1*ball_vel[0]
            ball_vel[1]=1.1*ball_vel[1]
        else:
            score2+=1
            spawn_ball(RIGHT)
    elif (ball_pos[1]+ball_radius)>=height:
        ball_vel[1]=-ball_vel[1]
    if (ball_pos[1]-ball_radius)<=0:
        ball_vel[1]=-ball_vel[1]    
        
    # draw ball
    c.draw_circle(ball_pos, ball_radius, 2, "cornflowerblue", "cornflowerblue")

    # update paddle's vertical position, keep paddle on the screen
    if paddle1_vel>0:
        paddle1_pos=min(paddle1_pos+paddle1_vel,height-HALF_PAD_HEIGHT-1)
    else:
        paddle1_pos=max(paddle1_pos+paddle1_vel,HALF_PAD_HEIGHT)
    
    
    if paddle2_vel>0:
        paddle2_pos=min(paddle2_pos+paddle2_vel,height-HALF_PAD_HEIGHT-1)
    else:
        paddle2_pos=max(paddle2_pos+paddle2_vel,HALF_PAD_HEIGHT)
    
    c.draw_point([width-1,height-1], "RED") 

    
    # draw paddles
    c.draw_polygon([(width - PAD_WIDTH+1,  paddle2_pos + HALF_PAD_HEIGHT-1), (width-1,  paddle2_pos + HALF_PAD_HEIGHT-1), (width-1,  paddle2_pos - HALF_PAD_HEIGHT+1),(width - PAD_WIDTH+1,  paddle2_pos - HALF_PAD_HEIGHT+1)], 1, 'cornflowerblue','cornflowerblue')
    
    c.draw_polygon([(1,  paddle1_pos + HALF_PAD_HEIGHT-1), (PAD_WIDTH-1,  paddle1_pos + HALF_PAD_HEIGHT-1),(PAD_WIDTH-1,  paddle1_pos - HALF_PAD_HEIGHT+1), (1,  paddle1_pos - HALF_PAD_HEIGHT+1)], 1, 'cornflowerblue','cornflowerblue')

    # draw scores
    c.draw_text(str(score1), [width/4,height/2], 50, "cornflowerblue")
    c.draw_text(str(score2), [3*width/4,height/2], 50, "cornflowerblue")
    c.draw_text("Player 2", [5*width/8,height/4], 50, "cornflowerblue")
    c.draw_text("Player 1", [width/8,height/4], 50, "cornflowerblue")


def keydown(key):
    global paddle1_vel, paddle2_vel
    # Key identifiers: W=87, S=83, UP=38, DOWN=40
 
    if key==87:
        paddle1_vel=-4
    elif key==83:
        paddle1_vel=4
    elif key==38:
        paddle2_vel=-4
    elif key==40:
        paddle2_vel=4
    
    
    
def keyup(key):
    global paddle1_vel, paddle2_vel
    paddle1_vel=0
    paddle2_vel=0

# create frame
frame = simplegui.create_frame("Pong", width, height)
frame.set_canvas_background('White')
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", new_game,100)


    
# start frame
new_game()
frame.start()



            margin: 10px 5px;
            cursor: pointer;
            background-color: #6495ED;
            color: white;
            border: none;
            border-radius: 5px;
            text-decoration: none;
            font-weight: bold;
            font-size: 16px;
            transition: background 0.3s;
        }
        .btn:hover { background-color: #4169E1; }
        
        .btn-github { background-color: #333; font-size: 14px; }
        .btn-github:hover { background-color: #000; }

        .controls-hint { font-size: 13px; color: #888; margin-top: 5px; }
    </style>
</head>
<body>

<div id="pong-container">
    <img id="game-image" 
         src="https://raw.githubusercontent.com/DEIN_NUTZERNAME/DEIN_REPO/main/Pong/preview.png" 
         alt="Click to Play Pong" 
         onclick="startGame()">
    
    <br>
    <button class="btn" id="play-btn" onclick="startGame()">Play Game</button>
    <br>
    <a href="DEIN_GITHUB_LINK_ZU_PONG" target="_blank" class="btn btn-github">Code here (GitHub)</a>
    
    <div id="game-area">
        <canvas id="pongCanvas" width="650" height="400"></canvas>
        <div id="hint" class="controls-hint" style="display:none;">
            Controls: Player 1 (W/S) | Player 2 (Arrow Up/Down)
        </div>
    </div>
</div>

<script>
    const canvas = document.getElementById("pongCanvas");
    const ctx = canvas.getContext("2d");
    const img = document.getElementById("game-image");
    const playBtn = document.getElementById("play-btn");
    const hint = document.getElementById("hint");

    // Variablen aus deinem Python-Code
    let ball_pos = [325, 200];
    let ball_vel = [0, 0];
    let paddle1_pos = 200, paddle2_pos = 200;
    let paddle1_vel = 0, paddle2_vel = 0;
    let score1 = 0, score2 = 0;
    const ball_radius = 20;
    const PAD_WIDTH = 8, PAD_HEIGHT = 85;

    function spawnBall(toRight) {
        ball_pos = [canvas.width / 2, canvas.height / 2];
        // Zufällige Velocity wie im Python-Original
        ball_vel[1] = -(Math.random() * (180 - 60) + 60) / 60;
        ball_vel[0] = (Math.random() * (240 - 120) + 120) / 60;
        if (!toRight) ball_vel[0] *= -1;
    }

    function startGame() {
        img.style.display = "none";
        playBtn.style.display = "none";
        canvas.style.display = "block";
        hint.style.display = "block";
        spawnBall(Math.random() > 0.5);
        requestAnimationFrame(gameLoop);
    }

    function update() {
        ball_pos[0] += ball_vel[0];
        ball_pos[1] += ball_vel[1];

        // Paddle Bewegung
        paddle1_pos += paddle1_vel;
        paddle2_pos += paddle2_vel;

        // Keep paddles on screen
        paddle1_pos = Math.max(PAD_HEIGHT/2, Math.min(canvas.height - PAD_HEIGHT/2, paddle1_pos));
        paddle2_pos = Math.max(PAD_HEIGHT/2, Math.min(canvas.height - PAD_HEIGHT/2, paddle2_pos));

        // Wand-Kollision (oben/unten)
        if (ball_pos[1] <= ball_radius || ball_pos[1] >= canvas.height - ball_radius) {
            ball_vel[1] *= -1;
        }

        // Kollision mit Paddles oder Gutters
        if (ball_pos[0] <= PAD_WIDTH + ball_radius) {
            if (ball_pos[1] > paddle1_pos - PAD_HEIGHT/2 && ball_pos[1] < paddle1_pos + PAD_HEIGHT/2) {
                ball_vel[0] = -ball_vel[0] * 1.1;
                ball_vel[1] *= 1.1;
            } else {
                score2++;
                spawnBall(true);
            }
        }
        if (ball_pos[0] >= canvas.width - PAD_WIDTH - ball_radius) {
            if (ball_pos[1] > paddle2_pos - PAD_HEIGHT/2 && ball_pos[1] < paddle2_pos + PAD_HEIGHT/2) {
                ball_vel[0] = -ball_vel[0] * 1.1;
                ball_vel[1] *= 1.1;
            } else {
                score1++;
                spawnBall(false);
            }
        }
    }

    function render() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        // Mittellinie & Gutters
        ctx.strokeStyle = "cornflowerblue";
        ctx.setLineDash([5, 5]);
        ctx.beginPath(); ctx.moveTo(canvas.width/2, 0); ctx.lineTo(canvas.width/2, canvas.height); ctx.stroke();
        ctx.setLineDash([]);
        ctx.strokeRect(PAD_WIDTH, 0, canvas.width - 2*PAD_WIDTH, canvas.height);

        // Ball
        ctx.fillStyle = "cornflowerblue";
        ctx.beginPath();
        ctx.arc(ball_pos[0], ball_pos[1], ball_radius, 0, Math.PI*2);
        ctx.fill();

        // Paddles
        ctx.fillRect(0, paddle1_pos - PAD_HEIGHT/2, PAD_WIDTH, PAD_HEIGHT);
        ctx.fillRect(canvas.width - PAD_WIDTH, paddle2_pos - PAD_HEIGHT/2, PAD_WIDTH, PAD_HEIGHT);

        // Scores
        ctx.font = "50px sans-serif";
        ctx.globalAlpha = 0.4;
        ctx.fillText(score1, canvas.width/4, canvas.height/2);
        ctx.fillText(score2, 3*canvas.width/4, canvas.height/2);
        ctx.globalAlpha = 1.0;
    }

    function gameLoop() {
        update();
        render();
        requestAnimationFrame(gameLoop);
    }

    // Keyboard-Events
    window.addEventListener("keydown", (e) => {
        if (e.key.toLowerCase() === "w") paddle1_vel = -4;
        if (e.key.toLowerCase() === "s") paddle1_vel = 4;
        if (e.key === "ArrowUp") paddle2_vel = -4;
        if (e.key === "ArrowDown") paddle2_vel = 4;
        if(["ArrowUp","ArrowDown"].includes(e.key)) e.preventDefault();
    });
    window.addEventListener("keyup", (e) => {
        if (["w", "s", "W", "S"].includes(e.key)) paddle1_vel = 0;
        if (["ArrowUp", "ArrowDown"].includes(e.key)) paddle2_vel = 0;
    });
</script>

</body>
</html>
