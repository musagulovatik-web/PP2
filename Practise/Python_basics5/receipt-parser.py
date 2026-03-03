import re
import json
import os
folder_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(folder_path, 'raw.txt')
with open(file_path, 'r', encoding='utf-8') as f:
    x=f.read()
y=re.findall(r"Стоимость\s*(\d+[.,]\b)", x)
p=[i.replace(',','') for i in y]
price=list(map(float,p))
items = re.findall(r"\d+\.\s+([А-Яа-яЁёA-Za-z\s]+)", x)
time=re.findall(r"Время:\s*([\d.]+\s*[\d:]+)", x)
type=re.findall(r"Банковская карта", x)
sum=0
for i in price:
    sum=sum+i
result_data = {
    "items": items,
    "price": price,
    "time": time,
    "type": type
}

with open('receipt_result.json', 'w', encoding='utf-8') as json_file:
    json.dump(result_data, json_file, indent=4, ensure_ascii=False)
