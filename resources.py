import pygame
import os
import re

RESOURCES = {}

def get_slice_params(filename):
    match = re.search(r'_(\d+)x(\d+)_(\d+)x(\d+)', filename)
    if match:
        num_x = int(match.group(1))
        num_y = int(match.group(2))
        width = int(match.group(3))
        height = int(match.group(4))

        return num_x, num_y, width, height
    
    return None

def load_and_slice_spritesheet(image_path, num_x, num_y, frame_width, frame_height):
    try:
        spritesheet = pygame.image.load(image_path).convert_alpha()
    except pygame.error as e:
        print(f"Can't load spritesheet {image_path}: {e}")
        return
    
    frames = []

    for row in range(num_y):
        for col in range(num_x):
            x = col * frame_width
            y = row * frame_height
            frame_rect = pygame.Rect(x, y, frame_width, frame_height)

            frame_surface = pygame.Surface((frame_width, frame_height), pygame.SRCALPHA)
            frame_surface.blit(spritesheet, (0, 0), frame_rect)

            frames.append(frame_surface)
        
    return frames

def load_all_images_and_spritesheets(image_dir='img'):
    for filename in os.listdir(image_dir):
        full_image_path = os.path.join(image_dir, filename)

        if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp')):
            resource_name = os.path.splitext(filename)[0]
            params = get_slice_params(resource_name)
            if params:
                num_x, num_y, width, height = params
                base_name = re.sub(r'_\d+x\d+_\d+x\d+', '', resource_name)
                print(f"Animation founded: {base_name}. Parameters: {num_x}x{num_y}, {width}x{height}")
                frames = load_and_slice_spritesheet(full_image_path, num_x, num_y, width, height)
                if frames:
                    RESOURCES[base_name] = frames
            else:
                print(f"One image loaded: {resource_name}")
                try:
                    loaded_image = pygame.image.load(full_image_path).convert_alpha()
                    RESOURCES[resource_name] = loaded_image
                except pygame.error as e:
                    print(f"Loading error {full_image_path}: {e}")
            
def initialize_resouces():
    if not pygame.get_init():
        pygame.init()
        pygame.mixer.init()
    load_all_images_and_spritesheets(image_dir='img')

class Animation:
    def __init__(self, frames, speed):
        self.frames = frames
        self.speed = speed
        self.num_frames = len(frames)
        self.current_frame_index = 0
        self.timer = 0
    
    def update(self):
        self.timer += 1
        if self.timer >= self.speed:
            self.timer = 0
            self.current_frame_index += 1
            if self.current_frame_index >= self.num_frames:
                self.current_frame_index = 0
    
    def get_current_frame(self):
        return self.frames[self.current_frame_index]

