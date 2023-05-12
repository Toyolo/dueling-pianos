import pygame

class Note:
    def __init__(self, track, start_time, color=(255, 255, 255)):
        self.track = track
        self.start_time = start_time
        self.color = color
        self.rect = pygame.Rect(track * 20, -20, 20, 20)

    def update(self, delta_time):
        # Move the note down the track
        self.rect.y += delta_time * 100  # Adjust this value to change the speed of the notes

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

class GameInterface:
    def __init__(self, screen):
        self.screen = screen
        self.notes = []

    def add_note(self, track, start_time):
        self.notes.append(Note(track, start_time))

    def update(self, delta_time):
        for note in self.notes:
            note.update(delta_time)

    def draw(self):
        self.screen.fill((0, 0, 0))  # Clear the screen
        for note in self.notes:
            note.draw(self.screen)
