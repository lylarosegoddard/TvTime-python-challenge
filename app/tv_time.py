class TvTime:
  def __init__(self, hours):
    self.hours = hours

  def comment(self):
    if self.hours < 2:
      return "That should be ok"
    if self.hours <= 4:
      return "That will rot your brain"
    return "That is too much tv"