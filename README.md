# PDF to plain text converter

Provides a simple commandline tool to transform a PDF file into a plain text file.  
Based on code from: [geeksforgeeks.org](https://www.geeksforgeeks.org/python-reading-contents-of-pdf-using-ocr-optical-character-recognition/)

## Installation

### Install terreract-ocr  
[See this link for (Windows) binaries](https://tesseract-ocr.github.io/tessdoc/Home.html#binaries)  
Or use `sudo apt-get install tesseract-ocr`

### Install and activate the conda environment  
```
conda env create --file PDF_OCR_tool.yml  
conda activate PDF_OCR_tool
```

## Usage

The following command will create a directory called `FILENAME` in `PATH/TO/PDF/`  with subdirectories `images`
and `text`.  

`python main.py --input PATH/TO/PDF/FILENAME.pdf`

The given `FILENAME.pdf` file will first be transformed to images of individual pages, which will be saved in
the `images` folder. These images are then transformed to a `FILENAME.txt` plain text file in the `text` folder

For example:  

```
python main.py --input C:\Users\Person\Documents\my_document.pdf
```  

Will give the output:  

```
Created directory 'C:\Users\Person\Documents\my_document
Created directory 'C:\Users\Person\Documents\my_document\images
Created directory 'C:\Users\Person\Documents\my_document\text
Outputted images of PDF file 'C:\Users\Person\Documents\my_document.pdf' in C:\Users\Person\Documents\my_document\images
Outputted plain text of PDF file 'C:\Users\Person\Documents\my_document.pdf' in C:\Users\Person\Documents\my_document\text
```



