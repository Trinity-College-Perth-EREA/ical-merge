import html, os

with open("/templates/index.html", "r") as f:
    page = f.read()
for name in ("PAGE_TITLE", "OUTPUT_FILENAME"):
    page = page.replace("{{ %s }}" % name, html.escape(os.getenv(name, "")))
with open("/app/index.html", "w") as f:
    f.write(page)