# WhatWhenWhere
- Client: Raspberry PI: Sends Timestamp, Image, Lat, Lon, Pitch, Roll, Heading To Server 
- Server: Linode
  - Receives, Organizes Client Images
  - Performs ML Analyses on Images
  - Browser GUI to view Images/Analyses
## Links to Session Videos
- [Project Start Discussion - README.md, Github/Collaboration, Requirements, Design](https://www.dropbox.com/s/0n04fva9aox8ddp/01_Project_Start_Discussion_README_Github_Collaboration_Requirements_Design.mp4?dl=0)
- [Image Change Detection (Saving Images, Measuring Similarity) - Session01](https://www.dropbox.com/s/g8hp5dt9finyv82/02_Image_Change_Detection_Session01.mp4?dl=0)
- [Image Change Detection (Displaying Images in a Useful Way) -  Session02](https://www.dropbox.com/s/gwg2qzi657srhc0/03_Image_Change_Detection_Session02.mp4?dl=0)
- [Making Classes for Images and Cameras](https://www.dropbox.com/s/1uzpz7x6c1ai35k/04_Classes_for_Image_and_Camera.mp4?dl=0)
## ASSUMPTIONS
- Raspberry PI 3 or 4
## Useful URLs
### Development Environment
- [\[solved \]Warning **: Error retrieving accessibility bus address:](https://forums.raspberrypi.com/viewtopic.php?t=196070)
- [How to set environment variables in PyCharm?](https://stackoverflow.com/questions/42708389/how-to-set-environment-variables-in-pycharm)
- [How to enable X11 forwarding in PyCharm SSH session?](https://stackoverflow.com/questions/41892039/how-to-enable-x11-forwarding-in-pycharm-ssh-session)
- [How do I type hint a method with the type of the enclosing class?](https://stackoverflow.com/questions/33533148/how-do-i-type-hint-a-method-with-the-type-of-the-enclosing-class)
### Python Type-Suggesting
- [Type hinting / annotation (PEP 484) for numpy.ndarray](https://stackoverflow.com/questions/35673895/type-hinting-annotation-pep-484-for-numpy-ndarray)
### Coding Python Well
- [Python 3 for Scientists](https://python-3-for-scientists.readthedocs.io/en/latest/index.html)
### Image Files on Disk
 - [JPEG vs. PNG](https://www.adobe.com/creativecloud/file-types/image/comparison/jpeg-vs-png.html)
### Capturing Images (Python, PiCamera, OpenCV)
- [Taking Photos with Python](https://libguides.lib.msu.edu/raspberry_pi/take_photo_w_python)
- [keep all picamera parameters held constant](https://raspberrypi.stackexchange.com/questions/28620/keyboardinterrupt-handling-with-picamera)
### OpenCV Image Comparison
- [Comparing Two Images](https://pyimagesearch.com/2014/09/15/python-compare-two-images/)
- [Detect, Visualize, Differences](https://stackoverflow.com/questions/56183201/detect-and-visualize-differences-between-two-images-with-opencv-python)
### Displaying Graphical Information
- [Installing MatPlotLib](https://linuxhint.com/install-matplotlib-raspberry-pi/)
### GPS Position
- [Calculate GPS position offset using roll, pitch, yaw and length](https://forums.raspberrypi.com/viewtopic.php?t=223080)
### Pitch, Roll, Yaw(Heading)
- [Calibration of an Inertial Measurement Unit (IMU) with Raspberry Pi - Part 1](https://makersportal.com/blog/calibration-of-an-inertial-measurement-unit-with-raspberry-pi)
- [Gyroscope and Accelerometer Calibration with Raspberry Pi](https://makersportal.com/blog/calibration-of-an-inertial-measurement-unit-imu-with-raspberry-pi-part-ii)
- [MPU9250 Calibration using Python and a Raspberry Pi Computer](https://github.com/makerportal/mpu92-calibration)
- [Interfacing An MPU6050 (Gyroscope + Accelerometer) Sensor Module To A Raspberry Pi](https://www.woolseyworkshop.com/2018/09/06/interfacing-an-mpu6050-gyroscope-accelerometer-sensor-module-to-a-raspberry-pi/)
- [Issues with accelero and gyro sensitivity](https://forums.raspberrypi.com/viewtopic.php?t=175001)
### Hardware for Pitch, Roll, Heading
- [Accelerometer, Gyroscope, and Magnetometer Analysis with Raspberry Pi Part I: Basic Readings](https://makersportal.com/blog/2019/11/11/raspberry-pi-python-accelerometer-gyroscope-magnetometer)
- [MPU9250 Inertial Measurement Unit (IMU)](https://makersportal.com/shop/mpu9250-inertial-measurement-unit-imu)
- [9D0F MPU 9250 SPI/IIC 9-Axis Attitude + Gyro + Accelerator + Magnetometer Module
](https://www.ebay.com/itm/224776937283?_trkparms=amclksrc%3DITM%26aid%3D1110018%26algo%3DHOMESPLICE.COMPLISTINGS%26ao%3D1%26asc%3D20200818142838%26meid%3Da8fdfc1bc8c142d2aaa2cea3337124a6%26pid%3D101197%26rk%3D1%26rkt%3D12%26sd%3D203980926899%26itm%3D224776937283%26pmt%3D1%26noa%3D0%26pg%3D2047675%26algv%3DItemStripV101HighAdFee%26brand%3DUnbranded&_trksid=p2047675.c101197.m1850&amdata=cksum%3A224776937283a8fdfc1bc8c142d2aaa2cea3337124a6%7Cenc%3AAQAHAAAA8C6VSE2uGkOxRbBlxpADtEtgP%252BOOxBIrBNlUKYUTGcTgDsrBeD8UmroOKseavaLSwVIXaHXQrFhHCDtUAbUsQpdVIcKn0PyYSLxGYNg%252BnLVuiaKEDbqeOu%252FGXR5TnLwWg%252FOdbI09InqsMYaF26PyvYetc0gHvYpOotTcpOxlDM%252BxjlIU0Zo%252FHGq9r3JY3BHeH914ONDTvV40KateunZXZ0Jnod91SEavEiGbY4gzE6%252BHyp2jdndTGoYp412BVyohSY5QRCyBnVPLCj7QDqVCB7oHM7JDNLWd2UM0WodFnsrPRN%252Fn8k8N5GYTEVkTW%252BMgxA%253D%253D%7Campid%3APL_CLK%7Cclp%3A2047675)
- [Adafruit LSM6DSOX + LIS3MDL - Precision 9 DoF IMU - STEMMA QT / Qwiic](https://www.adafruit.com/product/4517#technical-details)
### Hardware for Latitude, Longitude
- [setup GPS Module with Raspberry Pi and perform Google Map Geo-Location Tracking](https://collabnix.com/how-to-setup-gps-module-with-raspberry-pi-and-perform-google-map-geo-location-tracking-in-real-time/)
- [HiLetgo GY-NEO6MV2 NEO-6M GPS Flight Controller Module 3V-5V](https://smile.amazon.com/HiLetgo-GY-NEO6MV2-Controller-Ceramic-Antenna/dp/B01D1D0F5M/ref=sr_1_1_sspa?crid=32KIXT2OVZ9QE&keywords=neo+6m+gps+raspberry+pi&qid=1661472103&s=electronics&sprefix=neo+6m+gps+raspberry+po%2Celectronics%2C83&sr=1-1-spons&psc=1)
- [NEO-6M GPS Module Aircraft Flight Controller](https://www.ebay.com/itm/403641520095?chn=ps&_trkparms=ispr%3D1&amdata=enc%3A1hD9NYea0R0mW00gIY0v5Mw52&norover=1&mkevt=1&mkrid=711-117182-37290-0&mkcid=2&itemid=403641520095&targetid=&device=c&mktype=pla&googleloc=9013291&poi=&campaignid=17597089569&mkgroupid=&rlsatarget=&abcId=9300988&merchantid=586214813&gclid=CjwKCAjwu5yYBhAjEiwAKXk_eIeAqFu03iGLJ6_CFwiKTbPa25-3XIIDiOHdFAAuonm2p_1PQgsVexoCAGAQAvD_BwE)
- [Adafruit Ultimate GPS HAT for Raspberry Pi](https://learn.adafruit.com/adafruit-ultimate-gps-hat-for-raspberry-pi)
### Hardware for Images (Raspberry PI Camera)
- [Getting started with the Camera Module](https://projects.raspberrypi.org/en/projects/getting-started-with-picamera)
- [raspberry pi camera module v2](https://smile.amazon.com/Raspberry-Pi-Camera-Module-Megapixel/dp/B01ER2SKFS/ref=sr_1_3?keywords=raspberry+pi+camera+module+v2&qid=1661472427&sprefix=raspberry+pi+camera%2Caps%2C108&sr=8-3)
- [Raspberry Pi Camera Module v2 8MP 1080P](https://www.ebay.com/itm/294928606528?hash=item44ab1d6540:g:o88AAOSw49xhlwLY&amdata=enc%3AAQAHAAAA8JmS41wEMMER0dMaVviFaByYfYPDAyrhK5X7kAT1HqPBBaVPikf2ekUbByi%2FgoBuoekFQgCwurjZGrfaqq9m0EVrtljt151Fb7c8yQiqoUSw5o%2Bx0ZDJdT3nTfxMIW6m1P%2FlG2JCgPZBN2JM4HtzPqoHmjpLLyR5Y6%2B4vLeeWsldflC%2BhXa20aghnY5UkS%2By87aVTICa5RRnAlkQN9YeOX28mHeiqMsXEPJowox2c4LsLpjykpSconbfYKGKz6Wy3uAxyMgvbd9xFDS8%2FUEjoMLCRNGty0ulLlE3lX6at4rOcvEHOxOH3ELl2APEshjQXg%3D%3D%7Ctkp%3ABFBM5p_W99pg)
### Hardware for Storage (OPTIONAL)
- [How to set up an SSD with the Raspberry Pi 4](https://thepihut.com/blogs/raspberry-pi-tutorials/how-to-set-up-an-ssd-with-the-raspberry-pi)
- [Western Digital 240GB WD Green Internal PC SSD Solid State Drive](https://smile.amazon.com/Western-Digital-240GB-2-5-Inch-Internal/dp/B076Y374ZH/ref=sr_1_3?crid=3KUATWRKSIFGA&keywords=WD+Green+120GB+2.5%22+SSD&qid=1661472915&sprefix=wd+green+120gb+2.5+ssd%2Caps%2C195&sr=8-3)
- [WD Green 120GB 2.5" SSD](https://www.ebay.com/itm/175365399223?hash=item28d497a2b7:g:94kAAOSwCSxibdAK&amdata=enc%3AAQAHAAAA8GtC477enOLK4K4BCOloMW4waekj2oq2I%2FxHRuUoxWK%2BcNw6tKJ6%2Fsfvcw%2FsxdcntsH99eCimKjhSB9c2jxiqViZ0%2Bx0Xgm0iohqB4gvgASqgAGo37pQoA8fyjRYavYmt9SMl2gkOcOO3RMhnYDFL%2Bb72X2jNi2jxP%2BHNSJPElkL2dKJy7NNkyheCKAWf0OgcYXql2IP9WE0e4aFNtigJM10ZIEFqUrrTXiYvN9xKyNw8tXyRrXqHTJLwJACOoid6dJ3NS3kxTv6RsCpxYaccRdGA841iobKlOxyBm%2FxjZp19ckuPhgilR3g7TJuzY7v4w%3D%3D%7Ctkp%3ABFBM9LOe-Npg)
### Hardware for Mobile (Cellular?) Communications
- ?
### Hardware for Power while Mobile
- ?
### Housing/Enclosure (DIY?, 3D Printed?)
- ?
