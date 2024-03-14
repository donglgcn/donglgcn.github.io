import os
import re

# 要插入的新文本
new_text = "You don't take a photograph, you make it."

# 查找当前目录下所有的.html文件
for filename in os.listdir('.'):
    if filename.endswith('.html'):
        # 读取文件内容
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        # 在文件内容中查找并替换文本
        new_content = re.sub(r'<div class="sqs-html-content">\s*<h3 style="white-space:pre-wrap;">Daiqing Qi</h3>\s*<p class="" style="white-space:pre-wrap;">.*?</p>\s*<p class="" style="white-space:pre-wrap;">\s*</div>',
                             '<div class="sqs-html-content"><h3 style="white-space:pre-wrap;">Daiqing Qi</h3><p class="" style="white-space:pre-wrap;">' + new_text + '</p><p class="" style="white-space:pre-wrap;">',
                             content,
                             flags=re.DOTALL)

        # 将修改后的内容写入文件
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
