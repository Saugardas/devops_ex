import os
import pandas as pd
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset
from sklearn.model_selection import train_test_split

os.makedirs("reports", exist_ok=True)

df = pd.read_csv("data/dataset.csv")
features = df[['sepal.length', 'sepal.width']]
ref, cur = train_test_split(features, test_size=0.3, random_state=42)

# Создаём и запускаем отчёт
report = Report(metrics=[DataDriftPreset()])
report.run(reference_data=ref, current_data=cur)


report.save_html("reports/evidently_report.html")
print("Отчет сохранен: reports/evidently_report.html")
