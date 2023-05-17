import pygame
import random
#Declare variables
CHOICES = ['rock', 'paper', 'scissors']

# Initialize PygameR
pygame.init()

# Set the screen size
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Rock, Paper, Scissors")

#Define the padding
button_padding = 10

# Set the font for the text
font = pygame.font.Font(None, 36)

# Load the images
image1 = pygame.image.load("rock.png")
image2 = pygame.image.load("paper.png")
image3 = pygame.image.load("scissors.png")

# Resize the images to fit the screen width
image_width = (screen_width  - (4 * button_padding)) // 3
image_height = (screen_height  - (2 * button_padding)) // 2
image1 = pygame.transform.scale(image1, (image_width - 2*button_padding, image_height - 2*button_padding))
image2 = pygame.transform.scale(image2, (image_width - 2*button_padding, image_height - 2*button_padding))
image3 = pygame.transform.scale(image3, (image_width - 2*button_padding, image_height - 2*button_padding))

# Set the text for each button
button1_text = "Button 1"
button2_text = "Button 2"
button3_text = "Button 3"

# Set the default text
current_text = "Choose:"

# Set the button rects
button1_rect = pygame.Rect(button_padding, screen_height // 2, image_width, image_height)
button2_rect = pygame.Rect(image_width + button_padding * 2, screen_height // 2, image_width, image_height)
button3_rect = pygame.Rect(image_width * 2 + button_padding * 3, screen_height // 2, image_width, image_height)

# Set the button colors
button_color = (0, 0, 0)
highlight_color = (200, 200, 200)

# Winner function
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "equal"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "user won"
    else:
        return "user lost"
    
# Computer's choice
def get_computer_choice():
    return random.choice(CHOICES)

def render_multi_line(text):
    lines = text.splitlines()
    for  i, l  in enumerate(lines):
        text_render = font.render(l, True, (0, 0, 0))
        text_rect = text_render.get_rect(center=(screen_width // 2, screen_height // 8 + 26*i))
        screen.blit(text_render, text_rect)

# Track the time
start_time = 0
elapsed_time = 0
loading_time = 500

# Run the game loop
running = True
clickedButton = None

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if a button was clicked
            if button1_rect.collidepoint(event.pos):
                clickedButton = 1
            elif button2_rect.collidepoint(event.pos):
                clickedButton = 2
            elif button3_rect.collidepoint(event.pos):
                clickedButton = 3
            if clickedButton != None:
                current_text = "Loading..."
                start_time = pygame.time.get_ticks()
            
    # Calculate elapsed time
    current_time = pygame.time.get_ticks()
    elapsed_time = current_time - start_time
    if current_text == "Loading..." and elapsed_time >= loading_time:
        computer_choice = get_computer_choice()
        if clickedButton == 1:
            user_choice = "rock"
        elif clickedButton == 2:
            user_choice = "paper"
        elif clickedButton == 3:
            user_choice = "scissors"
        result = determine_winner(user_choice, computer_choice)
        if result == "equal":
            current_text = "Equal!\nSelect again:"
        elif result == "user won":
            current_text = f"Computer chose {computer_choice}\nYou're the master!\nSelect again:"
        elif result == "user lost":
            current_text = f"Computer chose {computer_choice}\nYou're a loser!\nSelect again:"
        clickedButton = None
            
            

    # Clear the screen
    screen.fill((255, 255, 255))


    render_multi_line(current_text)

    # Display the buttons
    if button1_rect.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(screen, highlight_color, button1_rect)
    else:
        pygame.draw.rect(screen, button_color, button1_rect)
    screen.blit(image1, (button1_rect.x + button_padding, button1_rect.y + button_padding))

    if button2_rect.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(screen, highlight_color, button2_rect)
    else:
        pygame.draw.rect(screen, button_color, button2_rect)
    screen.blit(image2, (button2_rect.x + button_padding, button2_rect.y + button_padding))

    if button3_rect.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(screen, highlight_color, button3_rect)
    else:
        pygame.draw.rect(screen, button_color, button3_rect)
    screen.blit(image3, (button3_rect.x + button_padding, button3_rect.y + button_padding))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()