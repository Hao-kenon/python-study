import streamlit as st

#配置页面
st.set_page_config(
    page_title="Streamlit入门",
    page_icon="🧊",
    layout="wide",
    #控制侧边栏状态
    initial_sidebar_state="expanded",
    menu_items={}
)

#大标题
st.title("Streamlit 入门演示")
st.header("Streamlit 一级标题")
st.subheader("Streamlit 二级标题")

#段落文字
st.write("布偶猫是猫界公认的“颜值天花板”。它们体型较大，是体格最结实的猫种之一，却拥有一身丝滑顺滑的中长毛，触感像上等的兔毛，而且幸运的是，它的底层绒毛极少，相对不易严重打结。")
st.write("布偶猫最著名的就是它的性格。为什么叫这个名字？因为当你抱起它们时，它们通常会全身放松、软绵绵地瘫在你的怀里，像极了真实的儿童布偶。")
st.write("虽然布偶猫优点很多，但在饲养前需要了解以下几点,布偶猫的肠胃相对敏感，需要选择优质、稳定的猫粮，换粮需要循序渐进。虽然是中长毛，不易打结，但掉毛量不可小觑（尤其在换毛季），需要定期梳毛以保持丝滑。")
st.write("布偶猫不仅是猫，更是温柔的守护者。它们安静、优雅，叫声轻柔细软（像小鸟一样）。它们非常适合有孩子的家庭、多猫家庭或者公寓生活。")

#图片
st.image("./resources/雨后外滩.jpg")

#音频
st.audio("./resources/rui-1.mp3")

#视频
st.video("./resources/video.mkv")

#logo
st.logo("./resources/logo.jpg")

#表格
student_data = {
    "姓名" : ["王林","李慕婉","韩立","萧炎"],
    "学号" : ["202601","202602","202603","202604"],
    "语文" : ["80","92","100","88"],
    "数学" : ["99","97","91","79"]
}
st.table(student_data)

#输入框
name = st.text_input("请输入姓名")
st.write(f"你的姓名是:{name}")


password = st.text_input("请输入密码",type="password")
st.write(f"你的密码是:{password}")

#单选按钮
gender = st.radio("请输入你的性别",["男","女","隐藏"],index=2)
st.write(f"你的性别是 {gender}")