import level
import device
import utils
import battle


device.init_device()
utils.init_ocr()
level.dungeon_select('龙', 12)
battle.battle_start('level_10')
n=1
count = 30
while count<n:
    battle.start_over()
    n += 1