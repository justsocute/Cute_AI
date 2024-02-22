from audio_recorder import record_audio
from speech_to_text import recognize
from AI_API import dialogue_with_ai
import os
from utils import get_json


if __name__ == '__main__':
    settings_file = os.path.join(os.path.dirname(__file__), 'settings.json')
    settings = get_json(settings_file)
    messages = []
    while True:
        # 录音，并将语音保存为wav文件
        print("请开始说话...")
        record_audio('data/voice_in.wav', 7)
        print("正在识别...")
        # 识别wav文件中的语音内容
        text_in = recognize('data/voice_in.wav', settings['baidu_stt_api'])
        print("我：", text_in)
        print("正在思考...")
        # 与AI对话
        dialogue_with_ai(text_in, settings['zhipu_ai'], messages)
