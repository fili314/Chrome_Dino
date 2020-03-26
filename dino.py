import time
from PIL import ImageGrab  # modulo para tirar print da tela
import pyautogui

# bg_color = (247, 247, 247)
# dino_color = (83, 83, 83)
j = 280
color_bg = 0


def capture_screen():
    screen = ImageGrab.grab()  # salva o print na varável screen
    return screen


def detect_enemyup(screen):
    global j
    global color_bg
    color_bg = screen.getpixel((200, 200))
    for x in range(280, 200 + int(j)):
        for y in range(645, 670):  # 612
            color = screen.getpixel((x, y))  # salva a cor do pixel
            if color != color_bg:
                return True
            else:
                color_bg = color


def detect_enemydown(screen):
    color_bg = screen.getpixel((200, 200))
    for x in range(int(j), 200 + int(j)):
        for y in range(545, 552):
            color = screen.getpixel((x, y))  # salva a cor do pixel
        if color != color_bg:
            return True
        else:
            color_bg = color


def jump():
    global j
    pyautogui.keyDown("up")
    time.sleep(0.2)
    pyautogui.keyDown("down")
    pyautogui.keyUp("down")
    j += 1.2


def down():
    pyautogui.keyDown("down")
    time.sleep(0.3)
    pyautogui.keyUp("down")


print("Start in 3 seconds...")
time.sleep(3)

while True:
    screen = capture_screen()  # chama a funcão
    if detect_enemyup(screen):
        jump()
    if detect_enemydown(screen):
        down()
