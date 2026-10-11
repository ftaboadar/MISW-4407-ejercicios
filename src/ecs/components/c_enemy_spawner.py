
class CEnemySpawner:

    def __init__(self, enemies_cfg, level_cfg):
        self.events = []
        
        self.time = 0

        for event in level_cfg["enemy_spawn_events"]:
            tipo_enemigo = enemies_cfg[event["enemy_type"]]
            self.events.append({**tipo_enemigo, **event, "triggered": False})

