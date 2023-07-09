import random
import sys
import time
import os
import msvcrt
import threading
import winsound

def generate_green_text():
    green_text = "\033[1;32;40m"  # Ustawienie koloru tekstu na zielony
    clear_screen = "\033[2J"  # Sekwencja ucieczki ANSI do wyczyszczenia ekranu
    while True:
        sys.stdout.write(clear_screen)  # Wyczyść ekran
        for _ in range(os.get_terminal_size().lines - 1):  # Pętla dla liczby linii w terminalu
            line = green_text + "".join(chr(random.randint(32, 126)) for _ in range(os.get_terminal_size().columns))  # Wygeneruj linie z losowymi znakami
            sys.stdout.write(line + "\n")  # Wyświetl linie
        sys.stdout.flush()
        time.sleep(0.1)

def play_sound():
    while True:
        winsound.Beep(500, 500)  # Odtwarzaj dźwięk beep
        time.sleep(1)
        winsound.Beep(1000, 500)  # Odtwarzaj dźwięk boop
        time.sleep(1)

if __name__ == '__main__':
    # Uruchomienie generowania zielonych znaków w oddzielnym wątku
    green_text_thread = threading.Thread(target=generate_green_text)
    green_text_thread.daemon = True
    green_text_thread.start()

    # Uruchomienie odtwarzania dźwięków w oddzielnym wątku
    sound_thread = threading.Thread(target=play_sound)
    sound_thread.daemon = True
    sound_thread.start()

    # Oczekiwanie na naciśnięcie klawisza zakończenia programu (np. Esc)
    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key == b'\x1b':  # Esc
                sys.exit(0)
