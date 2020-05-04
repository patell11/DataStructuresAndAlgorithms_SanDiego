import unittest
from partition_souvenirs import partitions3
from partition import findPartion


class PartitionSouvenirs(unittest.TestCase):
    def test(self):
        for values, answer in (
            ((20, ), 0),
            ((7, 7, 7), 1),
            ((3, 3, 3), 1),
            ((3, 3, 3, 3), 0),

        ):
            self.assertEqual(findPartion(values), answer)


if __name__ == '__main__':
    unittest.main()
