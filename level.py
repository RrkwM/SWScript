import math
import device
import utils

#选择关卡用的坐标
level_coord = [(313,273),(310,377),(304,493),(354,606)]
num_coord_1 = [(1068,268),(1068,385),(1073,519)]
num_coord_2 = [(1068,295)]
num_coord_3 = [(1057,352),(1067,471),(1066,607)]
difficulty_coord = (993,143)
difficulty_select_coord = [(954,274),(968,434),(962,570)]
#关卡
level_name = ['加仑丛林','西泽山','卡菲勒遗址','拉古恩雪山',
               '特拉恩丛林','夏依德尼遗址','塔摩勒沙漠','保罗帕库斯遗址',
               '帕伊摩恩火山','艾登丛林','佩伦古城','里纳德山','泽罗卡遗址']
level_num = [1, 2, 3, 4, 5, 6, 7]
level_difficulty = ['普通', '困难', '地狱']

def level_select(level, num, difficulty):
    try:
        level_index = level_name.index(level)
        level_num_index = level_num.index(num)
        level_difficulty_index = level_difficulty.index(difficulty)
    except ValueError:
        print("level_select: Unknown level select combination: " + level + ',' + num + ',' + 'difficulty')
        return

    #重置选择界面状态
    device.swipe('副本选择','up')
    device.swipe('副本选择','up')
    device.swipe('副本选择','up')
    utils.wait('animation')

    page_curr = 0
    #计算目标关卡要滑动的次数，用page表示不同的选择页面状态
    page = math.ceil(level_index/3)-1
    while page_curr < page :
        device.swipe('副本选择', 'down')
        page_curr += 1
    #计算关卡在当前页面对应的坐标，从当前页面映射到页面坐标
    #其实就只有几种固定的状态
    start_index = 4 * page_curr - page_curr
    end_index = start_index + 4
    level_curr = level_name[start_index:end_index]
    x1, y1 = level_coord[level_curr.index(level)]
    device.click(x1, y1)

    #选择难度
    xt,yt = difficulty_coord
    device.click(xt, yt)
    x2, y2 = difficulty_select_coord[level_difficulty.index(difficulty)]
    device.click(x2,y2)

    #选择层数并战斗
    device.swipe('层数选择','up')
    device.swipe('层数选择','up')
    utils.wait('animation')
    if num <=3:
        x3, y3 = num_coord_1[num-1]
    elif num == 4:
        device.swipe('层数选择', 'down')
        x3, y3 = num_coord_2[0]
    else:
        device.swipe('层数选择', 'down')
        device.swipe('层数选择', 'down')
        x3, y3 = num_coord_3[num-5]
    device.click(x3, y3)

dungeon_coord = [(313,273),(310,377),(304,493),(354,606)]
dungeon_name = ['巨人','龙','死亡','精灵','钢铁','审判','秘密','魔力']
dungeon_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
def dungeon_select(dungeon, num):
    try:
        dungeon_index = dungeon_name.index(dungeon)
        dungeon_num_index = dungeon_num.index(num)
    except ValueError:
        print("level_select: Unknown dungeon select combination: " + dungeon + ',' + num)
        return
    
    #重置选择界面状态
    device.swipe('副本选择','up')
    device.swipe('副本选择','up')
    device.swipe('副本选择','up')
    utils.wait('animation')

    page_curr = 0
    #计算目标关卡要滑动的次数，用page表示不同的选择页面状态
    page = math.ceil(dungeon_index/3)-1
    while page_curr < page :
        device.swipe('副本选择', 'down')
        page_curr += 1
    #计算关卡在当前页面对应的坐标，从当前页面映射到页面坐标
    #其实就只有几种固定的状态
    start_index = 4 * page_curr - page_curr
    end_index = start_index + 4
    dungeon_curr = dungeon_name[start_index:end_index]
    x1, y1 = level_coord[dungeon_curr.index(dungeon)]
    device.click(x1, y1)

    #直接打12层
    device.swipe('层数选择', 'down')
    device.swipe('层数选择', 'down')
    utils.wait('animation')
    device.click(1066,607)