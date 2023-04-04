"""
    In this python script we merge shifted predictions into one image.
"""

import os
import re
from PIL import Image


def get_concat_h(im1, im2, im3, im4):
    """
        Function for merging images horizontally.
        :im1: image of original plotted prediction;
        :im2: image of shifted plotted prediction 1 step up;
        :im3: image of shifted plotted prediction 2 steps up;
        :im4: image of shifted plotted prediction 1 step down;
        :return: image; merged image
    """
    dst = Image.new('RGB', (im1.width + im2.width + im3.width + im4.width, im1.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    dst.paste(im3, (im1.width + im2.width, 0))
    dst.paste(im4, (im1.width + im2.width + im3.width, 0))
    return dst


def get_comparison(dir_original, dir_shifted_one_up, dir_shifted_two_up, dir_shifted_one_down, dir_compared):
    """
        Function for finding if predictions with shifted values we achieved to plot and if so, we  will merge them horizontally.
        :dir_original: path to directory with original plotted predictions;
        :dir_shifted_one_up: path to directory with plotted predictions shifted 1 value up;
        :dir_shifted_two_up: path to directory with plotted predictions shifted 2 values up;
        :dir_shifted_one_down: path to directory with plotted predictions shifted 1 values down;
        :dir_compared: path to directory where we will save merged images;
    """
    global img2, img3, img4
    for original_pred_name in os.listdir(dir_original):
        orig_id = re.sub(r"\D", "", original_pred_name)
        img1 = Image.open(dir_original + original_pred_name)

        for shifted_one_up_pred_name in os.listdir(dir_shifted_one_up):
            shifted_one_up_id = re.sub(r"\D", "", shifted_one_up_pred_name)
            if shifted_one_up_id[1:] == orig_id:
                img2 = Image.open(dir_shifted_one_up + shifted_one_up_pred_name)
                break
            else:
                img2 = None

        for shifted_two_up_pred_name in os.listdir(dir_shifted_two_up):
            shifted_two_up_id = re.sub(r"\D", "", shifted_two_up_pred_name)
            if shifted_two_up_id[1:] == orig_id:
                img3 = Image.open(dir_shifted_two_up + shifted_two_up_pred_name)
                break
            else:
                img3 = None

        for shifted_one_down_pred_name in os.listdir(dir_shifted_one_down):
            shifted_one_down_id = re.sub(r"\D", "", shifted_one_down_pred_name)
            if shifted_one_down_id[1:] == orig_id:
                img4 = Image.open(dir_shifted_one_down + shifted_one_down_pred_name)
                break
            else:
                img4 = None
        if img2 is not None and img3 is not None and img4 is not None:
            get_concat_h(img1, img2, img3, img4).save(f'{dir_compared}' + f'{original_pred_name}')

"""We will define path to directiories we need to use in function get_comparison()"""
dir_original_preds = os.path.dirname(os.path.abspath(__file__)) + '\\plots\\Sensitivity_analysis\\predictions_original\\original_pred_kepler\\'
dir_shift_one_up_pred = os.path.dirname(os.path.abspath(__file__)) + '\\plots\\Sensitivity_analysis\\predictions_one_up\\one_up_pred_kepler\\'
dir_shift_two_up_pred = os.path.dirname(os.path.abspath(__file__)) + '\\plots\\Sensitivity_analysis\\predictions_two_up\\two_up_pred_kepler\\'
dir_shift_one_down_pred = os.path.dirname(os.path.abspath(__file__)) + '\\plots\\Sensitivity_analysis\\predictions_one_down\\one_down_pred_kepler\\'
dir_compared_preds = os.path.dirname(os.path.abspath(__file__)) + '\\plots\\Sensitivity_analysis\\comparison\\compared_kepler\\'

get_comparison(dir_original_preds, dir_shift_one_up_pred, dir_shift_two_up_pred, dir_shift_one_down_pred, dir_compared_preds)



