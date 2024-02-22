from aip import AipSpeech


# 将语音识别封装成函数
def recognize(file, settings):
    # 创建识别对象
    client = AipSpeech(settings['APP_ID'], settings['API_KEY'], settings['SECRET_KEY'])
    # 打开文件，读取内容
    data = open(file, 'rb').read()
    # 传递参数，文件，文件格式，采样频率，PID 1537
    result = client.asr(data, 'wav', 16000, {'dev_pid': 1537})
    # 返回结果
    if 'result' in result:
        return result['result'][0]
    else:
        print('识别失败')
        return None


# print(recognize('你好.wav'))
