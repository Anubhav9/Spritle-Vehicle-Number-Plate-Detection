**Spritle-Vehicle-Number-Plate-Detection**


**Made for Spritle as a part of their hiring assignment. It detects the number plate of a car and returns the value written on it. Made using OpenCV and Python**


**Steps to run this program**

a) Clone this repository on your local system and run the command 'python3 final_number_plate.py'. This is a hosted on Flask and therefore as soon as you hit this
command, it will fire up a local server on your system/localhost. Minimise the terminal and follow the below steps.

b) Navigate to templates. There is a file called upload.html. Open this using any browser and upload any image file and click on submit button.

c) It will redirect you to the result page. Please check if this was the result you were expecting.

**How this program was made?**

The following steps were followed

i) As soon as an image was given as input, it is converted into a gray scale image to reduce computation.

ii) Bilateral Filter was applied on the gray scale image to reduce the background noise.

iii) From the output we got after applying Bilateral Filter, Canny edge detection was used to detect all the possible edges.

iv) After the edges have been detected, we look out for the item which has 4 edges/boundries because this what a number plate symbolises to.

v) We then mask the image to get only the region of interest.

vi) Once, region of interest has been found, it is cropped and saved into a new image.

vii) On the saved image Tesseract OCR is applied to get the corresponding text on the number plate.

vii) This is returned as the final answer.


**Programming Language/Technologies/Libraries Used**

Programming Language: Python

Technologies: OpenCV,Tesseract OCR

Backend: Flask/REST API

**Known Issues with this program**

a) OCR often gets confused between 0 and O as they both look similar.

b) There might be case that you can get unwanted characters with the answer. I have tried my best to avoid this, but still it might happen.

c) Image quality must be of high qualify and preferrably captured from a close distance. Otherwise, it might not detect the number plate.

Rest assured, I am still working on this and will be resolved soon.


**Please note if you want to read the source code, please refer Cars.py/Cars.ipynb because it contains the comments for better understanding. There exists no comments in the flask file. So, if you are trying to understand the source code, please refer above as mentioned**.
