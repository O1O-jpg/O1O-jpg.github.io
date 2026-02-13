import os
import re
from datetime import datetime

ROOT_DIR = r"./python-study"   # 改成你的目录路径

def get_file_creation_time(path):
    stat = os.stat(path)
    return datetime.fromtimestamp(stat.st_ctime)

def extract_title(content, filename):
    for line in content.splitlines():
        if line.strip().startswith("# "):
            return line.strip()[2:].strip()
    # 如果没有标题，用文件名
    return os.path.splitext(os.path.basename(filename))[0]

def already_has_front_matter(content):
    return content.strip().startswith("---")

def process_markdown(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    if already_has_front_matter(content):
        print(f"跳过（已有front-matter）: {file_path}")
        return

    title = extract_title(content, file_path)
    date = get_file_creation_time(file_path).strftime("%Y-%m-%d %H:%M:%S")

    front_matter = f"""---
title: {title}
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

    print(f"已修复: {file_path}")

def main():
    for root, dirs, files in os.walk(ROOT_DIR):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                process_markdown(file_path)

if __name__ == "__main__":
    main()
