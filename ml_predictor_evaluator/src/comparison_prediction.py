import os
import re
from PIL import Image


def get_concat_v(im1, im2):
    """
        Function to vertically join images
    :param im1:
    :param im2:
    :return:
    """
    dst = Image.new('RGB', (im1.width, im1.height + im2.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (0, im1.height))
    return dst


def get_comparison(dir_original, dir_adjusted, dir_compared):
    """
        Function to vertically join images of original and adjusted predictions
    :param dir_original: directory with original predictions
    :param dir_adjusted: directory with adjusted predictions
    :param dir_compared: directory where to save compared predictions
    :return:
    """
    for original_pred_name in os.listdir(dir_original):
        orig_id = re.sub(r"\D", "", original_pred_name)
        img1 = Image.open(dir_original_predictions + original_pred_name)

        for adjusted_pred_name in os.listdir(dir_adjusted):
            adjusted_id = re.sub(r"\D", "", adjusted_pred_name)
            if adjusted_id == orig_id:
                img2 = Image.open(dir_adjusted_predictions + adjusted_pred_name)

                get_concat_v(img1, img2).save(f'{dir_compared}' + f'{original_pred_name}')


dir_original_predictions = os.path.dirname(os.path.abspath(__file__)) + '\\plots\\citlivost_true\\original_pred_tess\\'
dir_adjusted_predictions = os.path.dirname(os.path.abspath(__file__)) + '\\plots\\citlivost_upravene' \
                                                                        '\\upravene_pred_tess\\ '
dir_compared_preds = os.path.dirname(os.path.abspath(__file__)) + '\\plots\\predictions_compared\\compared_tess\\'

# COMPARISON OF ORIGINAL AND ADJUSTED PREDICTION
get_comparison(dir_original_predictions, dir_adjusted_predictions, dir_compared_preds)



