#!/usr/bin/env python3
"""由 dispatch-pages 生成，不要手改。

仓库里的文档按中文路径存放（文档/<项目>/<标题>.html），线上网址用英文：
按 catalog.json 把每篇复制到 <输出目录>/p/<slug>/index.html，再放上目录页 index.html。
用法：python3 .github/build-site.py <输出目录>
"""
import json
import os
import re
import shutil
import sys

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
out = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else "_site")
shutil.rmtree(out, ignore_errors=True)
os.makedirs(out)
with open(os.path.join(root, "catalog.json"), encoding="utf-8") as f:
    pages = json.load(f)["pages"]
for p in pages:
    with open(os.path.join(root, p["path"]), encoding="utf-8") as f:
        text = f.read()
    text = re.sub(r'<link rel="index" href="[^"]*">', '<link rel="index" href="../../index.html">', text, count=1)
    dst = os.path.join(out, "p", p["slug"])
    os.makedirs(dst, exist_ok=True)
    with open(os.path.join(dst, "index.html"), "w", encoding="utf-8") as f:
        f.write(text)
shutil.copy(os.path.join(root, "index.html"), os.path.join(out, "index.html"))
print(f"已生成 {len(pages)} 篇 → {out}")
