import streamlit as st
import os
import openai
import base64

# OpenAI API 키 설정

os.environ["OPENAI_API_KEY"] = "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"
openai.api_key = os.environ.get("OPENAI_API_KEY")

def display_page5_2():
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
            position: relative;
        }
        .center-img-container img {
            max-width: 100%;
            height: auto;
        }
        .label-left {
            position: absolute;
            top: 50%;
            left: 0;
            transform: translate(-50%, -50%);
            font-size: 20px;
            font-weight: bold;
            color: black;
        }
        .label-right {
            position: absolute;
            top: 50%;
            right: 0;
            transform: translate(50%, -50%);
            font-size: 20px;
            font-weight: bold;
            color: black;
        }
        .teeth-container {
            position: relative;
            width: 100%;
            max-width: 600px;
            margin: 0 auto;
        }
        .teeth-container img {
            width: 100%;
            display: block;
        }
        .button-overlay {
            position: absolute;
            background-color: transparent;
            border: none;
            cursor: pointer;
        }
        .button-overlay:hover {
            background-color: rgba(0, 0, 0, 0.3);
        }
        .button-overlay.selected {
            background-color: rgba(255, 0, 0, 0.3);
        }
        .button-overlay::before {
            content: attr(data-index);
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            color: black;
            font-weight: bold;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 class="center-text">치아 손상 진단</h1>', unsafe_allow_html=True)

    if 'selected_teeth' not in st.session_state:
        st.session_state.selected_teeth = []
    if 'selected_teeth_numbers' not in st.session_state:
        st.session_state.selected_teeth_numbers = []

    selected_teeth = st.session_state.selected_teeth
    selected_teeth_numbers = st.session_state.selected_teeth_numbers

    with open("./assets/teeth.jpg", "rb") as f:
        img_bytes = f.read()
        img_base64 = base64.b64encode(img_bytes).decode()

    # JavaScript for handling button clicks
    st.markdown("""
        <script>
        function select_tooth(index) {
            var toothInput = window.parent.document.getElementById('tooth-input');
            if (!toothInput.value.includes(index)) {
                toothInput.value += (toothInput.value ? "," : "") + index;
            } else {
                toothInput.value = toothInput.value.split(',').filter(num => num != index).join(',');
            }
            toothInput.dispatchEvent(new Event('input', { bubbles: true }));
            // Update button class
            var button = document.querySelector('.button-overlay[data-index="' + index + '"]');
            button.classList.toggle('selected');
        }
        </script>
    """, unsafe_allow_html=True)

    # CSS 스타일 정의 및 이미지 렌더링
    st.markdown(f"""
        <div class="center-img-container">
            <div class="teeth-container">
                <div class="label-left">L</div>
                <img src="data:image/jpeg;base64,{img_base64}">
                <div class="label-right">R</div>
                <!-- 윗니 -->
                <button class="button-overlay {"selected" if "1" in selected_teeth_numbers else ""}" data-index="1" style="top: 33%; left: 3%; width: 4.5%; height: 15%;" onclick="select_tooth(1)"></button>
                <button class="button-overlay {"selected" if "2" in selected_teeth_numbers else ""}" data-index="2" style="top: 33%; left: 6%; width: 5%; height: 17%;" onclick="select_tooth(2)"></button>
                <button class="button-overlay {"selected" if "3" in selected_teeth_numbers else ""}" data-index="3" style="top: 33%; left: 11%; width: 5%; height: 20%;" onclick="select_tooth(3)"></button>
                <button class="button-overlay {"selected" if "4" in selected_teeth_numbers else ""}" data-index="4" style="top: 33%; left: 17%; width: 6%; height: 22%;" onclick="select_tooth(4)"></button>
                <button class="button-overlay {"selected" if "5" in selected_teeth_numbers else ""}" data-index="5" style="top: 33%; left: 24.5%; width: 6%; height: 22%;" onclick="select_tooth(5)"></button>
                <button class="button-overlay {"selected" if "6" in selected_teeth_numbers else ""}" data-index="6" style="top: 33%; left: 32%; width: 7%; height: 21%;" onclick="select_tooth(6)"></button>
                <button class="button-overlay {"selected" if "7" in selected_teeth_numbers else ""}" data-index="7" style="top: 33%; left: 41%; width: 8%; height: 21%;" onclick="select_tooth(7)"></button>
                <button class="button-overlay {"selected" if "8" in selected_teeth_numbers else ""}" data-index="8" style="top: 33%; left: 50%; width: 8.8%; height: 21%;" onclick="select_tooth(8)"></button>
                <button class="button-overlay {"selected" if "9" in selected_teeth_numbers else ""}" data-index="9" style="top: 33%; left: 61%; width: 7%; height: 21%;" onclick="select_tooth(9)"></button>
                <button class="button-overlay {"selected" if "10" in selected_teeth_numbers else ""}" data-index="10" style="top: 33%; left: 68%; width: 7%; height: 22%;" onclick="select_tooth(10)"></button>
                <button class="button-overlay {"selected" if "11" in selected_teeth_numbers else ""}" data-index="11" style="top: 33%; left: 75.5%; width: 7%; height: 22%;" onclick="select_tooth(11)"></button>
                <button class="button-overlay {"selected" if "12" in selected_teeth_numbers else ""}" data-index="12" style="top: 33%; left: 82.7%; width: 6%; height: 21%;" onclick="select_tooth(12)"></button>
                <button class="button-overlay {"selected" if "13" in selected_teeth_numbers else ""}" data-index="13" style="top: 33%; left: 87.5%; width: 5%; height: 17%;" onclick="select_tooth(13)"></button>
                <button class="button-overlay {"selected" if "14" in selected_teeth_numbers else ""}" data-index="14" style="top: 33%; left: 91%; width: 5%; height: 15%;" onclick="select_tooth(14)"></button>
                <!-- 아랫니 -->
                <button class="button-overlay {"selected" if "15" in selected_teeth_numbers else ""}" data-index="15" style="top: 54%; left: 5%; width: 3%; height: 15%;" onclick="select_tooth(15)"></button>
                <button class="button-overlay {"selected" if "16" in selected_teeth_numbers else ""}" data-index="16" style="top: 56%; left: 8%; width: 3.5%; height: 18%;" onclick="select_tooth(16)"></button>
                <button class="button-overlay {"selected" if "17" in selected_teeth_numbers else ""}" data-index="17" style="top: 57%; left: 12%; width: 5.5%; height: 20%;" onclick="select_tooth(17)"></button>
                <button class="button-overlay {"selected" if "18" in selected_teeth_numbers else ""}" data-index="18" style="top: 57%; left: 19%; width: 5%; height: 22%;" onclick="select_tooth(18)"></button>
                <button class="button-overlay {"selected" if "19" in selected_teeth_numbers else ""}" data-index="19" style="top: 57%; left: 26%; width: 6%; height: 22%;" onclick="select_tooth(19)"></button>
                <button class="button-overlay {"selected" if "20" in selected_teeth_numbers else ""}" data-index="20" style="top: 57%; left: 34.5%; width: 6.5%; height: 21%;" onclick="select_tooth(20)"></button>
                <button class="button-overlay {"selected" if "21" in selected_teeth_numbers else ""}" data-index="21" style="top: 57%; left: 41.5%; width: 8%; height: 21%;" onclick="select_tooth(21)"></button>
                <button class="button-overlay {"selected" if "22" in selected_teeth_numbers else ""}" data-index="22" style="top: 57%; left: 50%; width: 8%; height: 21%;" onclick="select_tooth(22)"></button>
                <button class="button-overlay {"selected" if "23" in selected_teeth_numbers else ""}" data-index="23" style="top: 57%; left: 58.8%; width: 6.5%; height: 21%;" onclick="select_tooth(23)"></button>
                <button class="button-overlay {"selected" if "24" in selected_teeth_numbers else ""}" data-index="24" style="top: 57%; left: 67%; width: 7%; height: 22%;" onclick="select_tooth(24)"></button>
                <button class="button-overlay {"selected" if "25" in selected_teeth_numbers else ""}" data-index="25" style="top: 57%; left: 75%; width: 6.5%; height: 22%;" onclick="select_tooth(25)"></button>
                <button class="button-overlay {"selected" if "26" in selected_teeth_numbers else ""}" data-index="26" style="top: 57%; left: 81.5%; width: 6%; height: 21%;" onclick="select_tooth(26)"></button>
                <button class="button-overlay {"selected" if "27" in selected_teeth_numbers else ""}" data-index="27" style="top: 55%; left: 88%; width: 4%; height: 19%;" onclick="select_tooth(27)"></button>
                <button class="button-overlay {"selected" if "28" in selected_teeth_numbers else ""}" data-index="28" style="top: 54%; left: 92%; width: 3%; height: 15%;" onclick="select_tooth(28)"></button>
                <!-- 잇몸 -->
                <button class="button-overlay {"selected" if "29" in selected_teeth_numbers else ""}" data-index="29" style="top: 0%; left: 0%; width: 100%; height: 40%;" onclick="select_tooth(29)"></button>
                <button class="button-overlay {"selected" if "30" in selected_teeth_numbers else ""}" data-index="30" style="top: 80%; left: 0%; width:100%; height: 20%;" onclick="select_tooth(30)"></button>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown('<h3 class="center-text">증상 발생 부분:</h3>', unsafe_allow_html=True)
    for tooth_number, tooth_name in zip(selected_teeth_numbers, selected_teeth):
       st.markdown(f'<div class="center-text">{int(tooth_number)}번: {tooth_name}</div>', unsafe_allow_html=True)

    # 증상 선택 옵션 제공
    st.markdown('<div class="center-text">증상에 대해 선택해주세요.</div>', unsafe_allow_html=True)
    symptom_options = [
    "통증",
    "시림",
    "출혈",
    "부기",
    "이가 흔들림",
    "기타"
    ]
    selected_symptom = st.selectbox("", symptom_options)
    additional_info = st.text_area("자세한 증상에 대해 설명해주세요.")

# 폼 생성
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
         col1, col2, col3 = st.columns([1, 1, 1])
         with col2:
           submit = st.button("진단")

# 버튼을 눌렀을 때 입력된 내용 처리
    if submit:
       st.markdown(f'<div class="center-text">선택한 증상: {selected_symptom}</div>', unsafe_allow_html=True)
       st.markdown(f'<div class="center-text">추가 설명: {additional_info}</div>', unsafe_allow_html=True)



        # Format the selected teeth into a string
        # teeth_info = "; ".join([f"{int(num)}번: {name}" for num, name in zip(selected_teeth_numbers, selected_teeth)])
        # # OpenAI API 호출 및 응답 출력
        # response = openai.ChatCompletion.create(
        #     model="gpt-3.5-turbo",
        #      messages=[
        #        {"role": "system", "content": f"이 사용자는 일반인이며 어려운 설명은 이해하기 어려울 수 있습니다. 현재 FirstAID라는 인공지능 api 사용 웹에서 치아 손상진단을 위해 접근하였습니다. 구체적으로 행동요령과 구급처치법을 설명해 주세요. 그리고 이 환자의 문제가 발생한 부분은 {teeth_info}이며 증상은 {selected_symptom}입니다. 구체적인 증상은 사용자가 입력한 텍스트를 확인하십시오. 또한 각 치아의 위치와 명칭별로 특화된 설명도 부여하십시오. 참고로 한글로 말해줘"},
        #        {"role": "user", "content": additional_info}
        #    ]
        # )
        # st.write(response.choices[0].message.content)

        # 추가 도움말 링크 제공
       st.markdown('<div class="center-text"><a href="https://www.youtube.com/watch?v=Zd5kz2Q0U6Q" target="_blank">치아 응급처치 방법</a></div>', unsafe_allow_html=True)
       st.markdown('<div class="center-text"><a href="https://www.youtube.com/watch?v=zlvJuN5Gyec" target="_blank">치아 건강 관리 팁</a></div>', unsafe_allow_html=True)

# 앱 실행 부분
if __name__ == "__main__":
    display_page5_2()
