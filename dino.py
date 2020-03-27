# resolução da tela pode interferir a ação do programa
from selenium import webdriver  # modulo para abrir página web
from PIL import ImageGrab  # modulo para tirar print da tela
import pyautogui  # modulo para controlar ações do dino
import time

driver = webdriver.Chrome()  # abre a página do jogo no Chrome
driver.get('chrome://dino/')
driver.maximize_window()

speed = 280
color_bg = 0


def capture_screen():  # Captura a tela
    screen = ImageGrab.grab()
    return screen


def capture_color():  # Busca a cor de fundo do jogo
    color_bg = screen.getpixel((200, 200))
    return color_bg


def detect_enemyup(screen, color_bg):  # logica que determina se dino pula
    for x in range(280, 200 + int(speed)):
        for y in range(690, 700):
            color = screen.getpixel((x, y))
            if color != color_bg:
                return True
            else:
                color_bg = color


def detect_enemydown(screen, color_bg):  # logica que determina se dino se agacha
    for x in range(int(speed), 200 + int(speed)):
        for y in range(585, 595):
            color = screen.getpixel((x, y))  # salva a cor do pixel
            if color != color_bg:
                return True
            else:
                color_bg = color


def jump():  # pula
    pyautogui.keyDown("up")
    time.sleep(0.2)
    pyautogui.keyDown("down")
    pyautogui.keyUp("down")
    d_speed()


def down():  # agacha
    pyautogui.keyDown("down")
    time.sleep(0.2)
    pyautogui.keyUp("down")
    d_speed()


def d_speed():  # aumenta area de leitura de acordo com a velocidade
    global speed
    speed += 1


while driver.current_window_handle:  # corpo principal
    screen = capture_screen()
    color_bg = capture_color()
    if detect_enemyup(screen, color_bg):
        jump()
    if detect_enemydown(screen, color_bg):
        down()
    print(speed)
    if screen.getpixel((672, 446)) != color_bg or speed == 280:
       pyautogui.keyDown("space")
       time.sleep(0.2)
       pyautogui.keyUp("space")
       speed = 280
       d_speed()
