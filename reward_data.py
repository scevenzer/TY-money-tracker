import json
import os

class RewardData:
  def __init__(self):
    self.filename = "rewards.json"
    self.default_rewards = [
      {"이름": "포켓몬 카드", "스티커 개수": 5, "소진 여부": "없음"},
      {"이름": "건담", "스티커 개수": 30, "소진 여부": "소진"},
      {"이름": "해리포터 성 레고", "스티커 개수": 50, "소진 여부": "소진"},
      {"이름": "사자 성 레고", "스티커 개수": 50, "소진 여부": "소진"},
      {"이름": "가오레 카드", "스티커 개수": 20, "소진 여부": "소진"},
      {"이름": "MG건담", "스티커 개수": 300, "소진 여부": "소진"}
    ]
    self.rewards = self.load_rewards()

  def load_rewards(self):
    if not os.path.exists(self.filename):
      self.save_rewards(self.default_rewards)
    with open(self.filename, "r", encoding='utf-8') as f:
      return json.load(f)

  def save_rewards(self, rewards):
    with open(self.filename, "w", encoding='utf-8') as f:
      json.dump(rewards, f, ensure_ascii=False, indent=4)

  def get_rewards(self):
    return self.rewards

  def add_reward(self, reward):
    self.rewards.append(reward)
    self.save_rewards(self.rewards)

  def remove_reward(self, index):
    del self.rewards[index]
    self.save_rewards(self.rewards)
