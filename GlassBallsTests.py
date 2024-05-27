import time
import unittest

import GlassBalls


class MyTestCase(unittest.TestCase):

    def test_q1(self):
        start = time.time()
        self.assertEqual(GlassBalls.checking_number(1,1),1)
        self.assertEqual(GlassBalls.checking_number(10,1),10)
        self.assertEqual(GlassBalls.checking_number(1000,1),1000)
        self.assertEqual(GlassBalls.checking_number(100,2),14)
        self.assertEqual(GlassBalls.checking_number(10,2),4)
        self.assertEqual(GlassBalls.checking_number(11,2),5)
        self.assertEqual(GlassBalls.checking_number(50,3),7)
        self.assertEqual(GlassBalls.checking_number(300,5) ,9)
        self.assertEqual(GlassBalls.checking_number(100,7),7)
        self.assertEqual(GlassBalls.checking_number(45,4),6)
        self.assertEqual(GlassBalls.checking_number(1000,8),10)
        self.assertEqual(GlassBalls.checking_number(1000,7),11)
        end = time.time()
        print(end - start)

    def test_q2(self):
        floors1 =[1,2,3,4,5,6,7,8,9,10]
        floors2 =[1,2,4,6,10,16,20,24,28,36,48]
        floors3 = [1, 2, 3, 4,5]
        floors4 =[1,2,3,4,5,6,7,8,9,10,11]
        start = time.time()
        self.assertEqual(GlassBalls.index_floor(floors1,2),3)
        self.assertEqual(GlassBalls.index_floor(floors1,9),10)
        self.assertEqual(GlassBalls.index_floor(floors1, 10),-1)
        self.assertEqual(GlassBalls.index_floor(floors2,1),2)
        self.assertEqual(GlassBalls.index_floor(floors2,48),-1)
        self.assertEqual(GlassBalls.index_floor(floors2,47),11)
        self.assertEqual(GlassBalls.index_floor(floors2,10),6)

        self.assertEqual(GlassBalls.index_floor(floors3,2),3)
        self.assertEqual(GlassBalls.index_floor(floors3,3),4)
        self.assertEqual(GlassBalls.index_floor(floors3,4),5)
        self.assertEqual(GlassBalls.index_floor([2],1),1)
        self.assertEqual(GlassBalls.index_floor(floors4,10),11)
        self.assertEqual(GlassBalls.index_floor(floors4,11),-1)

        end = time.time()
        print(end - start)

    def test_q3(self):
        start = time.time()
        self.assertEqual(GlassBalls.index_first_floor(10),4)
        self.assertEqual(GlassBalls.index_first_floor(11),5)
        self.assertEqual(GlassBalls.index_first_floor(100),14)
        self.assertEqual(GlassBalls.index_first_floor(20), 6)
        self.assertEqual(GlassBalls.index_first_floor(21), 6)
        self.assertEqual(GlassBalls.index_first_floor(46), 10)
        self.assertEqual(GlassBalls.index_first_floor(1), 1)

        end = time.time()
        print(end - start)




if __name__ == '__main__':
    unittest.main()
