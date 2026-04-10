import re

# Update index.html
try:
    with open("index.html", "r", encoding="utf-8") as f:
        html = f.read()

    # If it has not been patched yet
    if 'id="difficulty-screen"' not in html:
        # Rename "card" main to "quiz-card" if not already named
        html = re.sub(r'<main class="card">', '<main id="quiz-card" class="card" style="display: none;">', html)
        
        difficulty_html = """
    <div id="difficulty-screen" class="card" style="display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 15px;">
        <h2 class="score-title" style="margin-bottom: 20px;">Nivel de Dificultad</h2>
        <button class="option-btn difficulty-btn" data-mode="easy" style="background-color: rgba(74, 222, 128, 0.2); border-color: #4ade80; text-align: center;">
            🟢 Fácil (5 Vidas, 20s)
        </button>
        <button class="option-btn difficulty-btn" data-mode="medium" style="background-color: rgba(250, 204, 21, 0.2); border-color: #facc15; text-align: center;">
            🟡 Intermedio (3 Vidas, 15s)
        </button>
        <button class="option-btn difficulty-btn" data-mode="hard" style="background-color: rgba(248, 113, 113, 0.2); border-color: #f87171; text-align: center;">
            🔴 Difícil (2 Vidas, 10s)
        </button>
    </div>
    <main id="quiz-card" class="card" style="display: none;">"""
        html = html.replace('<main id="quiz-card" class="card" style="display: none;">', difficulty_html)
        
        # Empty lives-container
        html = re.sub(r'<div class="lives-container">.*?</div>', '<div id="lives-container" class="lives-container"></div>', html, flags=re.DOTALL)
        
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(html)
        print("index.html patched successfully.")
except Exception as e:
    print(f"Error patching index.html: {e}")

# Update script.js
try:
    with open("script.js", "r", encoding="utf-8") as f:
        js = f.read()

    if 'let questionsPerSession' not in js:
        # Variables
        js = js.replace('const QUESTIONS_PER_SESSION = 6;', 'let questionsPerSession = 6;\nlet totalLives = 3;\nlet timeLeftPerQuestion = 15;')
        js = js.replace('const hearts = document.querySelectorAll(\'#lives-container .heart\');', 'let hearts = [];\nconst livesContainer = document.getElementById(\'lives-container\');\nconst difficultyScreen = document.getElementById(\'difficulty-screen\');\nconst quizCard = document.getElementById(\'quiz-card\');')
        
        # Select Option and Timer
        js = js.replace('lives = 3;', 'lives = totalLives;\n    livesContainer.innerHTML = "";\n    hearts = [];\n    for(let i=0; i<totalLives; i++) {\n        const heart = document.createElement("span");\n        heart.className = "heart active";\n        heart.textContent = "❤️";\n        livesContainer.appendChild(heart);\n        hearts.push(heart);\n    }')
        js = js.replace('timeLeft = 15;', 'timeLeft = timeLeftPerQuestion;')
        js = js.replace('currentQuestionIndex < currentQuizData.length', 'currentQuestionIndex < questionsPerSession')
        js = re.sub(r'currentQuizData = shuffledQuiz\.slice\(0, 6\);', 'currentQuizData = shuffledQuiz.slice(0, questionsPerSession);', js)
        
        # Window onload
        start_game_logic = """
// Difficulty selection
document.querySelectorAll('.difficulty-btn').forEach(btn => {
    btn.addEventListener('click', (e) => {
        const mode = e.currentTarget.getAttribute('data-mode');
        if (mode === 'easy') {
            totalLives = 5;
            timeLeftPerQuestion = 20;
            questionsPerSession = 5;
        } else if (mode === 'medium') {
            totalLives = 3;
            timeLeftPerQuestion = 15;
            questionsPerSession = 6;
        } else if (mode === 'hard') {
            totalLives = 2;
            timeLeftPerQuestion = 10;
            questionsPerSession = 10;
        }
        difficultyScreen.style.display = 'none';
        quizCard.style.display = 'block';
        restartQuiz();
    });
});

window.onload = () => {
    difficultyScreen.style.display = 'block';
    quizCard.style.display = 'none';
    createParticles();
};
"""
        js = re.sub(r'window\.onload = \(\) => \{[^}]*\};', start_game_logic, js, flags=re.DOTALL)
        
        # Results Show
        js = js.replace("document.querySelector('.card').style.display", "quizCard.style.display")
        
        # Restart logic
        js = js.replace("restartBtn.addEventListener('click', restartQuiz);", "restartBtn.addEventListener('click', () => {\n    resultsScreen.style.display = 'none';\n    difficultyScreen.style.display = 'block';\n});")
        js = js.replace("document.querySelector('#results-screen h2')", "document.querySelector('#results-screen h2')")
        
        with open("script.js", "w", encoding="utf-8") as f:
            f.write(js)
        print("script.js patched successfully.")
except Exception as e:
    print(f"Error patching script.js: {e}")
