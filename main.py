import mido
import pygame
import time
import asyncio
from game_interface import GameInterface
from timing_mechanism import TimingMechanism
from error_handling import handle_exception
from multiplayer_client import send_message

# Initialize Pygame
pygame.init()

# MIDI Input Setup
inport = mido.open_input('Arturia MiniLab mkII')  # Adjust this to match your MIDI device

# Game Variables
running = True
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))  # Adjust this to change the size of the game window
game_interface = GameInterface(screen)
timing_mechanism = TimingMechanism(120)  # Adjust this to match the tempo of the song

# Main Game Loop
while running:
    for msg in inport.iter_pending():
        # Handle MIDI input
        if msg.type == 'note_on':
            game_interface.add_note(msg.note % 88, timing_mechanism.get_elapsed_beats())
            # Send note to other players
            asyncio.get_event_loop().run_until_complete(send_message(f'note_on {msg.note}'))

    # Update game interface
    game_interface.update(clock.get_time() / 1000)

    # Draw game interface
    game_interface.draw()

    # Update display
    pygame.display.flip()

    # Limit the loop to 60 frames per second
    clock.tick(60)

# Close MIDI port and quit Pygame
inport.close()
pygame.quit()