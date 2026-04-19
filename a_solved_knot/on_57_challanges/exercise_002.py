import webbrowser
from pathlib import Path

# __file__ is this script's path; .with_suffix(".html") swaps .py → .html;
# .as_uri() converts it to a file:// URL; webbrowser.open() opens it in the browser.
webbrowser.open(Path(__file__).with_suffix(".html").as_uri())
