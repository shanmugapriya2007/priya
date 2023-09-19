class player:
  def paly(self):
    print("The palyer is playing cricket.")
class batsman(player):
  def play(self):
    print("The batsman is batting.")
class bowler(player):
  def play(self):
    print("The bowler is bowling.")
batsman1=batsman()
bowler1=bowler()
batsman1.play()
bowler1.play()

    