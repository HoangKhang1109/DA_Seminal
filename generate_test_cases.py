# generate_test_cases.py
from model import analyzer
import pandas as pd

test_sentences = [
    "Hôm nay tôi rất vui",
    "Món ăn này dở quá",
    "Thời tiết bình thường",
    "Rất vui hôm nay",
    "Công việc ổn định",
    "Phim này hay lắm",
    "Tôi buồn vì thất bại",
    "Ngày mai đi học",
    "Cảm ơn bạn rất nhiều",
    "Mệt mỏi quá hôm nay"
]

expected = ["POSITIVE","NEGATIVE","NEUTRAL","POSITIVE","NEUTRAL",
            "POSITIVE","NEGATIVE","NEUTRAL","POSITIVE","NEGATIVE"]

results = []
for i, text in enumerate(test_sentences, 1):
    pred = analyzer.predict(text)
    results.append({
        "STT": i,
        "Câu tiếng Việt": text,
        "Kỳ vọng": expected[i-1],
        "Kết quả thực tế": pred["sentiment"],
        "Độ tin cậy": round(pred["confidence"], 4),
        "Đúng/Sai": "Đúng" if expected[i-1] == pred["sentiment"] else "Sai"
    })

df = pd.DataFrame(results)

# Tạo 2 file để không bao giờ lo bị ghi đè nhầm
df.to_excel("test_cases.xlsx", index=False)
df.to_excel("test_cases_FINAL.xlsx", index=False)

print("="*50)
print("HOÀN TẤT! ĐÃ TẠO FILE NỘP ĐỒ ÁN")
print("→ File dùng test: test_cases.xlsx")
print("→ File NỘP: test_cases_FINAL.xlsx")
print("="*50)