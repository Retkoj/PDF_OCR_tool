import os

from PIL import Image
import pytesseract


def get_text_from_images(image_path: str, out_dir: str, out_file: str):
    """
    Uses Tesseract to extract text from an image or a directory of images.
    In the case of multiple images, the output text is concatenated in the same file.
    Doesn't check for existing files: If the file already exists, text is appended to it.

    :param image_path: directory or path to image(s)
    :param out_dir: output directory for text file
    :param out_file: name of outputted text file
    """
    if os.path.isdir(image_path):
        files = [os.path.join(os.path.abspath(image_path), file_name) for file_name in os.listdir(image_path)
                 if os.path.splitext(file_name)[-1].lower() in ['.jpg', '.jpeg']]
    elif os.path.isfile(image_path) and os.path.splitext(image_path)[-1].lower() in ['.jpg', '.jpeg']:
        files = [os.path.abspath(image_path)]
    else:
        raise Warning(f"File '{image_path}' is not recognized as a directory or JPEG file")

    with open(os.path.join(out_dir, out_file), "a") as f:
        for file in files:
            text = pytesseract.image_to_string(Image.open(file))

            # The recognized text is stored in variable text
            # Any string processing may be applied on text
            # Here, basic formatting has been done:
            # In many PDFs, at line ending, if a word can't
            # be written fully, a 'hyphen' is added.
            # The rest of the word is written in the next line
            # Eg: This is a sample text this word here GeeksF-
            # orGeeks is half on first line, remaining on next.
            # To remove this, we replace every '-\n' to ''.
            text = text.replace('-\n', '')

            f.write(text)
