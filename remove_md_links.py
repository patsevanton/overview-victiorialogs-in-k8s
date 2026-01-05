import re
from pathlib import Path

# регулярка для markdown-ссылок [текст](url)
LINK_RE = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')

def process_file(path: Path):
    text = path.read_text(encoding="utf-8")
    new_text = LINK_RE.sub(r'`\1`', text)

    if new_text != text:
        path.write_text(new_text, encoding="utf-8")
        print(f"Обработан: {path}")

def main(root_dir="."):
    for md_file in Path(root_dir).rglob("*.md"):
        process_file(md_file)

if __name__ == "__main__":
    main()
