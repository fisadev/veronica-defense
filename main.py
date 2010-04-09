#!/usr/bin/env python

import pyglet.resource
from cocos.director import director

import settings
from levels import levels
from level_scene import LevelScene

def main():
    pyglet.resource.path.append("images")
    pyglet.resource.reindex()
    
    director.init(vsync=True)
    
    settings.WINDOW_SIZE = director.get_window_size()
    settings.GRID_SIZE = (settings.WINDOW_SIZE[0] / settings.GRID_CELL,
                          settings.WINDOW_SIZE[1] / settings.GRID_CELL)

    level_0 = levels[0]
    scene = LevelScene(level_0)
    director.run(scene)
    

if __name__ == '__main__':
    main()
