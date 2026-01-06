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

# Hệ thống CSS tùy chỉnh tối ưu cho bài thuyết trình
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    .stApp {
        background: linear-gradient(180deg, #f0f7ff 0%, #ffffff 100%);
    }
    
    .main-title {
        font-size: 3.8rem;
        font-weight: 800;
        color: #0c4a6e;
        text-align: center;
        margin-bottom: 0.2rem;
        letter-spacing: -0.06em;
        line-height: 1.1;
    }
    
    .sub-title {
        font-size: 1.5rem;
        color: #0284c7;
        text-align: center;
        margin-bottom: 3.5rem;
        font-weight: 500;
    }
    
    .card {
        padding: 2.5rem;
        border-radius: 1.5rem;
        background: white;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.05);
        border: 1px solid #e0f2fe;
        border-top: 8px solid #0ea5e9;
        margin-bottom: 2rem;
        line-height: 1.8;
    }

    .card h3 {
        color: #075985;
        margin-top: 0;
        font-weight: 800;
        font-size: 1.8rem;
        margin-bottom: 1rem;
    }
    
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 1.25rem;
        text-align: center;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);
    }
    
    .stImage > img {
        border-radius: 1.5rem !important;
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1) !important;
        height: 400px !important;
        object-fit: cover !important;
        border: 4px solid white;
    }

    .analysis-text {
        font-size: 1.05rem;
        color: #334155;
        text-align: justify;
    }

    .highlight {
        color: #0284c7;
        font-weight: 700;
    }

    .tab-content {
        padding: 1.5rem 0;
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
    st.caption("Sản phẩm của Nhóm Nghiên cứu Tổ 4")

# --- HÀM HIỂN THỊ ẢNH ---
def safe_image(url, cap):
    st.image(url, caption=cap, use_container_width=True)

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
        Với sự dịch chuyển mạnh mẽ từ nông nghiệp truyền thống sang dịch vụ logistics cao cấp và sản xuất công nghệ, 
        vùng đang chứng minh bản lĩnh của một "con rồng mới" đang trỗi dậy.
        <br><br>
        Hệ thống dữ liệu tại <b>to4lol.xyz</b> sẽ làm rõ cách mà 14 tỉnh thành kết nối thành một chuỗi giá trị thống nhất, 
        tạo ra sức mạnh cộng hưởng chưa từng có trong lịch sử phát triển vùng.
        </p>
        </div>
        """, unsafe_allow_html=True)
        
        m1, m2, m3 = st.columns(3)
        with m1:
            st.markdown('<div class="metric-card">🌊 <b>Kinh tế biển</b><br><span style="font-size:1.6rem; color:#0284c7; font-weight:800;">55% GRDP</span></div>', unsafe_allow_html=True)
        with m2:
            st.markdown('<div class="metric-card">⚡ <b>Năng lượng sạch</b><br><span style="font-size:1.6rem; color:#0284c7; font-weight:800;">~40% Toàn quốc</span></div>', unsafe_allow_html=True)
        with m3:
            st.markdown('<div class="metric-card">🏙️ <b>Đô thị hóa</b><br><span style="font-size:1.6rem; color:#0284c7; font-weight:800;">48.5%</span></div>', unsafe_allow_html=True)
            
    with col2:
        safe_image("https://images.unsplash.com/photo-1596422846543-75c6fc18a594?q=80&w=1000", "Tầm nhìn đô thị ven biển hiện đại 2026")

elif app_mode == "02. Thế mạnh Tự nhiên & Vị thế":
    st.markdown('<h3>📍 Vị thế "Mặt tiền" & Tài nguyên Chiến lược</h3>', unsafe_allow_html=True)
    
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
                <li><b>Hành lang EWEC:</b> Là cửa ngõ ngắn nhất nối liền Ấn Độ Dương và Thái Bình Dương thông qua Myanmar, Thái Lan và Lào.</li>
                <li><b>Trục xương sống quốc gia:</b> Điểm giao thoa bắt buộc của mọi tuyến vận tải Bắc - Nam, đóng vai trò "trạm trung chuyển" khổng lồ cho nền kinh tế Việt Nam.</li>
                <li><b>Vùng đệm chiến lược:</b> Bảo đảm an ninh quốc phòng biển đảo, đồng thời là hậu cứ vững chắc cho sự phát triển của vùng Tây Nguyên.</li>
            </ul>
            </p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            safe_image("https://images.unsplash.com/photo-1528127269322-539801943592?q=80&w=1000", "Sự giao thoa hùng vĩ giữa núi và biển")

    with t2:
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown("""
            <div class="card">
            <h3>Địa hình "Sâu & Dốc" - Một nghịch lý lợi thế</h3>
            <p class="analysis-text">
            Khác với đồng bằng, địa hình miền Trung tạo ra những giá trị đặc biệt:
            <ul>
                <li><b>Hệ thống vịnh nước sâu:</b> Các vịnh như Cam Ranh, Vân Phong có độ sâu tự nhiên lý tưởng cho tàu siêu trọng, điều mà các vùng khác phải tốn hàng tỷ USD nạo vét mới có được.</li>
                <li><b>Độ dốc thủy văn:</b> Tạo tiềm năng thủy điện tích năng và hệ thống cung cấp nước ngọt ổn định cho các khu công nghiệp ven biển.</li>
            </ul>
            </p>
            </div>
            """, unsafe_allow_html=True)
        with col_b:
            st.markdown("""
            <div class="card">
            <h3>Trung tâm Năng lượng tái tạo</h3>
            <p class="analysis-text">
            Khí hậu khắc nghiệt (nắng gắt, gió mạnh) đã được chuyển hóa thành nguồn lực kinh tế:
            <ul>
                <li><b>Bức xạ nhiệt:</b> Ninh Thuận và Bình Thuận trở thành "thủ phủ" điện mặt trời của Đông Nam Á.</li>
                <li><b>Điện gió ngoài khơi:</b> Vùng biển từ Bình Định đến Ninh Thuận có vận tốc gió trung bình lý tưởng nhất để phát triển điện gió quy mô lớn, hướng tới xuất khẩu điện sạch sang Singapore và khu vực.</li>
            </ul>
            </p>
            </div>
            """, unsafe_allow_html=True)

elif app_mode == "03. Xung lực Kinh tế 2026":
    st.markdown('<h3>📈 Phân tích Chuyên sâu Kinh tế & FDI</h3>', unsafe_allow_html=True)
    
    st.write("Dòng vốn đầu tư vào Miền Trung năm 2026 cho thấy sự dịch chuyển từ 'số lượng' sang 'chất lượng' với tiêu chuẩn ESG (Môi trường - Xã hội - Quản trị).")

    df = pd.DataFrame({
        'Tỉnh/Thành': ['Thanh Hóa', 'Đà Nẵng', 'Quảng Ngãi', 'Khánh Hòa', 'Ninh Thuận'],
        'GRDP (%)': [9.4, 10.2, 8.5, 11.5, 9.8],
        'FDI (Tỷ USD)': [3.2, 2.8, 3.5, 2.5, 1.8],
        'Trọng tâm': ['Hóa dầu', 'Chip bán dẫn', 'Gang thép xanh', 'Logistics biển', 'Năng lượng Hydrogen']
    })
    
    c1, c2 = st.columns(2)
    with c1:
        fig1 = px.bar(df, x='Tỉnh/Thành', y='GRDP (%)', color='GRDP (%)', text='Trọng tâm',
                     title="Tốc độ tăng trưởng và Mũi nhọn kinh tế", color_continuous_scale='Blues')
        st.plotly_chart(fig1, use_container_width=True)
    with c2:
        fig2 = px.pie(df, values='FDI (Tỷ USD)', names='Tỉnh/Thành', hole=.5,
                     title="Cơ cấu thu hút vốn FDI toàn vùng")
        st.plotly_chart(fig2, use_container_width=True)

    st.markdown("""
    <div class="card">
    <b>Lập luận kinh tế:</b> Sự xuất hiện của các nhà máy sản xuất bán dẫn tại Đà Nẵng và trung tâm Hydro xanh tại Ninh Thuận 
    đã chính thức đưa Miền Trung vào chuỗi cung ứng công nghệ toàn cầu. Đây là bước đi logic để thoát khỏi bẫy thu nhập trung bình 
    và tận dụng tối đa nguồn nhân lực trẻ tại địa phương.
    </div>
    """, unsafe_allow_html=True)

elif app_mode == "04. Văn hóa & Kinh tế Di sản":
    st.markdown('<h3>🏛️ Di sản Văn hóa - Tài sản Kinh tế bền vững</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("""
        <div class="card">
        <h3>Từ bảo tồn đến khai thác giá trị</h3>
        <p class="analysis-text">
        Năm 2026, du lịch miền Trung thực hiện cuộc cách mạng về mô hình:
        <ul>
            <li><b>Kinh tế đêm:</b> Phố cổ Hội An và Cố đô Huế trở thành các trung tâm trình diễn ánh sáng và nghệ thuật số hóa, kéo dài thời gian lưu trú và chi tiêu của khách quốc tế.</li>
            <li><b>Di sản số:</b> Ứng dụng Blockchain để định danh và bảo tồn các cổ vật, giúp khách du lịch tương tác với lịch sử thông qua không gian ảo trước khi đến tham quan thực tế.</li>
            <li><b>Du lịch xanh:</b> Các tour thám hiểm hang động Quảng Bình cam kết Net Zero, tạo ra chuẩn mực mới cho du lịch bền vững.</li>
        </ul>
        </p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        safe_image("https://images.unsplash.com/photo-1583417319070-4a69db38a482?q=80&w=1000", "Huế - Sự kết hợp giữa cổ kính và công nghệ ánh sáng")

    st.subheader("Hệ sinh thái du lịch đa tầng")
    cols = st.columns(3)
    imgs = [
        "https://images.unsplash.com/photo-1610448721566-47369c768e70?q=80&w=600",
        "https://images.unsplash.com/photo-1559592490-348633c74825?q=80&w=600",
        "https://images.unsplash.com/photo-1590001158193-7903d24d326e?q=80&w=600"
    ]
    lbls = ["Hội An: Kinh tế sáng tạo", "Nha Trang: Nghỉ dưỡng cao cấp", "Sơn Trà: Bảo tồn sinh thái"]
    for i, img in enumerate(imgs):
        cols[i].image(img, caption=lbls[i], use_container_width=True)

elif app_mode == "05. Hạ tầng số & Kết nối thực":
    st.markdown('<h3>🛣️ Hạ tầng đồng bộ - Nền tảng của sự thịnh vượng</h3>', unsafe_allow_html=True)
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("""
        <div class="card">
        <h3>Mạng lưới giao thông thông minh</h3>
        <ul>
            <li><b>Cao tốc ven biển:</b> Tuyến đường không chỉ kết nối các tỉnh mà còn mở ra không gian phát triển đô thị mới, biến miền Trung thành một "đô thị dải" thống nhất.</li>
            <li><b>Cảng biển 4.0:</b> Cảng Đà Nẵng và Quy Nhơn vận hành tự động hóa bằng AI, tối ưu hóa thời gian bốc dỡ hàng hóa tăng 30%.</li>
            <li><b>Sân bay quốc tế:</b> Sự mở rộng của Cam Ranh và Đà Nẵng giúp miền Trung kết nối trực tiếp với 50+ thành phố lớn trên thế giới.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        safe_image("https://images.unsplash.com/photo-1545143333-6382b1e58473?q=80&w=1000", "Hệ thống giao thông xương sống ven biển")

    with col_b:
        st.markdown("""
        <div class="card">
        <h3>Hạ tầng số & Logistics</h3>
        <ul>
            <li><b>Trung tâm dữ liệu (Data Center):</b> Đà Nẵng trở thành trạm cập bờ của các tuyến cáp quang biển quốc tế mới, thu hút các ông lớn công nghệ toàn cầu.</li>
            <li><b>Logistics đa phương thức:</b> Kết nối thông suốt Đường bộ - Đường biển - Đường hàng không, giúp giảm chi phí logistics từ 18% xuống còn 12% GRDP vào năm 2026.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        safe_image("https://images.unsplash.com/photo-1494412519320-aa613dfb7738?q=80&w=1000", "Logistics hiện đại - Cửa ngõ ra thế giới")

elif app_mode == "06. Cam kết Tương lai":
    st.markdown('<h3>🏁 Kết luận & Tầm nhìn Net Zero 2045</h3>', unsafe_allow_html=True)
    st.balloons()
    
    st.markdown("""
    <div class="card">
    <h3>Thông điệp gửi tới tương lai</h3>
    <p class="analysis-text">
    Duyên hải Miền Trung 2026 là minh chứng cho sự chuyển mình mạnh mẽ của Việt Nam. Chúng ta không chỉ xây dựng kinh tế, 
    chúng ta đang xây dựng một <b>tương lai bền vững</b>. Bài thuyết trình của Tổ 4 thông qua <b>to4lol.xyz</b> hy vọng đã mang 
    đến cho quý vị cái nhìn sắc nét về một vùng đất đang làm chủ vận mệnh của mình.
    <br><br>
    <b>Tầm nhìn:</b> Trở thành vùng kinh tế thịnh vượng, thích ứng với biến đổi khí hậu và là niềm tự hào của cả nước.
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    c1, c2 = st.columns(2)
    with c1:
        st.success("💪 **Nhân lực:** 70% lao động được đào tạo kỹ năng số vào 2030.")
        safe_image("https://images.unsplash.com/photo-1477959858617-67f85cf4f1df?q=80&w=1000", "Đô thị xanh thông minh")
    with c2:
        st.success("🍃 **Môi trường:** Bảo tồn 100% diện tích rừng ngập mặn hiện có.")
        safe_image("https://images.unsplash.com/photo-1518467166778-b88f373ffec7?q=80&w=1000", "Bảo tồn hệ sinh thái biển")

st.markdown("<br><hr><center><b>to4lol.xyz</b> | Nhóm Nghiên cứu Kinh tế Tổ 4 | Phiên bản 2.4.0 (Logic Optimized)</center>", unsafe_allow_html=True)