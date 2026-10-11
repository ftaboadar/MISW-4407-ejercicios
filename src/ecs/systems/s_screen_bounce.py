

import pygame
import esper

from src.ecs.components.c_velocidad import Cvelocity
from src.ecs.components.c_transform import CTransfom
from src.ecs.components.c_surface import CSurface

def system_screen_bounce(world:esper.World,screen_rect:pygame.Rect):
    components = world.get_components(CTransfom, Cvelocity, CSurface)

    c_t:CTransfom
    c_v:Cvelocity
    c_s:CSurface


    for entity, (c_t, c_v, c_s) in components:

        cuad_react = c_s.surf.get_rect(topleft = c_t.pos)

        if cuad_react.left <= 0 or cuad_react.right >= screen_rect.width:
            c_v.vel.x *= -1
            if cuad_react.left <= 0:
                c_t.pos.x = 0
            else:
                c_t.pos.x = screen_rect.width - cuad_react.width

        if cuad_react.top <= 0 or cuad_react.bottom >= screen_rect.height:
            c_v.vel.y *= -1
            if cuad_react.top <= 0:
                c_t.pos.y = 0
            else:
                c_t.pos.y = screen_rect.height - cuad_react.height
