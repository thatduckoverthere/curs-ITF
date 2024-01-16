import pyautogui, time


time.sleep(5)

f = open("./bee_movie_transcript.txt", 'r')

for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")