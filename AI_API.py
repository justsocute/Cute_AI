from zhipuai import ZhipuAI

client = ZhipuAI(api_key="d2bf8ab50ec79daefe4c8fcb747b9990.abqhgLXKj3LSncv4")  # 填写您自己的APIKey
response = client.chat.completions.create(
    model="glm-3-turbo",  # 填写需要调用的模型名称
    messages=[
        {"role": "user", "content": "叫我宝宝"},
        # {"role": "assistant", "content": "当然，为了创作一个吸引人的slogan，请告诉我一些关于您产品的信息"},
        # {"role": "user", "content": "智谱AI开放平台"},
        # {"role": "assistant", "content": "智启未来，谱绘无限一智谱AI，让创新触手可及!"},
        # {"role": "user", "content": "叫我宝宝"}
    ],
)
print(response.choices[0].message)
