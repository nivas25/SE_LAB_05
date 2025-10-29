# Lab 5: Static Analysis Reflection

## 1. Which issues were the easiest to fix, and which were the hardest? Why?

**Easiest:** The easiest issues to fix were the direct, single-line changes reported by Bandit and Flake8. For example, removing the unused logging import, deleting the dangerous eval() call, and adding encoding="utf-8" to file operations were all very clear and simple fixes.

**Hardest:** The hardest issue was refactoring the code to remove the global variable, as suggested by Pylint. This wasn't a one-line fix; it required changing the design of the program. We had to update every single function definition to accept stock as a parameter and then update the main() function to manage and pass that stock dictionary. The picky whitespace errors at the very end (like C0305: Trailing newlines) were also hard, not because they were complex, but because they were invisible and required a lot of trial and error to get a perfect score.

## 2. Did the static analysis tools report any false positives?

No, the tools did not report any false positives in this lab. Every issue flagged was a valid problem:

- Bandit correctly identified a major security risk (eval()) and a bad practice (bare-except).
- Flake8 was right about all the PEP 8 style and whitespace violations.
- Pylint correctly pointed out bad design (like global and dangerous-default-value) and poor style (like invalid-name and missing docstrings).

## 3. How would you integrate static analysis tools into your actual software development workflow?

I would integrate these tools at two key stages:

**Local Development:** I would install them as a plugin for my code editor (like VS Code). This gives me real-time feedback, so I can fix Pylint and Flake8 errors as I type, before I even save the file.

**Continuous Integration (CI):** I would set up a GitHub Action to automatically run pylint, bandit, and flake8 on every git push. If the code doesn't meet a certain quality score (e.g., 9.5/10) or if Bandit finds any security issue, the build would fail, and the code would be blocked from being merged.

## 4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?

The improvements were huge:

**Robustness & Security:** The code is no longer vulnerable to code injection (by removing eval()). It also handles errors much more gracefully by catching specific KeyError and FileNotFoundError exceptions instead of silencing everything.

**Readability:** The code is much easier to read. All the functions now have clear snake_case names and docstrings explaining what they do. Removing the global variable makes the flow of data explicit and easy to follow.

**Maintainability:** The new 10/10 version is far easier to maintain. Because the functions no longer depend on a hidden global variable, they are "pure" and could be easily tested, reused, or moved to another module.