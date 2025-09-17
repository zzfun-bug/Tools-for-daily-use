import os
from PyPDF2 import PdfReader, PdfWriter

def split_pdf_pages(input_pdf_path, output_folder):
    # 确保输出文件夹存在
    os.makedirs(output_folder, exist_ok=True)

    # 读取原始 PDF
    reader = PdfReader(input_pdf_path)

    for page_num in range(len(reader.pages)):
        writer = PdfWriter()
        writer.add_page(reader.pages[page_num])

        # 输出文件名
        output_filename = os.path.join(output_folder, f"page_{page_num + 1}.pdf")

        # 写入单个页面到新的 PDF 文件
        with open(output_filename, "wb") as output_pdf:
            writer.write(output_pdf)

        print(f"已保存：{output_filename}")

    print("✅ 所有页面拆分完成！")

# 示例用法
if __name__ == "__main__":
    input_pdf = r"D:\For_study\简历\前端\宜宾\唐浩成都工业学院web前端.pdf"  # 替换为你的 PDF 文件路径
    output_dir = "split_pages"  # 输出文件夹名称
    split_pdf_pages(input_pdf, output_dir)