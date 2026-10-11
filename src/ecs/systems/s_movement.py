
import esper
import pygame

from src.ecs.components.c_velocidad import Cvelocity
from src.ecs.components.c_transform import CTransfom

def system_movement(world:esper.World, delta_time:float):
    components = world.get_components(CTransfom, Cvelocity)

    c_t:CTransfom
    c_v:Cvelocity

    for entity, (c_t, c_v) in components:
     
     c_t.pos.x += c_v.vel.x * delta_time
     c_t.pos.y += c_v.vel.y * delta_time