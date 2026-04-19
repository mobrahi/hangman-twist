# 🎮 Word Guesser - Hangman with a Twist

[![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-macOS%20%7C%20Windows%20%7C%20Linux-lightgrey)]()

> A unique twist on the classic Hangman game with scoring, hints, health bars, and multiple categories!

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🎯 **Multiple Categories** | Choose from Animals, Fruits, Countries, or Movies |
| 💚 **Health Bar System** | Visual health indicator (❤️/🖤) instead of hangman |
| 📊 **Dynamic Scoring** | Start with 100 points, earn bonuses, lose points for mistakes |
| 💡 **Hint System** | Buy hints with points when you're stuck |
| 🎲 **Word Guessing** | Guess letters OR guess the entire word for bonus points |
| 🏆 **High Scores** | Save and view top scores across sessions |
| 🎨 **Colorful UI** | Enhanced visual experience with color support |

## 🎮 How to Play

1. **Choose a category** - Pick your favorite topic
2. **Guess letters** - Each correct letter reveals part of the word
3. **Watch your health** - Wrong guesses reduce your health bar
4. **Use hints wisely** - Hints cost points but can save the game
5. **Guess the word** - Try guessing the whole word for big bonus points
6. **Beat high scores** - Try to get the highest score possible!

### Game Controls

```
Option 1 - Guess a single letter
Option 2 - Guess the entire word  
Option 3 - Buy a hint (costs 15 points)
```

## 📊 Scoring System

| Action | Points Change |
|--------|---------------|
| Starting score | +100 |
| Wrong letter guess | -10 |
| Wrong word guess | -20 & -2 attempts |
| Buy a hint | -15 |
| Bonus for no hints | +10 per unique letter |
| Correct word guess | +50 |

### Example Score Calculation

```
Start: 100 points
Wrong letter (x2): -20 points
Use hint: -15 points  
Correct word guess: +50 points
Bonus (no hints used: 0)
Final Score: 115 points
```

## 🚀 Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package manager)
- Git (optional, for cloning)

### Quick Start (macOS / Linux)

```bash
# Clone the repository
git clone https://github.com/yourusername/hangman-twist.git
cd hangman-twist

# Run the game directly (no dependencies needed!)
python3 main.py
```

### With Virtual Environment (Recommended)

```bash
# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate  # On macOS/Linux
# OR
venv\Scripts\activate     # On Windows

# Install optional dependencies (for colored output)
pip install -r requirements.txt

# Run the game
python main.py
```

### Windows Users

```bash
# Clone or download the project
git clone https://github.com/yourusername/hangman-twist.git
cd hangman-twist

# Run the game
python main.py
```

## 📁 Project Structure

```
hangman-twist/
│
├── main.py              # Main game logic
├── game_data.py         # Words and hints database
├── utils.py             # Helper functions
├── high_scores.txt      # Saved scores (auto-generated)
├── requirements.txt     # Dependencies (optional)
├── .gitignore          # Git ignore rules
├── LICENSE             # MIT License
└── README.md           # Documentation
```

## 🎯 Game Preview

```
🎉 WELCOME TO WORD GUESSER (HANGMAN WITH A TWIST) 🎉
--------------------------------------------------

🏆 TOP SCORES:
   1. Alice: 145
   2. Bob: 120
   3. Charlie: 95

📂 Choose a category:
1. Animals
2. Fruits
3. Countries
4. Movies

Enter number: 1

✅ Category: Animals
🎯 Word length: 7 letters
🔢 Unique letters: 5
💪 Health: 6 attempts | 💯 Starting score: 100

==================================================
❤️ ❤️ ❤️ ❤️ ❤️ ❤️
📊 Score: 100
📝 Word: _ _ _ _ _ _ _
🔤 Guessed letters: None

Options:
  1. Guess a letter
  2. Guess the whole word
  3. 💡 Buy hint (costs 15 points)

Choose option (1/2/3): 1
Guess a letter: e

✅ Good guess!

==================================================
❤️ ❤️ ❤️ ❤️ ❤️ ❤️
📊 Score: 100
📝 Word: e _ e _ _ _ _
🔤 Guessed letters: e
```

## 🛠️ Customization

### Adding New Words

Edit `game_data.py` and add words to existing categories:

```python
words_db = {
    "Animals": ["elephant", "giraffe", "your_word_here"],
    # ... more categories
}
```

### Adding Hints

Add corresponding hints in `hints_db`:

```python
hints_db = {
    "your_word_here": "Your hint description here",
    # ... more hints
}
```

### Adding New Categories

```python
words_db = {
    "Your New Category": ["word1", "word2", "word3"],
    # ... existing categories
}
```

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| `python3: command not found` | Install Python 3 from [python.org](https://python.org) |
| No colors in output | Install colorama: `pip install colorama` |
| High scores not saving | Check write permissions in game folder |
| Unicode character errors | Set terminal to UTF-8 encoding |

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Commit your changes**
   ```bash
   git commit -m 'Add amazing feature'
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/amazing-feature
   ```
5. **Open a Pull Request**

### Ideas for Contributions

- 🎨 Add ASCII art for game over screens
- 🔊 Add sound effects for correct/incorrect guesses
- 🌐 Add more word categories (Space, Technology, Sports)
- 🎮 Create a GUI version with tkinter or Pygame
- 📱 Add multiplayer mode
- 🏆 Add achievements system

## 📈 Future Roadmap

- [ ] GUI version with tkinter
- [ ] Daily challenges
- [ ] Difficulty levels (Easy/Medium/Hard)
- [ ] Time attack mode
- [ ] Multiplayer vs mode
- [ ] Sound effects and music
- [ ] Cloud save for high scores

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Your Name**
- GitHub: [@mobrahi](https://github.com/mobrahi)
- Twitter: [@faairuz](https://twitter.com/faairuz)

## 🙏 Acknowledgments

- Inspired by classic Hangman games
- Thanks to all contributors and testers
- Built with Python and lots of ☕

## ⭐ Show Your Support

If you enjoyed this project, please:
- Star this repository ⭐
- Share it with friends 🎮
- Report bugs or suggest features 🐛

---

## 📞 Contact & Support

- **Issues**: [GitHub Issues](https://github.com/mobrahi/hangman-twist/issues)
- **Discussions**: [GitHub Discussions](https://github.com/mobrahi/hangman-twist/discussions)

---
