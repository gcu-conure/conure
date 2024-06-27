import streamlit as st
import base64

def display_page5():
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

    st.markdown('<h1 class="center-text">치아 구조도 선택</h1>', unsafe_allow_html=True)
    st.markdown('<div class="center-text">아픈 부위를 선택해주세요</div>', unsafe_allow_html=True)

    teeth_names = [
        '왼쪽 위 제 2대구치', '왼쪽 위 제 1대구치', '왼쪽 위 제 2소구치', '왼쪽 위 제 1소구치',
        '왼쪽 위 송곳니', '왼쪽 위 측절치', '왼쪽 위 중절치', '오른쪽 위 중절치',
        '오른쪽 위 측절치', '오른쪽 위 송곳니', '오른쪽 위 제 1소구치', '오른쪽 위 제 2소구치',
        '오른쪽 위 제 1대구치', '오른쪽 위 제 2대구치', '왼쪽 아래 제 2대구치',
        '왼쪽 아래 제 1대구치', '왼쪽 아래 제 2소구치', '왼쪽 아래 제 1소구치',
        '왼쪽 아래 송곳니', '왼쪽 아래 측절치', '왼쪽 아래 중절치', '오른쪽 아래 중절치',
        '오른쪽 아래 측절치', '오른쪽 아래 송곳니', '오른쪽 아래 제 1소구치',
        '오른쪽 아래 제 2소구치', '오른쪽 아래 제 1대구치', '오른쪽 아래 제 2대구치',
        '윗 잇몸', '아래 잇몸'
    ]

    if 'selected_teeth' not in st.session_state:
        st.session_state.selected_teeth = []
    if 'selected_teeth_numbers' not in st.session_state:
        st.session_state.selected_teeth_numbers = []

    if 'tooth_input_count' not in st.session_state:
        st.session_state.tooth_input_count = 1

    # 이미지 파일을 읽어 Base64 인코딩
    with open("./assets/teeth.jpg", "rb") as f:
        img_bytes = f.read()
        img_base64 = base64.b64encode(img_bytes).decode()

    # CSS 스타일 정의 및 이미지 렌더링
    st.markdown(f"""
        <div class="center-img-container">
            <div class="teeth-container">
                <div class="label-left">L</div>
                <img src="data:image/jpeg;base64,{img_base64}">
                <div class="label-right">R</div>
                <!-- 윗니 -->
                <button class="button-overlay {"selected" if "1" in st.session_state.selected_teeth_numbers  else ""}" data-index="1" style="top: 33%; left: 3%; width: 4.5%; height: 15%;" onclick="select_tooth(1)"></button>
                <button class="button-overlay {"selected" if "2" in st.session_state.selected_teeth_numbers  else ""}" data-index="2" style="top: 33%; left: 6%; width: 5%; height: 17%;" onclick="select_tooth(2)"></button>
                <button class="button-overlay {"selected" if "3" in st.session_state.selected_teeth_numbers  else ""}" data-index="3" style="top: 33%; left: 11%; width: 5%; height: 20%;" onclick="select_tooth(3)"></button>
                <button class="button-overlay {"selected" if "4" in st.session_state.selected_teeth_numbers  else ""}" data-index="4" style="top: 33%; left: 17%; width: 6%; height: 22%;" onclick="select_tooth(4)"></button>
                <button class="button-overlay {"selected" if "5" in st.session_state.selected_teeth_numbers  else ""}" data-index="5" style="top: 33%; left: 24.5%; width: 6%; height: 22%;" onclick="select_tooth(5)"></button>
                <button class="button-overlay {"selected" if "6" in st.session_state.selected_teeth_numbers  else ""}" data-index="6" style="top: 33%; left: 32%; width: 7%; height: 21%;" onclick="select_tooth(6)"></button>
                <button class="button-overlay {"selected" if "7" in st.session_state.selected_teeth_numbers  else ""}" data-index="7" style="top: 33%; left: 41%; width: 8%; height: 21%;" onclick="select_tooth(7)"></button>
                <button class="button-overlay {"selected" if "8" in st.session_state.selected_teeth_numbers  else ""}" data-index="8" style="top: 33%; left: 50%; width: 8.8%; height: 21%;" onclick="select_tooth(8)"></button>
                <button class="button-overlay {"selected" if "9" in st.session_state.selected_teeth_numbers  else ""}" data-index="9" style="top: 33%; left: 61%; width: 7%; height: 21%;" onclick="select_tooth(9)"></button>
                <button class="button-overlay {"selected" if "10" in st.session_state.selected_teeth_numbers  else ""}" data-index="10" style="top: 33%; left: 68%; width: 7%; height: 22%;" onclick="select_tooth(10)"></button>
                <button class="button-overlay {"selected" if "11" in st.session_state.selected_teeth_numbers  else ""}" data-index="11" style="top: 33%; left: 75.5%; width: 7%; height: 22%;" onclick="select_tooth(11)"></button>
                <button class="button-overlay {"selected" if "12" in st.session_state.selected_teeth_numbers  else ""}" data-index="12" style="top: 33%; left: 82.7%; width: 6%; height: 21%;" onclick="select_tooth(12)"></button>
                <button class="button-overlay {"selected" if "13" in st.session_state.selected_teeth_numbers  else ""}" data-index="13" style="top: 33%; left: 87.5%; width: 5%; height: 17%;" onclick="select_tooth(13)"></button>
                <button class="button-overlay {"selected" if "14" in st.session_state.selected_teeth_numbers  else ""}" data-index="14" style="top: 33%; left: 91%; width: 5%; height: 15%;" onclick="select_tooth(14)"></button>
                <!-- 아랫니 -->
                <button class="button-overlay {"selected" if "15" in st.session_state.selected_teeth_numbers  else ""}" data-index="15" style="top: 54%; left: 5%; width: 3%; height: 15%;" onclick="select_tooth(15)"></button>
                <button class="button-overlay {"selected" if "16" in st.session_state.selected_teeth_numbers  else ""}" data-index="16" style="top: 56%; left: 8%; width: 3.5%; height: 18%;" onclick="select_tooth(16)"></button>
                <button class="button-overlay {"selected" if "17" in st.session_state.selected_teeth_numbers  else ""}" data-index="17" style="top: 57%; left: 12%; width: 5.5%; height: 20%;" onclick="select_tooth(17)"></button>
                <button class="button-overlay {"selected" if "18" in st.session_state.selected_teeth_numbers  else ""}" data-index="18" style="top: 57%; left: 19%; width: 5%; height: 22%;" onclick="select_tooth(18)"></button>
                <button class="button-overlay {"selected" if "19" in st.session_state.selected_teeth_numbers  else ""}" data-index="19" style="top: 57%; left: 26%; width: 6%; height: 22%;" onclick="select_tooth(19)"></button>
                <button class="button-overlay {"selected" if "20" in st.session_state.selected_teeth_numbers  else ""}" data-index="20" style="top: 57%; left: 34.5%; width: 6.5%; height: 21%;" onclick="select_tooth(20)"></button>
                <button class="button-overlay {"selected" if "21" in st.session_state.selected_teeth_numbers  else ""}" data-index="21" style="top: 57%; left: 41.5%; width: 8%; height: 21%;" onclick="select_tooth(21)"></button>
                <button class="button-overlay {"selected" if "22" in st.session_state.selected_teeth_numbers  else ""}" data-index="22" style="top: 57%; left: 50%; width: 8%; height: 21%;" onclick="select_tooth(22)"></button>
                <button class="button-overlay {"selected" if "23" in st.session_state.selected_teeth_numbers  else ""}" data-index="23" style="top: 57%; left: 58.8%; width: 6.5%; height: 21%;" onclick="select_tooth(23)"></button>
                <button class="button-overlay {"selected" if "24" in st.session_state.selected_teeth_numbers  else ""}" data-index="24" style="top: 57%; left: 67%; width: 7%; height: 22%;" onclick="select_tooth(24)"></button>
                <button class="button-overlay {"selected" if "25" in st.session_state.selected_teeth_numbers  else ""}" data-index="25" style="top: 57%; left: 75%; width: 6.5%; height: 22%;" onclick="select_tooth(25)"></button>
                <button class="button-overlay {"selected" if "26" in st.session_state.selected_teeth_numbers  else ""}" data-index="26" style="top: 57%; left: 81.5%; width: 6%; height: 21%;" onclick="select_tooth(26)"></button>
                <button class="button-overlay {"selected" if "27" in st.session_state.selected_teeth_numbers  else ""}" data-index="27" style="top: 55%; left: 88%; width: 4%; height: 19%;" onclick="select_tooth(27)"></button>
                <button class="button-overlay {"selected" if "28" in st.session_state.selected_teeth_numbers  else ""}" data-index="28" style="top: 54%; left: 92%; width: 3%; height: 15%;" onclick="select_tooth(28)"></button>
                <!-- 잇몸 -->
                <button class="button-overlay {"selected" if "29" in st.session_state.selected_teeth_numbers  else ""}" data-index="29" style="top: 0%; left: 0%; width: 100%; height: 40%;" onclick="select_tooth(29)"></button>
                <button class="button-overlay {"selected" if "30" in st.session_state.selected_teeth_numbers  else ""}" data-index="30" style="top: 80%; left: 0%; width:100%; height: 20%;" onclick="select_tooth(30)"></button>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # 이빨 선택 폼
    with st.form(key='tooth_form'):
        col1, col2, col3 = st.columns([0.35, 1, 0.35])
        with col2:
            col1, col2, col3 = st.columns([0.4, 1, 0.4])
            with col2:
                tooth_numbers = []
                for i in range(st.session_state.tooth_input_count):
                    tooth_number = st.text_input(f"선택한 치아 번호를 입력하세요 (치아 {i+1}):", key=f"tooth_number_{i}")
                    tooth_numbers.append(tooth_number)
            col1, col2, col3 = st.columns([1.2, 1, 1])
            with col2:
                submit = st.form_submit_button("치아 선택")

    if st.button("치아 추가(클릭 후 치아 선택 버튼을 누르면 추가 입력할 수 있습니다!)"):
        st.session_state.tooth_input_count += 1

    if submit:
        selected_teeth_names = []
        for tooth_number in tooth_numbers:
            if tooth_number.isdigit() and 1 <= int(tooth_number) <= 30:
                selected_teeth_names.append(teeth_names[int(tooth_number) - 1])
            else:
                st.error("유효한 치아 번호를 입력하세요. (1-30)")
                return

        st.session_state.selected_teeth = selected_teeth_names
        st.session_state.selected_teeth_numbers = tooth_numbers

        st.markdown(f'<div class="center-text">선택된 치아:</div>', unsafe_allow_html=True)
        for tooth_number, tooth_name in zip(tooth_numbers, selected_teeth_names):
            st.markdown(f'<div class="center-text">{int(tooth_number)}번은 {tooth_name}입니다.</div>', unsafe_allow_html=True)
        st.markdown('<div class="center-text">손상이 의심되는 부위가 맞으면 확인 버튼을 눌러주세요!</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1.68, 1, 1])
    with col2:
        # 선택된 치아 이름 표시 및 확인 버튼
        if st.session_state.selected_teeth:
            if st.button("확인"):
                st.session_state.step = 52  # 다음 페이지로 이동하기 위해 step 값을 설정
                st.experimental_rerun()  # 페이지를 리프레시하여 step 값을 반영

# 앱 실행 부분
if __name__ == "__main__":
    display_page5()
