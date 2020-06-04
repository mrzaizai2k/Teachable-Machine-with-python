import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
# Kết nối với arduino###################################################################################################################
import serial
import time
arduino=serial.Serial('COM8',9600)
time.sleep(2)
# Teachable machine###################################################################################################################
import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np

# Disable scientific notation for clarity 
# (set_printoptions dùng biểu diễn bảo nhiêu số sau dấu phẩy, suppress để cho đẹp số thay vì dùng e mũ)
np.set_printoptions(suppress=True) 

# Load the model
model = tensorflow.keras.models.load_model('keras_model.h5')

# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1.
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

# Replace this with the path to your image
# Nên để hình vào thư mục chứa py)
image = Image.open('pythonimage.jpg')

#resize the image to a 224x224 with the same strategy as in TM2:
#resizing the image to be at least 224x224 and then cropping from the center
# Cắt hình chỉ lấy phần trung tâm, chứ không thu nhỏ
size = (224, 224)
image = ImageOps.fit(image, size, Image.ANTIALIAS)

#turn the image into a numpy array
# Chuyển hình ảnh sang ma trận số 
image_array = np.asarray(image)

# display the resized image
image.show()

# Normalize the image
normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

# Load the image into the array
data[0] = normalized_image_array

# run the inference
prediction = model.predict(data)
print(prediction)

############# Kết nối với arduino cho sáng LED nè#####################################################################################
notilt = prediction[0,0]
lefttilt = prediction[0,1]
righttilt = prediction[0,2]

print ("lefttilt is %f" %(lefttilt))
max = max(notilt, lefttilt, righttilt)
if max == lefttilt:
    arduino.write(b'1')

