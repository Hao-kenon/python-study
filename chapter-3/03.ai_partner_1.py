import streamlit as st
import os
from openai import OpenAI


#设置页面配置项
st.set_page_config(
    page_title="AI智能伴侣",
    page_icon="😂",
    #布局
    layout="wide",
    #控制侧边栏状态
    initial_sidebar_state="expanded",
    menu_items={}
)

#标题
st.title("AI智能伴侣")

#logo
st.logo("./resources/logo.jpg")

#系统提示词
system_prompt = "你作为一名可爱的AI助理，名字叫小甜甜，请你使用温柔的语气回答问题"

#初始化聊天信息
if "messages" not in st.session_state:
    st.session_state.messages = []

#展示聊天信息
for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])
    # if message["role"] == "user":
    #     st.chat_message("user").write(message["content"])
    # else:
    #     st.chat_message("assistant").write(message["content"])

#创建与大模型交互的客户端对象(DEEPSEEK_API_KEY 环境变量的名字，值是DeepSeek的API_KEY)
client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'), base_url="https://api.deepseek.com")

#消息输入框
prompt = st.chat_input("请输入你的问题")
if prompt:#字符串会自动转为布尔值，如果字符串非空，则返回True；如果字符串为空，则返回False
    st.chat_message("user").write(prompt)

    #调式
    print("-------------> 调用AI大模型,提示词为:",prompt)

    #保存用户输入的提示词
    st.session_state.messages.append({"role": "user", "content": prompt})


    #调用AI大模型
    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ],
        stream=False
    )


    print("<-----------------------大模型返回结果:",response.choices[0].message.content)#终端调试
    # 输出大模型返回的结果
    st.chat_message("assistant").write(response.choices[0].message.content)

    #保存大模型返回的结果
    st.session_state.messages.append({"role": "assistant", "content": response.choices[0].message.content})