#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Justin Baumann
#9/8/2025
#SSW567
#I pledge my honor that I have abided by the Stevens Honor System


# In[3]:


def classify_triangle(a,b,c):
    if a + b <= c or a + c <= b or b + c <= a:
        return "Not a valid triangle"
        return "Not a valid triangle"
    if a == b == c:
       triangle_type = "Equilateral"
    elif a == b or a == c or b == c:
        triangle_type = "Isosceles"
    else:
        triangle_type = "Scalene"
        
    if a**2 + b**2 == c**2:
        triangle_type += " Right"
        
    return triangle_type


# In[6]:


import unittest

class TestClassifyTriangle(unittest.TestCase):
    def test_equilateral(self):
        self.assertEqual(classify_triangle(5, 5, 5), "Equilateral")

    def test_isosceles(self):
        self.assertEqual(classify_triangle(5, 5, 7), "Isosceles")

    def test_scalene(self):
        self.assertEqual(classify_triangle(4, 5, 6), "Scalene")

    def test_right_triangle(self):
        self.assertEqual(classify_triangle(3, 4, 5), "Scalene Right")

    def test_invalid(self):
        self.assertEqual(classify_triangle(1, 2, 3), "Not a valid triangle")


# In[7]:


suite = unittest.TestLoader().loadTestsFromTestCase(TestClassifyTriangle)
unittest.TextTestRunner(verbosity=2).run(suite)

