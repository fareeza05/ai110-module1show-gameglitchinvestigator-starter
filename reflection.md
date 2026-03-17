# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- The first bug that I noticed was that the hint provided was inconsistent, and seemed randomized. For example, if target number is 20 and I put in a guess of 50, the hint would say 'Go Higher' which is incorrect.
- The second bug I noticed also related to hints. The hints provided mixed results for the same input. For example, if I guessed '1' incorrectly twice in a row, the first hint would say 'Go Higher' while the second hint would say to 'Go Lower' which is contradictory information. 
- The third bug I noticed was that the target numbers did not always correspond to the difficulty level. For example, when I set the difficulty level to easy, then a target number of '89' was set which is well beyond the maximum threshhold. 
- The fourth bug I noticed was that the New Game button did not reset the message displayed. If the game was over, it would continuously display 'Game Over' and not the hint until a manual refresh of the page was done. I also noticed that in this state, the submit button would not work properly either, and that the game was essentially frozen until the refresh. The same thing occurs once the user wins the game too.
- The fifth bug I noticed was that the answer was revealed to the user with 1 attempt still remaining, with the message reading 'Out of attempts!'

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

I used Copilot, mostly in agent mode on this project.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

The AI suggestions were correct when it came to determining bugs in the code. For example, the small bug fixes in app.py which did not necessarily need complete refactoring, but slight changes.  

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

An example is the test file, where the AI incorrectly imported the logic_utils file and assumed it was in the same directory because it did not have proper context regarding the directory structure.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

This was decided using a 2 step process - first I created additional test cases in my test file for all the new refactored changes. I ran these cases and ensured that the files behaved as expected, and fixed minor bugs along the way. Then I functionally tested the application by running app.py once more and playing around with the UI like I did before when trying to look for bus.

- Describe at least one test you ran (manual or using pytest)  

Using pytest, I tested all of the new refactored code in logic_utils.py. 
Manually, I reproduced the situations where I found bugs, and tried multiple approaches on the UI to mimic a similar environment to when the bug was produced in order to see changed behavior.

The pytest test cases showed me that my code still needed minor fixes and refactors that I had not caught before. The functional testing showed me that once all the pytests were fixed and all relevant bug causing functions were refactored, the application was behaving as it should.

- Did AI help you design or understand any tests? How?

Yes, AI particularly helped to speed up the process of creating specific test cases and using pytest to parametrize. This would have been something quite tedious to write out myself, and was a low cognitive effort task that would've taken up time, when there were more complex functionalities to concentrate on fixing.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

I would tell them to think of Streamlit as a script that reruns everything from top to bottom every single time someone clicks a button or moves a slider, effectively forgetting everything that happened during a prior run. However, for the cases wherein we want to prevent the app from resetting to 0 every single time, Session State acts like a shared notebook for important data so after resetting the script can read this session state and pick up where it left off during the next run.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?

One major thing I learned was how to use the agent mode effectively in Copilot. Before this, I would've probably only gone as far as to ask AI to analyze my code and then go line-by-line to implement fixes myself. But, now I think it has been valuable to learn how to delegate that and focus on really understanding the code diffs once agent mode has ran to make the proper judgement calls and develop a better instinct for analyzing refactored code as a developer.

- What is one thing you would do differently next time you work with AI on a coding task?

I would like to try and be more organized and thoughtful while prompting. For example, I think I could have done a better job at starting a new chat for each bug and compartmentalizing the chats so Copilot could focus on one thing at a time. This time around, because I was so focused on learning I did not prompt in the most clear and efficient way.

- In one or two sentences, describe how this project changed the way you think about AI generated code.

I think it fostered more trust in AI's analysis of the code, and prompted me to have more back and forth conversations where I could truly be inquisitive about this new codebase and trust Copilot to explain all of the nuances to me. 
