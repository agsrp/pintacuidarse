import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

hud_html = """        <div class="card">
            <!-- Game HUD -->
            <div id="game-hud" class="game-hud">
                <div class="lives-container" id="lives-container">
                    <span class="heart">❤️</span>
                    <span class="heart">❤️</span>
                    <span class="heart">❤️</span>
                </div>
                <div class="timer-wrapper">
                    <div class="timer-fill" id="timer-fill"></div>
                </div>
            </div>"""

content = content.replace('<div class="card">', hud_html, 1)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Patch applied")
