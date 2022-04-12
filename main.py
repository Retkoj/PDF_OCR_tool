import argparse
import os

from convert_pdf_to_image import convert_pdf_to_image
from get_text_from_image import get_text_from_images


def run(args):
    file_path = os.path.dirname(args.input)
    file_name = os.path.splitext(os.path.basename(args.input))[0]

    output_folder = os.path.join(file_path, file_name)
    images_folder = os.path.join(output_folder, 'images')
    text_folder = os.path.join(output_folder, 'text')

    os.makedirs(output_folder, exist_ok=True)
    os.makedirs(images_folder, exist_ok=True)
    os.makedirs(text_folder, exist_ok=True)

    for dir in [output_folder, images_folder, text_folder]:
        print(f"Created directory '{dir}")

    convert_pdf_to_image(args.input, out_dir=images_folder)
    print(f"Outputted images of PDF file '{args.input}' in {images_folder}")
    get_text_from_images(image_path=images_folder, out_dir=text_folder,
                         out_file=f"{file_name}.txt")
    print(f"Outputted plain text of PDF file '{args.input}' in {text_folder}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="OCR tool for PDF files. A folder with the file name is created in "
                                                 "the same folder as the file itself, with in it a images folder "
                                                 "for images of the pdf pages and a "
                                                 "text folder for the plain text output.")

    parser.add_argument('-i', '--input', type=str, help="Full path to input PDF")

    args = parser.parse_args()
    run(args)
