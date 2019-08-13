import threading
from server.battle.battle_manager import BattleManager


def send_battle_finish_command(battle_id):
    for thread in threading.enumerate():
        if (type(thread) == BattleManager) and (thread.battle_id == battle_id):
            thread.finish()
