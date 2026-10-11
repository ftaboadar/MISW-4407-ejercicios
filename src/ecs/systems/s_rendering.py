
import esper
import pygame

from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_transform import CTransfom

def system_rendering(world:esper.World, screen:pygame.surface):
    components = world.get_components(CTransfom, CSurface)

    c_t:CTransfom
    c_s:CSurface

    for entity, (c_t, c_s) in components:
        screen.blit(c_s.surf, c_t.pos)