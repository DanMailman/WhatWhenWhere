# tCamera.py - Camera Class to Return OpenCV Images
# REF: https://pyimagesearch.com/2015/03/30/accessing-the-raspberry-pi-camera-with-opencv-and-python/
# REF: https://picamera.readthedocs.io/en/release-1.13/
from picamera.array import PiRGBArray  # REF: https://picamera.readthedocs.io/en/release-1.13/api_array.html#pirgbarray
from picamera import PiCamera          # REF: https://picamera.readthedocs.io/en/release-1.13/index.html
from time import sleep                 # REF: https://docs.python.org/3/library/time.html#time.sleep
from numpy import ndarray              # REF: https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy-ndarray
from socket import gethostname         # REF: https://docs.python.org/3/library/socket.html#socket.gethostname
from Util import RoundToMultiple, NOW, HumanReadable
class tCamera:
    # tCamera - Camera Class to Return OpenCV Images
    def __init__(self, ID: str = ''):
        # __init__(): Constructor
        # Implementation: Instance Variable Assigment, Initialization
        # NOTE: when outputting to unencoded formats, the camera rounds the requested resolution.
        #       The horizontal resolution is rounded up to the nearest multiple of 32 pixels,
        #       while the vertical resolution is rounded up to the nearest multiple of 16 pixels.
        #       REF: https://picamera.readthedocs.io/en/release-1.13/recipes2.html?highlight=round#capturing-to-a-numpy-array
        # REF: https://picamera.readthedocs.io/en/release-1.13/api_array.html#pirgbarray
        # print(f'tCamera(): ENTER.')
        WAKEUP_SECONDS = 0.1  # 1/10th Second for Camera to Warm up
        HORZ_CAM_ROUND = 32  # See NOTE above
        VERT_CAM_ROUND = 16  # See NOTE above
        self.camera = PiCamera()
        self.MetaData = dict()
        self.MetaData['ID'] = gethostname() if ID == '' else ID
        self.MetaData['Timestamp'] = NOW()
        self.MetaData['dpxw'], self.MetaData['dpxh'] = self.camera.resolution  # Default Width, Height in Pixels
        self.MetaData['pxw'] = RoundToMultiple(self.MetaData['dpxw'], HORZ_CAM_ROUND, 'down')
        self.MetaData['pxh'] = RoundToMultiple(self.MetaData['dpxh'], VERT_CAM_ROUND, 'down')
        self.camera.resolution = (self.MetaData['pxw'], self.MetaData['pxh'])
        self.praRawCapture = PiRGBArray(self.camera)  # PiRGBArray to Receive Raw Data
        sleep(WAKEUP_SECONDS)
        self.capture()
        # print(f"tCamera(): ID({self.MetaData['ID']}), "
        #       f"Pixels: W({self.MetaData['dpxw']}), H({self.MetaData['dpxh']}), "
        #       f"ROUND: W({self.MetaData['pxw']}), H({self.MetaData['pxh']}): "
        #       f'RETURN.')
        return
    def capture(self,ID: str = None) -> (dict,ndarray):
        # capture(): Update and Return Image and MetaData Dict
        # Implementation: PiCamera.capture()
        # print(f'capture(): ENTER.')
        self.praRawCapture.truncate(0)
        self.camera.capture(self.praRawCapture, format='bgr')
        self.MetaData['Timestamp'] = NOW()
        # print(f'capture(): RETURN.')
        return self.MetaData, self.praRawCapture.array
    def close(self):
        # print(f'tCamera.close(): ENTER.')
        self.camera.close()
        # print(f'tCamera.close(): RETURN.')
    @staticmethod
    def MakeName(dictMeta: dict) -> str:
        return dictMeta['ID'] + '-' + HumanReadable(dictMeta['Timestamp'])
if __name__ == '__main__':
    def main():
        from cv2 import imshow   # REF: https://docs.opencv.org/4.x/d7/dfc/group__highgui.html#ga453d42fe4cb60e5723281a89973ee563
        from cv2 import waitKey  # REF: https://docs.opencv.org/4.x/d7/dfc/group__highgui.html#ga5628525ad33f52eab17feebcfba38bd7
        oCam = tCamera()
        for i in range(3):
            dictMeta,ndaImage = oCam.capture()
            imshow(tCamera.MakeName(dictMeta), ndaImage)
            waitKey(0)
        oCam.close()
    main()

