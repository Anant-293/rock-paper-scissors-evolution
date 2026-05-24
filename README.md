# Rock, Paper, Scissors: Evolution 

This repository tracks my programming progress over the span of a single week, showcasing how I took a basic command-line game concept and refactored it into a robust, feature-rich, and crash-proof application.

---

## 📁 Project Structure

* **`rps_v1_basic.py`**: The baseline script built using a straightforward `for` loop. It successfully handles core game logic but lacks user input protection, structural error-handling, or continuous session tracking.
* **`rps_v2_advanced.py`**: The fully refactored, 83-line advanced version. This script hardens the codebase against real-world user interactions.

---

## 🚀 Key Upgrades in Version 2

1. **Input Validation Loops:** Wrapped all player interactions in `while` validation loops. If a user inputs an invalid command or makes a typo, the application catches it gracefully and prompts them again instead of crashing or defaulting a point to the computer.
2. **Flexible Case & Term Handling:** Expanded choice arrays to catch and validate alternative terms natively (like supporting both `"scissor"` and `"scissors"` automatically) and standardized inputs to lowercase.
3. **Infinite Session Replayability:** Migrated the execution logic inside a comprehensive session loop that evaluates replay selections (`y`, `n`, `yes`, `no`), running continuous matches without forcing the script to terminate and restart.
4. **Aggregate Analytics:** Implemented persistence counters that track total scores and games played over multiple entirely separate multi-round series, outputting advanced margin metrics (`Player won by a margin of X rounds`) at the end of each session.

---

## 🛠️ Built With

* **Python 3**
* **Spyder IDE**
* Python's Built-in `random` module
