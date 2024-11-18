# *** Quiz Game ***

def load_questions():
    return [
        # General Knowledge questions
        {
            "question": "What is the capital of France?",
            "type": "multiple_choice",
            "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
            "answer": "C"
        },  # Paris is the capital of France.
        
        {
            "question": "Which planet in our solar system is known as the Red Planet?",
            "type": "multiple_choice",
            "options": ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
            "answer": "B"
        },  # Mars is known as the Red Planet due to its reddish appearance.
        
        {
            "question": "Who wrote 'Romeo and Juliet'?",
            "type": "multiple_choice",
            "options": ["A. William Shakespeare", "B. Mark Twain", "C. Charles Dickens", "D. Jane Austen"],
            "answer": "A"
        },  # William Shakespeare is the author of 'Romeo and Juliet'.
        
        {
            "question": "What is the value of the mathematical constant 'π' (pi) up to two decimal places?",
            "type": "numeric",
            "answer": 3.14,
            "tolerance": 0.01
        },  # Pi (π) is approximately 3.14 up to two decimal places.
        
        # Algebra Question
        {
            "question": "What is the value of y if y/3 = 9?",
            "type": "numeric",
            "answer": 27
        },  # Solving y/3 = 9 gives y = 9 * 3 = 27.
        
        # Geometry Questions
        {
            "question": "What is the area of a circle with radius 7 units up to three decimal places?",
            "type": "numeric",
            "answer": 153.938,
            "tolerance": 0.01  # Allow slight deviation due to rounding
        },  # Area = π * r^2 = π * 7^2 ≈ 153.938 units squared.
        
        {
            "question": "Calculate the hypotenuse of a right-angled triangle with sides 3 and 4 units.",
            "type": "numeric",
            "answer": 5
        },  # Using Pythagoras' theorem: hypotenuse = √(3^2 + 4^2) = 5.
        
        # Trigonometry Questions
        {
            "question": "What is sin(30°)?",
            "type": "numeric",
            "answer": 0.5,
            "tolerance": 0.01
        },  # sin(30°) equals 0.5.
        
        {
            "question": "Find the value of tan(45°).",
            "type": "numeric",
            "answer": 1
        },  # tan(45°) equals 1.
        
        # Calculus Questions
        {
            "question": "What is the derivative of f(x) = x²?",
            "type": "short_answer",
            "answer": "2x"
        },  # The derivative of x² with respect to x is 2x.
        
        {
            "question": "Compute the integral of f(x) = 3x.",
            "type": "short_answer",
            "answer": "1.5x^2 + C"
        },  # The integral of 3x dx is (3x²)/2 + C = 1.5x² + C.
        
        # Probability Question
        {
            "question": "If a fair coin is flipped twice, what is the probability of getting two heads?",
            "type": "numeric",
            "answer": 0.25,
            "tolerance": 0.01
        },  # Probability = 0.5 (first head) * 0.5 (second head) = 0.25.
        
        # Computer Science Questions
        {
            "question": "Which programming language is known for its use in data analysis and statistical computing?",
            "type": "multiple_choice",
            "options": ["A. Python", "B. R", "C. Java", "D. C++"],
            "answer": "B"
        },  # R is specifically designed for statistical analysis and graphics.
        
        {
            "question": "Which programming paradigm is focused on the concept of 'objects' containing data and methods?",
            "type": "multiple_choice",
            "options": ["A. Procedural Programming", "B. Functional Programming", "C. Object-Oriented Programming", "D. Logical Programming"],
            "answer": "C"
        },  # Object-Oriented Programming centers around objects with data and methods.
        
        {
            "question": "In computer science, what does 'CPU' stand for?",
            "type": "multiple_choice",
            "options": ["A. Central Process Unit", "B. Computer Processing Unit", "C. Central Processing Unit", "D. Core Processing Unit"],
            "answer": "C"
        },  # CPU stands for Central Processing Unit.
        
        {
            "question": "What data structure uses a FIFO (First In, First Out) methodology?",
            "type": "multiple_choice",
            "options": ["A. Stack", "B. Queue", "C. Tree", "D. Graph"],
            "answer": "B"
        },  # A queue operates on a First In, First Out basis.
        
        {
            "question": "True or False: The Big O notation describes the worst-case scenario of an algorithm's time or space complexity.",
            "type": "true_false",
            "answer": "True"
        },  # Big O notation represents the upper bound of an algorithm's complexity.
        
        {
            "question": "What is the time complexity of binary search in a sorted array?",
            "type": "multiple_choice",
            "options": ["A. O(n)", "B. O(log n)", "C. O(n log n)", "D. O(1)"],
            "answer": "B"
        },  # Binary search has a time complexity of O(log n).
        
        # Philosophy Questions
        {
            "question": "True or False: René Descartes is famous for the quote 'I think, therefore I am.'",
            "type": "true_false",
            "answer": "True"
        },  # Descartes coined the phrase "Cogito, ergo sum" meaning "I think, therefore I am."
        
        {
            "question": "Which philosopher is known for the allegory of the cave?",
            "type": "multiple_choice",
            "options": ["A. Aristotle", "B. Plato", "C. Socrates", "D. Descartes"],
            "answer": "B"
        }  # Plato presented the allegory of the cave in 'The Republic.'
    ]





def play_quiz():
    questions = load_questions()
    score = 0

    for q in questions:
        print("\n" + q["question"])
        
        if q["type"] == "multiple_choice":
            for option in q["options"]:
                print(option)
            answer = input("Your answer: ").strip().upper()
            correct = answer == q["answer"]
        
        elif q["type"] == "numeric":
            while True:
                try:
                    answer = float(input("Your answer (enter a number): ").strip())
                    correct = answer == q["answer"]
                    break
                except ValueError:
                    print("Please enter a valid number.")
        
        elif q["type"] == "true_false":
            answer = input("Your answer (True/False): ").strip().capitalize()
            correct = answer == q["answer"]
        
        else:
            # Handle other types or default behavior
            answer = input("Your answer: ").strip()
            correct = answer.lower() == q["answer"].lower()
        
        if correct:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect! The correct answer was {q['answer']}.")
    
    print(f"\nQuiz Over! Your final score is {score}/{len(questions)}.")

play_quiz()
