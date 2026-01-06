import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Cấu hình trang web chuyên nghiệp cho vùng Tây Nguyên
st.set_page_config(
    page_title="Tây Nguyên Đại Ngàn 2026 - to4lol.xyz",
    page_icon="⛰️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Hệ thống CSS tùy chỉnh cho Giao diện Dark Mode & Image Fix
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
        text-shadow: 0px 4px 15px rgba(234, 179, 8, 0.3);
    }
    
    .sub-title {
        font-size: 1.5rem;
        color: #fbbf24;
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
        border-top: 8px solid #fbbf24;
        margin-bottom: 2rem;
        line-height: 1.8;
        color: #e5e7eb;
    }

    .card h3 {
        color: #fbbf24;
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
    
    /* CSS FIX TRIỆT ĐỂ CHO ẢNH */
    .custom-img-container {
        width: 100%;
        height: 450px;
        overflow: hidden;
        border-radius: 1.5rem;
        border: 2px solid #374151;
        box-shadow: 0 0 25px rgba(234, 179, 8, 0.15);
        margin-bottom: 10px;
    }

    .custom-img-container img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        transition: transform 0.5s ease;
    }

    .custom-img-container img:hover {
        transform: scale(1.05);
    }

    .img-caption {
        text-align: center;
        color: #9ca3af;
        font-size: 0.9rem;
        margin-top: 5px;
        font-style: italic;
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

# Hàm Render ảnh chống vỡ (Sử dụng Fallback)
def render_image(url, caption):
    fallback_url = "https://images.unsplash.com/photo-1500673922987-e212871fec22?auto=format&fit=crop&w=1200&q=80"
    st.markdown(f"""
        <div class="custom-img-container">
            <img src="{url}" onerror="this.src='{fallback_url}'" alt="{caption}">
        </div>
        <p class="img-caption">{caption}</p>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://img.icons8.com/fluency/100/mountain.png", width=80)
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
    st.info("💡 **Dự báo:** Tây Nguyên hướng tới mục tiêu trở thành trung tâm kinh tế xanh bền vững năm 2030.")
    st.caption("© 2026 Tổ 4 Research")

# --- NỘI DUNG ---

if app_mode == "01. Tầm nhìn Chiến lược":
    st.markdown('<p class="main-title">Tây Nguyên Đại Ngàn</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">Khát vọng Xanh - Vươn tầm Cao nguyên 2026</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 2])
    with col1:
        st.markdown("""
        <div class="card">
        <h3>Kỷ nguyên Nông nghiệp Công nghệ cao</h3>
        <p class="analysis-text">
        Bước vào năm 2026, Tây Nguyên không chỉ là "vùng đất đỏ" của cà phê và hồ tiêu. 
        Thay vào đó, nơi đây đang chuyển mình mạnh mẽ thành <b>"Trung tâm Năng lượng sạch và Nông nghiệp bền vững"</b> của cả nước. 
        Với sự phát triển của hạ tầng cao tốc, Tây Nguyên đang phá bỏ thế "ngõ cụt" để trở thành cửa ngõ quan trọng trong tam giác phát triển Việt Nam - Lào - Campuchia.
        <br><br>
        Hệ thống dữ liệu tại <b>to4lol.xyz</b> phân tích chiến lược phát triển 5 tỉnh Cao nguyên đồng bộ.
        </p>
        </div>
        """, unsafe_allow_html=True)
        
        m1, m2, m3 = st.columns(3)
        with m1:
            st.markdown('<div class="metric-card">☕ <b>Nông nghiệp</b><br><span style="font-size:1.6rem; color:#fbbf24; font-weight:800;">45% GRDP</span></div>', unsafe_allow_html=True)
        with m2:
            st.markdown('<div class="metric-card">☀️ <b>Năng lượng tái tạo</b><br><span style="font-size:1.6rem; color:#fbbf24; font-weight:800;">~35% Tiềm năng</span></div>', unsafe_allow_html=True)
        with m3:
            st.markdown('<div class="metric-card">🏔️ <b>Độ che phủ rừng</b><br><span style="font-size:1.6rem; color:#fbbf24; font-weight:800;">46.2%</span></div>', unsafe_allow_html=True)
            
    with col2:
        render_image("https://images.unsplash.com/photo-1582201943021-e8e5b2612303?auto=format&fit=crop&w=1000&q=80", "Đồi chè và núi rừng Tây Nguyên")

elif app_mode == "02. Thế mạnh Tự nhiên & Vị thế":
    st.markdown('<h3 style="color:white;">📍 Vị thế Chiến lược & Tài nguyên Đất đỏ</h3>', unsafe_allow_html=True)
    
    t1, t2 = st.tabs(["🌎 Vị trí Địa chính trị", "💎 Lợi thế Tự nhiên"])
    
    with t1:
        col1, col2 = st.columns([1, 1])
        with col1:
            st.markdown("""
            <div class="card">
            <h3>Tâm điểm "Ngã ba Đông Dương"</h3>
            <p class="analysis-text">
            Tây Nguyên sở hữu vị trí chiến lược cực kỳ quan trọng về an ninh và kinh tế:
            <ul>
                <li><b>Giao điểm quốc tế:</b> Kết nối hành lang kinh tế Đông - Tây từ biển ra vùng hạ lưu sông Mê Kông.</li>
                <li><b>An ninh quốc phòng:</b> Là "mái nhà" của Đông Dương, giữ vai trò lá chắn sinh thái cho khu vực phía Nam.</li>
                <li><b>Kết nối liên vùng:</b> Cầu nối quan trọng giữa các cảng biển miền Trung với thị trường Đông Bắc Campuchia và Nam Lào.</li>
            </ul>
            </p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            render_image("https://images.unsplash.com/photo-1543160732-2d15ab462bf4?auto=format&fit=crop&w=1000&q=80", "Thác nước hùng vĩ tại Đắk Lắk")

    with t2:
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown("""
            <div class="card">
            <h3>Đất đỏ Bazan & Thủy văn</h3>
            <p class="analysis-text">
            Lợi thế đặc trưng của vùng cao nguyên:
            <ul>
                <li><b>Đất đỏ cực kỳ màu mỡ:</b> Phù hợp với các loại cây công nghiệp lâu năm giá trị xuất khẩu tỷ đô.</li>
                <li><b>Địa hình bậc thang:</b> Tạo ra hệ thống thác nước lý tưởng cho phát triển thủy điện và du lịch sinh thái.</li>
            </ul>
            </p>
            </div>
            """, unsafe_allow_html=True)
        with col_b:
            st.markdown("""
            <div class="card">
            <h3>Khí hậu ôn hòa & Cảnh quan</h3>
            <p class="analysis-text">
            <ul>
                <li><b>Đà Lạt & Măng Đen:</b> Những trung tâm nghỉ dưỡng đẳng cấp với khí hậu cận ôn đới giữa lòng nhiệt đới.</li>
                <li><b>Đa dạng sinh học:</b> Hệ thống các vườn quốc gia lớn nhất cả nước (Chư Mom Ray, Yok Đôn).</li>
            </ul>
            </p>
            </div>
            """, unsafe_allow_html=True)

elif app_mode == "03. Xung lực Kinh tế 2026":
    st.markdown('<h3 style="color:white;">📈 Phân tích Tăng trưởng & Xuất khẩu Nông sản</h3>', unsafe_allow_html=True)
    
    df = pd.DataFrame({
        'Tỉnh': ['Đắk Lắk', 'Lâm Đồng', 'Gia Lai', 'Kon Tum', 'Đắk Nông'],
        'GRDP (%)': [8.8, 9.5, 8.2, 7.9, 8.4],
        'Xuất khẩu (Tỷ USD)': [1.6, 1.2, 0.9, 0.5, 0.7]
    })
    
    c1, c2 = st.columns(2)
    with c1:
        fig1 = px.bar(df, x='Tỉnh', y='GRDP (%)', color='GRDP (%)', 
                     title="Tăng trưởng GRDP dự báo 2026", color_continuous_scale='YlOrBr', template="plotly_dark")
        st.plotly_chart(fig1, use_container_width=True)
    with c2:
        fig2 = px.pie(df, values='Xuất khẩu (Tỷ USD)', names='Tỉnh', hole=.5,
                     title="Cơ cấu xuất khẩu nông sản 2026", template="plotly_dark")
        st.plotly_chart(fig2, use_container_width=True)

    st.markdown("""
    <div class="card">
    <b>Động lực mới:</b> Việc khánh thành tuyến cao tốc Buôn Ma Thuột - Khánh Hòa và Dầu Giây - Liên Khương đã giúp 
    giảm chi phí logistics nông sản Tây Nguyên xuống 15%, tăng sức cạnh tranh toàn cầu.
    </div>
    """, unsafe_allow_html=True)

elif app_mode == "04. Văn hóa & Kinh tế Di sản":
    st.markdown('<h3 style="color:white;">🥁 Văn hóa Cồng chiêng - Di sản phi vật thể nhân loại</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("""
        <div class="card">
        <h3>Kinh tế Di sản & Du lịch Cộng đồng</h3>
        <ul>
            <li><b>Không gian Cồng chiêng:</b> Trở thành sản phẩm du lịch văn hóa đặc sắc hút khách quốc tế.</li>
            <li><b>Bảo tàng Cà phê:</b> Buôn Ma Thuột định vị là "Thành phố cà phê thế giới".</li>
            <li><b>Làng nghề truyền thống:</b> Phục hồi dệt thổ cẩm và đan lát gắn với thương mại điện tử.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        render_image("https://images.unsplash.com/photo-1541432901042-2d8bd64b4a9b?auto=format&fit=crop&w=1000&q=80", "Vườn cà phê vào mùa thu hoạch")

elif app_mode == "05. Hạ tầng số & Kết nối thực":
    st.markdown('<h3 style="color:white;">🛣️ Mở đường lên Cao nguyên - Kết nối hạ tầng</h3>', unsafe_allow_html=True)
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("""
        <div class="card">
        <h3>Mạng lưới Cao tốc</h3>
        <ul>
            <li><b>Cao tốc Đông - Tây:</b> Phá thế độc đạo của Quốc lộ 14 và Quốc lộ 19.</li>
            <li><b>Sân bay quốc tế:</b> Nâng cấp Liên Khương và Pleiku đón các chuyến bay thẳng quốc tế.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        render_image("https://images.unsplash.com/photo-1500382017468-9049fed747ef?auto=format&fit=crop&w=1000&q=80", "Những cung đường xuyên rừng hùng vĩ")

    with col_b:
        st.markdown("""
        <div class="card">
        <h3>Hạ tầng số Nông nghiệp</h3>
        <ul>
            <li><b>Nông nghiệp chính xác:</b> Ứng dụng IoT và cảm biến trong quản lý vườn cây.</li>
            <li><b>Truy xuất nguồn gốc:</b> 100% cà phê xuất khẩu được định danh vùng trồng số.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        render_image("https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=1000&q=80", "Mô hình nông nghiệp hiện đại")

elif app_mode == "06. Cam kết Tương lai":
    st.markdown('<h3 style="color:white;">🏁 Kết luận & Tầm nhìn Tây Nguyên Xanh 2045</h3>', unsafe_allow_html=True)
    st.balloons()
    
    st.markdown("""
    <div class="card">
    <h3>Tầm nhìn Bền vững</h3>
    Tây Nguyên 2045 sẽ là vùng kinh tế xanh bền vững, nơi bản sắc văn hóa dân tộc được gìn giữ song hành cùng 
    sự hiện đại hóa nông nghiệp và dịch vụ nghỉ dưỡng cao cấp.
    <br><br>
    <i>to4lol.xyz tự hào phân tích tiềm năng đất rừng Cao nguyên.</i>
    </div>
    """, unsafe_allow_html=True)
    
    c1, c2 = st.columns(2)
    with c1:
        render_image("https://images.unsplash.com/photo-1596395819057-e37f55a8519a?auto=format&fit=crop&w=1000&q=80", "Hồ T'Nưng Gia Lai - Đôi mắt Pleiku")
    with c2:
        render_image("https://images.unsplash.com/photo-1447752875215-b2761acb3c5d?auto=format&fit=crop&w=1000&q=80", "Bình minh trên cao nguyên")

st.markdown("<br><hr><center style='color:white;'><b>to4lol.xyz</b> | Tổ 4 Research | Dữ liệu Tây Nguyên 2026</center>", unsafe_allow_html=True)