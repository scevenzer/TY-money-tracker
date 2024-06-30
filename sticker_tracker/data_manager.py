def save_record(stickers, description, record_type):
  data_file = "data/sticker_tracker_data.txt"  # 파일 이름을 명확하게 변경
  with open(data_file, 'a', encoding='utf-8') as f:
    f.write(f"{record_type}: {stickers} 개, 내용: {description}\n")

def load_saved_records():
  data_file = "data/sticker_tracker_data.txt"
  try:
    with open(data_file, 'r', encoding='utf-8') as f:
      return f.readlines()
  except FileNotFoundError:
    return []

def calculate_total_stickers():
  records = load_saved_records()
  total_stickers = 0
  for line in records:
    if "보상: " in line or "지출: " in line:
      stickers_str = line.split(": ")[1].split(" 개")[0]
      total_stickers += int(stickers_str)
  return total_stickers
