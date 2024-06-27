import streamlit as st
import os
import openai
import base64

# OpenAI API 키 설정
os.environ["OPENAI_API_KEY"] = "여기에 발급받은 API 키를 입력해 주세요"

openai.api_key = os.environ.get("OPENAI_API_KEY")

def display_page7_5():
    st.markdown("""
        <style>
        .center-text {
            text-align: center;
        }
        .center-img-container {
            display: flex;
            justify-content: center;
            align-items: center;
            width: 100%;
        }
        .center-img-container img {
            max-width: 100%;
            height: auto;
        }
        </style>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([0.57, 1, 0.35])
    with col2:
        st.markdown('<h1 class="center-text">흉곽 골절</h1>', unsafe_allow_html=True)

    if 'selected_bone' not in st.session_state or not st.session_state.selected_bone:
        st.error("먼저 골절 부위를 선택해 주세요.")
        return
    selected_bone = st.session_state.selected_bone

    with open("assets/rib.jpg", "rb") as f:
        img_bytes = f.read()
        img_base64 = base64.b64encode(img_bytes).decode()

    st.markdown(f"""
        <div class="center-img-container">
            <img src="data:image/jpeg;base64,{img_base64}" alt="흉곽 이미지">
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([0.35, 1, 0.35])
    with col2:
        st.markdown('<div class="center-text">흉곽에 골절이 예상되는 부위를 선택해주세요.</div>', unsafe_allow_html=True)
    
    symptom_options = [
        "흉골",
        "늑골",
        "늑연골",
        "흉추",
        "기타"
    ]
    
    selected_symptom = st.selectbox("부위", symptom_options)
    additional_info = st.text_area("자세한 증상에 대해 설명해주세요.")

    # 폼 생성
    with st.form(key='diagnosis_form'):
        col1, col2, col3 = st.columns([1.68, 1, 1])
        with col2:
            submit = st.form_submit_button("진단")

    # 버튼을 눌렀을 때 입력된 내용 처리
    if submit:
        # response = client.chat.completions.create(
        #     messages=[
        #         {
        #             "role": "user",
        #             "content": text,
        #         },
        #         {
        #             "role": "system",
        #            "content": f"이 사용자는 일반인이며 어려운 설명은 이해하기 어려울 수 있습니다. 현재 FirstAID라는 인공지능 api 사용 웹에서 골절 진단을 위해 접근하였습니다. 환자의 문제가 발생한 부분은 {selected_bone}의 {selected_symptom}d로 이 부분이 현재 환자가 골절되었다고 의심하는 부분입니다. 환자가 제시한 상황을 잘 듣고 골절인지 아닌지를 판단하여 골절 참 거짓 여부를 말하며 간략히 설명하고 만약 골절이 아니라고 판단되면 골절이 아닌 것 같다고 말해주세요. 또한 구체적으로 행동요령과 구급처치법을 설명해 주세요. ",
        #         },
        #     ],
        #     model="gpt-4",
        # )
        st.write(f"증상 부위: 흉곽-{selected_symptom}")
        st.write(f"추가 설명: {additional_info}")
        # st.write(response['choices'][0]['message']['content'])

# 앱 실행 부분
if __name__ == "__main__":
    display_page7_5()
