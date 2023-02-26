"""
    Skript, ktory sluzi na porovnanie upravenych predikcii pre analyzu citlivosti
"""

import os
import re
from PIL import Image


def get_concat_h(im1, im2, im3, im4):
    """
        Funkcia na horizontalne spojenie obrazkov
    """
    dst = Image.new('RGB', (im1.width + im2.width + im3.width + im4.width, im1.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    dst.paste(im3, (im1.width + im2.width, 0))
    dst.paste(im4, (im1.width + im2.width + im3.width, 0))
    return dst


def get_comparison(dir_original, dir_shifted_one_up, dir_shifted_two_up, dir_shifted_one_down, dir_compared):
    """
        Funkcia na ziskanie plotov zo 4 suborov, ktore ak sa zhoduju v ID v nazve, spoja sa do jedneho obrazka
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

"""Zadefinovanie ciest k suborom"""
dir_original_preds = os.path.dirname(os.path.abspath(__file__)) + '\\plots\\Analyza_citlivosti\\predictions_original\\original_pred_kepler\\'
dir_shift_one_up_pred = os.path.dirname(os.path.abspath(__file__)) + '\\plots\\Analyza_citlivosti\\predictions_one_up\\one_up_pred_kepler\\'
dir_shift_two_up_pred = os.path.dirname(os.path.abspath(__file__)) + '\\plots\\Analyza_citlivosti\\predictions_two_up\\two_up_pred_kepler\\'
dir_shift_one_down_pred = os.path.dirname(os.path.abspath(__file__)) + '\\plots\\Analyza_citlivosti\\predictions_one_down\\one_down_pred_kepler\\'
dir_compared_preds = os.path.dirname(os.path.abspath(__file__)) + '\\plots\\Analyza_citlivosti\\comparison\\compared_kepler\\'

"""Pouzitie funkcie na porovnanie plotov predikcii"""
get_comparison(dir_original_preds, dir_shift_one_up_pred, dir_shift_two_up_pred, dir_shift_one_down_pred, dir_compared_preds)



