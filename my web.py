import streamlit as st

st.set_page_config(
    page_title="선택과목조사",
    page_icon='❤')

st.header('2023학년도 2학년 이과 선택과목 조사')

option = st.selectbox(
        '반을 선택해주세요',
        ('1반', '2반', '3반', '4반','5반','6반','7반','8반','9반'))

option = st.selectbox(
    '번호를 선택해주세요',
    ('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28')
)

st.write(''   )
st.write( ''  )
st.write( ''  )


수학과목 = st.radio(
        "수강하고 싶은 수학과목을 선택하세요.",
        ('수학1', '수학2', '미적분',))

if 수학과목 == '수학1':
        st.write('수학1을 선택하셨습니다.')
elif 수학과목 == '수학2':
        st.write("수학2을 선택하셨습니다.")
else:
        st.write('미적분을 선택하셨습니다.')

st.write(''   )
st.write( ''  )
st.write( ''  )

option = st.selectbox(
        '수강하고 싶은 과학과목을 선택하세요',
        ('물리학I', '화학I', '생명과학I', '지구과학I'))

st.write('선택한 과목을 확인하세요:', option)

st.write(''   )
st.write( ''  )
st.write( ''  )

if st.button('제출하기'):
    st.write('제출 되었습니다.')
else:
    st.write('반과 번호, 선택한 과목을 다시 한번 더 확인해주시길 바랍니다.')



