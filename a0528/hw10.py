class Appliance:
  def __init__(self, name, power):
    self.name = name
    self.power = power

class WashingMachine(Appliance):
  def __init__(self, name, power, modes):
    super().__init__(name, power)
    self.modes = modes

  def start(self):
    if not self.power:
      print("전원이 꺼져 있습니다.")

    else:
      print(f"'{self.name}' 작동 시작!")
      for mode in self.modes:
        print(f" [모드] {mode}")

washer1 = WashingMachine("삼성 세탁기", True, ["헹굼", "세탁", "탈수"])
washer1.start()

washer2 = WashingMachine("삼성 세탁기", False, ["헹굼", "세탁", "탈수"])
washer2.start()


