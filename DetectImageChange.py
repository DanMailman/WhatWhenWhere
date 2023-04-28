# DetectImageChange.py - Program to compare images at intervals and (TODO) send significant changes to server
## CONSTANTS
MSE_THRESHOLD = 15.00 # MSE == 0 ==>> "perfect similarity"; > 1 ==>> "less similarity"
SSIM_THRESHOLD = 0.80 # SSIM in [-1:1], where 1 indicates perfect similarity.
# IMPORTS
from os import replace
from picamera import PiCamera
from time import sleep
from skimage.metrics import structural_similarity
import matplotlib.pyplot as plt
from numpy import  sum, zeros, average
from cv2 import threshold, findContours, contourArea, drawContours, cvtColor,boundingRect, imread
from cv2 import merge, imshow, rectangle, waitKey
from cv2 import THRESH_BINARY_INV, THRESH_OTSU, RETR_EXTERNAL, CHAIN_APPROX_SIMPLE, COLOR_BGR2GRAY
## CLASSES/TYPES
class tCamera:
    def __init__(self):
        # print(f'tCamera.__init__(): ENTER.')
        self.CAM = PiCamera()
        print(f'RESOLUTION: {self.CAM.resolution}') #  Credit: Sarath
        self.SleepTime = 3
        # print(f'tCamera.__init__(): RETURN.')
    def __del__(self):
        # print(f'tCamera.__del__(): ENTER.')
        self.CAM.close()
        # print(f'tCamera.__del__(): RETURN.')
    def DoPreview(self):
        self.CAM.start_preview()
        sleep(5)
        self.CAM.stop_preview()
    def CaptureImage(self, name):
        self.CAM.capture(name)
## FUNCTIONS
def GetMeanSquaredErr(img01, img02):
    # GetMeanSquaredErr(): Return the 'Mean Squared Error' of given images
    # implementation: math
    # NOTE: the two images must have the same dimension
    # NOTE: Lower MSE ==>> More "similar"
    print(f'GS: Img01: {float(average(img01.astype("float")))}, Img02: {float(average(img02.astype("float")))}')
    err = sum((img01.astype("float") - img02.astype("float")) ** 2)
    err /= float(img01.shape[0] * img01.shape[1])
    return err
def DisplayPlot(img01, img02, nSSIM, nMSE, sTitle01, sTitle02):
    # DisplayPlot(): Display Given Images, MSE, SSIM, with Titles
    # Implementation: PyPlot Calls
    fig = plt.figure(f'{sTitle01} + " vs " + {sTitle02}')
    plt.suptitle("MSE: %.2f, SSIM: %.2f" % (nMSE, nSSIM))

    fig.add_subplot(1, 3, 1)  # 1 Row, 3 Cols. Pos 1
    plt.imshow(img01, cmap=plt.cm.gray)
    plt.axis("off")

    fig.add_subplot(1, 3, 2) # 1 Row, 3 Cols, Pos 2
    plt.imshow(img02, cmap=plt.cm.gray)
    plt.axis("off")

    fig.add_subplot(1, 3, 3) # 1 Row, 3 Cols, Pos 3
    plt.imshow(img01, cmap=plt.cm.gray)
    plt.axis("off")

    plt.show()
def DisplayDiffImg(img01,img02,diff):
    # The diff image contains the actual image differences between the two images
    # and is represented as a floating point data type in the range [0,1]
    # so we must convert the array to 8-bit unsigned integers in the range
    # [0,255] before we can use it with OpenCV
    diff = (diff * 255).astype("uint8")
    diff_box = merge([diff,diff,diff])
    # Threshold the difference image, followed by finding contours to
    # obtain the regions of the two input images that differ
    thresh = threshold(diff, 0, 255, THRESH_BINARY_INV | THRESH_OTSU)[1]
    contours = findContours(thresh, RETR_EXTERNAL, CHAIN_APPROX_SIMPLE)
    contours = contours[0] if len(contours) == 2 else contours[1]
    mask = zeros(img01.shape, dtype='uint8')
    filled_after = img02.copy()

    for c in contours:
        area = contourArea(c)
        if area > 40:
            x, y, w, h = boundingRect(c)
            rectangle(img01, (x, y), (x + w, y + h), (36, 255, 12), 2)
            rectangle(img02, (x, y), (x + w, y + h), (36, 255, 12), 2)
            rectangle(diff_box, (x, y), (x + w, y + h), (36, 255, 12), 2)
            drawContours(mask, [c], 0, (255, 255, 255), -1)
            drawContours(filled_after, [c], 0, (0, 255, 0), -1)

    imshow('before', img01)
    imshow('img02', img02)
    imshow('diff', diff)
    imshow('diff_box', diff_box)
    imshow('mask', mask)
    imshow('filled img02', filled_after)
    waitKey()
def DifferentEnough(s01, s02):
    # DifferentEnough(): Return True if Images are Sufficiently dissimilar
    # Implementation: Compare SSIM to Constant Threshold (MSE Currently Unused, TODO Expunge?)
    # print(f'PrettyDifferent(): ENTER.')
    img01 = imread(s01)
    img02 = imread(s02)

    gs_img01 = cvtColor(img01, COLOR_BGR2GRAY)
    gs_img02 = cvtColor(img02, COLOR_BGR2GRAY)
    m = GetMeanSquaredErr(gs_img01, gs_img02) # TODO: Expunge!
    (s, diff) = structural_similarity(gs_img01, gs_img02, full=True)
    # if (MSE_THRESHOLD < m) or (s < SSIM_THRESHOLD):
    if (s < SSIM_THRESHOLD):
        # print(f'{MSE_THRESHOLD} < GetMeanSquaredErr({m}) OR ssim({s}) < {SSIM_THRESHOLD}')
        # TODO: Expunge when this functionality is on the server
        DisplayPlot(img01, img02, s, m, s01, s02)
        # DisplayDiffImg(img01, img02, diff)
        print(f'PrettyDifferent(): RETURN TRUE.')
        return True
    print(f'PrettyDifferent(): RETURN FALSE.')
    return False
def SendToServer(sImg):
    # SendToServer(): TODO
    # Implementation: TODO
    pass
    # print(f'SendToServer(): ENTER.')
    # print(f'SendToServer(): RETURN.')
def ProcessImages():
    # ProcessImages(): Send Sufficiently Different Images to Server.
    # Implementation: Iterate on CaptureImage(), DifferentEnough(), (TODO) SendToServer()
    oCamera = tCamera()
    sFirstImgName = 'FirstImage.jpg'
    sSecondImgName = 'SecondImage.jpg'
    print("Capturing " + sFirstImgName + ".")
    sleep(3)  # Credit Matthew
    oCamera.CaptureImage(sFirstImgName)
    while True:
        print("Sleeping.")
        sleep(3)
        oCamera.CaptureImage(sSecondImgName)
        # print("Captured " + sSecondImgName + ".")
        if DifferentEnough(sFirstImgName, sSecondImgName):
            SendToServer(sSecondImgName)
        replace(sSecondImgName,sFirstImgName)
        print("Replaced " + sFirstImgName + " with " + sSecondImgName + ".")
## PROGRAM
if __name__ == '__main__':
   ProcessImages()
#     vNames = GetImages()
#     vImages = []
#     for x in range(2):
#         vImages.append(imread(vNames[x]))
#         vImages[x] = cvtColor(vImages[x], COLOR_BGR2GRAY)
#     compare_images(vImages[0], vImages[1], vNames[0], vNames[1])
#

# def GetImages():
#     vNames = []
#     oCamera = tCamera()
#     # print("GetImages(): ENTER.")
#     for x in range(2):
#         if x != 0:
#             # print("GetImages(): SLEEPING " + str(oCamera.SleepTime) + " Seconds.")
#             sleep(oCamera.SleepTime)
#         vNames.append("Image" + str(x) + ".jpg")
#         # print("Capturing " + vNames[x] + ".")
#         oCamera.CaptureImage(vNames[x])
#     # print("GetImages(): Return.")
#     return vNames
# def compare_images(img01, img02, s01,s02):
#     # compute the mean squared error and structural similarity
#     # index for the images
#     m = GetMeanSquaredErr(img01, img02)
#     (s, diff) = structural_similarity(img01, img02, full=True)
#     DisplayPlot(img01, img02, s, m, s01, s02)
