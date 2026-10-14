# OS Synchronization Assignment - Readers-Writers & Dining Philosophers

**Student name:** Jyothi
**USN:** NNM25is505 
**Course:** Operating Systems

## 1. What this project contains

This project contains four Python programs that demonstrate synchronization techniques for two classical operating system problems.

- **Readers-Writers using Semaphores:** Implemented using semaphores to coordinate readers and writers. File: `readers_writers/semaphore/main.py`
- **Readers-Writers using a Monitor:** Implemented using a monitor-style approach with a lock and condition variable. File: `readers_writers/monitor/main.py`
- **Dining Philosophers using Semaphores:** Uses semaphores to coordinate four philosophers and manage access to shared forks. File: `dining_philosophers/semaphore/main.py`
- **Dining Philosophers using a Monitor:** Uses a monitor-style approach with a condition variable to coordinate access to forks. File: `dining_philosophers/monitor/main.py`

The programs record execution events and use the recorded information to generate HTML simulations, provided this matches the actual implementation.

## 2. Language and requirements

- Python 3.10 or newer, if supported by the implementation.
- No external libraries are required if the programs use only Python's standard library.
- A modern web browser is required to view the generated HTML simulations.

## 3. Build / compile

Python does not require a separate compilation step. The programs can be executed directly using Python.

## 4. How to run (this also generates the HTML)

Open a terminal in the project root folder and run each command separately:

```bash
python readers_writers/semaphore/main.py
python readers_writers/monitor/main.py
python dining_philosophers/semaphore/main.py
python dining_philosophers/monitor/main.py
```

Use `python3` instead of `python` on systems where Python is invoked using `python3`.

## 5. How to view the simulation

Each program is intended to generate an HTML file in the `generated_html/` folder. After running a program, check the terminal output for the generated file's location. Open the HTML file in a web browser to view the simulation. Run the program again to regenerate the simulation.

## 6. Expected output

Each program should execute its synchronization logic and generate the corresponding HTML simulation. The exact terminal messages and execution order may vary depending on the implementation and thread scheduling.

## 7. Screenshots

The `screenshots/` folder will contain screenshots of the terminal output and the four HTML simulations. Add screenshots after running and testing all four programs.

## 8. How the HTML is generated

The programs record execution events or state changes while their threads are running. The recorded information is then used to generate HTML pages that visualize the synchronization process. The details should match the actual source code.

## 9. Known limitations

- Thread scheduling and execution order may vary between runs.
- Python semaphores and condition variables do not guarantee strict FIFO scheduling.
- Starvation may be possible depending on the synchronization policy.
- The HTML replay may simplify the timing of the original thread execution.

## 10. AI tools used

ChatGPT (OpenAI) was used to assist with understanding the assignment requirements, explaining synchronization concepts, troubleshooting issues, and preparing documentation.

Prompt log: [ai_prompts/prompts.md](ai_prompts/prompts.md)

## 11. References and acknowledgements

See [references/references.md](references/references.md) for the references used in this assignment.
