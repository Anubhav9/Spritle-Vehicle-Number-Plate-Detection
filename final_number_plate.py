from flask import Flask, render_template, jsonify,request
from werkzeug import secure_filename
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[3]:


import cv2
import imutils
import pytesseract
app = Flask(__name__)


@app.route('/upload')
def upload_file():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_files():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      print(f.filename)
      img=cv2.imread(f.filename)
      img_cvt=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
      img_new=cv2.bilateralFilter(img_cvt,10,10,10)
      img_new=cv2.Canny(img_new,10,200)
      print("here")
      cnt = cv2.findContours(img_new.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
      cnt = imutils.grab_contours(cnt)
      cnt=sorted(cnt, key = cv2.contourArea, reverse = True)[:20]
      PlateDetected = None 
      count = 0 
      for c in cnt:
      	perimeter = cv2.arcLength(c, True)
      	approx = cv2.approxPolyDP(c, 0.03 * perimeter, True)
      	if len(approx) == 4: 
      		PlateDetected = approx
      		break
      mask = np.zeros(img_cvt.shape,np.uint8)
      img_latest=cv2.drawContours(mask,[PlateDetected],0,255,-1)
      new_image = cv2.bitwise_and(img,img,mask=mask)
      (x, y) = np.where(mask == 255)
      (topx, topy) = (np.min(x), np.min(y))
      (bottomx, bottomy) = (np.max(x), np.max(y))
      Cropped = img_cvt[topx:bottomx+1, topy:bottomy+1]
      text = pytesseract.image_to_string(Cropped,config='--psm 11')
      return render_template('final.html',pred=text)
      ##return jsonify({'numberplate': text})
		
if __name__ == '__main__':
   app.run(debug = True)