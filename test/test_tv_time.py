import unittest
from app.tv_time import TvTime

class TestTvTime(unittest.TestCase):
  def test_tv_ok(self):
    tvTime = TvTime(1.99)
    self.assertEqual("That should be ok", tvTime.comment())

  def test_tv_rot_brain(self):
    tvTime = TvTime(2)
    self.assertEqual("That will rot your brain", tvTime.comment())
  
  def test_tv_too_much(self):
    tvTime = TvTime(4.01)
    self.assertEqual("That is too much tv", tvTime.comment())