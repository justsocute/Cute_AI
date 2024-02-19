import audio_recorder
import speech_to_text
import AI_API
import keyboard


try:
    while True:
        record_audio('data/voice_in.wav', 10)
except keyboard.KeyboardInterrupt:
    print("检测到Ctrl+C，正在退出程序...")