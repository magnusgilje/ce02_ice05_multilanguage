import sys
sys.path.insert(0,"..")
import circle


def test_circle_with_radius_0_2dp():
    myC = circle.Circle(float(0.0))
    assert round(myC.area(),2) == 0
    assert round(myC.perimeter(),2) == 0


def test_circle_with_radius_1_2dp():
    myC = circle.Circle(float(1.0))
    assert round(myC.area(),2) == 3.14
    assert round(myC.perimeter(),2) == 6.28

