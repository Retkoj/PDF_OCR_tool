import os

from pdf2image import convert_from_path


def convert_pdf_to_image(pdf_file: str, out_dir: str):
    """
    Converts pdf to images and saves the pages in individual jpg files in the folder out_dir.

    :param pdf_file: path to PDF file
    :param out_dir: Optional output directory, default './pdf_images'
    """
    pages = convert_from_path(pdf_file, dpi=500)
    file_name = os.path.splitext(os.path.basename(pdf_file))[0]

    for i, page in enumerate(pages):
        page_file_name = f"{file_name}_{i}.jpg"
        page.save(os.path.join(out_dir, page_file_name), 'JPEG')
