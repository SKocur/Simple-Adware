import os
import urllib.request
import cv2


class AdManager(object):
    url = ""
    extension = ""

    def __init__(self):
        self.new_file_name = ""

    def process_file(self):
        file_name, _ = urllib.request.urlretrieve(self.url)
        base = os.path.splitext(file_name)[0]
        self.new_file_name = base + self.extension
        os.rename(file_name, self.new_file_name)

    def show_window(self):
        image_ad = cv2.imread(self.new_file_name)
        image_ad = cv2.resize(image_ad, (300, 300))

        while True:
            cv2.moveWindow("ad", 0, 0)
            cv2.imshow("ad", image_ad)
            cv2.waitKey(0)

    def execute_adware(self):
        self.process_file()
        self.show_window()