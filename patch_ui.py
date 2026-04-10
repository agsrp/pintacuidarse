import re

# Update index.html for active hearts
try:
    with open("index.html", "r", encoding="utf-8") as f:
        html = f.read()

    # Make hearts active by default
    html = re.sub(r'<span class="heart">❤️</span>', '<span class="heart active">❤️</span>', html)

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("index.html patched successfully.")
except Exception as e:
    print(f"Error patching index.html: {e}")

# Update style.css for 50px border radius
try:
    with open("style.css", "r", encoding="utf-8") as f:
        css = f.read()

    # The previous patch resulted in: border-radius: var(--border-radius-md);
    # Inside .option-btn block
    if '.option-btn {' in css:
        # Find .option-btn block
        css = re.sub(
            r'(\.option-btn\s*\{[^}]*)border-radius:\s*var\(--border-radius-md\);',
            r'\1border-radius: 50px;',
            css
        )
    with open("style.css", "w", encoding="utf-8") as f:
        f.write(css)
    print("style.css patched successfully.")
except Exception as e:
    print(f"Error patching style.css: {e}")
