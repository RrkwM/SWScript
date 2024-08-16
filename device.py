import os.path
import uiautomator2 as u2
import utils
import settings

#全局变量d
d = None


def init_device():
    global d
    device = u2.connect()  
    d = device
    # 确保目录存在
    if not os.path.exists(settings.screenshot_dir):
        os.makedirs(settings.screenshot_dir)

    return d

def screenshot():
    d.screenshot(settings.screenshot_path)

def swipe(scene, direction):
    if scene == '副本选择':
        start_rx, start_ry = utils.get_random_coordinate_int(374,609)
        end_rx, end_ry= utils.get_random_coordinate_int(313,273)
    elif scene == '层数选择':
        start_rx, start_ry = utils.get_random_coordinate_int(1075,626)
        end_rx, end_ry= utils.get_random_coordinate_int(1073,259)
    
    else:
        print("swipe: Unkown scene: " + scene)
        return
    #up向上滚动，down向下滚动
    if direction == 'down':
        d.swipe(start_rx,start_ry, end_rx,end_ry)
    elif direction == 'up':
        d.swipe(end_rx,end_ry,start_rx,start_ry)
    else:
        print("swipe: Unknown direction: " + direction)
        return

def click(x, y, bias=None):
    rx, ry = utils.get_random_coordinate_int(x, y)
    d.click(rx, ry)