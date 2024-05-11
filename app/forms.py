import os

from flask import render_template, request, flash

from app import app

from app.forms import (UploadForm, ResultForm)

from datetime import datetime

from werkzeug.utils import secure_filename

import numpy as np

# from keras_preprocessing import image

from keras.utils import img_to_array

from keras.models import load_model

from PIL import Image

import cv2