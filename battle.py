import device
import utils
import state
import item_mgr

start_button_coord = (1106,541)
quit_button_coord = (1106,657)
thirty_coord = (1013,460)

shouldExitBattle = False

battle_state = {
    'ongoing_times': 0,
    'total_times' : 0,
    'end': False,
    'success': False,
    'current_energy': state.current_energy,
    'result' : ''
}
battle_state_coord = {
    'text_times': [(219,156),(293,191)],
    'text_success': [(301,496),(553,542)],
    'text_energy': [(606,155),(750,182)],
}

def update_state():
    global battle_state

    utils.wait('loading')
    device.screenshot()

    x1, y1= battle_state_coord['text_times'][0]
    x2, y2= battle_state_coord['text_times'][1]
    text = utils.get_ocr_text(x1, y1, x2, y2)
    ongoing_times, total_times = map(int, text.split('/'))
    x1, y1= battle_state_coord['text_energy'][0]
    x2, y2= battle_state_coord['text_energy'][1]
    text = utils.get_ocr_text(x1, y1, x2, y2)
    #去掉数字里的逗号,点号和识别出的能量上限
    tmp = str(state.current_energy_limit)
    tmp_len = len(tmp)
    tmp_text = text[:-tmp_len]
    current_energy = int(tmp_text.replace(',', '').replace('.', '').replace('/', ''))
    if current_energy - battle_state['current_energy'] > 10 and battle_state['current_energy'] != 0:
        current_energy = current_energy // 10
    x1, y1= battle_state_coord['text_success'][0]
    x2, y2= battle_state_coord['text_success'][1]
    result = utils.get_ocr_text(x1, y1, x2, y2)

    if '完成' in result:
        end = True
        success = True
    elif '已满级' in result:
        end = True
        success = True
    elif '战斗失败' in result:
        end = True
        success = False
    elif '已结束' in result:
        end = True
        success = False
    else:
        end = False
        success = False
    battle_state = {
        'ongoing_times': ongoing_times,
        'total_times': total_times,
        'end': end,
        'success': success,
        'current_energy': current_energy,
        'result' : result
    }


def battle_start(battle_type):
    battle_state['end'] = False
    xt, yt = thirty_coord
    x, y = start_button_coord
    utils.wait('animation')
    if battle_type == 'level_10':
        device.click(x, y)
    elif battle_type == 'level_30':
        device.click(xt, yt, bias=1)
        device.click(x, y)
    else:
        print("Unknown battle type: " + battle_type)
        return
    
    utils.wait('loading')

    while(not shouldExitBattle):
        update_state()
        print('战斗进行中: ' + str(battle_state['ongoing_times'])+'/'+str(battle_state['total_times']))
        print('当前剩余能量： ' + str(battle_state['current_energy']))
        utils.wait('battle')
        if battle_state['end']:
            battle_end()

def battle_end():
        global shouldExitBattle

        print(battle_state['result'])
        print('确认战利品中...')
        item_mgr.check('battle_end')
        print('确认完成。')
        shouldExitBattle = True

def battle_time_estimate():
    estimate_time = 0
    return estimate_time

def start_over():
    device.click(651,626)
    battle_start('level_10')