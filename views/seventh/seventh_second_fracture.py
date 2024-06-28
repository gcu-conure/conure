import streamlit as st
import os
import openai
import base64

# OpenAI API 키 설정
os.environ["OPENAI_API_KEY"] = "여기에 발급받은 API 키를 입력해 주세요"

openai.api_key = os.environ.get("OPENAI_API_KEY")

def display_page7_2():
    st.title("안면부 골절")

    if 'selected_bone' not in st.session_state or not st.session_state.selected_bone:
        st.error("먼저 골절 부위를 선택해 주세요.")
        return
    selected_bone = st.session_state.selected_bone

    with open("assets/face_bone2.jpg", "rb") as f:
        img_bytes = f.read()
        img_base64 = base64.b64encode(img_bytes).decode()

    st.markdown(f'<img src="data:image/jpeg;base64,{img_base64}" alt="안면부 이미지" style="width:100%; max-width:600px;">', unsafe_allow_html=True)

    # 증상 선택 옵션 제공
    st.markdown("안면부에 골절이 예상되는 부위를 선택해주세요.")
    symptom_options = [
        "이마뼈",
        "관자뼈",
        "나비뼈",
        "눈물뼈",
        "벌집뼈",
        "코뼈",
        "광대뼈",
        "위턱뼈",
        "아래턱뼈",
        "기타"
    ]
    selected_symptom = st.selectbox("증상", symptom_options)
    additional_info = st.text_area("자세한 증상에 대해 설명해주세요.")

    # 폼 생성
    with st.form(key='diagnosis_form'):
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
        #             "content": f"이 사용자는 일반인이며 어려운 설명은 이해하기 어려울 수 있습니다. 현재 FirstAID라는 인공지능 api 사용 웹에서 골절 진단을 위해 접근하였습니다. 구체적으로 행동요령과 구급처치법을 설명해 주세요. 그리고 이 환자의 문제가 발생한 부분은 {selected_bone}의 {selected_symptom}입니다.",
        #         },
        #     ],
        #     model="gpt-4",
        # )
        st.write(f"아픈 부위: 안면부-{selected_symptom}")
        st.write(f"추가 설명: {additional_info}")
        # st.write(response['choices'][0]['message']['content'])



