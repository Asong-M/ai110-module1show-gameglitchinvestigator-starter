# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
When I first ran the game, the interface loaded correctly, but several behaviors were incorrect. 
First, the game sometimes did not end even after guessing the correct number. 
Second, the hints occasionally contradicted the actual secret number, which made the game confusing. 
Third, the score sometimes reset unexpectedly during the game.
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---I used ChatGPT as my main AI assistant during this project. 
ChatGPT helped me understand the structure of the code and suggested possible locations where the bugs might exist. 
One helpful suggestion was checking how the secret number was stored in the session state. That advice helped me understand why the number kept changing during the game. 
However, one suggestion from the AI initially focused on the UI instead of the game logic, which did not solve the problem. I verified this by testing the game again and checking the logic functions.

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---To verify whether a bug was fixed, I ran the game multiple times and tested different guesses to observe the behavior. 
For example, I tested whether the game would end after the correct guess and whether the hints matched the secret number. 
I also manually checked the logic functions to make sure the correct values were being returned. 
AI helped me understand how to design simple tests to confirm that the game logic behaved as expected.

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---I learned that Streamlit reruns the entire script every time the user interacts with the interface. 
Because of this behavior, the secret number can change if it is not stored properly. 
Session state is important because it allows the program to keep important values, such as the secret number and score, across multiple interactions. 
Using Streamlit session state ensures that the game behaves consistently while the user is playing.

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
