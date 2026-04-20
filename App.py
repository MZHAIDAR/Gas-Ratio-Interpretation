import streamlit as st

st.set_page_config(page_title="Gas Ratio Software", layout="wide")


st.markdown("""
<h1 style='text-align: center; color: #1f77b4;'>
Gas Ratio Interpretation Software
</h1>
""", unsafe_allow_html=True)

st.markdown("---")

st.markdown(
    "<p style='font-size:22px; font-weight:bold;'>This software is designed for mud gas analysis and reservoir evaluation using:</p>",
    unsafe_allow_html=True
)
st.write("""

- Gas Ratio Triangular Plot  
- Gas Ratio Rectangular (Pixler) Plot  
- Hydrocarbon Ratio Analysis  
- Wetness, Balance and Character Interpretation  
""")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("📘 Theory Module")
    st.write("""
    - Detailed explanation of gas ratio methods  
    - Triangular and rectangular plot theory  
    - Hydrocarbon ratio interpretation  
    """)
    if st.button("📘 Go to Theory"):
        st.switch_page("pages/1_📘_Theory.py")

with col2:
    st.subheader("📊 Calculation Module")
    st.write("""
    - Input gas composition data  
    - Generate plots automatically  
    - Calculate ratios and interpretations  
    """)
    if st.button("📊 Go to Calculation"):
        st.switch_page("pages/2_📊_Calculation.py")

st.markdown("---")

st.subheader("🔄 Workflow")

st.write("""
1. Go to **Theory Page** to understand concepts  
2. Move to **Calculation Page**  
3. Input gas composition  
4. Analyze plots and results  
""")

st.markdown("""
<center>
Developed for Reservoir Engineering & Mud Logging Analysis
</center>
""", unsafe_allow_html=True)
