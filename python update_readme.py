import os
import re

# Root of the repo (where README.md is)
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# Path to the folder containing all solutions
SOLUTIONS_DIR = os.path.join(ROOT_DIR, "leetcode-solutions")

# Paths for each difficulty level
levels = {
    "Easy": os.path.join(SOLUTIONS_DIR, "01_Easy"),
    "Medium": os.path.join(SOLUTIONS_DIR, "02_Medium"),
    "Hard": os.path.join(SOLUTIONS_DIR, "03_Hard")
}

def count_solved_problems(path):
    """
    Counts how many problem folders contain a solution.py file
    in the given path.
    """
    count = 0
    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        if os.path.isdir(full_path) and "solution.py" in os.listdir(full_path):
            count += 1
    return count

def update_readme(readme_path, counts):
    """
    Updates the README.md file by replacing the old counts with
    the new ones based on current solved problems.
    """
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    for level, num in counts.items():
        pattern = rf"(\|\s*{level}\s*\|\s*)\d+(\s*\|)"
        content = re.sub(pattern, lambda m: f"{m.group(1)}{num}{m.group(2)}", content)

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    # Count problems for each level
    problem_counts = {
        level: count_solved_problems(path)
        for level, path in levels.items()
    }

    print("✅ Detected number of solved problems:")
    for level, count in problem_counts.items():
        print(f"  {level}: {count}")

    # Path to README file
    readme_path = os.path.join(ROOT_DIR, "README.md")

    # Update the README file with new counts
    update_readme(readme_path, problem_counts)

    print("📄 README.md has been successfully updated.")