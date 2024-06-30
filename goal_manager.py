import tkinter as tk
from tkinter import Toplevel

class GoalManager:
  def __init__(self, root):
    self.root = root

    # 목표 목록
    self.goals = [
      {"목표": "한글 쓰기", "횟수": "3일", "성공": "스티커 1장", "추가 성공": "추가 스티커 1장", "실패": "다음 주에 추가"},
      {"목표": "숫자 쓰기", "횟수": "2일", "성공": "스티커 1장", "추가 성공": "-", "실패": "다음 주에 추가"},
      {"목표": "종이 접기", "횟수": "별 3개 2번, 별 2개 3번, 별 1개 5번", "성공": "스티커 1장", "추가 성공": "별 3개 2장, 별 2개 1장", "실패": "다음 주에 추가"},
      {"목표": "영어책 읽기", "횟수": "5권", "성공": "스티커 1장", "추가 성공": "추가권당 1장", "실패": "-"},
      {"목표": "보드게임", "횟수": "1회 주말", "성공": "완벽한 게임 1장", "추가 성공": "-", "실패": "-"},
      {"목표": "가배", "횟수": "일주일에 1회", "성공": "스티커 1장", "추가 성공": "1장", "실패": "다음 주에 추가"}
    ]

    self.show_goal_popup()

  def show_goal_popup(self):
    # 팝업 창 생성
    self.popup = Toplevel(self.root)
    self.popup.title("목표 관리")
    self.popup.geometry("600x300")

    # 팝업 프레임 생성
    self.popup_frame = tk.Frame(self.popup)
    self.popup_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    # 목표 테이블
    self.create_goal_table()

  def create_goal_table(self):
    # 테이블 헤더
    headers = ["목표", "일주일 동안 해야 할 횟수", "성공", "추가 성공", "실패"]
    for col, header in enumerate(headers):
      header_label = tk.Label(self.popup_frame, text=header, font=("Arial", 10, "bold"), borderwidth=2, relief="groove", padx=5, pady=5)
      header_label.grid(row=0, column=col, sticky=tk.NSEW)

    # 목표 목록 출력
    for row, goal in enumerate(self.goals, start=1):
      for col, key in enumerate(goal.keys()):
        cell = tk.Label(self.popup_frame, text=goal[key], borderwidth=1, relief="solid", padx=5, pady=5)
        cell.grid(row=row, column=col, sticky=tk.NSEW)
