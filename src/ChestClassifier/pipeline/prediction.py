import os
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image


class Prediction:
    def __init__(self, filename):
        self.filename = filename

    def predict(self):
        # load model
        model = load_model(os.path.join('artifacts', 'training', 'trained_model.h5'))

        image_name = self.filename
        test_image =  image.load_img(image_name, target_size = (64, 64))
        test_image =  image.img_to_array(test_image)
        test_image =  np.expand_dims(test_image, axis = 0)
        result = np.argmax(model.predict(test_image), axis=1)

        if result[0] == 0:
            prediction = 'Normal'
        else:
            prediction = 'Cancer'       
        return {'image': prediction}