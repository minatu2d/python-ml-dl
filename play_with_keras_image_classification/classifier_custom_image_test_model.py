from keras.models import load_model
from keras.preprocessing.image import load_img, img_to_array
import sys
import numpy as np

weight_file =  sys.argv[1]
img_file = sys.argv[2] 
print("Weight file :{0}".format(weight_file))
print("Weight file :{0}".format(weight_file))

# returns a compiled model
# identical to the previous one
model = load_model(weight_file)

# Load image
img = load_img(img_file, target_size=(150, 150))    # 画像ファイルの読み込み
img_array = img_to_array(img) / 255                                     #
img_list = []
img_list.append(img_array)
pred = model.predict(np.array(img_list))
print(pred)
