import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Cấu hình trang web chuyên nghiệp
st.set_page_config(
    page_title="Duyên hải Miền Trung 2026 - to4lol.xyz",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Hệ thống CSS tùy chỉnh cho Giao diện Dark Mode
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        color: #ffffff !important;
    }
    
    .stApp {
        background-color: #000000 !important;
    }
    
    .main-title {
        font-size: 3.8rem;
        font-weight: 800;
        color: #ffffff;
        text-align: center;
        margin-bottom: 0.2rem;
        letter-spacing: -0.06em;
        line-height: 1.1;
        text-shadow: 0px 4px 10px rgba(255, 255, 255, 0.1);
    }
    
    .sub-title {
        font-size: 1.5rem;
        color: #38bdf8;
        text-align: center;
        margin-bottom: 3.5rem;
        font-weight: 500;
    }
    
    .card {
        padding: 2.5rem;
        border-radius: 1.5rem;
        background: #111827;
        box-shadow: 0 10px 30px -5px rgba(0, 0, 0, 0.5);
        border: 1px solid #1f2937;
        border-top: 8px solid #38bdf8;
        margin-bottom: 2rem;
        line-height: 1.8;
        color: #e5e7eb;
    }

    .card h3 {
        color: #38bdf8;
        margin-top: 0;
        font-weight: 800;
        font-size: 1.8rem;
        margin-bottom: 1rem;
    }
    
    .metric-card {
        background: #1f2937;
        padding: 1.5rem;
        border-radius: 1.25rem;
        text-align: center;
        border: 1px solid #374151;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.2);
        color: #ffffff;
    }
    
    .stImage > img {
        border-radius: 1.5rem !important;
        box-shadow: 0 0 25px rgba(56, 189, 248, 0.15) !important;
        height: 450px !important;
        object-fit: cover !important;
        border: 2px solid #374151;
        transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }
    
    .stImage > img:hover {
        transform: scale(1.02);
        border-color: #38bdf8;
    }

    .analysis-text {
        font-size: 1.05rem;
        color: #d1d5db;
        text-align: justify;
    }

    [data-testid="stSidebar"] {
        background-color: #0b0f1a !important;
        border-right: 1px solid #1f2937;
    }
    
    p, span, label, li {
        color: #ffffff !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://img.icons8.com/fluency/100/lighthouse.png", width=80)
    st.title("🌐 to4lol.xyz")
    st.markdown("---")
    app_mode = st.selectbox(
        "Lộ trình thuyết trình:",
        ["01. Tầm nhìn Chiến lược", 
         "02. Thế mạnh Tự nhiên & Vị thế", 
         "03. Xung lực Kinh tế 2026", 
         "04. Văn hóa & Kinh tế Di sản", 
         "05. Hạ tầng số & Kết nối thực", 
         "06. Cam kết Tương lai"]
    )
    st.markdown("---")
    st.info("💡 **Dự báo:** GRDP vùng dự kiến dẫn đầu cả nước giai đoạn 2026-2030.")
    st.caption("© 2026 Tổ 4 Research")

# --- NỘI DUNG ---

if app_mode == "01. Tầm nhìn Chiến lược":
    st.markdown('<p class="main-title">Duyên hải Miền Trung</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">Bản lĩnh vượt sóng - Khát vọng thịnh vượng 2026</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 2])
    with col1:
        st.markdown("""
        <div class="card">
        <h3>Khởi đầu một kỷ nguyên mới</h3>
        <p class="analysis-text">
        Bước vào năm 2026, Duyên hải Miền Trung không còn được nhắc đến như một dải đất "khó khăn, thiên tai". 
        Thay vào đó, đây là <b>"Hành lang kinh tế xanh"</b> đóng vai trò then chốt trong chiến lược tiến ra biển của Việt Nam. 
        Với sự dịch chuyển mạnh mẽ từ mô hình cũ sang kinh tế số, vùng đang chứng minh bản lĩnh của một trung tâm tăng trưởng mới.
        <br><br>
        Hệ thống dữ liệu tại <b>to4lol.xyz</b> làm rõ cách 14 tỉnh thành kết nối thành chuỗi giá trị thống nhất.
        </p>
        </div>
        """, unsafe_allow_html=True)
        
        m1, m2, m3 = st.columns(3)
        with m1:
            st.markdown('<div class="metric-card">🌊 <b>Kinh tế biển</b><br><span style="font-size:1.6rem; color:#38bdf8; font-weight:800;">55% GRDP</span></div>', unsafe_allow_html=True)
        with m2:
            st.markdown('<div class="metric-card">⚡ <b>Năng lượng sạch</b><br><span style="font-size:1.6rem; color:#38bdf8; font-weight:800;">~40% Toàn quốc</span></div>', unsafe_allow_html=True)
        with m3:
            st.markdown('<div class="metric-card">🏙️ <b>Đô thị hóa</b><br><span style="font-size:1.6rem; color:#38bdf8; font-weight:800;">48.5%</span></div>', unsafe_allow_html=True)
            
    with col2:
        st.image("https://images.unsplash.com/photo-1502602898657-3e91760cbb34?q=80&w=1000", caption="Cảnh quan đô thị hiện đại ven biển")

elif app_mode == "02. Thế mạnh Tự nhiên & Vị thế":
    st.markdown('<h3 style="color:white;">📍 Vị thế "Mặt tiền" & Tài nguyên Chiến lược</h3>', unsafe_allow_html=True)
    
    t1, t2 = st.tabs(["🌎 Vị trí Địa chính trị", "💎 Lợi thế Tự nhiên"])
    
    with t1:
        col1, col2 = st.columns([1, 1])
        with col1:
            st.markdown("""
            <div class="card">
            <h3>Tâm điểm kết nối khu vực</h3>
            <p class="analysis-text">
            Miền Trung sở hữu vị trí "độc bản" trên bản đồ Đông Nam Á:
            <ul>
                <li><b>Cửa ngõ EWEC:</b> Điểm cuối của hành lang kinh tế Đông - Tây kết nối Thái Bình Dương.</li>
                <li><b>Xương sống quốc gia:</b> Giao điểm huyết mạch của mọi tuyến đường sắt, bộ Bắc - Nam.</li>
                <li><b>Hậu cứ Tây Nguyên:</b> Là cửa ngõ xuất khẩu chính cho các mặt hàng nông sản giá trị cao.</li>
            </ul>
            </p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.image("https://images.unsplash.com/photo-1559592490-348633c74825?q=80&w=1000", caption="Bờ biển Nha Trang từ trên cao")

    with t2:
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown("""
            <div class="card">
            <h3>Địa hình & Cảng nước sâu</h3>
            <p class="analysis-text">
            Lợi thế tự nhiên hiếm có:
            <ul>
                <li><b>Vịnh thẳm:</b> Cam Ranh, Vân Phong đón tàu container hạng nặng không cần nạo vét nhiều.</li>
                <li><b>Bờ biển hẹp:</b> Tập trung hạ tầng logistics cực kỳ hiệu quả.</li>
            </ul>
            </p>
            </div>
            """, unsafe_allow_html=True)
        with col_b:
            st.markdown("""
            <div class="card">
            <h3>Năng lượng mặt trời & Gió</h3>
            <p class="analysis-text">
            Chuyển hóa cái nắng cái gió thành tiền:
            <ul>
                <li><b>Ninh Thuận - Bình Thuận:</b> Vùng bức xạ nhiệt cao nhất cả nước.</li>
                <li><b>Điện gió:</b> Các trang trại gió ngoài khơi lớn nhất khu vực.</li>
            </ul>
            </p>
            </div>
            """, unsafe_allow_html=True)

elif app_mode == "03. Xung lực Kinh tế 2026":
    st.markdown('<h3 style="color:white;">📈 Phân tích Chuyên sâu Kinh tế & FDI</h3>', unsafe_allow_html=True)
    
    df = pd.DataFrame({
        'Tỉnh/Thành': ['Thanh Hóa', 'Đà Nẵng', 'Quảng Ngãi', 'Khánh Hòa', 'Ninh Thuận'],
        'GRDP (%)': [9.4, 10.2, 8.5, 11.5, 9.8],
        'FDI (Tỷ USD)': [3.2, 2.8, 3.5, 2.5, 1.8]
    })
    
    c1, c2 = st.columns(2)
    with c1:
        fig1 = px.bar(df, x='Tỉnh/Thành', y='GRDP (%)', color='GRDP (%)', 
                     title="Tăng trưởng GRDP dự báo 2026", template="plotly_dark")
        st.plotly_chart(fig1, use_container_width=True)
    with c2:
        fig2 = px.pie(df, values='FDI (Tỷ USD)', names='Tỉnh/Thành', hole=.5,
                     title="Phân bổ dòng vốn đầu tư ngoại", template="plotly_dark")
        st.plotly_chart(fig2, use_container_width=True)

    st.markdown("""
    <div class="card">
    <b>Động lực mới:</b> Sự dịch chuyển đầu tư vào Chip bán dẫn (Đà Nẵng) và Lọc hóa dầu (Thanh Hóa, Quảng Ngãi) 
    đã thay đổi hoàn toàn diện mạo kinh tế vùng.
    </div>
    """, unsafe_allow_html=True)

elif app_mode == "04. Văn hóa & Kinh tế Di sản":
    st.markdown('<h3 style="color:white;">🏛️ Di sản Văn hóa - Tài sản Kinh tế bền vững</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("""
        <div class="card">
        <h3>Du lịch Thông minh & Xanh</h3>
        <ul>
            <li><b>Phố cổ Hội An:</b> Mô hình di sản không rác thải nhựa đầu tiên.</li>
            <li><b>Cố đô Huế:</b> Ứng dụng VR/AR tái hiện lịch sử cung đình.</li>
            <li><b>Hang động Quảng Bình:</b> Du lịch thám hiểm đẳng cấp thế giới.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.image("https://images.unsplash.com/photo-1599708153386-62bf3f0334ef?q=80&w=1000", caption="Nét đẹp Hội An cổ kính")

elif app_mode == "05. Hạ tầng số & Kết nối thực":
    st.markdown('<h3 style="color:white;">🛣️ Hạ tầng đồng bộ - Nền tảng thịnh vượng</h3>', unsafe_allow_html=True)
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("""
        <div class="card">
        <h3>Giao thông cao tốc</h3>
        <ul>
            <li><b>Cao tốc Bắc-Nam:</b> Kết nối thông suốt toàn dải miền Trung.</li>
            <li><b>Đường sắt ven biển:</b> Dự án chiến lược kết nối các khu kinh tế.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        st.image("https://images.unsplash.com/photo-1444312645910-ffa973656eba?q=80&w=1000", caption="Hệ thống cầu cảng hiện đại")

    with col_b:
        st.markdown("""
        <div class="card">
        <h3>Kinh tế Số & Logistics</h3>
        <ul>
            <li><b>Trạm cáp quang biển:</b> Đà Nẵng kết nối trực tiếp với Mỹ, Nhật.</li>
            <li><b>Logistics AI:</b> Tự động hóa kho bãi tại các cảng loại 1.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        st.image("https://images.unsplash.com/photo-1494412519320-aa613dfb7738?q=80&w=1000", caption="Vận chuyển hàng hóa quốc tế")

elif app_mode == "06. Cam kết Tương lai":
    st.markdown('<h3 style="color:white;">🏁 Kết luận & Tầm nhìn 2045</h3>', unsafe_allow_html=True)
    st.balloons()
    
    st.markdown("""
    <div class="card">
    <h3>Khát vọng Miền Trung</h3>
    Đến năm 2045, miền Trung sẽ là vùng kinh tế giàu mạnh, thích ứng linh hoạt với biến đổi khí hậu và là 
    trung tâm kinh tế biển của cả khu vực Đông Nam Á.
    <br><br>
    <i>to4lol.xyz đồng hành cùng sự phát triển bền vững của Tổ 4.</i>
    </div>
    """, unsafe_allow_html=True)
    
    c1, c2 = st.columns(2)
    with c1:
        st.image("https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?q=80&w=1000", caption="Kiến trúc xanh trong đô thị")
    with c2:
        st.image("https://images.unsplash.com/photo-1473116763249-2faaef81ccda?q=80&w=1000", caption="Bãi biển sạch và bảo tồn sinh thái")

st.markdown("<br><hr><center style='color:white;'><b>to4lol.xyz</b> | Tổ 4 Research | Hình ảnh đã được tối ưu 2026</center>", unsafe_allow_html=True)