# AI Prompt Log

**Student:** D Jyothi 
**USN:**  NNM25IS505
**AI tool used:** ChatGPT (OpenAI)

## 1. Initial Prompt

I provided the Operating Systems Synchronization Assignment PDF and requested help understanding the requirements and planning the four implementations: Readers-Writers using semaphores and monitors, and Dining Philosophers using semaphores and monitors. I also requested program-generated HTML simulations.

## 2. Important Follow-up Prompts

- Asked for a step-by-step plan to complete the assignment.
- Asked how to run the Python programs in VS Code and what output to expect.
- Requested simple explanations of all four programs and possible viva questions.
- Asked for help preparing the GitHub repository, README, references, prompt log and assignment report.
- Asked for help checking the project structure and identifying missing files or necessary fixes.

## 3. Changes and Testing Performed

- Added my details to the README and report.
- Ran the Python programs on my computer and generated the HTML simulations.
- Captured screenshots of the program executions and simulations.
- Updated the HTML simulations with a Shared Resource Status panel, if applicable.

## 4. Limitations and Possible Improvements

- **Replay timing:** The HTML replay may use a fixed playback interval instead of reproducing the original time gaps between events. It could be improved by using recorded timestamps.
- **Fairness:** Python semaphores and condition variables do not necessarily guarantee FIFO scheduling. Starvation depends on the synchronization logic and scheduling behaviour.
- **Readers-Writers:** A reader-priority implementation may allow writers to wait for a long time if readers continue arriving. A writer-priority monitor can reduce this risk, depending on its implementation.

## 5. Reflection

AI assistance helped me understand the assignment requirements, organize the project and troubleshoot implementation issues. I tested the programs and reviewed the generated HTML simulations.