import pyaudio
import wave

# pyaudio是用于音频处理的库，它提供了录制和播放音频的功能。
# wave是用于处理WAV文件的库。

# 音频格式为16位整形
FORMAT = pyaudio.paInt16
# 单声道录音
CHANNELS = 1
# 采样率为16000
RATE = 16000
# 每次读取音频数据帧大小为2048字节
CHUNK = 2048


def record_audio(wave_out_path, record_second):
    # 创建pyaudio对象
    p = pyaudio.PyAudio()

    # 打开音频流
    stream = p.open(format=FORMAT,  # format：指定音频数据的格式。
                    channels=CHANNELS,  # channels：指定声道数。
                    rate=RATE,  # rate：指定采样率
                    input=True,  # input：布尔值，指定是否为输入流。如果为True，则该流用于录音；如果为False，则该流用于播放。

                    # frames_per_buffer：指定每次从音频设备读取或写入的帧数。这个值应该与录音缓冲区大小和播放缓冲区大小相匹配，以避免数据丢失或重叠。
                    frames_per_buffer=CHUNK)

    # 创建wav文件，并设置参数
    wf = wave.open(wave_out_path, 'wb')
    # 设置WAV文件的声道数。对于单声道音频，这通常是1；对于立体声，则是2。
    wf.setnchannels(CHANNELS)
    # 设置WAV文件的采样宽度，即每个样本的字节大小。
    wf.setsampwidth(p.get_sample_size(FORMAT))
    # 设置WAV文件的采样率，即每秒采样的次数。
    wf.setframerate(RATE)

    # 开始录音并写入数据
    for _ in range(0, int(RATE * record_second / CHUNK)):
        data = stream.read(CHUNK)
        wf.writeframes(data)

    # 停止音频流流
    stream.stop_stream()

    # 关闭音频流
    stream.close()

    # 终止pyaudio对象
    p.terminate()

    # 关闭wav文件
    wf.close()


# record_audio('data/voice_in.wav', 10)
