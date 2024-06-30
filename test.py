import tkinter as tk
from tkinter import messagebox

class MoneyTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("용돈 기록장")

        # 입력 부분
        self.label_title = tk.Label(root, text="아이 용돈 기록")
        self.label_title.pack(pady=10)

        self.label_amount = tk.Label(root, text="금액:")
        self.label_amount.pack()

        self.entry_amount = tk.Entry(root, width=30)
        self.entry_amount.pack()

        self.label_description = tk.Label(root, text="지출 내용:")
        self.label_description.pack()

        self.entry_description = tk.Entry(root, width=30)
        self.entry_description.pack()

        self.save_button = tk.Button(root, text="저장", command=self.save_button_clicked)
        self.save_button.pack(pady=10)

        # 출력 부분
        self.label_saved_record = tk.Label(root, text="")
        self.label_saved_record.pack()

        # 현재 금액 표시 부분
        self.label_current_amount = tk.Label(root, text="현재 총 지출 금액: 0 원", fg="blue")
        self.label_current_amount.pack()

        # 초기화면에서 저장된 기록 및 현재 금액 표시
        self.show_saved_record()
        self.update_current_amount()

    def save_button_clicked(self):
        amount_str = self.entry_amount.get()
        description = self.entry_description.get()

        # 유효성 검사: 금액이 숫자인지 확인
        if not amount_str.isdigit():
            messagebox.showwarning("입력 오류", "금액은 숫자로 입력해주세요.")
            return

        amount = int(amount_str)

        # 금액과 지출 내용이 입력되었는지 확인
        if amount > 0 and description:
            self.save_record(amount, description)
            self.show_saved_record()
            self.update_current_amount()
        else:
            messagebox.showwarning("입력 오류", "금액을 양수로 입력하고, 지출 내용을 모두 입력해주세요.")

    def save_record(self, amount, description):
        # 기록 저장 함수
        data_file = "money_tracker_data.txt"
        with open(data_file, 'a') as f:
            f.write(f"금액: {amount} 원, 지출 내용: {description}\n")

        # 저장 후 메시지 박스로 저장 완료 메시지 보여주기
        messagebox.showinfo("저장 완료", "기록이 성공적으로 저장되었습니다.")

    def show_saved_record(self):
        # 저장된 기록을 텍스트로 보여주는 함수
        try:
            data_file = "money_tracker_data.txt"
            with open(data_file, 'r') as f:
                saved_records = f.readlines()

            # 최근 5개 기록만 가져와서 GUI에 표시
            if saved_records:
                last_records = saved_records[-5:]  # 최근 5개 기록 가져오기
                display_text = "\n".join(last_records)
                self.label_saved_record.config(text=f"최근 저장된 기록:\n{display_text}")
            else:
                self.label_saved_record.config(text="저장된 기록 없음")
        except FileNotFoundError:
            self.label_saved_record.config(text="저장된 기록 없음")

    def update_current_amount(self):
        # 현재 총 지출 금액 업데이트 함수
        try:
            data_file = "money_tracker_data.txt"
            total_amount = 0
            with open(data_file, 'r') as f:
                for line in f:
                    if "금액: " in line:
                        amount_str = line.split("금액: ")[1].split(" 원")[0]
                        total_amount += int(amount_str)

            self.label_current_amount.config(text=f"현재 총 지출 금액: {total_amount} 원", fg="blue")
        except FileNotFoundError:
            self.label_current_amount.config(text="현재 총 지출 금액: 0 원", fg="blue")

# tkinter 애플리케이션 생성
root = tk.Tk()
app = MoneyTrackerApp(root)

# 애플리케이션 실행
root.mainloop()
