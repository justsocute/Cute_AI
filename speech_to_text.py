from aip import AipSpeech

# 百度语音识别API配置
APP_ID = '51947267'
API_KEY = '89FyKzuxRAcemT9jGVf8jLq7'
SECRET_KEY = '8sA4BDGBw06S4BW0Z9bZPV47wGADHend'

# 创建识别对象
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


# 将语音识别封装成函数
def recognize(file):
    # 传递参数，文件，文件格式，采样频率，PID 1537
    data = open(file, 'rb').read()
    result = client.asr(data, 'wav', 16000, {'dev_pid': 1537})
    return result['result'][0]


print(recognize('你好.wav'))
