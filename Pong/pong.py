<!DOCTYPE html>
<html>
<head>
    <style>
        #pong-container { 
            text-align: center; 
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
            color: #6495ED; 
            max-width: 650px; 
            margin: auto;
        }
        /* Das Vorschaubild (von GitHub gehostet) */
        #game-image { 
            width: 100%; 
            max-width: 500px; 
            cursor: pointer; 
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
            transition: transform 0.2s;
        }
        #game-image:hover { transform: scale(1.02); }

        /* Der Canvas */
        canvas { 
            border: 2px solid #6495ED; 
            background-color: #ffffff; 
            display: none; 
            margin: 15px auto; 
            max-width: 100%;
            height: auto;
        }

        /* Buttons */
        .btn {
            display: inline-block;
            padding: 12px 25px;
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
