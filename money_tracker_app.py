import tkinter as tk
from reward_gui import RewardManager

class MoneyTrackerApp:
  def __init__(self, root):
    self.root = root
    self.root.title("스티커 기록장")
    self.main_frame = tk.Frame(root)
    self.main_frame.pack(padx=10, pady=10)

    self.label_title = tk.Label(self.main_frame, text="아이 스티커 기록", font=("Arial", 16))
    self.label_title.grid(row=0, columnspan=2, pady=10)

    self.label_reward = tk.Label(self.main_frame, text="보상 내용", font=("Arial", 14))
    self.label_reward.grid(row=1, columnspan=2, pady=5)

    self.label_reward_stickers = tk.Label(self.main_frame, text="보상 스티커 개수:")
    self.label_reward_stickers.grid(row=2, column=0, sticky=tk.W)

    self.entry_reward_stickers = tk.Entry(self.main_frame, width=10)
    self.entry_reward_stickers.grid(row=2, column=1, pady=2)

    self.label_reward_description = tk.Label(self.main_frame, text="보상 내용:")
    self.label_reward_description.grid(row=3, column=0, sticky=tk.W)

    self.entry_reward_description = tk.Entry(self.main_frame, width=20)
    self.entry_reward_description.grid(row=3, column=1, pady=2)

    self.reward_save_button = tk.Button(self.main_frame, text="보상 저장", command=self.reward_save_button_clicked)
    self.reward_save_button.grid(row=4, columnspan=2, pady=10)

    self.label_expense = tk.Label(self.main_frame, text="지출 내용", font=("Arial", 14))
    self.label_expense.grid(row=5, columnspan=2, pady=5)

    self.label_expense_stickers = tk.Label(self.main_frame, text="지출 스티커 개수:")
    self.label_expense_stickers.grid(row=6, column=0, sticky=tk.W)

    self.entry_expense_stickers = tk.Entry(self.main_frame, width=10)
    self.entry_expense_stickers.grid(row=6, column=1, pady=2)

    self.label_expense_description = tk.Label(self.main_frame, text="지출 내용:")
    self.label_expense_description.grid(row=7, column=0, sticky=tk.W)

    self.entry_expense_description = tk.Entry(self.main_frame, width=20)
    self.entry_expense_description.grid(row=7, column=1, pady=2)

    self.expense_save_button = tk.Button(self.main_frame, text="지출 저장", command=self.expense_save_button_clicked)
    self.expense_save_button.grid(row=8, columnspan=2, pady=10)

    self.goals_button = tk.Button(self.main_frame, text="목표 보기", command=self.show_goals)
    self.goals_button.grid(row=9, columnspan=2, pady=10)

    self.reward_manager_button = tk.Button(self.main_frame, text="보상 관리", command=self.show_reward_manager)
    self.reward_manager_button.grid(row=10, columnspan=2, pady=10)

  def reward_save_button_clicked(self):
    stickers_str = self.entry_reward_stickers.get()
    description = self.entry_reward_description.get()

    if not stickers_str.isdigit():
      messagebox.showwarning("입력 오류", "스티커 개수는 숫자로 입력해주세요.")
      return

    stickers = int(stickers_str)

    if stickers > 0 and description:
      self.save_reward(stickers, description)
    else:
      messagebox.showwarning("입력 오류", "스티커 개수를 양수로 입력하고, 보상 내용을 모두 입력해주세요.")

  def save_reward(self, stickers, description):
    with open("reward_data.txt", 'a') as f:
      f.write(f"스티커 개수: {stickers} 개, 보상 내용: {description}\n")

    messagebox.showinfo("저장 완료", "보상이 성공적으로 저장되었습니다.")

  def expense_save_button_clicked(self):
    stickers_str = self.entry_expense_stickers.get()
    description = self.entry_expense_description.get()

    if not stickers_str.isdigit():
      messagebox.showwarning("입력 오류", "스티커 개수는 숫자로 입력해주세요.")
      return

    stickers = int(stickers_str)

    if stickers > 0 and description:
      self.save_expense(stickers, description)
    else:
      messagebox.showwarning("입력 오류", "스티커 개수를 양수로 입력하고, 지출 내용을 모두 입력해주세요.")

  def save_expense(self, stickers, description):
    with open("expense_data.txt", 'a') as f:
      f.write(f"스티커 개수: {stickers} 개, 지출 내용: {description}\n")

    messagebox.showinfo("저장 완료", "지출이 성공적으로 저장되었습니다.")

  def show_goals(self):
    # 목표 팝업 열기
    # self.goal_manager = GoalManager(self.root)  # GoalManager 클래스를 별도로 정의해야 합니다.
    pass

  def show_reward_manager(self):
    # 보상 관리 팝업 열기
    self.reward_manager = RewardManager(self.root)

if __name__ == "__main__":
  root = tk.Tk()
  app = MoneyTrackerApp(root)
  root.mainloop()
