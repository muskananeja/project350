import pygame
import time

pygame.font.init()


class Clock:
    def __init__(self):
        """
        Initialize the Clock object with default values.
        """
        self.start_time = None
        self.elapsed_time = 0
        self.font = pygame.font.SysFont("monospace", 35)
        self.message_color = pygame.Color("yellow")

    def start_timer(self):
        """
        Start the timer by recording the current time.
        """
        self.start_time = time.time()

    def update_timer(self):
        """
        Update the elapsed time if the timer is running.
        """
        if self.start_time is not None:
            self.elapsed_time = time.time() - self.start_time

    def display_timer(self):
        """
        Render the elapsed time as a formatted string.

        :return: Pygame surface with the formatted time.
        """
        secs = int(self.elapsed_time % 60)
        mins = int(self.elapsed_time / 60)
        my_time = self.font.render(
            f"{mins:02}:{secs:02}", True, self.message_color)
        return my_time

    def stop_timer(self):
        """
        Stop the timer by resetting the start time.
        """
        self.start_time = None
