# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
- [ ] Detail which bugs you found.
- [ ] Explain what fixes you applied.
## Document Your Experience

During this project, I used AI tools to help investigate and fix bugs in the game logic.

Initially, the game had several issues:
- The hint messages were inconsistent with the actual secret number.
- The comparison logic in `check_guess()` was incorrect.
- The function argument order caused incorrect results in the tests.

Using AI assistance, I identified the issues and corrected the logic in `logic_utils.py`.

I verified the fixes by running automated tests with `pytest`, which confirmed that the game logic now works correctly.

This project helped me understand how to debug code systematically, verify behavior with tests, and collaborate effectively with AI tools during development.

## 📸 Demo
## Demo

This project is a simple number guessing game built with Streamlit.

The user tries to guess a secret number between 1 and 100.  
After each guess, the game provides feedback:

- "Too High" if the guess is higher than the secret number
- "Too Low" if the guess is lower than the secret number
- "Win" if the guess matches the secret number

The game logic was debugged and improved using AI tools and automated tests with pytest.
- [ ] [Insert a screenshot of your fixed, winning game here]

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
