import urllib.request
import os
import cv2

url = "http://d.wpimg.pl/1098145671--204938399/movies.jpg"
extension = ".jpg"
file_name, _ = urllib.request.urlretrieve(url)

base = os.path.splitext(file_name)[0]
new_file_name = base + extension
os.rename(file_name, new_file_name)

print(new_file_name)

image_ad = cv2.imread(new_file_name)
image_ad = cv2.resize(image_ad, (300, 300))

while True:
    cv2.moveWindow("ad", 0, 0)
    cv2.imshow("ad", image_ad)
    cv2.waitKey(0)