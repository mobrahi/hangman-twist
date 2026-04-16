def display_word(word, guessed_letters):
    """Show the word with unguessed letters as _"""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def show_health_bar(attempts_left, max_attempts):
    """Display health bar instead of hangman"""
    filled = attempts_left
    empty = max_attempts - attempts_left
    bar = "❤️ " * filled + "🖤 " * empty
    return bar.strip()

def get_unique_letters(word):
    """Return count of unique letters in word"""
    return len(set(word))

def save_high_score(name, score):
    """Save high score to file"""
    try:
        with open("high_scores.txt", "a") as file:
            file.write(f"{name},{score}\n")
    except Exception as e:
        print(f"Could not save score: {e}")

def load_high_scores():
    """Load and sort high scores"""
    scores = []
    try:
        with open("high_scores.txt", "r") as file:
            for line in file:
                if line.strip():
                    name, score = line.strip().split(",")
                    scores.append((name, int(score)))
        # Sort by score (highest first)
        scores.sort(key=lambda x: x[1], reverse=True)
        return scores
    except FileNotFoundError:
        return []
    except Exception as e:
        print(f"Could not load scores: {e}")
        return []