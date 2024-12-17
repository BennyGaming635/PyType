import time
import random
import os
import datetime

sentences = {
    "easy": [
        "The quick brown fox jumps over the lazy dog.",
        "Python is fun.",
        "Typing is a skill.",
        "Keep practicing to get better."
    ],
    "medium": [
        "Python is a versatile programming language used worldwide.",
        "Practice typing to improve your speed and accuracy.",
        "Coding challenges help us think critically and solve problems.",
        "A good programmer writes clean, efficient, and effective code."
    ],
    "hard": [
        "The juxtaposition of programming paradigms fosters innovation in coding.",
        "Asynchronous functions in Python simplify multitasking without blocking operations.",
        "To err is human, but to debug is divine, so keep honing your coding skills.",
        "Object-oriented programming in Python promotes reusability and modularity in design."
    ]
}

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def get_random_sentence(difficulty):
    return random.choice(sentences[difficulty])

def calculate_wpm(start_time, end_time, num_words):
    elapsed_time = end_time - start_time
    minutes = elapsed_time / 60
    wpm = num_words / minutes
    return round(wpm)

def calculate_accuracy(user_input, original_sentence):
    correct_chars = sum(1 for i, j in zip(user_input, original_sentence) if i == j)
    total_chars = len(original_sentence)
    accuracy = (correct_chars / total_chars) * 100
    return round(accuracy, 2)

def save_streak(streak_count):
    with open("streak.txt", "w") as file:
        file.write(str(streak_count))

def load_streak():
    if os.path.exists("streak.txt"):
        with open("streak.txt", "r") as file:
            return int(file.read().strip())
    return 0

def load_daily_challenge():
    date_today = datetime.datetime.now().strftime("%Y-%m-%d")
    challenge_file = "daily_challenge.txt"

    if os.path.exists(challenge_file):
        with open(challenge_file, "r") as file:
            saved_date, sentence = file.read().split("|", 1)
            if saved_date == date_today:
                return sentence

    sentence = get_random_sentence("medium")
    with open(challenge_file, "w") as file:
        file.write(f"{date_today}|{sentence}")
    return sentence

def save_daily_result(wpm, accuracy):
    with open("daily_results.txt", "a") as file:
        file.write(f"{datetime.datetime.now()} - WPM: {wpm}, Accuracy: {accuracy}%\n")

def typing_with_distractions(sentence):
    clear_screen()
    print("\n🚨 Expert Mode - Typing With Distractions! 🚨\n")
    print("Type this sentence (good luck!):\n")
    print(f"{sentence}\n")
    input("Press Enter when you are ready to start typing...")

    start_time = time.time()
    user_input = ""
    for char in sentence:
        print(char, end="", flush=True)
        time.sleep(random.uniform(0.05, 0.2))
        if random.random() < 0.1:
            clear_screen()  # Screen flicker
            print("⚡ Whoops, screen glitch! Keep typing! ⚡\n")
            print(f"{sentence}\n")
    user_input = input("\nStart typing: ")
    end_time = time.time()

    num_words = len(sentence.split())
    wpm = calculate_wpm(start_time, end_time, num_words)
    accuracy = calculate_accuracy(user_input, sentence)

    print("\n⏱️ Test Results:")
    print(f"✅ Words Per Minute (WPM): {wpm}")
    print(f"🎯 Accuracy: {accuracy}%")
    print(f"⏳ Time Taken: {round(end_time - start_time, 2)} seconds")

    if user_input.strip() != sentence.strip():
        print("\n🔍 Mistakes detected! Practice makes perfect.")
    return accuracy >= 80

def daily_challenge():
    clear_screen()
    print("\n📅 Daily Challenge - Test Your Skills! 📅\n")
    sentence = load_daily_challenge()
    print(f"💬 Today's Challenge:\n\n{sentence}\n")

    input("Press Enter when you are ready to start typing...")
    start_time = time.time()
    user_input = input("\nStart typing: ")
    end_time = time.time()

    num_words = len(sentence.split())
    wpm = calculate_wpm(start_time, end_time, num_words)
    accuracy = calculate_accuracy(user_input, sentence)

    print("\n⏱️ Test Results:")
    print(f"✅ Words Per Minute (WPM): {wpm}")
    print(f"🎯 Accuracy: {accuracy}%")
    print(f"⏳ Time Taken: {round(end_time - start_time, 2)} seconds")

    save_daily_result(wpm, accuracy)
    print("\n📊 Results saved! Check your progress in 'daily_results.txt'.")

def typing_speed_test(difficulty):
    clear_screen()
    print(f"\n🚀 PyType - {difficulty.capitalize()} Mode 🚀\n")
    sentence = get_random_sentence(difficulty)
    print(f"💬 Type this sentence:\n\n{sentence}\n")

    input("Press Enter when you are ready to start typing...")

    start_time = time.time()
    user_input = input("\nStart typing: ")
    end_time = time.time()

    num_words = len(sentence.split())
    wpm = calculate_wpm(start_time, end_time, num_words)
    accuracy = calculate_accuracy(user_input, sentence)

    print("\n⏱️ Test Results:")
    print(f"✅ Words Per Minute (WPM): {wpm}")
    print(f"🎯 Accuracy: {accuracy}%")
    print(f"⏳ Time Taken: {round(end_time - start_time, 2)} seconds")

    if user_input.strip() != sentence.strip():
        print("\n🔍 Mistakes detected! Practice makes perfect.")
    return accuracy >= 80

def main():
    streak_count = load_streak()

    while True:
        clear_screen()
        print("\n🚀 Welcome to PyType 🚀\n")
        print(f"🔥 Current Streak: {streak_count} days 🔥")
        print("\nSelect Mode:")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")
        print("4. Daily Challenge")
        print("5. Typing With Distractions")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")
        if choice == "1":
            difficulty = "easy"
            success = typing_speed_test(difficulty)
        elif choice == "2":
            difficulty = "medium"
            success = typing_speed_test(difficulty)
        elif choice == "3":
            difficulty = "hard"
            success = typing_speed_test(difficulty)
        elif choice == "4":
            daily_challenge()
            success = True
        elif choice == "5":
            sentence = get_random_sentence("hard")
            success = typing_with_distractions(sentence)
        elif choice == "6":
            print("\n👋 Thanks for using PyType! Goodbye!\n")
            break
        else:
            print("\n❌ Invalid choice. Please select 1-6.")
            time.sleep(2)
            continue

        if success:
            print("\n🎉 Well done! Your accuracy was above 80%! Streak continues. 🔥")
            streak_count += 1
        else:
            print("\n😢 Accuracy below 80%. Streak reset. Keep practicing!")
            streak_count = 0
        save_streak(streak_count)

if __name__ == "__main__":
    main()
