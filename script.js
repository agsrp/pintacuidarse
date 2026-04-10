// Dataset of all questions
const allQuestions = [
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
    },
    // New Questions Added
    {
        id: 7,
        question: "¿Qué se recomienda hacer si un amigo/a decide no beber alcohol durante la noche?",
        options: [
            "Insistirle constantemente para que tome \"aunque sea un trago\" y no se aburra.",
            "Respetar su decisión y asegurar que el grupo lo integre igual en todas las actividades.",
            "Dejar que se encargue de cuidar las pertenencias de todos por no estar bebiendo."
        ],
        answer: "Respetar su decisión y asegurar que el grupo lo integre igual en todas las actividades."
    },
    {
        id: 8,
        question: "¿Qué se recomienda hacer antes de salir para cuidar al grupo de amigos?",
        options: [
            "Establecer un punto de encuentro y asegurarse de tener batería en el celular.",
            "No hablar de los riesgos para no \"quemar\" la noche.",
            "Que cada uno se maneje por su cuenta y se encuentren adentro."
        ],
        answer: "Establecer un punto de encuentro y asegurarse de tener batería en el celular."
    },
    {
        id: 9,
        question: "¿Cómo afecta la mezcla de diferentes bebidas alcohólicas al organismo?",
        options: [
            "Las mezclas anulan el efecto del alcohol y te mantienen sobrio.",
            "No cambia nada, solo importa el gusto de la bebida.",
            "Puede aumentar la irritación gástrica y acelerar la sensación de malestar o mareo."
        ],
        answer: "Puede aumentar la irritación gástrica y acelerar la sensación de malestar o mareo."
    },
    {
        id: 10,
        question: "Ante una situación de riesgo o una emergencia médica por consumo en una fiesta, ¿qué es lo más importante?",
        options: [
            "Pedir ayuda médica de inmediato y no dejar sola a la persona.",
            "Darle de comer algo dulce o darle café negro para que se despierte.",
            "Esperar un par de horas a que se le pase solo antes de avisar a alguien."
        ],
        answer: "Pedir ayuda médica de inmediato y no dejar sola a la persona."
    },
    {
        id: 11,
        question: "¿Por qué es importante comer algo antes de empezar a beber alcohol?",
        options: [
            "Para que el alcohol se absorba más lentamente en el torrente sanguíneo.",
            "Para evitar tener hambre durante la madrugada.",
            "Para que el cuerpo no necesite tomar agua después."
        ],
        answer: "Para que el alcohol se absorba más lentamente en el torrente sanguíneo."
    },
    {
        id: 12,
        question: "Sobre el consentimiento en la salud sexual, ¿cuál de estas afirmaciones es correcta?",
        options: [
            "Si alguien dijo que sí una vez, significa que siempre dirá que sí.",
            "El consentimiento debe ser libre, informado, específico y reversible.",
            "El silencio o la falta de resistencia se consideran un \"sí\"."
        ],
        answer: "El consentimiento debe ser libre, informado, específico y reversible."
    },
    {
        id: 13,
        question: "¿Qué efecto produce el alcohol en los reflejos de un conductor?",
        options: [
            "Los vuelve más agudos y rápidos por la euforia.",
            "No produce ningún cambio si la persona está acostumbrada a beber.",
            "Realentiza el tiempo de reacción y disminuye la capacidad de atención."
        ],
        answer: "Realentiza el tiempo de reacción y disminuye la capacidad de atención."
    },
    {
        id: 14,
        question: "¿A dónde se puede acudir para obtener preservativos de forma gratuita en Argentina?",
        options: [
            "Solo se consiguen en farmacias con receta médica.",
            "En hospitales públicos, centros de salud y diversos puntos de salud territorial.",
            "Únicamente en las sedes del Ministerio de Salud en la capital."
        ],
        answer: "En hospitales públicos, centros de salud y diversos puntos de salud territorial."
    },
    {
        id: 15,
        question: "¿Qué significa la \"reducción de daños\" en el contexto de las salidas nocturnas?",
        options: [
            "Prohibir totalmente la entrada a lugares donde se venda alcohol.",
            "Aplicar estrategias para minimizar las consecuencias negativas del consumo.",
            "Ignorar el consumo y enfocarse solo en la música."
        ],
        answer: "Aplicar estrategias para minimizar las consecuencias negativas del consumo."
    },
    {
        id: 16,
        question: "Si durante una jornada alguien pregunta qué hacer si un preservativo se rompe, ¿cuál es la respuesta correcta sobre la anticoncepción de emergencia (pastilla del día después)?",
        options: [
            "Debe tomarse lo antes posible (preferentemente antes de las 12-24hs) para mayor efectividad.",
            "Solo es efectiva si se toma exactamente a los tres días del incidente.",
            "No es necesaria si la persona se siente bien y no tiene síntomas."
        ],
        answer: "Debe tomarse lo antes posible (preferentemente antes de las 12-24hs) para mayor efectividad."
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
let currentQuizData = [];
let currentQuestionIndex = 0;
let answered = false;
let correctAnswers = 0;
const QUESTIONS_PER_SESSION = 6;

// Utility function to shuffle an array (Fisher-Yates)
function shuffleArray(array) {
    const arr = [...array];
    for (let i = arr.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [arr[i], arr[j]] = [arr[j], arr[i]];
    }
    return arr;
}

// Initialize quiz
function initQuiz() {
    // 1. Shuffle all questions
    const shuffledQuestions = shuffleArray(allQuestions);

    // 2. Pick the first 6 questions for this session
    currentQuizData = shuffledQuestions.slice(0, QUESTIONS_PER_SESSION);

    // 3. Shuffle options for each selected question
    currentQuizData = currentQuizData.map(q => ({
        ...q,
        options: shuffleArray(q.options)
    }));

    totalQuestionsElement.textContent = currentQuizData.length;
    totalCountElement.textContent = currentQuizData.length;
    showQuestion();
}

// Display current question
function showQuestion() {
    const question = currentQuizData[currentQuestionIndex];

    // Update question text
    questionTextElement.textContent = question.question;

    // Update question number
    currentQuestionElement.textContent = currentQuestionIndex + 1;

    // Update progress bar
    const progressPercentage = ((currentQuestionIndex) / currentQuizData.length) * 100;
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
    const correctAnswer = currentQuizData[currentQuestionIndex].answer;

    // Disable all buttons during feedback
    buttons.forEach(btn => btn.disabled = true);

    // Check if answer is correct
    const isCorrect = selectedOption === correctAnswer;

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
    currentQuizData = [];
    resultsScreen.style.display = 'none';
    document.querySelector('.card').style.display = 'block';

    // Pick new 6 random questions again
    initQuiz();
}

// Event listeners
restartBtn.addEventListener('click', restartQuiz);

// Start the quiz when page loads
window.onload = initQuiz;
