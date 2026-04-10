// Simulated dataset with provided questions
        // INTEGRACIÓN DE DATOS EXTERNOS: Reemplaza este array con tu JSON externo
        const quizData = [
            {
                id: 1,
                question: "¿Cuál es la forma correcta de guardar los preservativos para que no se dañen?",
                options: [
                    "En la billetera o el bolsillo del pantalón",
                    "En un lugar fresco, seco y lejos de la luz solar directa",
                    "En la guantera del auto"
                ],
                answer: "En un lugar fresco, seco y lejos de la luz solar directa"
            },
            {
                id: 2,
                question: "Si se usa lubricante junto con el preservativo de látex, este debe ser:",
                options: [
                    "Al aceite (como vaselina o crema de manos)",
                    "A base de agua",
                    "Cualquier tipo de lubricante es igual"
                ],
                answer: "A base de agua"
            },
            {
                id: 3,
                question: "Si un amigo/a tomó de más y se siente mal, ¿qué es lo primero que deberías hacer?",
                options: [
                    "Darle café fuerte o una ducha fría para que se despabile",
                    "Dejarlo solo en un lugar tranquilo para que duerma la siesta",
                    "No dejarlo solo, hidratarlo con agua y, si se duerme, ponerlo de costado (posición lateral de seguridad)"
                ],
                answer: "No dejarlo solo, hidratarlo con agua y, si se duerme, ponerlo de costado (posición lateral de seguridad)"
            },
            {
                id: 4,
                question: "Para reducir los riesgos del alcohol durante la noche, la estrategia más efectiva es:",
                options: [
                    "Tomar un vaso de agua por cada vaso de alcohol",
                    "Mezclar diferentes tipos de bebidas para que el efecto pase rápido",
                    "Tomar con el estómago vacío"
                ],
                answer: "Tomar un vaso de agua por cada vaso de alcohol"
            },
            {
                id: 5,
                question: "¿Cuál es la función principal del \"Conductor Designado\" en el grupo de amigos?",
                options: [
                    "Es el que elige la música y paga el estacionamiento",
                    "Es quien decide no tomar alcohol para llevar a todos a casa seguros",
                    "Es el que maneja más rápido para llegar antes"
                ],
                answer: "Es quien decide no tomar alcohol para llevar a todos a casa seguros"
            },
            {
                id: 6,
                question: "Si ves una situación de acoso o alguien se siente incómodo en el boliche, ¿qué podés hacer?",
                options: [
                    "No meterse, es un problema de pareja",
                    "Avisar al personal del lugar o acercarse a preguntar \"¿estás bien?\" para ofrecer apoyo",
                    "Fotear con el celular y subirlo a redes"
                ],
                answer: "Avisar al personal del lugar o acercarse a preguntar \"¿estás bien?\" para ofrecer apoyo"
            }
        ];

        // DOM elements
        const questionTextElement = document.getElementById('question-text');
        const optionsContainer = document.getElementById('options-container');
        const currentQuestionElement = document.getElementById('current-question');
        const totalQuestionsElement = document.getElementById('total-questions');
        const progressFill = document.getElementById('progress-fill');
        const feedbackElement = document.getElementById('feedback');
        const resultsScreen = document.getElementById('results-screen');
        const correctCountElement = document.getElementById('correct-count');
        const totalCountElement = document.getElementById('total-count');
        const restartBtn = document.getElementById('restart-btn');

        // Quiz state
        let currentQuestionIndex = 0;
        let answered = false;
        let correctAnswers = 0;

        // Initialize quiz
        function initQuiz() {
            totalQuestionsElement.textContent = quizData.length;
            totalCountElement.textContent = quizData.length;
            showQuestion();
        }

        // Display current question
        function showQuestion() {
            const question = quizData[currentQuestionIndex];

            // Update question text
            questionTextElement.textContent = question.question;

            // Update question number
            currentQuestionElement.textContent = currentQuestionIndex + 1;

            // Update progress bar
            const progressPercentage = ((currentQuestionIndex) / quizData.length) * 100;
            progressFill.style.width = `${progressPercentage}%`;

            // Clear previous options
            optionsContainer.innerHTML = '';

            // Create option buttons
            question.options.forEach((option, index) => {
                const button = document.createElement('button');
                button.classList.add('option-btn');
                button.textContent = option;
                button.addEventListener('click', () => selectOption(index, option));
                optionsContainer.appendChild(button);
            });

            // Reset feedback
            feedbackElement.textContent = '';
            answered = false;
        }

        // Handle option selection
        function selectOption(optionIndex, selectedOption) {
            if (answered) return;

            answered = true;

            const buttons = optionsContainer.querySelectorAll('.option-btn');
            const correctAnswer = quizData[currentQuestionIndex].answer;

            // Disable all buttons during feedback
            buttons.forEach(btn => btn.disabled = true);

            // Check if answer is correct
            const isCorrect = selectedOption === correctAnswer;

            // Apply visual feedback
            buttons[optionIndex].classList.add(isCorrect ? 'correct' : 'incorrect');

            // Highlight correct answer
            if (!isCorrect) {
                buttons.forEach((btn, idx) => {
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

                if (currentQuestionIndex < quizData.length) {
                    showQuestion();
                } else {
                    // Show results screen
                    showResults();
                }
            }, 1500);
        }

        // Show results screen
        function showResults() {
            document.querySelector('.card').style.display = 'none';
            resultsScreen.style.display = 'block';
            correctCountElement.textContent = correctAnswers;
        }

        // Restart quiz
        function restartQuiz() {
            currentQuestionIndex = 0;
            answered = false;
            correctAnswers = 0;
            resultsScreen.style.display = 'none';
            document.querySelector('.card').style.display = 'block';
            initQuiz();
        }

        // Event listeners
        restartBtn.addEventListener('click', restartQuiz);

        // Start the quiz when page loads
        window.onload = initQuiz;
