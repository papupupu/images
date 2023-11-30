import re
import sys


'''
      命令行中运行：python replace_images.py your_markdown_file.md
'''

def replace_image_tags(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # 正则表达式匹配
        pattern = r'<img src="images/([^"]+\.png)" alt="([^"]+)" style="[^"]*" />'
        replacement = r'![](https://cdn.jsdelivr.net/gh/papupupu/images/images/\1)'

        # 执行替换
        new_content = re.sub(pattern, replacement, content)

        # 写回文件
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(new_content)

        print("替换完成。")

    except FileNotFoundError:
        print(f"文件 '{file_path}' 未找到。")
    except Exception as e:
        print(f"发生错误: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("请提供要处理的Markdown文件的路径。")
    else:
        file_path = sys.argv[1]
        replace_image_tags(file_path)

