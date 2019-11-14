from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator
import os


def predict():
    """
    Function to predict if the retina image has diabetic retinopathy or not.

    Parameters
    ----------
    None

    Returns
    -------
    y_pred: bool
            Whether or not the retina has diabetic retinopathy.
    percent_chance: float
            Percentage of chance the retina image has diabetic retinopathy.
    """
    PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
    model_path = os.path.join(PROJECT_PATH,'ml_model/model.hd5')
    mod = load_model(model_path)

    test_gen = ImageDataGenerator(rescale=1. / 255)

    CAPTHA_ROOT = os.path.join(PROJECT_PATH,'uploads')
    test_data = test_gen.flow_from_directory(CAPTHA_ROOT,
                                             target_size=(64, 64),
                                             batch_size=32,
                                             class_mode='binary', shuffle=False)
    #print(CAPTHA_ROOT)
    predicted = mod.predict_generator(test_data)

    y_pred = predicted[0][0] > 0.4
    percent_chance = round(predicted[0][0] * 100, 2)

    return y_pred, percent_chance
