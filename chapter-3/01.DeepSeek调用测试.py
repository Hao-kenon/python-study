
import os
from openai import OpenAI

#创建与大模型交互的客户端对象(DEEPSEEK_API_KE 环境变量的名字，值是DeepSeek的API_KEY)
client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'),base_url="https://api.deepseek.com")

#与AI大模型进行交互(参数)
response = client.chat.completions.create(
    model="deepseek-v4-pro",
    messages=[
        {"role": "system", "content": "你是一名可爱的AI助理，名字叫小甜甜，请你使用温柔的预期回答问题"},
        {"role": "user", "content": "你是谁"},
    ],
    stream=False
)

#输出
print(response.choices[0].message.content)