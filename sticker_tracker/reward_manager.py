import tkinter as tk
from tkinter import Toplevel, messagebox, Label, Entry, Button, Radiobutton, IntVar
import json

class RewardManager:
  def __init__(self, parent):
    self.parent = parent
    self.load_rewards()
    self.show_reward_popup()

  def load_rewards(self):
    try:
      with open("data/rewards.json", "r") as f:
        self.rewards = json.load(f)
    except FileNotFoundError:
      self.rewards = [
        {"이름": "포켓몬 카드", "스티커 개수": 5, "소진 여부": "없음"},
        {"이름": "건담", "스티커 개수": 30, "소진 여부": "소진"},
        {"이름": "해리포터 성 레고", "스티커 개수": 50, "소진 여부": "소진"},
        {"이름": "사자 성 레고", "스티커 개수": 50, "소진 여부": "소진"},
        {"이름": "가오레 카드", "스티커 개수": 20, "소진 여부": "소진"},
        {"이름": "MG건담", "스티커 개수": 300, "소진 여부": "소진"}
      ]
      self.save_rewards()

  def save_rewards(self):
    with open("data/rewards.json", "w") as f:
      json.dump(self.rewards, f, indent=4)

  def show_reward_popup(self):
    self.popup = Toplevel(self.parent)
    self.popup.title("보상 안내 관리")
    self.popup.geometry("600x400")

    self.popup_frame = tk.Frame(self.popup)
    self.popup_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    self.selected_reward = IntVar(value=-1)
    self.create_reward_table()

    # 보상 추가 입력 필드
    Label(self.popup_frame, text="보상 이름:").grid(row=len(self.rewards) + 1, column=0, padx=5, pady=5)
    self.name_entry = Entry(self.popup_frame)
    self.name_entry.grid(row=len(self.rewards) + 1, column=1, padx=5, pady=5)

    Label(self.popup_frame, text="스티커 개수:").grid(row=len(self.rewards) + 2, column=0, padx=5, pady=5)
    self.stickers_entry = Entry(self.popup_frame)
    self.stickers_entry.grid(row=len(self.rewards) + 2, column=1, padx=5, pady=5)

    Label(self.popup_frame, text="소진 여부:").grid(row=len(self.rewards) + 3, column=0, padx=5, pady=5)
    self.status_entry = Entry(self.popup_frame)
    self.status_entry.grid(row=len(self.rewards) + 3, column=1, padx=5, pady=5)

    # 보상 추가 버튼
    add_button = Button(self.popup_frame, text="보상 추가", command=self.save_new_reward)
    add_button.grid(row=len(self.rewards) + 4, column=0, columnspan=2, padx=5, pady=10)

    # 보상 제거 버튼
    remove_button = Button(self.popup_frame, text="보상 제거", command=self.remove_reward)
    remove_button.grid(row=len(self.rewards) + 5, column=0, columnspan=2, padx=5, pady=10)

  def create_reward_table(self):
    headers = ["선택", "이름", "스티커 개수", "소진 여부"]
    for col, header in enumerate(headers):
      header_label = Label(self.popup_frame, text=header, font=("Arial", 10, "bold"), borderwidth=2, relief="groove", padx=5, pady=5)
      header_label.grid(row=0, column=col, sticky=tk.NSEW)

    for row, reward in enumerate(self.rewards, start=1):
      Radiobutton(self.popup_frame, variable=self.selected_reward, value=row-1).grid(row=row, column=0, sticky=tk.NSEW)
      for col, key in enumerate(reward.keys(), start=1):
        cell = Label(self.popup_frame, text=reward[key], borderwidth=1, relief="solid", padx=5, pady=5)
        cell.grid(row=row, column=col, sticky=tk.NSEW)

  def save_new_reward(self):
    # 새로운 보상 저장
    name = self.name_entry.get()
    stickers = self.stickers_entry.get()
    status = self.status_entry.get()

    try:
      stickers = int(stickers)
      new_reward = {"이름": name, "스티커 개수": stickers, "소진 여부": status}
      self.rewards.append(new_reward)
      self.save_rewards()
      self.refresh_table()
      self.name_entry.delete(0, tk.END)
      self.stickers_entry.delete(0, tk.END)
      self.status_entry.delete(0, tk.END)
      messagebox.showinfo("성공", "새 보상이 추가되었습니다.")
    except ValueError:
      messagebox.showerror("오류", "스티커 개수는 숫자로 입력해주세요.")

  def remove_reward(self):
    # 선택된 보상 제거
    selected_index = self.selected_reward.get()
    if selected_index == -1:
      messagebox.showwarning("경고", "제거할 보상을 선택해주세요.")
      return
    del self.rewards[selected_index]
    self.save_rewards()
    self.refresh_table()
    messagebox.showinfo("성공", "선택된 보상이 제거되었습니다.")

  def refresh_table(self):
    # 테이블 업데이트
    for widget in self.popup_frame.winfo_children():
      widget.destroy()
    self.create_reward_table()

    # 보상 추가 입력 필드 및 버튼 재생성
    Label(self.popup_frame, text="보상 이름:").grid(row=len(self.rewards) + 1, column=0, padx=5, pady=5)
    self.name_entry = Entry(self.popup_frame)
    self.name_entry.grid(row=len(self.rewards) + 1, column=1, padx=5, pady=5)

    Label(self.popup_frame, text="스티커 개수:").grid(row=len(self.rewards) + 2, column=0, padx=5, pady=5)
    self.stickers_entry = Entry(self.popup_frame)
    self.stickers_entry.grid(row=len(self.rewards) + 2, column=1, padx=5, pady=5)

    Label(self.popup_frame, text="소진 여부:").grid(row=len(self.rewards) + 3, column=0, padx=5, pady=5)
    self.status_entry = Entry(self.popup_frame)
    self.status_entry.grid(row=len(self.rewards) + 3, column=1, padx=5, pady=5)

    add_button = Button(self.popup_frame, text="보상 추가", command=self.save_new_reward)
    add_button.grid(row=len(self.rewards) + 4, column=0, columnspan=2, padx=5, pady=10)

    remove_button = Button(self.popup_frame, text="보상 제거", command=self.remove_reward)
    remove_button.grid(row=len(self.rewards) + 5, column=0, columnspan=2, padx=5, pady=10)

if __name__ == "__main__":
  root = tk.Tk()
  app = RewardManager(root)
  root.mainloop()
