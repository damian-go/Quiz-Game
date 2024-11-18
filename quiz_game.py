def load_questions():
    return [
        # General Knowledge Questions
        {
            "question": "What is the capital of France?",
            "type": "multiple_choice",
            "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
            "answer": "C",
            "category": "General Knowledge",
            "difficulty": "Easy",
            "points": 1,
            "explanation": "Paris is the capital city of France."
        },
        {
            "question": "Which planet in our solar system is known as the Red Planet?",
            "type": "multiple_choice",
            "options": ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
            "answer": "B",
            "category": "General Knowledge",
            "difficulty": "Easy",
            "points": 1,
            "explanation": "Mars is called the Red Planet due to its reddish appearance."
        },
        {
            "question": "Who wrote 'Romeo and Juliet'?",
            "type": "multiple_choice",
            "options": ["A. William Shakespeare", "B. Mark Twain", "C. Charles Dickens", "D. Jane Austen"],
            "answer": "A",
            "category": "General Knowledge",
            "difficulty": "Easy",
            "points": 1,
            "explanation": "William Shakespeare is the author of 'Romeo and Juliet'."
        },
        {
            "question": "What is the largest ocean on Earth?",
            "type": "multiple_choice",
            "options": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"],
            "answer": "D",
            "category": "General Knowledge",
            "difficulty": "Medium",
            "points": 2,
            "explanation": "The Pacific Ocean is the largest ocean on Earth."
        },
        {
            "question": "In which year did the Titanic sink?",
            "type": "numeric",
            "answer": 1912,
            "tolerance": 0,
            "category": "General Knowledge",
            "difficulty": "Medium",
            "points": 2,
            "explanation": "The Titanic sank on April 15, 1912."
        },
        # Mathematics Questions
        # Algebra Questions
        {
            "question": "What is the value of y if y/3 = 9?",
            "type": "numeric",
            "answer": 27,
            "tolerance": 0,
            "category": "Mathematics",
            "difficulty": "Easy",
            "points": 1,
            "explanation": "Solving y/3 = 9 gives y = 9 * 3 = 27."
        },
        {
            "question": "Solve for x: 2x - 5 = 9.",
            "type": "numeric",
            "answer": 7,
            "tolerance": 0,
            "category": "Mathematics",
            "difficulty": "Easy",
            "points": 1,
            "explanation": "Adding 5 to both sides gives 2x = 14; then x = 7."
        },
        # Geometry Questions
        {
            "question": "What is the area of a circle with radius 7 units (up to three decimal places)?",
            "type": "numeric",
            "answer": 153.938,
            "tolerance": 0.01,
            "category": "Mathematics",
            "difficulty": "Medium",
            "points": 2,
            "explanation": "Area = π * r² = π * 7² ≈ 153.938 units squared."
        },
        {
            "question": "Calculate the hypotenuse of a right-angled triangle with sides 3 and 4 units.",
            "type": "numeric",
            "answer": 5,
            "tolerance": 0,
            "category": "Mathematics",
            "difficulty": "Easy",
            "points": 1,
            "explanation": "Using Pythagoras' theorem: √(3² + 4²) = 5."
        },
        # Trigonometry Questions
        {
            "question": "What is sin(30°)?",
            "type": "numeric",
            "answer": 0.5,
            "tolerance": 0.01,
            "category": "Mathematics",
            "difficulty": "Medium",
            "points": 2,
            "explanation": "The sine of 30 degrees is 0.5."
        },
        {
            "question": "Find the value of tan(45°).",
            "type": "numeric",
            "answer": 1,
            "tolerance": 0.01,
            "category": "Mathematics",
            "difficulty": "Easy",
            "points": 1,
            "explanation": "The tangent of 45 degrees is 1."
        },
        {
            "question": "What is cos(60°)?",
            "type": "numeric",
            "answer": 0.5,
            "tolerance": 0.01,
            "category": "Mathematics",
            "difficulty": "Medium",
            "points": 2,
            "explanation": "The cosine of 60 degrees is 0.5."
        },
        # Calculus Questions
        {
            "question": "What is the derivative of f(x) = x²?",
            "type": "short_answer",
            "answer": "2x",
            "category": "Mathematics",
            "difficulty": "Easy",
            "points": 1,
            "explanation": "The derivative of x² with respect to x is 2x."
        },
        {
            "question": "Compute the integral of f(x) = 3x.",
            "type": "short_answer",
            "answer": "1.5x^2 + C",
            "category": "Mathematics",
            "difficulty": "Medium",
            "points": 2,
            "explanation": "The integral of 3x dx is (3x²)/2 + C."
        },
        {
            "question": "What is the derivative of f(x) = sin(x)?",
            "type": "short_answer",
            "answer": "cos(x)",
            "category": "Mathematics",
            "difficulty": "Medium",
            "points": 2,
            "explanation": "The derivative of sin(x) is cos(x)."
        },
        # Probability Questions
        {
            "question": "If a fair coin is flipped twice, what is the probability of getting two heads?",
            "type": "numeric",
            "answer": 0.25,
            "tolerance": 0.01,
            "category": "Mathematics",
            "difficulty": "Easy",
            "points": 1,
            "explanation": "Probability = 0.5 * 0.5 = 0.25."
        },
        {
            "question": "What is the probability of rolling a sum of 7 with two six-sided dice?",
            "type": "numeric",
            "answer": 0.1667,
            "tolerance": 0.01,
            "category": "Mathematics",
            "difficulty": "Medium",
            "points": 2,
            "explanation": "There are 6 favorable outcomes out of 36 total, so probability ≈ 0.1667."
        },
        # Computer Science Questions
        {
            "question": "Which programming language is known for its use in data analysis and statistical computing?",
            "type": "multiple_choice",
            "options": ["A. Python", "B. R", "C. Java", "D. C++"],
            "answer": "B",
            "category": "Computer Science",
            "difficulty": "Easy",
            "points": 1,
            "explanation": "R is designed for statistical analysis and graphical models."
        },
        {
            "question": "Which programming paradigm focuses on objects containing data and methods?",
            "type": "multiple_choice",
            "options": ["A. Procedural Programming", "B. Functional Programming", "C. Object-Oriented Programming", "D. Logical Programming"],
            "answer": "C",
            "category": "Computer Science",
            "difficulty": "Easy",
            "points": 1,
            "explanation": "Object-Oriented Programming centers around objects with data and methods."
        },
        {
            "question": "In computer science, what does 'CPU' stand for?",
            "type": "multiple_choice",
            "options": ["A. Central Process Unit", "B. Computer Processing Unit", "C. Central Processing Unit", "D. Core Processing Unit"],
            "answer": "C",
            "category": "Computer Science",
            "difficulty": "Easy",
            "points": 1,
            "explanation": "CPU stands for Central Processing Unit."
        },
        {
            "question": "What data structure uses a FIFO (First In, First Out) methodology?",
            "type": "multiple_choice",
            "options": ["A. Stack", "B. Queue", "C. Tree", "D. Graph"],
            "answer": "B",
            "category": "Computer Science",
            "difficulty": "Easy",
            "points": 1,
            "explanation": "A queue operates on a First In, First Out basis."
        },
        {
            "question": "True or False: The Big O notation describes the worst-case scenario of an algorithm's time or space complexity.",
            "type": "true_false",
            "answer": "True",
            "category": "Computer Science",
            "difficulty": "Medium",
            "points": 2,
            "explanation": "Big O notation represents the upper bound of an algorithm's complexity."
        },
        {
            "question": "What is the time complexity of binary search in a sorted array?",
            "type": "multiple_choice",
            "options": ["A. O(n)", "B. O(log n)", "C. O(n log n)", "D. O(1)"],
            "answer": "B",
            "category": "Computer Science",
            "difficulty": "Medium",
            "points": 2,
            "explanation": "Binary search has a time complexity of O(log n)."
        },
        {
            "question": "What does 'HTTP' stand for in web communication?",
            "type": "multiple_choice",
            "options": ["A. HyperText Transfer Protocol", "B. Hyperlink Text Transfer Protocol", "C. HyperText Transmission Protocol", "D. Hyperlink Transmission Protocol"],
            "answer": "A",
            "category": "Computer Science",
            "difficulty": "Easy",
            "points": 1,
            "explanation": "HTTP stands for HyperText Transfer Protocol."
        },
        {
            "question": "In Big O notation, what is the time complexity of the bubble sort algorithm in the average case?",
            "type": "multiple_choice",
            "options": ["A. O(n)", "B. O(n log n)", "C. O(n^2)", "D. O(log n)"],
            "answer": "C",
            "category": "Computer Science",
            "difficulty": "Medium",
            "points": 2,
            "explanation": "Bubble sort has an average time complexity of O(n²)."
        },
        # Philosophy Questions
        {
            "question": "True or False: René Descartes is famous for the quote 'I think, therefore I am.'",
            "type": "true_false",
            "answer": "True",
            "category": "Philosophy",
            "difficulty": "Easy",
            "points": 1,
            "explanation": "Descartes coined 'Cogito, ergo sum' meaning 'I think, therefore I am.'"
        },
        {
            "question": "Which philosopher is known for the allegory of the cave?",
            "type": "multiple_choice",
            "options": ["A. Aristotle", "B. Plato", "C. Socrates", "D. Descartes"],
            "answer": "B",
            "category": "Philosophy",
            "difficulty": "Easy",
            "points": 1,
            "explanation": "Plato presented the allegory in his work 'The Republic.'"
        },
        {
            "question": "Who is the philosopher known for the statement 'God is dead'?",
            "type": "multiple_choice",
            "options": ["A. Friedrich Nietzsche", "B. Immanuel Kant", "C. Søren Kierkegaard", "D. Jean-Paul Sartre"],
            "answer": "A",
            "category": "Philosophy",
            "difficulty": "Medium",
            "points": 2,
            "explanation": "Nietzsche proclaimed 'God is dead' to express the decline of religious and moral absolutes."
        },
        {
            "question": "True or False: Utilitarianism advocates for the greatest good for the greatest number.",
            "type": "true_false",
            "answer": "True",
            "category": "Philosophy",
            "difficulty": "Easy",
            "points": 1,
            "explanation": "Utilitarianism seeks to maximize overall happiness."
        },
        {
            "question": "Which philosopher is associated with the concept of the 'categorical imperative'?",
            "type": "multiple_choice",
            "options": ["A. Immanuel Kant", "B. John Locke", "C. David Hume", "D. Thomas Hobbes"],
            "answer": "A",
            "category": "Philosophy",
            "difficulty": "Medium",
            "points": 2,
            "explanation": "Kant introduced the 'categorical imperative' as a central philosophical concept."
        },
        # Additional General Knowledge Questions
        {
            "question": "What is the chemical symbol for gold?",
            "type": "short_answer",
            "answer": "Au",
            "category": "General Knowledge",
            "difficulty": "Easy",
            "points": 1,
            "explanation": "The symbol 'Au' comes from the Latin word 'Aurum' for gold."
        },
        {
            "question": "Who painted the Mona Lisa?",
            "type": "multiple_choice",
            "options": ["A. Vincent van Gogh", "B. Pablo Picasso", "C. Leonardo da Vinci", "D. Michelangelo"],
            "answer": "C",
            "category": "General Knowledge",
            "difficulty": "Easy",
            "points": 1,
            "explanation": "Leonardo da Vinci painted the Mona Lisa."
        },
        {
            "question": "What is the smallest prime number?",
            "type": "numeric",
            "answer": 2,
            "tolerance": 0,
            "category": "Mathematics",
            "difficulty": "Easy",
            "points": 1,
            "explanation": "2 is the smallest and the only even prime number."
        },
        # Additional Computer Science Questions
        {
            "question": "In object-oriented programming, what does 'encapsulation' refer to?",
            "type": "short_answer",
            "answer": "Grouping data and methods",
            "category": "Computer Science",
            "difficulty": "Medium",
            "points": 2,
            "explanation": "Encapsulation is bundling data with methods that operate on that data."
        },
        {
            "question": "What is the main purpose of a DNS server?",
            "type": "multiple_choice",
            "options": ["A. To translate domain names into IP addresses", "B. To manage email delivery", "C. To store website content", "D. To secure network communications"],
            "answer": "A",
            "category": "Computer Science",
            "difficulty": "Medium",
            "points": 2,
            "explanation": "DNS servers map domain names to their corresponding IP addresses."
        },
        # Additional Mathematics Question
        {
            "question": "What is the sum of the interior angles of a triangle?",
            "type": "numeric",
            "answer": 180,
            "tolerance": 0,
            "category": "Mathematics",
            "difficulty": "Easy",
            "points": 1,
            "explanation": "The interior angles of any triangle sum up to 180 degrees."
        },
        # Additional Philosophy Question
        {
            "question": "Which philosopher is known for the concept of 'Tabula Rasa' or blank slate?",
            "type": "multiple_choice",
            "options": ["A. John Locke", "B. René Descartes", "C. Thomas Hobbes", "D. David Hume"],
            "answer": "A",
            "category": "Philosophy",
            "difficulty": "Medium",
            "points": 2,
            "explanation": "John Locke proposed that the mind is a blank slate at birth."
        },
    ]





import random
import threading
import math

def play_quiz():
    questions = load_questions()

    # Category selection
    categories = list(set(q['category'] for q in questions))
    print("Available Categories:")
    for idx, category in enumerate(categories, 1):
        print(f"{idx}. {category}")
    choice = input("Select a category by number (or 0 for all): ")
    while not choice.isdigit() or int(choice) < 0 or int(choice) > len(categories):
        choice = input("Invalid input. Please enter a valid category number: ")
    choice = int(choice)
    if choice != 0:
        selected_category = categories[choice - 1]
        questions = [q for q in questions if q['category'] == selected_category]
    random.shuffle(questions)

    # Customize quiz length
    while True:
        try:
            num_questions = int(input("How many questions would you like to answer? "))
            if 1 <= num_questions <= len(questions):
                break
            else:
                print(f"Please enter a number between 1 and {len(questions)}.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    questions = questions[:num_questions]

    # Initialize score and streak
    total_possible_score = sum(q.get('points', 1) for q in questions)
    score = 0
    streak = 0
    max_streak = 0
    incorrect_questions = []
    lifelines = {'hint': 1, 'fifty_fifty': 1}

    for q in questions:
        print("\n" + q["question"])

        # Lifeline: 50/50
        if q["type"] == "multiple_choice" and lifelines['fifty_fifty'] > 0:
            use_lifeline = input("Do you want to use the 50/50 lifeline? (yes/no): ").strip().lower()
            if use_lifeline == 'yes':
                lifelines['fifty_fifty'] -= 1
                correct_option = q['answer']
                options = q['options']
                # Remove two incorrect options
                incorrect_options = [opt for opt in options if not opt.startswith(correct_option)]
                options_to_remove = random.sample(incorrect_options, 2)
                q['options'] = [opt for opt in options if opt not in options_to_remove]
                print("Options after 50/50 lifeline:")
                for option in q['options']:
                    print(option)
            else:
                for option in q['options']:
                    print(option)
        elif q["type"] == "multiple_choice":
            for option in q['options']:
                print(option)

        # Timer for each question
        def input_with_timeout(prompt, timeout):
            answer = [None]
            def get_input():
                answer[0] = input(prompt)
            thread = threading.Thread(target=get_input)
            thread.daemon = True
            thread.start()
            thread.join(timeout)
            if thread.is_alive():
                print("\nTime's up!")
                return None
            else:
                return answer[0]

        # Get user's answer
        if q["type"] in ["multiple_choice", "numeric", "true_false", "short_answer"]:
            answer = input_with_timeout("Your answer: ", timeout=15)  # 15-second timer
            if answer is None:
                correct = False
            else:
                answer = answer.strip()
                # Check the answer based on question type
                if q["type"] == "multiple_choice":
                    correct = answer.upper() == q["answer"]
                elif q["type"] == "numeric":
                    try:
                        user_answer = float(answer)
                        tolerance = q.get("tolerance", 0)
                        correct = math.isclose(user_answer, q["answer"], abs_tol=tolerance)
                    except ValueError:
                        correct = False
                elif q["type"] == "true_false":
                    correct = answer.capitalize() == q["answer"]
                elif q["type"] == "short_answer":
                    correct = answer.lower() == q["answer"].lower()
                else:
                    correct = False
        else:
            correct = False

        # Update score and streak
        if correct:
            points = q.get('points', 1)
            score += points
            streak += 1
            max_streak = max(max_streak, streak)
            print(f"Correct! You've earned {points} point(s).")
            print(f"Current streak: {streak}")
        else:
            streak = 0
            incorrect_questions.append(q)
            print(f"Incorrect! The correct answer was {q['answer']}.")
        # Provide explanation
        print(f"Explanation: {q.get('explanation', 'No explanation provided.')}")

    # Display final score and statistics
    accuracy = (score / total_possible_score) * 100
    print(f"\nQuiz Over! Your final score is {score}/{total_possible_score}.")
    print(f"Your accuracy was {accuracy:.2f}%.")
    print(f"Your longest streak was {max_streak} correct answers in a row.")

    # Offer to review incorrect answers
    if incorrect_questions:
        review = input("Do you want to review the incorrect answers? (yes/no): ").strip().lower()
        if review == 'yes':
            for q in incorrect_questions:
                print(f"\nQuestion: {q['question']}")
                print(f"Correct Answer: {q['answer']}")
                print(f"Explanation: {q.get('explanation', 'No explanation provided.')}")

play_quiz()
