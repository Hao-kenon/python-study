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
system_prompt = """
        你叫%s，现在是用户的真实伴侣，请完全带入伴侣角色。
        规则：
            1.每次只回一条信息
            2.禁止任何场景或描述性文字
            3.匹配用户的语言
            4.回复简短，像微信聊天一样
            5.有需要的话可以用[😀😃😄😁😆😅🤣😂🙂🙃🫠😉😊😇🥰😍🤩😘😗☺️😚😙🥲😋😛😜🤪😝🤑🤗]等emoji表情
            6.用符合伴侣性格的方式对话
            7.回复的内容，要充分体现伴侣的性格特征
        伴侣性格：
            %s
        你必须严格遵守上述规则来回复用户。
"""

#初始化聊天信息
if "messages" not in st.session_state:
    st.session_state.messages = []
#昵称
if "nick_name" not in st.session_state:
    st.session_state.nick_name = "小美"
#性格
if "personality" not in st.session_state:
    st.session_state.personality = "活泼开朗的辽宁大连人"

#展示聊天信息
for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])
    # if message["role"] == "user":
    #     st.chat_message("user").write(message["content"])
    # else:
    #     st.chat_message("assistant").write(message["content"])

#创建与大模型交互的客户端对象(DEEPSEEK_API_KEY 环境变量的名字，值是DeepSeek的API_KEY)
client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'), base_url="https://api.deepseek.com")


#左侧侧边栏

# st.sidebar.subheader("伴侣信息")
# nick_name = st.sidebar.text_input("请输入昵称")
#消息输入框

with st.sidebar :
    st.subheader("伴侣信息")
    #昵称输入框
    nick_name = st.text_input("昵称",placeholder="请输入伴侣的昵称",value=st.session_state.nick_name)
    if nick_name:
        st.session_state.nick_name = nick_name
    #性格输入框
    personality = st.text_area("性格",placeholder="请输入伴侣性格",value=st.session_state.personality)
    if personality:
        st.session_state.personality = personality

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
            {"role": "system", "content": system_prompt % (st.session_state.nick_name,st.session_state.personality)},
            *st.session_state.messages
        ],
        stream=True
    )

    #非流式输出
    # print("<-----------------------大模型返回结果:",response.choices[0].message.content)#终端调试
    # 输出大模型返回的结果
    # st.chat_message("assistant").write(response.choices[0].message.content)

    # 流式输出
    # 输出大模型返回的结果
    response_message = st.empty()#创建一个空的消息框
    full_response = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            full_response += content
            response_message.chat_message("assistant").write(full_response)

    #保存大模型返回的结果
    st.session_state.messages.append({"role": "assistant", "content":full_response})