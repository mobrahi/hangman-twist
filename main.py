import random
from game_data import words_db, hints_db
from utils import display_word, show_health_bar, get_unique_letters, save_high_score, load_high_scores

def main():
    print("🎉 WELCOME TO WORD GUESSER (HANGMAN WITH A TWIST) 🎉")
    print("-" * 50)
    
    # Show high scores
    high_scores = load_high_scores()
    if high_scores:
        print("\n🏆 TOP SCORES:")
        for i, (name, score) in enumerate(high_scores[:3], 1):
            print(f"   {i}. {name}: {score}")
    
    # Choose category
    print("\n📂 Choose a category:")
    categories = list(words_db.keys())
    for i, cat in enumerate(categories, 1):
        print(f"{i}. {cat}")
    
    while True:
        try:
            choice = int(input("\nEnter number: "))
            if 1 <= choice <= len(categories):
                category = categories[choice-1]
                break
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Enter a number.")
    
    # Select random word
    word = random.choice(words_db[category]).lower()
    unique_letters = get_unique_letters(word)
    
    # Game setup
    guessed_letters = []
    attempts = 6
    score = 100
    hint_used = False
    
    print(f"\n✅ Category: {category}")
    print(f"🎯 Word length: {len(word)} letters")
    print(f"🔢 Unique letters: {unique_letters}")
    print(f"💪 Health: 6 attempts | 💯 Starting score: {score}")
    
    # Main game loop
    while attempts > 0:
        print("\n" + "=" * 50)
        print(show_health_bar(attempts, 6))
        print(f"📊 Score: {score}")
        print(f"📝 Word: {display_word(word, guessed_letters)}")
        print(f"🔤 Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        
        # Check win
        if all(letter in guessed_letters for letter in word):
            print("\n🎉🎉🎉 CONGRATULATIONS! YOU WON! 🎉🎉🎉")
            bonus = unique_letters * 10 if not hint_used else 0
            score += bonus
            print(f"✨ Bonus for no hints: +{bonus}")
            print(f"🏆 Final Score: {score}")
            
            # Save score
            player_name = input("\nEnter your name for high score: ").strip()
            save_high_score(player_name, score)
            break
        
        # Ask for guess
        print("\nOptions:")
        print("  1. Guess a letter")
        print("  2. Guess the whole word")
        print("  3. 💡 Buy hint (costs 15 points)")
        
        action = input("Choose option (1/2/3): ").strip()
        
        if action == "1":
            guess = input("Guess a letter: ").lower().strip()
            
            if len(guess) != 1 or not guess.isalpha():
                print("❌ Please enter a single letter!")
                continue
            
            if guess in guessed_letters:
                print("⚠️ You already guessed that letter!")
                continue
            
            guessed_letters.append(guess)
            
            if guess in word:
                print("✅ Good guess!")
            else:
                attempts -= 1
                print(f"❌ Wrong! {attempts} attempts left.")
                score = max(0, score - 10)
        
        elif action == "2":
            word_guess = input("Guess the whole word: ").lower().strip()
            if word_guess == word:
                print("\n🎉🎉🎉 PERFECT! YOU GUESSED THE WORD! 🎉🎉🎉")
                bonus = 50 if not hint_used else 20
                score += bonus
                print(f"✨ Bonus: +{bonus}")
                print(f"🏆 Final Score: {score}")
                
                player_name = input("\nEnter your name for high score: ").strip()
                save_high_score(player_name, score)
                break
            else:
                attempts -= 2
                score = max(0, score - 20)
                print(f"❌ Wrong word! -2 attempts. {attempts} left.")
        
        elif action == "3":
            if score >= 15:
                if word in hints_db:
                    print(f"💡 HINT: {hints_db[word]}")
                    score -= 15
                    hint_used = True
                    print(f"💰 -15 points. Remaining score: {score}")
                else:
                    print("⚠️ No hint available for this word.")
            else:
                print("❌ Not enough points for a hint!")
        
        else:
            print("Invalid option. Choose 1, 2, or 3.")
        
        if attempts <= 0:
            print("\n💀 GAME OVER! You ran out of attempts. 💀")
            print(f"The word was: {word.upper()}")
            print(f"Final Score: {score}")

if __name__ == "__main__":
    main()