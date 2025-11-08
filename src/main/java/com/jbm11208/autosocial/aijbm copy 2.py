import time
import ollama
import pyautogui
import pynput.keyboard as keys
from pynput.mouse import Button, Controller as MouseController
from random import randint
import threading
import queue
from profanity_check import predict, predict_prob
from pygame import mixer
import pyglet
import random
from mutagen.mp3 import MP3
import yt_dlp
import os
import threading
keyboard = keys.Controller()
mouse = MouseController()
shared_queue = queue.Queue()
logfile = open(r"C:\Users\mcken\Downloads\mmc-develop-win32\MultiMC\instances\DougDoug SMP Quality of life 1.2.1\.minecraft\logs\latest.log","w")
logfile.close()
def on_press(key):
    if key == keys.Key.f8:
        while not shared_queue.empty():
            response = shared_queue.get()
            indx = 0
            while True:
                print(indx)
                res = response[indx:indx+225]
                print(res)
                print(res[len(res)-1])
                if len(res) == 225:
                    try:
                        lastspace = len(res) - 1 - res[::-1].index(' ')
                    except:
                        lastspace = 225
                    res = res[:lastspace]
                    indx += lastspace
                    keyboard.type("\nt")
                    time.sleep(0.05)
                    keyboard.type(f"IAMAB0T[AI] jbm11208: {res}\n")
                else:
                    keyboard.type("\nt")
                    time.sleep(0.05)
                    keyboard.type(f"IAMAB0T[AI] jbm11208: {res}\n")
                    break
def beegpt():
    mixer.init(devicename='CABLE Input (VB-Audio Virtual Cable)')
    mixer.music.set_volume(0.2)  # Set playback volume to 20%
    mixer.music.set_volume(0.2)  # Set playback volume to 20%
    # Remove TTS, use random Wario mp3 clips instead
    skip_event = threading.Event()

    def on_skip(key):
        # Press F7 to skip current video/audio
        if key == keys.Key.f7:
            skip_event.set()

    skip_listener = keys.Listener(on_press=on_skip)
    skip_listener.daemon = True
    skip_listener.start()
    responding = False
    while True:
        with open(r"C:\Users\mcken\Downloads\mmc-develop-win32\MultiMC\instances\DougDoug SMP Quality of life 1.2.1\.minecraft\logs\latest.log", "r", encoding='utf-8') as logfile:
            # Move to the end of the file before starting to read new lines
            logfile.seek(0, os.SEEK_END)
            while True:
                line = logfile.readline()
                if not line:
                    time.sleep(0.01)
                    continue
                checkmsg = line
                if "[Render thread/INFO]: [System] [CHAT]" in line:
                    indx = line.index("[")
                    chat = line[indx+49:]
                    checkmsg = chat
                    msgName = "-"
                    name = "-"
                    msg = ""
                    print(chat)
                    try:
                        checkmsg = line
                        bracketOne = chat.index("]")
                        chat = chat[bracketOne+2:]
                        colon = chat.index(":")
                        name = chat[:colon]
                        message = chat[colon+2:]
                        msg = message.lower()
                        msgName = chat[:colon]
                        bracket = name.index("[")
                        msgName = chat[:bracket]
                    except:
                        pass
                    try:
                        arrow = chat.index("»")
                        name = chat[:arrow]
                        message = chat[arrow+2:]
                        msg = message.lower()
                        msgName = chat[:arrow]
                    except:
                        pass
                    print(checkmsg)
                    # Ignore new wario messages while responding
                    if responding and "wario" in msg:
                        continue
                    if ("[ai] wario has been cleared" in msg):
                        msg = ""
                    if ("[me -> [Best Town] jbm11208] clearwario" in str(checkmsg)):
                        mem = ""
                        with open(r"minecraft.txt", "w") as historytxt:
                            historytxt.write("")
                            historytxt.close()
                            msg = ""
                        pyautogui.keyDown('t')
                        time.sleep(0.2)
                        pyautogui.keyUp('t')
                        keyboard.type(f"IAMAB0T[AI] Wario HAS BEEN cleared\n")
                    if ("wario" in msg) or ("wario" in msg):
                        if msgName and (not "wario:" in msg) and (not "] ooga [" in msg) and (not "} ooga {" in msg) and ((not "] axogpt:" in msg) and randint(1,3)) and (not "ＤＵＮＥ" in msgName) and (not "-" in msgName) and ((not "] e. gadd:" in msg) and randint(1,3)):
                            responding = True
                            try:
                                with open(r"minecraft.txt", "r") as historytxt:
                                    mem = historytxt.read()
                                    historytxt.close()
                                    mem = str(mem)
                                    print(mem)
                                response = ollama.chat(model='gpt-oss:20b-cloud', messages=[
                                    {
                                        'role': 'system',
                                        'content': 'You are Wario. Here is your previous conversations, with User Question: being a question from a user, and Your Response: being what you responded to the question. ' + mem + "\n Remember, keep your response to 3 sentences or less. Each sentence is a maximum of 20 words. DO NOT say Your Response: or User Question:, as those are meant to be for you to tell who is saying what, not to say.",
                                    },
                                    {
                                        'role': 'user',
                                        'content': message,
                                    },
                                ])
                                response = response['message']['content']
                                with open(r"minecraft.txt", "w") as historytxt:
                                    historytxt.write(mem)
                                    historytxt.write('User Question: ' + message + "\n")
                                    historytxt.write('Your Response: ' + response + "\n")
                                    historytxt.close()
                                while not shared_queue.empty():
                                    shared_queue.get()
                                    shared_queue.task_done()
                                shared_queue.put(response)
                                response = response.replace("\n"," ")
                                for i in range(100):
                                    keyboard.press(keys.Key.backspace)
                                    keyboard.release(keys.Key.backspace)
                                keyboard.release(keys.Key.ctrl_l)
                                keyboard.release(keys.Key.shift)
                                indx = 0
                                waitTime = len(response) / 25
                                # Parse sound effect tags from response
                                sounds = []
                                length = 0
                                while True:
                                    bracketA = response.find("{")
                                    bracketZ = response.find("}")
                                    if bracketA == -1:
                                        sounds.append(response[length:])
                                        break
                                    sounds.append(response[length:bracketA])
                                    length = bracketA
                                    sounds.append(response[bracketA:bracketZ+1])
                                    response = response[:bracketA] + response[bracketZ+1:]

                                # --- Type response into chat as before ---
                                indx = 0
                                while True:
                                    res = response[indx:indx+225]
                                    if len(res) == 225:
                                        try:
                                            lastspace = len(res) - 1 - res[::-1].index(' ')
                                        except:
                                            lastspace = 225
                                        res = res[:lastspace]
                                        indx += lastspace
                                        keyboard.type("\n")
                                        time.sleep(0.1)
                                        pyautogui.keyDown('t')
                                        time.sleep(0.2)
                                        pyautogui.keyUp('t')
                                        time.sleep(0.2)
                                        keyboard.type(f"IAMAB0T[AI] Wario: {res}\n")
                                        if "𝒶𝒹" in res:
                                            break
                                    else:
                                        keyboard.type("\n")
                                        pyautogui.keyDown('t')
                                        time.sleep(0.2)
                                        pyautogui.keyUp('t')
                                        time.sleep(0.5)
                                        keyboard.type(f"IAMAB0T[AI] Wario: {res}\n")
                                        break
                                # --- Play random Wario mp3 clips throughout the response, pausing for curly brackets, and continuing after ---
                                wario_folder = os.path.join("wario")
                                wario_clips = [f for f in os.listdir(wario_folder) if f.lower().endswith('.mp3')]
                                # Join all text segments (not curly brackets) and split into words
                                text_segments = [s for s in sounds if not (s.startswith('{') and s.endswith('}')) and s.strip()]
                                words = ' '.join(text_segments).split()
                                # Play a random Wario clip for every 2 words
                                word_idx = 0
                                # Ensure responseNum is initialized before use
                                if not hasattr(beegpt, 'responseNum'):
                                    beegpt.responseNum = 0
                                responseNum = beegpt.responseNum
                                try:
                                    for idx, sound in enumerate(sounds):
                                        if not (sound.startswith('{') and sound.endswith('}')) and sound.strip():
                                            seg_words = sound.split()
                                            for w in seg_words:
                                                word_idx += 1
                                                if word_idx % 2 == 0:
                                                    clip = random.choice(wario_clips)
                                                    mixer.music.load(os.path.join(wario_folder, clip))
                                                    mixer.music.set_volume(0.2)  # Ensure volume is set for each clip
                                                    mixer.music.play()
                                                    start = time.time()
                                                    audio = MP3(os.path.join(wario_folder, clip))
                                                    while time.time() - start < audio.info.length:
                                                        if skip_event.is_set():
                                                            skip_event.clear()
                                                            mixer.music.stop()
                                                            break
                                                        time.sleep(0.1)
                                        elif sound.startswith('{') and sound.endswith('}'): 
                                            file = sound[1:sound.find("}")]
                                            try:
                                                mixer.music.load(f"Sounds\\{file}.mp3")
                                                mixer.music.set_volume(0.2)  # Ensure volume is set for each sfx
                                                mixer.music.play()
                                                audio = MP3(f"Sounds\\{file}.mp3")
                                                start = time.time()
                                                while time.time() - start < audio.info.length:
                                                    if skip_event.is_set():
                                                        skip_event.clear()
                                                        mixer.music.stop()
                                                        break
                                                    time.sleep(0.1)
                                            except:
                                                mp3file = f'sfx{str(responseNum)}'
                                                if os.path.exists(mp3file + '.mp3'):
                                                    try:
                                                        os.remove(mp3file + '.mp3')
                                                    except Exception as e:
                                                        print(f"Could not delete {mp3file}.mp3 before download: {e}")
                                                # Check if file is a YouTube URL (normal or shorts)
                                                import re
                                                yt_url_pattern = r"(https?://)?(www\.)?(youtube\.com|youtu\.be)/[\w\-?&=/%#\.]+"
                                                shorts_pattern = r"https?://(www\.)?youtube\.com/shorts/([\w\-]+)"
                                                shorts_match = re.match(shorts_pattern, file)
                                                if shorts_match:
                                                    # Convert shorts URL to watch URL
                                                    video_id = shorts_match.group(2)
                                                    download_target = f"https://www.youtube.com/watch?v={video_id}"
                                                elif re.match(yt_url_pattern, file):
                                                    download_target = file
                                                else:
                                                    download_target = f"ytsearch1:{file}"
                                                ydl_opts = {
                                                    'format': 'bestaudio/best',
                                                    'outtmpl': mp3file,
                                                    'postprocessors': [{
                                                        'key': 'FFmpegExtractAudio',
                                                        'preferredcodec': 'mp3',
                                                        'preferredquality': '192',
                                                    }],
                                                    'quiet': True
                                                }
                                                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                                                    ydl.download([download_target])
                                                print("Downloaded")
                                                time.sleep(2)
                                                mixer.music.load(mp3file + '.mp3')
                                                mixer.music.set_volume(0.2)  # Ensure volume is set for each yt_dlp sfx
                                                mixer.music.play()
                                                audio = MP3(mp3file + '.mp3')
                                                start = time.time()
                                                while time.time() - start < audio.info.length:
                                                    if skip_event.is_set():
                                                        skip_event.clear()
                                                        mixer.music.stop()
                                                        break
                                                    time.sleep(0.1)
                                                responseNum += 1
                                                beegpt.responseNum = responseNum
                                    mixer.music.stop()
                                    # (Removed duplicate/old audio playback loop)
                                finally:
                                    responding = False
                                    # After processing a question, skip to the end of the log to avoid queueing messages
                                    logfile.seek(0, os.SEEK_END)
                            except:
                                print("sound error")
        logfile = open(r"C:\Users\mcken\Downloads\mmc-develop-win32\MultiMC\instances\DougDoug SMP Quality of life 1.2.1\.minecraft\logs\latest.log","w")
        logfile.close()
        time.sleep(0.01)
thread1 = threading.Thread(target=beegpt)
thread1.start()
with keys.Listener(on_press=on_press) as listener:
    try:
        listener.join()
        thread1.join()
    except:
        pass