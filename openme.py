from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
import sys
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import settings
import os
import tkinter.messagebox
import math
from multiprocessing import Process

chrome_options = webdriver.ChromeOptions()
options = Options()
options.add_argument("--headless") 
options.add_argument("window-size=10000,10000")
#pageContainer_7_documentViewer_textLayer
def split_range(n):
    start_index = math.floor(n / 4)
    ranges = []
    for i in range(4):
        start = 1 + i * start_index
        end = (i + 1) * start_index
        if i == 3:
            ranges.append((start, n))
        else:
            ranges.append((start, end))
    return ranges

def download(start, end):
    brower = webdriver.Chrome(executable_path=settings.driver_path,
                              chrome_options=options)
    brower.implicitly_wait(20)
    brower.get(settings.url)
    brower.execute_script('$FlowPaper("documentViewer").Zoom(' + str(settings.zoom) + ')')
    for i in range(start, end + 1, 1):
        j = int(i) - 1
        brower.execute_script("""$FlowPaper("documentViewer").gotoPage(""" + str(i) + """)""")
        brower.find_element(By.ID, "pageContainer_" + str(j) + "_documentViewer_textLayer")
        sleep(1.5)
        element = brower.find_element(By.ID, "dummyPage_" + str(j) + "_documentViewer")
        element.screenshot(settings.path_luu_anh + "/" + str(i) + ".png")
    print("Kết Thúc")
    brower.quit()

def convert_images_to_pdf(image_paths, output_path):
    pdf_canvas = canvas.Canvas(output_path, pagesize=letter)
    for image_path in image_paths:
        image = Image.open(image_path)
        image_width, image_height = image.size
        pdf_canvas.setPageSize((image_width, image_height))
        pdf_canvas.drawImage(image_path, 0, 0, width=image_width, height=image_height)
        pdf_canvas.showPage()
    pdf_canvas.save()

def main():
    image_paths = []
    output_path = "./output/" + settings.output_name + '.pdf'
    current = 0
    #"""
    
    dir_list = os.listdir('./downloaded')
    if(len(dir_list) != 0):
        for img in dir_list:
            os.remove('./downloaded/' + img)

    processes = []
    split = split_range(settings.trang_ket_thuc)

    for i in range(4):
        start, end = split[i]
        process = Process(target = download, args = (start, end))
        processes.append(process)

    for process in processes:
        process.start()

    # Chờ cho tất cả các tiến trình kết thúc
    for process in processes:
        process.join()

    
    #"""
    for i in range(1, settings.trang_ket_thuc + 1, 1):
        path = './downloaded/' + str(i) + '.png'
        image_paths.append(path)
    convert_images_to_pdf(image_paths, output_path)
    for image_path in image_paths:
        os.remove(image_path)
    print("Kết thúc")
if __name__ == "__main__":
    try:
        main()
    except:
        main()