# Normal Smart Device

### Technical white paper

Authors: Normal Team - Dmytro Koziy, Inesa Hermaniuk, Nazar Mamchur 

Published: May 2018  

Applies to: Normal Smart Device    

Summary: This paper provides an overview of how Normal 
Smart Device users can set up the person identification smart system based on a Raspberry Pi 3.   

## Getting Started with Raspberry Pi
This section provides an information to help you succesfully set up Raspberry Pi to get a powerful portable cammera.
### Prerequisites:
1. Raspberry Pi 3   
2. MicroSD card with cappacity 8GB or more
3. USB webcam

* Set up your Raspberry Pi 3 - install OS by following <a href = "https://www.raspberrypi.org/help/noobs-setup/2/">this guide</a>
* Install Python 3.6
``` terminal
$ sudo apt-get install python-dev
$ curl -O https://bootstrap.pypa.io/get-pip.py
$ sudo python get-pip.py
```
* Install numpy 
``` terminal
$ pip install numpy 
```
* Install OpenCV by following <a href = "https://www.pyimagesearch.com/2017/09/04/raspbian-stretch-install-opencv-3-python-on-your-raspberry-pi/">this guide</a> 

* Install git
``` terminal
$ sudo apt-get install git
``` 

## Prerequisites
1. Install python 3.6.
2. Install, create and activate your virtual environment in the <strong> Recognition </strong> folder by following <a href = "https://virtualenv.pypa.io/en/stable/installation/">this guide</a>:

3. Install the required modules: 
```terminal 
Django==2.0.5 
djangorestframework==3.8.2
opencv-python==3.4.0.12 
opencv-contrib-python==3.4.0.12
```
## Clone the Repository
 1. On GitHub, navigate to the main page of the repository https://github.com/Dmytruto/NormalSmartDevice.
 2. Click <strong> Clone or download. </strong>
 3. Copy the URL provided.
 4. Open <strong> Git Bash. </strong>
 5. Choose and go to the directory where you want the cloned directory to be made.(It must be the same folder where you want to use this project)
 6. Type there <strong> git clone (URL that you copied) </strong>
 ```git
 $ git clone https://github.com/Dmytruto/NormalSmartDevice.git
 ```
 7. Press <strong> Enter. </strong> Your local clone will be created.

## Creating RESTful client on the Raspberry
1. Download folder with code from Github repository:
``` terminal
$ cd
$ mkdir NormalDir
$ cd NormalDir
$ git init
$ git config core.sparsecheckout true
$ echo Dmytruto/NormalSmartDevice/tree/InesaBranch/Device >> .git/info/sparse-checkout
$ git remote add origin -f https://github.com/Dmytruto/NormalSmartDevice
$ git pull origin master
```
2. Make program run at a startup:  
* Open rc.local file:
``` terminal
$ sudo nano /etc/rc.local
``` 
* Add the following line there
``` terminal
sudo python /home/NormalDir/detection.py &
```
## Face detection  
### Import detection.py 
You need to import module in a file you want to use it in
``` python
import NormalDir.detection as FDR
```
### Image preprocessing
``` python
FDR.detect(img)
```
<strong>Parametrer:</strong> img - image, where you want to detect a face and crop it out. 
<strong>Return type</strong> - numpy.array 

The function <strong>detect(img)</strong> detects face on an image and returns a croped and grayScaled image of a face if it was detected, or a numpy.array([0]) if not. 

### Take photos
``` python
FDR.process()
```
<strong>Parametrer:</strong> void   
<strong>Return type</strong> - void

The function <strong>process()</strong> contains a <strong>while True </strong> loop which takes 2 photos on webcam per second, converts an image to the base64 String.
### Make request to the server
``` python
FDR.request(str)
```

<strong>Parametrer:</strong> str - String, you want to send to the server   
<strong>Return type</strong> - bool

The function <strong>request(str)</strong> sends request with the str String to the server and returns its response.