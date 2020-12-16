from main import Box1, Box2
import unittest


class SummaTest(unittest.TestCase):
    def test_sum_Box1(self):
        order = Box1()
        order.add_all()
        self.assertEqual(order.box.get_sum(), 5750, "Should be 5750")

    def test_sum_Box2(self):
        order = Box2()
        order.add_all()
        self.assertEqual(order.box.get_sum(), 6009, "Should be 6009")


if __name__ == "__main__":
    unittest.main()