import os
import re
from datetime import datetime

ROOT_DIR = r"./python-study"   # 改成你的目录路径

def get_file_creation_time(path):
    stat = os.stat(path)
    return datetime.fromtimestamp(stat.st_ctime)

def clean_title(title):
    title = title.replace("`", "")
    title = re.sub(r"[^\w\u4e00-\u9fff\s-]", "", title)
    title = re.sub(r"\s+", " ", title).strip()
    return title

def extract_title(content, filename):
    for line in content.splitlines():
        if line.strip().startswith("# "):
            raw_title = line.strip()[2:].strip()
            return clean_title(raw_title)

    name = os.path.splitext(os.path.basename(filename))[0]
    return clean_title(name)

def remove_existing_front_matter(content):
    if content.lstrip().startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            return parts[2].lstrip()
    return content

def process_markdown(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 🔥 先删除旧的 front-matter
    content = remove_existing_front_matter(content)

    title = extract_title(content, file_path)
    date = get_file_creation_time(file_path).strftime("%Y-%m-%d %H:%M:%S")

    front_matter = f"""---
title: "{title}"
date: {date}
tags:
  - Python
categories:
  - Python学习
---

"""

    new_content = front_matter + content

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"已重建: {file_path}")

def main():
    for root, dirs, files in os.walk(ROOT_DIR):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                process_markdown(file_path)

if __name__ == "__main__":
    main()
