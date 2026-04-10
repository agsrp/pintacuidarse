import re

with open("script.js", "r", encoding="utf-8") as f:
    content = f.read()

# 1. DOM elements
dom_elements = """const correctCountElement = document.getElementById('correct-count');
const totalCountElement = document.getElementById('total-count');
const restartBtn = document.getElementById('restart-btn');

// Gamification DOM
const hearts = document.querySelectorAll('#lives-container .heart');
const timerFill = document.getElementById('timer-fill');
const timerWrapper = document.querySelector('.timer-wrapper');"""

content = content.replace("const correctCountElement = document.getElementById('correct-count');\nconst totalCountElement = document.getElementById('total-count');\nconst restartBtn = document.getElementById('restart-btn');", dom_elements, 1)


# 2. State elements
state_elements = """// Quiz state
let currentQuizData = [];
let currentQuestionIndex = 0;
let answered = false;
let correctAnswers = 0;
const QUESTIONS_PER_SESSION = 6;

// Gamification State
let lives = 3;
let timerInterval;
let timeLeft = 15;
let audioCtx;

function playSound(type) {
    if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    if (audioCtx.state === 'suspended') audioCtx.resume();
    const osc = audioCtx.createOscillator();
    const gainNode = audioCtx.createGain();
    osc.connect(gainNode);
    gainNode.connect(audioCtx.destination);
    
    if (type === 'correct') {
        osc.type = 'sine';
        osc.frequency.setValueAtTime(440, audioCtx.currentTime);
        osc.frequency.exponentialRampToValueAtTime(880, audioCtx.currentTime + 0.1);
        gainNode.gain.setValueAtTime(0.5, audioCtx.currentTime);
        gainNode.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.3);
        osc.start(); osc.stop(audioCtx.currentTime + 0.3);
    } else if (type === 'incorrect') {
        osc.type = 'sawtooth';
        osc.frequency.setValueAtTime(300, audioCtx.currentTime);
        osc.frequency.exponentialRampToValueAtTime(150, audioCtx.currentTime + 0.2);
        gainNode.gain.setValueAtTime(0.5, audioCtx.currentTime);
        gainNode.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.2);
        osc.start(); osc.stop(audioCtx.currentTime + 0.2);
    } else if (type === 'win') {
        osc.type = 'square';
        osc.frequency.setValueAtTime(400, audioCtx.currentTime);
        osc.frequency.setValueAtTime(600, audioCtx.currentTime + 0.1);
        osc.frequency.setValueAtTime(800, audioCtx.currentTime + 0.2);
        gainNode.gain.setValueAtTime(0.3, audioCtx.currentTime);
        gainNode.gain.linearRampToValueAtTime(0.01, audioCtx.currentTime + 0.5);
        osc.start(); osc.stop(audioCtx.currentTime + 0.5);
    }
}

function createParticles() {
    const container = document.getElementById('particles-container');
    if(!container) return;
    container.innerHTML = '';
    for(let i=0; i<30; i++) {
        const p = document.createElement('div');
        p.className = 'particle';
        const size = Math.random() * 8 + 2;
        p.style.width = size + 'px';
        p.style.height = size + 'px';
        p.style.left = Math.random() * 100 + 'vw';
        p.style.setProperty('--pd', (Math.random() * 3 + 4) + 's');
        p.style.animationDelay = (Math.random() * 5) + 's';
        container.appendChild(p);
    }
}

function triggerConfetti() {
    const canvas = document.getElementById('confetti-canvas');
    if(!canvas) return;
    const ctx = canvas.getContext('2d');
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    let particles = [];
    for(let i=0; i<150; i++) {
        particles.push({
            x: Math.random() * canvas.width,
            y: Math.random() * canvas.height - canvas.height,
            w: Math.random() * 10 + 5,
            h: Math.random() * 10 + 5,
            c: `hsl(${Math.random()*360}, 100%, 50%)`,
            vy: Math.random() * 3 + 2,
            vx: Math.random() * 4 - 2,
            rot: Math.random() * 360,
            rotSpeed: Math.random() * 10 - 5
        });
    }
    function draw() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        let active = 0;
        particles.forEach(p => {
            if(p.y < canvas.height) active++;
            p.y += p.vy; p.x += p.vx; p.rot += p.rotSpeed;
            ctx.save();
            ctx.translate(p.x, p.y);
            ctx.rotate(p.rot * Math.PI / 180);
            ctx.fillStyle = p.c;
            ctx.fillRect(-p.w/2, -p.h/2, p.w, p.h);
            ctx.restore();
        });
        if(active > 0) requestAnimationFrame(draw);
        else ctx.clearRect(0,0,canvas.width,canvas.height);
    }
    requestAnimationFrame(draw);
}
"""

content = re.sub(r'// Quiz state.*const QUESTIONS_PER_SESSION = 6;', state_elements, content, flags=re.DOTALL)


# 3. showQuestion reset timer

show_question = """    // Reset feedback
    feedbackElement.textContent = '';
    answered = false;
    
    // Timer reset
    clearInterval(timerInterval);
    timeLeft = 15;
    timerFill.textContent = timeLeft;
    if(timerWrapper) timerWrapper.classList.remove('danger');
    
    timerInterval = setInterval(() => {
        if(answered) {
            clearInterval(timerInterval);
            return;
        }
        timeLeft--;
        timerFill.textContent = timeLeft;
        if(timeLeft <= 5 && timerWrapper) {
            timerWrapper.classList.add('danger');
        }
        if(timeLeft <= 0) {
            clearInterval(timerInterval);
            timerFill.textContent = "0";
            selectOption(-1, null); // Time's up!
        }
    }, 1000);"""

content = content.replace("    // Reset feedback\n    feedbackElement.textContent = '';\n    answered = false;", show_question, 1)

# 4. Handle Option Selection Additions
select_logic_old = """    // Apply visual feedback
    buttons[optionIndex].classList.add(isCorrect ? 'correct' : 'incorrect');

    // Highlight correct answer
    if (!isCorrect) {
        buttons.forEach((btn) => {
            if (btn.textContent === correctAnswer) {
                btn.classList.add('correct');
            }
        });
    } else {
        correctAnswers++;
    }

    // Show feedback message
    feedbackElement.textContent = isCorrect ? '✅ ¡Correcto!' : '❌ Incorrecto';
    feedbackElement.style.color = isCorrect ? '#16a34a' : '#dc2626';

    // Move to next question after delay
    setTimeout(() => {
        currentQuestionIndex++;

        if (currentQuestionIndex < currentQuizData.length) {
            showQuestion();
        } else {
            // Show results screen
            showResults();
        }
    }, 1500);
"""

select_logic_new = """    // Time up condition
    if(optionIndex === -1) {
        isCorrect = false;
        feedbackElement.textContent = '⏰ ¡Se acabó el tiempo!';
        feedbackElement.style.color = '#dc2626';
        buttons.forEach((btn) => {
            if (btn.textContent === correctAnswer) {
                btn.classList.add('correct');
            }
        });
    } else {
        // Apply visual feedback
        buttons[optionIndex].classList.add(isCorrect ? 'correct' : 'incorrect');
        // Highlight correct answer
        if (!isCorrect) {
            buttons.forEach((btn) => {
                if (btn.textContent === correctAnswer) {
                    btn.classList.add('correct');
                }
            });
        } else {
            correctAnswers++;
        }
        // Show feedback message
        feedbackElement.textContent = isCorrect ? '✅ ¡Correcto!' : '❌ Incorrecto';
        feedbackElement.style.color = isCorrect ? '#16a34a' : '#dc2626';
    }

    // Sound and Gamification
    if (isCorrect) {
        playSound('correct');
        document.body.classList.add('state-correct');
    } else {
        playSound('incorrect');
        document.body.classList.add('state-incorrect');
        lives--;
        if (lives >= 0 && hearts[lives]) {
            hearts[lives].classList.remove('active');
            hearts[lives].classList.add('lost');
        }
    }

    setTimeout(() => {
        document.body.classList.remove('state-correct');
        document.body.classList.remove('state-incorrect');
    }, 1000);

    // Move to next question after delay
    setTimeout(() => {
        if (lives <= 0) {
            showResults(true); // Game over early
            return;
        }

        currentQuestionIndex++;

        if (currentQuestionIndex < currentQuizData.length) {
            showQuestion();
        } else {
            // Show results screen
            showResults();
        }
    }, 1500);
"""

content = content.replace(select_logic_old, select_logic_new)

# 5. ShowResults Fixes
show_results = """// Show results screen
function showResults(gameOver = false) {
    document.querySelector('.card').style.display = 'none';
    resultsScreen.style.display = 'block';
    
    clearInterval(timerInterval);
    
    if (gameOver) {
        playSound('incorrect');
        document.querySelector('#results-screen h2').textContent = '¡Juego Terminado!';
        feedbackElement.textContent = 'Te has quedado sin corazones.';
    } else {
        playSound('win');
        triggerConfetti();
        document.querySelector('#results-screen h2').textContent = '¡Trivia Completada!';
    }
    
    correctCountElement.textContent = correctAnswers;
}

// Restart quiz
function restartQuiz() {
    currentQuestionIndex = 0;
    answered = false;
    correctAnswers = 0;
    currentQuizData = [];
    resultsScreen.style.display = 'none';
    document.querySelector('.card').style.display = 'block';

    // Gamification resets
    lives = 3;
    hearts.forEach(h => {
        h.classList.remove('lost');
        h.classList.add('active');
    });

    // Pick new random questions again
    initQuiz();
}
"""

content = re.sub(r'// Show results screen.*// Restart quiz\nfunction restartQuiz.*?\n}', show_results, content, flags=re.DOTALL)

# add create particles call
content = content.replace("window.onload = initQuiz;", "window.onload = () => {\n    initQuiz();\n    createParticles();\n};")

with open("script.js", "w", encoding="utf-8") as f:
    f.write(content)

print("Patch applied to script.js")
