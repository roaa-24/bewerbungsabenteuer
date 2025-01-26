import pygame
import sys

# Initialisierung 
pygame.init()

# Grössen  und Farben
WIDTH, HEIGHT = 900, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (70, 130, 180)
GREEN = (34, 139, 34)
RED = (220, 20, 60)
BACKGROUND_COLOR = (250, 200, 200)  


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bewerbungsabenteuer")


pygame.font.init()
font_large = pygame.font.SysFont("Arial", 40)  
font_medium = pygame.font.SysFont("Arial", 32)  
font_small = pygame.font.SysFont("Arial", 20)  

# Player
player_img = pygame.image.load(player.png")
player_img = pygame.transform.scale(player_img, (50, 50)) 
player = player_img.get_rect(topleft=(155, 145)) 

# bewegung
player_speed = 4
velocity_x, velocity_y = 0, 0

# Quests
quests = [
    {"name": "1. Recherche starten", "rect": pygame.Rect(250, 150, 200, 50), "completed": False, "message": "Besuche LinkedIn oder Xing, um dein Netzwerk zu erweitern."},
    {"name": "2. Firma analysieren", "rect": pygame.Rect(300, 250, 200, 50), "completed": False, "message": "Analysiere die Firma auf Glassdoor oder Indeed."},
    {"name": "3. Lebenslauf erstellen", "rect": pygame.Rect(350, 350, 200, 50), "completed": False, "message": "Erstelle einen klar strukturierten Lebenslauf mit passenden Keywords."},
    {"name": "4. Anschreiben verfassen", "rect": pygame.Rect(400, 450, 200, 50), "completed": False, "message": "Schreibe ein überzeugendes Anschreiben, das die Anforderungen hervorhebt."},
]


background_text = "Den Einstieg in den Arbeitsmarkt wagen"


current_message = ""  
message_display_time = 0  


final_message = ""
final_message_display_time = 0


sound_effect = pygame.mixer.Sound(r"C:\Users\Roaa\Desktop\MeineWebseite\Spiel\success.wav")  #  Soundeffekt

# Spiel-Loop
clock = pygame.time.Clock()

while True:
    screen.fill(BACKGROUND_COLOR)  

    
    text_surface = font_large.render(background_text, True, BLACK)
    text_rect = text_surface.get_rect(center=(WIDTH // 2, 50))
    screen.blit(text_surface, text_rect)

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                velocity_x = -player_speed
            if event.key == pygame.K_RIGHT:
                velocity_x = player_speed
            if event.key == pygame.K_UP:
                velocity_y = -player_speed
            if event.key == pygame.K_DOWN:
                velocity_y = player_speed
        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                velocity_x = 0
            if event.key in (pygame.K_UP, pygame.K_DOWN):
                velocity_y = 0

    # Spielerbewegung
    player.x += velocity_x
    player.y += velocity_y

    # Spielfigur innerhalb des Fensters halten
    player.x = max(0, min(WIDTH - player.width, player.x))
    player.y = max(0, min(HEIGHT - player.height, player.y))


    for i, quest in enumerate(quests):
        if player.colliderect(quest["rect"]) and not quest["completed"]:
          
            if i == 0 or quests[i - 1]["completed"]:
                quest["completed"] = True
                message_display_time = 1800  

               
                sound_effect.play()


    for quest in quests:
        color = GREEN if not quest["completed"] else RED
        pygame.draw.rect(screen, color, quest["rect"])
        quest_text = font_small.render(quest["name"], True, BLACK)
        screen.blit(quest_text, (quest["rect"].x + 10, quest["rect"].y + 10))

    # Spielfigur zeichnen
    screen.blit(player_img, player)

    # Fortschrittsanzeige
    completed_count = sum(1 for q in quests if q["completed"])
    progress_text = font_medium.render(f"Fortschritt: {completed_count}/{len(quests)} abgeschlossen", True, BLACK)
    screen.blit(progress_text, (10, 100))

    # Nachricht anzeigen
    if completed_count < len(quests) and message_display_time > 0:
        message_surface = font_medium.render(current_message, True, BLACK)
        message_rect = message_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(message_surface, message_rect)
        message_display_time -= 1

   
    if completed_count == len(quests) and final_message_display_time == 0:
        final_message = "Geschafft! Viel Glück bei deinem Einstieg in den Arbeitsmarkt!"
        final_message_display_time = 300  # Nachricht für 5 Sekunden anzeigen

    if final_message_display_time > 0:
        final_message_surface = font_large.render(final_message, True, BLACK)
        final_message_rect = final_message_surface.get_rect(center=(WIDTH // 2, HEIGHT - 30))
        screen.blit(final_message_surface, final_message_rect)
        final_message_display_time -= 1

  
    pygame.display.flip()
    clock.tick(60)
