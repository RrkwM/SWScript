import random
import time
import settings
from cnocr import CnOcr
from PIL import Image

ocr = None

def init_ocr():
    global ocr
    ocr = CnOcr()

def get_random_coordinate_int(x1, y1, bias=None):
    if bias is None:
        random_int_1 = random.randint(-10, 10)
        random_int_2 = random.randint(-3, 3)
        x = random_int_1 + x1
        y = random_int_2 + y1
    else:
        x = random.randint(-bias, bias)
        y = random.randint(-bias, bias)
    return (x, y)

def wait(scene=None, seconds=None):
    # 设置默认的等待时间
    default_times = {
        'animation': 0.75,
        'loading': 5,
        'battle': 15
    }
    
    # 使用传入的 seconds 参数，如果提供了的话
    if seconds is not None:
        time_to_wait = seconds
    elif scene in default_times:
        time_to_wait = default_times[scene]
    else:
        print(f"wait: Unknown scene: {scene}, skipping wait")
        return
    
    # 执行等待
    time.sleep(time_to_wait)

def get_ocr_text(x1, y1, x2, y2):
    image = Image.open(settings.screenshot_path)
    cropped_image = image.crop((x1,y1,x2,y2))

    result = ocr.ocr(img_fp=cropped_image)
    text = ''.join([item['text'] for item in result if 'text' in item])
    
    return text