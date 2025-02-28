import pygame
import numpy as np

class KeyIconPanel():
    def __init__(self, side: str, edge_percentage: float,
                 width_percentage: float, height_percentage: float,
                 font_size: int = 12):
        """
        :param side: "left" or "right". Determines which edge (far left or far right) is positioned at the given percentage.
        :param edge_percentage: Fraction of the screen width at which the far edge of the panel is placed.
                                For "left", this is the left edge; for "right", this is the right edge.
        :param width_percentage: Panel width as a fraction of screen width.
        :param height_percentage: Panel height as a fraction of screen height.
        :param font_size: Font size for the key labels.
        """
        self.side = side.lower()
        self.edge_percentage = edge_percentage
        self.width_percentage = width_percentage
        self.height_percentage = height_percentage
        self.font_size = font_size
        # Define the keys in order: first 4 (W, A, S, D), then space, then 5 (G, H, J, K, L)
        self.keys = ["W", "A", "S", "D", "Space", "G", "H", "J", "K", "L"]

    def draw_key_icon(self, surface, rect: pygame.Rect, key_label: str, pressed: bool, font):
        """
        Draws a key icon in the specified rect.
          - Draws a rectangle with a 2-pixel border.
          - If pressed, the border and text are red; if not, they are white.
        """
        color = (255, 0, 0) if pressed else (255, 255, 255)
        # Draw the rectangle outline
        pygame.draw.rect(surface, color, rect, 1)
        # Render the key label (centered)
        text_surface = font.render(key_label, True, color)
        text_rect = text_surface.get_rect(center=rect.center)
        surface.blit(text_surface, text_rect)

    def draw(self, camera, input_vector: np.ndarray):
        """
        Draws the panel and key icons onto the given canvas.

        :param canvas: The pygame.Surface on which to draw.
        :param screen_size: Tuple (screen_width, screen_height).
        :param input_vector: np.ndarray of booleans or 0/1 with length 10 in the order [W, A, S, D, Space, G, H, J, K, L].
        """
        canvas = camera.canvas
        screen_width, screen_height = camera.window_width, camera.window_height

        # Calculate panel dimensions
        panel_width = screen_width * self.width_percentage
        panel_height = screen_height * self.height_percentage

        # Determine panel x based on side
        if self.side == "left":
            x = screen_width * self.edge_percentage
        elif self.side == "right":
            x = screen_width * self.edge_percentage - panel_width
        else:
            # Default to centered horizontally if side is invalid.
            x = (screen_width - panel_width) / 2

        # For vertical placement, we'll position the panel at 10% from the top.
        y = screen_height * 0.2
        panel_rect = pygame.Rect(int(x), int(y), int(panel_width), int(panel_height))
        # Draw panel background and border
        pygame.draw.rect(canvas, (50, 50, 50), panel_rect)  # dark gray background
        pygame.draw.rect(canvas, (255, 255, 255), panel_rect, 2)  # white border

        # Create a font for the key icons.
        font = pygame.font.Font(None, self.font_size)
        # Divide the panel vertically into 3 rows.
        row_height = panel_rect.height / 3

        # Row 1: WASD (first 4 keys)
        row1_keys = self.keys[0:4]
        row1_count = len(row1_keys)
        for idx, key in enumerate(row1_keys):
            cell_width = panel_rect.width / row1_count
            cell_rect = pygame.Rect(
                panel_rect.x + idx * cell_width,
                panel_rect.y,
                cell_width,
                row_height
            )
            # Add padding for the icon.
            icon_rect = cell_rect.inflate(-2, -2)
            pressed = input_vector[idx] > 0.5
            self.draw_key_icon(canvas, icon_rect, key, pressed, font)

        # Row 2: Spacebar (only one icon)
        cell_rect = pygame.Rect(
            panel_rect.x,
            panel_rect.y + row_height,
            panel_rect.width,
            row_height
        )
        # Center the spacebar icon in its cell.
        icon_rect = cell_rect.inflate(-2, -2)
        pressed = input_vector[4] > 0.5
        self.draw_key_icon(canvas, icon_rect, "Space", pressed, font)

        # Row 3: GHJKL (last 5 keys)
        row3_keys = self.keys[5:10]
        row3_count = len(row3_keys)
        for idx, key in enumerate(row3_keys):
            cell_width = panel_rect.width / row3_count
            cell_rect = pygame.Rect(
                panel_rect.x + idx * cell_width,
                panel_rect.y + 2 * row_height,
                cell_width,
                row_height
            )
            icon_rect = cell_rect.inflate(-2, -2)
            pressed = input_vector[5 + idx] > 0.5
            self.draw_key_icon(canvas, icon_rect, key, pressed, font)
