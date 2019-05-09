
import cv2
import sys
import os
import numpy as np

from pdf2image import convert_from_path
from matplotlib import pyplot as plt

from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox, LTTextLine, LTFigure

from PyPDF2 import PdfFileWriter,PdfFileReader,PdfFileMerger



PDF = str(41)


def to_image(pdf_path, pdf_name, number_of_pages, output_path):

    pages = convert_from_path(pdf_path + pdf_name + '.PDF', 100, last_page=number_of_pages)

    for page in pages:
        page.save(os.path.join(output_path, "%s-page-%d.jpg" % (pdf_name, pages.index(page))), "JPEG")


#
#   Crop the specified image to the first horizontal line.
#

def first_crop(input_dir, image_name, output_dir):

    img = cv2.imread(os.path.join(input_dir, image_name), 0)
    height, width = img.shape[:2]

    edges = cv2.Canny(img, 100, 200)

    lines = cv2.HoughLines(edges, 1, np.pi/90, 400)

    for rho,theta in lines[0]:

        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))

        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255),2)
        crop_img = img[y1+6:height, 0:width]

        print(os.path.join(input_dir, image_name))
        cv2.imwrite(str(os.path.join(output_dir, 'crop-1-' + image_name)), crop_img)

    # To Show Matplot graph with drawn line, uncomment

    # plt.subplot(121),plt.imshow(img, cmap = 'gray')
    # plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    # plt.plot(122),plt.imshow(edges,cmap = 'gray')
    # plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
    # plt.show()


#
#   Crop the specified image to the second horizontal line
#   (After first Crop has been called)
#

def second_crop(input_dir, image_name, output_dir):

    img = cv2.imread(os.path.join(input_dir, image_name), 0)
    height, width = img.shape[:2]

    edges = cv2.Canny(img, 100, 200)

    lines = cv2.HoughLines(edges, 1, np.pi / 90, 100)

    for rho, theta in lines[0]:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))

        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)


        crop_img = img[y1 + 6:height, 0:width]
        path = str(os.path.join(output_dir, 'crop-2-' + image_name.replace("crop-1-", "")))

        cv2.imwrite(path, crop_img)


def parse_layout(layout):

    """Function to recursively parse the layout tree."""
    for lt_obj in layout:
        print(lt_obj.__class__.__name__)
        print(lt_obj.bbox)
        if isinstance(lt_obj, LTTextBox) or isinstance(lt_obj, LTTextLine):
            print(lt_obj.get_text())
        elif isinstance(lt_obj, LTFigure):
            parse_layout(lt_obj)  # Recurs



#
#   Parse the pdf into an xml structure
#

def parse_pdf(pdf_path):

    fp = open(pdf_path, 'rb')

    parser = PDFParser(fp)
    doc = PDFDocument(parser)

    rsrcmgr = PDFResourceManager()
    laparams = LAParams()
    device = PDFPageAggregator(rsrcmgr, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)

    for page in PDFPage.create_pages(doc):
        interpreter.process_page(page)
        layout = device.get_result()
        parse_layout(layout)



def page_to_pdf(image_path, pdf_path, page_number):

    img = cv2.imread(image_path, 0)
    height, width = img.shape[:2]

    print(height)
    print(width)

    pdf_file = PdfFileReader(open(pdf_path, "rb"))
    page = pdf_file.getPage(page_number)

    print(page.cropBox.getLowerLeft())
    print(page.cropBox.getLowerRight())
    print(page.cropBox.getUpperLeft())
    print(page.cropBox.getUpperRight())

    page.mediaBox.lowerLeft = (0, 0)
    page.mediaBox.lowerRight = (width, 0)

    page.mediaBox.upperLeft = (0, height - 175)
    page.mediaBox.upperRight = (width, height - 175)

    writer = PdfFileWriter()
    outfp = open(pdf_path + '-cropped-page-' + str(page_number) + ".pdf", 'wb')

    writer.addPage(page)
    writer.write(outfp)



#
#   Example conversion of particular pdf page to cropped image and
#   then "cropped pdf" equivalent.
#

if __name__ == '__main__':

    # Input Directory, Name of Pdf, Page to Convert, Place to Save Image
    to_image('input_pdfs/', str(41), 1, output_path='output_images/')

    # Crop the images down via the horizontal line
    first_crop('output_images', '41-page-0.jpg', output_dir="output_images")
    second_crop('output_images', 'crop-1-41-page-0.jpg', output_dir="output_images")

    # Covert the cropped image back to pdf form
    page_to_pdf("output_images/crop-2-41-page-0.jpg", "input_pdfs/41.PDF", 1)
