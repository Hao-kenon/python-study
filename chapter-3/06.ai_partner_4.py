import streamlit as st
import os
from openai import OpenAI
from datetime import datetime
import json
from streamlit.elements.widgets import button



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

#生成会话标识
def generate_session_id():
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

#保存会话信息函数
def save_session():
    if st.session_state.current_session:
        # 构建新的对话对象
        session_date = {
            "nick_name": st.session_state.nick_name,
            "personality": st.session_state.personality,
            "current_session": st.session_state.current_session,
            "messages": st.session_state.messages,
        }

        # 如果 session 文件夹不存在，则创建
        if not os.path.exists("sessions"):
            os.mkdir("sessions")

        #保存会话数据
        with open(f"sessions/{st.session_state.current_session}.json", "w", encoding="utf-8") as f:
            json.dump(session_date, f, ensure_ascii=False, indent=2)


#加载所有会话列表信息
def load_sessions():
    session_list = []
    # 加载sessions文件夹下的所有会话文件
    if os.path.exists("sessions"):
        file_list = os.listdir("sessions")
        for filename in file_list:
            if filename.endswith(".json"):
                session_list.append(filename[:-5])
    session_list.sort(reverse=True)
    return session_list

#加载指定会话信息
def load_session(session_id):
    try:
        if os.path.exists(f"sessions/{session_id}.json"):
            # 读取会话数据
            with open(f"sessions/{session_id}.json", "r", encoding="utf-8") as f:
                session_data = json.load(f)
                st.session_state.messages = session_data["messages"]
                st.session_state.nick_name = session_data["nick_name"]
                st.session_state.personality = session_data["personality"]
                st.session_state.current_session = session_id
    except Exception:
        st.error("加载会话数据失败")


#删除会话信息
def delete_session(session_id):
    try:
        if os.path.exists(f"sessions/{session_id}.json"):
            os.remove(f"sessions/{session_id}.json")#删除文件
            #如果删除的是当前会话，则更新当前会话
            if st.session_state.current_session == session_id:
                st.session_state.messages = []
                st.session_state.current_session = generate_session_id()
    except Exception:
        st.error("删除会话数据失败")

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
#当前会话
if "current_session" not in st.session_state:
    st.session_state.current_session = generate_session_id()



#展示聊天信息
st.text(f"会话名称:{st.session_state.current_session}")
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
    st.subheader("AI控制面板")
    #新建会话
    if st.button("新建会话",width="stretch",icon="🔵"):
        # 1.保存当前会话
        save_session()

        # 2.创建新的会话
        if st.session_state.messages: #如果聊天信息不为空，True;否则， False
            st.session_state.messages= []
            st.session_state.current_session = generate_session_id()
            save_session()
            st.rerun()#重新运行当前页面

    # 历史会话
    st.text("会话历史")
    session_list = load_sessions()
    for session in session_list:
        col1,col2 = st.columns([4,1])
        with col1:
            #加载会话信息
            #三元运算符 值1 if 条件 else 值2
            if st.button(session,width="stretch",icon="🔵",key=f"load_{session}",type="primary" if st.session_state.current_session == session else "secondary"):
                load_session( session)
                st.rerun()
        with col2:
            #删除会话信息
            if st.button("",width="stretch",icon="❌",key=f"delete_{session}"):
                delete_session(session)
                st.rerun()
        # st.button(session,width="stretch",icon="🔵")
        # st.button("",width="stretch",icon="❌")

    #分隔符
    st.divider()
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

    #保存会话信息
    save_session()

