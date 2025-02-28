class UIHandler():

    def __init__(self, camera):
        # Score images

        SCALE_FACTOR = 0.11
        self.agent_1_score = pygame.image.load('assets/ui/player1ui.png')
        self.agent_1_score = pygame.transform.scale(self.agent_1_score, (int(SCALE_FACTOR * self.agent_1_score.get_width()), int(SCALE_FACTOR * self.agent_1_score.get_height())))
        self.agent_2_score = pygame.image.load('assets/ui/player2ui.png')
        self.agent_2_score = pygame.transform.scale(self.agent_2_score, (int(SCALE_FACTOR * self.agent_2_score.get_width()), int(SCALE_FACTOR * self.agent_2_score.get_height())))

        # Life and death images
        SCALE_FACTOR_2 = SCALE_FACTOR * 0.375
        self.life = pygame.image.load('assets/ui/alicon_alive.png')
        self.life = pygame.transform.scale(self.life, (int(SCALE_FACTOR_2 * self.life.get_width()), int(SCALE_FACTOR_2 * self.life.get_height())))
        self.death = pygame.image.load('assets/ui/alicon_dead.png')
        self.death = pygame.transform.scale(self.death, (int(SCALE_FACTOR_2 * self.death.get_width()), int(SCALE_FACTOR_2 * self.death.get_height())))

        self.score_width, self.score_height = self.agent_1_score.get_size()
        self.agent_1_score_pos = (10, -10)  # Top-left
        self.agent_2_score_pos = (camera.window_width - self.score_width - 10, -10)  # Top-right

    def render(self, camera, env):
        canvas = camera.canvas

        # Score UI positions


        # Draw Score UI

        canvas.blit(self.agent_1_score, self.agent_1_score_pos)
        canvas.blit(self.agent_2_score, self.agent_2_score_pos)

        # Agent lives
        spacing = self.score_width / 3
        for i in range(len(env.players)):
            for j in range(env.players[i].stocks):
                canvas.blit(self.life, (10+j*spacing + i*(camera.window_width - 1.2 * self.score_width), self.score_height - 30))

            # Agent deaths
            for j in range(3 - env.players[i].stocks):
                canvas.blit(self.death, (10 + 2*spacing - j*spacing + i*(camera.window_width - 1.2 * self.score_width), self.score_height - 30))

        self.display_percentages(camera, env)
        self.display_team_name(camera, env)

    def display_team_name(self, camera, env):
        # Define the team name and the bounding rectangle for the text.
        team_name = "Testing this team name"
        # These values can be adjusted to suit your UI layout:
        team_rect_1 = pygame.Rect(self.agent_1_score_pos[0] + 0.2 * self.score_width,
                                self.agent_1_score_pos[1] + 0.75 * self.score_height,
                                0.8 * self.score_width,
                                0.2 * self.score_height)
        team_rect_2 = pygame.Rect(self.agent_2_score_pos[0] + 0 * self.score_width,
                                self.agent_2_score_pos[1] + 0.75 * self.score_height,
                                0.8 * self.score_width,
                                0.2 * self.score_height)
        team_rects = [team_rect_1, team_rect_2]

        # Create a font (same as used for percentages or adjust as needed)
        font = pygame.font.Font(None, 20)

        for i, team_rect in enumerate(team_rects):
            # Render the team name and check if it fits in the rectangle.
            text = env.agent_1_name if i == 0 else env.agent_2_name
            text_surface = font.render(text, True, (255, 255, 255))

            # If the text is too wide, shorten it and add an ellipsis.
            if text_surface.get_width() > team_rect.width:
                # Remove characters until it fits, then add ellipsis.
                while text_surface.get_width() > team_rect.width and len(text) > 0:
                    text = text[:-1]
                    text_surface = font.render(text + "...", True, (255, 255, 255))
                text = text + "..."
                text_surface = font.render(text, True, (255, 255, 255))

            # Draw a red rectangle outline for the team name.
            pygame.draw.rect(camera.canvas, (255, 0, 0), team_rect, 2)

            # Center the text in the rectangle and draw it.
            text_rect = text_surface.get_rect(center=team_rect.center)
            camera.canvas.blit(text_surface, text_rect)

    # Percentages (like SSBU)
    def display_percentages(self, camera, env):
        WHITE = (255, 255, 255)
        ORANGE = (255, 165, 0)
        RED = (255, 0, 0)
        YELLOW = (255, 255, 0)
        DARK_RED = (139, 0, 0)

        # Agent percentage text
        font = pygame.font.Font(None, 35)
        # render text & text colours:
        for i in range(len(env.players)):
            COLOUR = WHITE
            if 50 < env.players[i].damage < 100:
                COLOUR = YELLOW
            elif 100 <= env.players[i].damage < 150:
                COLOUR = ORANGE
            elif 150 <= env.players[i].damage < 200:
                COLOUR = RED
            elif env.players[i].damage >= 200:
                COLOUR = DARK_RED
            percentage = env.players[i].damage * 5 / 7
            text_surface = font.render(f'{percentage:.1f}%', True, COLOUR)
            # text_rect_background = pygame.draw.rect(self.screen, (255,255,255), (220+i*100, 75, 70, 56))
            # text_rect_background_border = pygame.draw.rect(self.screen, (0, 0, 0), (220+i*100, 75, 70, 56), 3)
            text_rect = text_surface.get_rect(center=(self.score_width + i*(camera.window_width - 2 * self.score_width), self.score_height * 1.5/4))
            camera.canvas.blit(text_surface, text_rect)