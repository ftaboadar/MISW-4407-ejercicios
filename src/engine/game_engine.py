import pygame

import esper

from src.ecs.systems.s_movement import system_movement
from src.ecs.systems.s_rendering import system_rendering
from src.ecs.systems.s_screen_bounce import system_screen_bounce

from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_transform import CTransfom
from src.ecs.components.c_velocidad import Cvelocity

class GameEngine:
    def __init__(self) -> None:
        self.is_running = False
        self.screen = pygame.display.set_mode((640, 360), pygame.SCALED)
        self.clock = pygame.time.Clock()
        self.is_running = False
        self.framerate = 60
        self.delta_time = 0
        self.world = esper.World()


    def run(self) -> None:
        self._create()
        self.is_running = True
        while self.is_running:
            self._calculate_time()
            self._process_events()
            self._update()
            self._draw()
        self._clean()

    def _create(self):
        self.vel_cuad = Cvelocity(pygame.Vector2(100,200))  
        self.pos_cuad = CTransfom(pygame.Vector2(-25,100))

        self.surf_cuad = CSurface(pygame.Vector2(50, 50), pygame.Color(255, 255, 100))

        self.world.create_entity(self.vel_cuad, self.pos_cuad, self.surf_cuad)


    def _calculate_time(self):
        self.clock.tick(self.framerate)
        self.delta_time = self.clock.get_time() / 1000.0

    def _process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

    def _update(self):
        system_movement(world=self.world, delta_time=self.delta_time)
        screen_rect = self.screen.get_rect()
        system_screen_bounce(world=self.world, screen_rect=screen_rect)

    def _draw(self):
        self.screen.fill((0,200, 128))
        system_rendering(world=self.world, screen=self.screen)
        pygame.display.flip()

    def _clean(self):
        pygame.quit()
