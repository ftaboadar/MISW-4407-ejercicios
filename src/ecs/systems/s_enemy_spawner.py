import esper
import pygame
import random

from src.ecs.components.c_enemy_spawner import CEnemySpawner
from src.ecs.components.c_velocidad import Cvelocity
from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_transform import CTransfom

def system_enemy_spawner(world:esper.World, delta_time:float):
    component = world.get_component(CEnemySpawner)
    c_e:CEnemySpawner

    for entity, c_e in component :
        c_e.time += delta_time
        for event in c_e.events:
            if (event["time"] <= c_e.time) and (event["triggered"] == False):
                magnitud = random.uniform(event["velocity_min"], event["velocity_max"])  
                angulo = random.uniform(0, 360)                                       
                vel = Cvelocity(pygame.Vector2(magnitud, 0).rotate(angulo))
                pos_cuad = CTransfom(pygame.Vector2(event["position"]["x"],event["position"]["y"]))
                surf_cuad = CSurface(pygame.Vector2(event["size"]["x"], event["size"]["y"]), pygame.Color(event["color"]["r"], event["color"]["g"], event["color"]["b"]))   
                event["triggered"] = True 
                world.create_entity(vel,pos_cuad,surf_cuad)                    
  
