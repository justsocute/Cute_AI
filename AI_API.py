from zhipuai import ZhipuAI


def dialogue_with_ai(text_in, settings, _messages):
    client = ZhipuAI(api_key=settings["api_key"])
    # 将变量放入字典中
    message = {"role": "user", "content": text_in}
    _messages.append(message)
    response = client.chat.completions.create(
        model="glm-3-turbo",  # 填写需要调用的模型名称
        messages=_messages
    )
    text_out = response.choices[0].message.content
    # 更新对话历史
    _messages.append({"role": "assistant", "content": text_out})
    print("AI：", text_out)
