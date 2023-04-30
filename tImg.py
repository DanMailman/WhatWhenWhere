# tImg.py - Class for OpenCV/ndarray  Images and Associated Data
# REF: ndarray: https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html
from __future__ import annotations
from tCamera import tCamera
import matplotlib.pyplot as plt  # TODO: Import Used Methods Explicitly
from cv2 import imwrite                            # REF: https://docs.opencv.org/3.4/d4/da8/group__imgcodecs.html#gabbc7ef1aa2edfaa87772f1202d67e0ce
from cv2 import COLOR_BGR2GRAY                     # REF: https://docs.opencv.org/3.4/d8/d01/group__imgproc__color__conversions.html
from cv2 import cvtColor                           # REF: https://www.educba.com/opencv-cvtcolor/
from skimage.metrics import structural_similarity  # REF: https://scikit-image.org/docs/stable/api/skimage.metrics.html#skimage.metrics.structural_similarity
class tImg:
    # tImg - OpenCV Image Methods
    FILE_TYPE = 'png'  # LOSSLESS, Can have Transparent Background
    SSIM_THRESHOLD = 0.80  # SSIM in [-1:1], where 1 indicates perfect similarity.
    def __init__(self, Camera: tCamera, ID: str = ''):
        # __init__(): Constructor
        # Implementation: Set Instance Variables, Take Pic, Write File
        print(f'tImg(): ENTER.')
        self.Camera = Camera  # The Camera for updating the image
        self.ID = ID  # The Source ID for the Image
        self.dictCamMeta, self.ndaImage = self.Camera.capture()
        self.fn = self.GetTitle() + '.' + tImg.FILE_TYPE
        self.WriteToDisk()
        print(f'tImg(): RETURN.')
    def GetGreyscale(self):
        # GetGreyscale(): Return GreyScale Version of Image
        # Implementation: cvtColor(), COLOR_BGR2GRAY
        return cvtColor(self.ndaImage, COLOR_BGR2GRAY)
    def SendToServer(self):
        # SendToServer(): Send Image and MetaData to Server
        # Implementation: TODO
        # REF: https://stackoverflow.com/questions/47391774/send-and-receive-objects-through-sockets-in-python
        # REF: https://grpc.io/docs/languages/python/
        pass
    def UpdateImageAndMeta(self):
        # UpdateImageAndMeta(): Update Image and MetaData From Camera
        # Implementation: Camera.capture()
        self.dictCamMeta, self.ndaImage = self.Camera.capture()
    def WriteToDisk(self):
        # WriteToDisk(): Save Image to Disk as FILE_TYPE
        # Implementation: imwrite()
        # REF: https://stackoverflow.com/questions/51808908/how-to-check-if-python-cv2-imwrite-worked-properly
        imwrite(self.fn, self.ndaImage)
    def GetTitle(self):
        # GetTitle(): Return Title for Image
        # Implementation: String Concatenation with ID and Camera Metadata
        return self.ID + '_' + tCamera.MakeName(self.dictCamMeta)
    def ReplaceImageAndMeta(self, Img: tImg):
        # ReplaceImage(): Replace Image Array and Camera MetaData for Image
        # Implementation: Assignment
        self.dictCamMeta = Img.dictCamMeta
        self.ndaImage = Img.ndaImage
    @staticmethod
    def GetAvgAndImgFromSSIM(Img01: tImg, Img02: tImg) -> dict:
        # GeNumAndArrayForGreyScaleSSIM(): Compare using SSIM. Return mean structural similarity index and full diff image
        # Implementation: structural_similarity()
        #  TODO: Would something other than greyscale make a difference?
        dictRet = dict()  # dictRet = {'avg': None, 'img': None} TODO Expunge Commented
        dictRet['avg'], dictRet['img'] = structural_similarity(Img01.GetGreyscale(), Img02.GetGreyscale(), full=True)
        return dictRet
    @staticmethod
    def GetImageFromSSIM(Img01: tImg, Img02: tImg):
        # GetGreyScaleDiff(): Return Image Representing SSIM
        # Implementation: GeNumAndArrayForGreyScaleSSIM
        return tImg.GetAvgAndImgFromSSIM(Img01, Img02)['img']
    @staticmethod
    def GetAverageFromSSIM(Img01: tImg, Img02: tImg):
        # GetGreyScaleDiff(): Return Mean SSIM for Images
        # Implementation: GeNumAndArrayForGreyScaleSSIM
        return tImg.GetAvgAndImgFromSSIM(Img01, Img02)['avg']
    @staticmethod
    def DifferentEnough(Img01: tImg, Img02: tImg):
        # DifferentEnough(): Return True of Images are Sufficiently Different
        # Implementation: GetAverageSSIM()
        SSIM_THRESHOLD = 0.80  # SSIM in [-1:1], where 1 indicates perfect similarity.
        return True if tImg.GetAverageFromSSIM(Img01, Img02) < SSIM_THRESHOLD else False
    @staticmethod
    def ShowDiff(Img01: tImg, Img02: tImg):
        # ShowDiff(): Display Given Images
        # Implementation: PyPlot Calls
        # TODO: https://stackoverflow.com/questions/56183201/detect-and-visualize-differences-between-two-images-with-opencv-python
        # TODO: Manage figure, title: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html
        NUM_ROWS = 1
        NUM_COLS = 3
        fig = plt.figure()
        plt.suptitle(f'{Img01.GetTitle()} + " vs " + {Img02.GetTitle()}')
        plt.title("SSIM: %.2f" % (tImg.GetAverageFromSSIM(Img01, Img02)))
        vImg = [Img01, Img02, Img01]  # TODO: Replace last member with Ideal Difference-Showing Image
        for Idx, Img in enumerate(vImg):
            fig.add_subplot(NUM_ROWS, NUM_COLS, 1+Idx)
            plt.imshow(Img.ndaImage, cmap=plt.cm.gray)
            plt.axis("off")
        plt.show()
## PROGRAM
if __name__ == '__main__':
    print(f'{__name__}: ENTER.')
    from time import sleep
    SLEEP_SECS = 3
    def ProcessImages():
        # ProcessImages(): Send Sufficiently Different Images to Server.
        # Implementation: Iterate on CaptureImage(), DifferentEnough(), (TODO) SendToServer()
        oCam = tCamera()
        oImg01 = tImg(oCam, 'Img01')
        oImg02 = tImg(oCam, 'Img02')
        while True:
            print("Sleeping.")
            sleep(SLEEP_SECS)
            oImg02.UpdateImageAndMeta()
            if tImg.DifferentEnough(oImg01, oImg02):
                tImg.ShowDiff(oImg01, oImg02)
                oImg01.SendToServer()
                oImg02.SendToServer()
            oImg01.ReplaceImageAndMeta(oImg02)
    ProcessImages()
    print(f'{__name__}: RETURN.')
