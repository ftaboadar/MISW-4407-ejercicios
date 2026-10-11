import pygame
import esper
import json

from src.ecs.systems.s_movement import system_movement
from src.ecs.systems.s_rendering import system_rendering
from src.ecs.systems.s_screen_bounce import system_screen_bounce
from src.ecs.systems.s_enemy_spawner import system_enemy_spawner

from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_transform import CTransfom
from src.ecs.components.c_velocidad import Cvelocity
from src.ecs.components.c_enemy_spawner import CEnemySpawner

class GameEngine:
    def __init__(self) -> None:
        with open("assets/cfg/window.json") as f:
            self.cfg_window = json.load(f)
            if "window" in self.cfg_window:
                self.cfg_window = self.cfg_window["window"]

        with open("assets/cfg/enemies.json") as f:
            self.cfg_enemies = json.load(f)

        with open("assets/cfg/level_01.json") as f:
            self.cfg_levels = json.load(f)


        self.is_running = False
        self.w_color = (self.cfg_window["bg_color"]["r"],self.cfg_window["bg_color"]["g"], self.cfg_window["bg_color"]["b"])
        self.w_titulo = self.cfg_window["title"]
        self.w_size = (self.cfg_window["size"]["w"],self.cfg_window["size"]["h"])
        self.screen = pygame.display.set_mode(self.w_size, pygame.SCALED)
        pygame.display.set_caption(self.w_titulo)
        self.clock = pygame.time.Clock()
        self.is_running = False
        self.framerate = self.cfg_window["framerate"]
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
        self.enemies = CEnemySpawner(self.cfg_enemies,self.cfg_levels)
        self.world.create_entity(self.enemies)



    def _calculate_time(self):
        self.clock.tick(self.framerate)
        self.delta_time = self.clock.get_time() / 1000.0

    def _process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

    def _update(self):
        system_enemy_spawner(self.world, self.delta_time)
        system_movement(world=self.world, delta_time=self.delta_time)
        screen_rect = self.screen.get_rect()
        system_screen_bounce(world=self.world, screen_rect=screen_rect)
        

    def _draw(self):
        self.screen.fill(self.w_color)
        system_rendering(world=self.world, screen=self.screen)
        pygame.display.flip()

    def _clean(self):
        pygame.quit()
