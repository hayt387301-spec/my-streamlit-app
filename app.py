import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Quản lý điểm sinh viên", layout="wide")
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

# Dữ liệu sinh viên
data = {
    "Họ tên": ["An", "Nam", "Bình", "Linh", "Lan", "My", "Dung", "Đạt", "Hà", "Mỹ"],
    "Chuyên cần": [9, 8, 4, 8, 9.5, 9, 5, 10, 9.5, 10],
    "Giữa kỳ": [9, 8, 6, 8.5, 9, 10, 4, 9.5, 10, 10],
    "Cuối kỳ": [9, 9, 4.5, 8, 8.5, 10, 3, 10, 9.5, 8.5]
}

df = pd.DataFrame(data)

# Tính điểm tổng kết
df["Tổng kết"] = (
    0.2 * df["Chuyên cần"]
    + 0.3 * df["Giữa kỳ"]
    + 0.5 * df["Cuối kỳ"]
).round(2)

# Xếp loại
def xep_loai(diem):
    if diem >= 8.5:
        return "Giỏi"
    elif diem >= 7:
        return "Khá"
    elif diem >= 5:
        return "Trung bình"
    return "Yếu"

df["Xếp loại"] = df["Tổng kết"].apply(xep_loai)

# Bảng điểm
st.subheader("1. Bảng điểm 10 sinh viên")
st.dataframe(df, hide_index=True, use_container_width=True)

# Thống kê
st.subheader("2. Thống kê kết quả")

cao = df.loc[df["Tổng kết"].idxmax()]
thap = df.loc[df["Tổng kết"].idxmin()]
diem_tb = df["Tổng kết"].mean()
so_dat = (df["Tổng kết"] >= 5).sum()

c1, c2, c3, c4 = st.columns(4)
c1.metric("Điểm trung bình lớp", round(diem_tb, 2))
c2.metric("Điểm cao nhất", cao["Tổng kết"])
c3.metric("Điểm thấp nhất", thap["Tổng kết"])
c4.metric("Số sinh viên đạt", f"{so_dat}/10")

st.write("**Sinh viên cao nhất:**", cao["Họ tên"])
st.write("**Sinh viên thấp nhất:**", thap["Họ tên"])

# Chọn sinh viên
st.subheader("3. Tra cứu điểm sinh viên")
ten = st.selectbox("Chọn sinh viên", df["Họ tên"])
sv = df[df["Họ tên"] == ten].iloc[0]

st.write("**Họ tên:**", sv["Họ tên"])
st.write("**Điểm chuyên cần:**", sv["Chuyên cần"])
st.write("**Điểm giữa kỳ:**", sv["Giữa kỳ"])
st.write("**Điểm cuối kỳ:**", sv["Cuối kỳ"])
st.write("**Điểm tổng kết:**", sv["Tổng kết"])
st.write("**Xếp loại:**", sv["Xếp loại"])

# Biểu đồ cột
st.subheader("4. Biểu đồ điểm tổng kết")
fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(df["Họ tên"], df["Tổng kết"], color="skyblue")
ax.set_title("Điểm tổng kết của 10 sinh viên")
ax.set_xlabel("Họ tên")
ax.set_ylabel("Điểm tổng kết")
ax.set_ylim(0, 10)
plt.tight_layout()
st.pyplot(fig)
plt.close(fig)

# Thông tin người tạo
st.divider()
st.caption("Người tạo: Yên Thị Hà | MSSV: 038308017301")