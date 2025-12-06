
````markdown
# 🇻🇳 Vietnamese Sentiment Analysis (Phân loại cảm xúc Tiếng Việt)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-red)
![FastAPI](https://img.shields.io/badge/Backend-FastAPI-green)
![Model](https://img.shields.io/badge/AI-PhoBERT-yellow)

Dự án xây dựng ứng dụng Web phân tích cảm xúc văn bản Tiếng Việt (Tích cực / Tiêu cực / Trung tính) sử dụng mô hình Deep Learning **PhoBERT** kết hợp với **FastAPI** và **Streamlit**.

Demo Trực Tuyến
**[https://camxuc-tiengviet.streamlit.app/](https://camxuc-tiengviet.streamlit.app/)**


##  Tính Năng Chính

* **Phân loại cảm xúc:** Xác định câu văn thuộc nhóm `POSITIVE` (Tích cực), `NEGATIVE` (Tiêu cực) hoặc `NEUTRAL` (Trung tính).
* **Xử lý Teencode:** Tích hợp từ điển chuẩn hóa để xử lý các từ viết tắt, tiếng lóng thông dụng (VD: "hnay", "ko", "dc", "wa"...).
* **Độ tin cậy (Confidence Score):** Hiển thị chỉ số tự tin của mô hình. Tự động gán nhãn Trung tính nếu độ tin cậy < 0.5.
* **Lịch sử phân tích:** Lưu trữ lịch sử các câu đã nhập vào cơ sở dữ liệu SQLite để xem lại.

##  Công Nghệ Sử Dụng

* **Ngôn ngữ:** Python
* **Mô hình AI:** [wonrax/phobert-base-vietnamese-sentiment](https://huggingface.co/wonrax/phobert-base-vietnamese-sentiment) (Hugging Face)
* **Backend API:** FastAPI & Uvicorn
* **Frontend:** Streamlit
* **Database:** SQLite

##  Hướng Dẫn Cài Đặt (Local)

Để chạy dự án trên máy tính cá nhân, hãy làm theo các bước sau:

### 1. Clone dự án
```bash
git clone https://github.com/HoangKhang1109/DA_Seminal.git
cd DA_Seminal
```

### 2. Cài đặt thư viện
Yêu cầu Python 3.8 trở lên.
```bash
pip install -r requirements.txt
```

### 3. Khởi chạy hệ thống
Hệ thống cần chạy song song API và Giao diện trên 2 cửa sổ Terminal (CMD) khác nhau.

**Terminal 1 (Chạy API Backend):**
```bash
uvicorn main:app --reload
```
*API sẽ chạy tại: http://127.0.0.1:8000*

**Terminal 2 (Chạy Giao diện Streamlit):**

```bash
streamlit run streamlit_app.py
```
*Web App sẽ mở tại: http://localhost:8501*

##  Cấu Trúc Dự Án

  * `model.py`: Chứa class `SentimentAnalyzer`, xử lý load model PhoBERT và chuẩn hóa text.
  * `main.py`: API Server (FastAPI), xử lý request và lưu database.
  * `streamlit_app.py`: Giao diện người dùng (Frontend).
  * `generate_test_cases.py`: Script dữ liệu kiểm thử, kết quả xuất ra 2 file excel là "test_cases.xlsx" và "test_cases_FINAL.xlsx" lưu kết quả phân tích test-case.
  * `requirements.txt`: Danh sách các thư viện cần thiết.

##  Kiểm Thử

Để chạy bộ kiểm thử và xuất báo cáo ra Excel:
```bash
python generate_test_cases.py
```


