import tkinter as tk
from tkinter import messagebox
import audio_recorder
import speech_to_text
import AI_API
from utils import get_json
import os

# 全局变量，用于存储对话和AI的回答
messages = []
settings_file = os.path.join(os.path.dirname(__file__), 'settings.json')
settings = get_json(settings_file)


def start_recording():
    # 开始录音的逻辑
    audio_recorder.record_audio('data/voice_in.wav', 7)
    print("正在识别...")
    # 识别wav文件中的语音内容
    text_in = speech_to_text.recognize('data/voice_in.wav', settings['baidu_stt_api'])
    print("我：", text_in)
    print("正在思考...")
    # 与AI对话
    AI_API.dialogue_with_ai(text_in, settings['zhipu_ai'], messages)
    # 更新文本框内容
    conversation_box.delete(1.0, tk.END)
    for message in messages:
        if message["role"] == "user":
            conversation_box.insert(tk.END, "你: " + message["content"] + "\n")
        else:
            conversation_box.insert(tk.END, "AI: " + message["content"] + "\n")

# 创建窗口
root = tk.Tk()
root.title("语音对话demo")

# 创建文本框用于显示对话
conversation_box = tk.Text(root, height=10, width=50)
conversation_box.pack(padx=10, pady=10)

# 创建按钮用于开始录音
record_button = tk.Button(root, text="开始/结束录音", command=start_recording)
record_button.pack(pady=5)

# 运行主循环
root.mainloop()
