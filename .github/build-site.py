#!/usr/bin/env python3
"""由 dispatch-pages 生成，不要手改。

仓库里的页面按中文路径存放（文档/<项目>/<标题>.html、知识库/<目录>/<笔记>.html），
线上网址用英文：按 catalog.json 和 kb.json 复制成 p/<slug>/、kb/<slug>/，
再放上目录页 index.html 和图谱页 graph/index.html。
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


def load(name, key):
    try:
        with open(os.path.join(root, name), encoding="utf-8") as f:
            return json.load(f)[key]
    except (OSError, ValueError, KeyError):
        return []


def copy(rel, parts, index_href):
    """把一个中文路径的页面复制到英文网址下；单篇出错只跳过这一篇，不拖垮整站部署。"""
    try:
        with open(os.path.join(root, rel), encoding="utf-8") as f:
            text = f.read()
    except OSError as err:
        print(f"跳过 {'/'.join(parts)}：读不到 {rel}（{err.strerror}）", file=sys.stderr)
        return 0
    text = re.sub(r'<link rel="index" href="[^"]*">', f'<link rel="index" href="{index_href}">', text, count=1)
    dst = os.path.join(out, *parts)
    os.makedirs(dst, exist_ok=True)
    with open(os.path.join(dst, "index.html"), "w", encoding="utf-8") as f:
        f.write(text)
    return 1


pages = load("catalog.json", "pages")
notes = load("kb.json", "notes")
done = sum(copy(p.get("path") or f"p/{p['slug']}/index.html", ("p", p["slug"]), "../../index.html") for p in pages)
done += sum(copy(n["path"], ("kb", n["slug"]), "../../index.html") for n in notes)
if notes and os.path.exists(os.path.join(root, "知识图谱.html")):
    done += copy("知识图谱.html", ("graph",), "../index.html")
shutil.copy(os.path.join(root, "index.html"), os.path.join(out, "index.html"))
print(f"已生成 {done} 个页面（文档 {len(pages)} · 笔记 {len(notes)}）→ {out}")
