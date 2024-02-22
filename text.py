import pyaudio
import wave
from audio_recorder import record_audio
import tkinter as tk
# 录音配置
CHUNK = 1024  # 每次读取音频数据帧大小为1024字节
FORMAT = pyaudio.paInt16  # 音频格式为16位整形
CHANNELS = 1  # 单声道录音
RATE = 16000  # 采样率为16000

# 录音状态变量
recording = False
audio_frames = []

def start_recording():
    global recording, audio_frames
    if not recording:
        # 开始录音
        print("请开始说话...")
        recording = True
        p = pyaudio.PyAudio()
        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

        # 收集音频数据
        while recording:
            data = stream.read(CHUNK)
            audio_frames.append(data)

        # 停止录音并关闭流
        stream.stop_stream()
        stream.close()
        p.terminate()

def end_recording():
    global recording
    if recording:
        # 结束录音并保存
        recording = False
        wav_output_filename = 'data/voice_in.wav'
        wf = wave.open(wav_output_filename, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(audio_frames))
        wf.close()
        # 清空录音帧列表
        audio_frames = []

# 创建窗口
root = tk.Tk()
root.title("语音对话demo")

# 创建开始录音按钮
start_button = tk.Button(root, text="开始录音", command=start_recording)
start_button.pack(side=tk.LEFT, padx=10, pady=5)

# 创建结束录音按钮
end_button = tk.Button(root, text="结束录音", command=end_recording)
end_button.pack(side=tk.RIGHT, padx=10, pady=5)

# 运行主循环
root.mainloop()
