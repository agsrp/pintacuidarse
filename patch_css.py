import re

with open("style.css", "r", encoding="utf-8") as f:
    css = f.read()

# Replace question-text font-size
css = re.sub(
    r'\.question-text\s*\{[^}]*font-size:\s*1\.[0-9]+rem;?[^}]*\}',
    '.question-text {\n    font-size: clamp(1.1rem, 3vw, 1.5rem);\n    margin-bottom: var(--spacing-lg);\n    font-weight: 700;\n    color: var(--text);\n    line-height: 1.4;\n}',
    css, count=1
)

# Replace option-btn font-size
css = re.sub(
    r'\.option-btn\s*\{[^}]*font-size:\s*1.[0-9]+rem[^\}]*\}',
    '.option-btn {\n    display: block;\n    width: 100%;\n    padding: var(--spacing-md);\n    margin-bottom: var(--spacing-sm);\n    background-color: rgba(255, 255, 255, 0.4);\n    border: 2px solid rgba(255, 255, 255, 0.5);\n    border-radius: 50px;\n    font-family: inherit;\n    font-size: clamp(0.95rem, 2vw, 1.15rem);\n    font-weight: 600;\n    color: var(--text);\n    text-align: left;\n    cursor: pointer;\n    transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);\n    backdrop-filter: blur(5px);\n}',
    css, count=1
)

# Replace score-title font-size
css = re.sub(
    r'font-size:\s*2\.2rem;',
    'font-size: clamp(1.8rem, 5vw, 2.8rem);',
    css
)

# Replace final-score font-size
css = re.sub(
    r'font-size:\s*4\.5rem;',
    'font-size: clamp(3.5rem, 8vw, 6rem);',
    css
)

# Clean media query font sizes so clamp can do its job
css = re.sub(r'(\.question-text\s*\{\s*)font-size:\s*1\.2rem;(\s*\})', r'', css)
css = re.sub(r'(\.option-btn\s*\{\s*padding:[^;]+;\s*)font-size:\s*1rem;(\s*\})', r'\1\2', css)
css = re.sub(r'(\.score-title\s*\{\s*)font-size:\s*1\.8rem;(\s*\})', r'', css)
css = re.sub(r'(\.final-score\s*\{\s*)font-size:\s*3\.5rem;(\s*\})', r'', css)
css = re.sub(r'(\.question-text\s*\{\s*)font-size:\s*1\.1rem;(\s*\})', r'', css)
css = re.sub(r'(\.option-btn\s*\{\s*)font-size:\s*0\.95rem;(\s*\})', r'', css)

# Fix empty brackets left by regex
css = re.sub(r'\.[a-zA-Z0-9_-]+\s*\{\s*\}', '', css)

with open("style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Clamp typography applied")
