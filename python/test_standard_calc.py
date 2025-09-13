from standard_calc import bound_to_180, is_angle_between


""" Tests for bound_to_180() """


def test_bound_basic1():
    # negative < -180
    assert bound_to_180(-450) == -90
    assert bound_to_180(-220) == 140
    assert bound_to_180(-359) == 11
    assert bound_to_180(-181) == 179

    # negative > -180
    assert bound_to_180(-27) == -27
    assert bound_to_180(-150) == -150

    # postive < 180
    assert bound_to_180(27) == 27
    assert bound_to_180(150) == 150
    
    # 360 > positve > 180
    assert bound_to_180(181) == -179
    assert bound_to_180(220) == -140
    assert bound_to_180(359) == -1
    
    # positive > 360
    assert bound_to_180(361) == 1
    assert bound_to_180(450) == 90
    assert bound_to_180(700) == -20

    # boundary
    assert bound_to_180(-180) == -180
    assert bound_to_180(0) == 0
    assert bound_to_180(180) == -180
    assert bound_to_180(360) == 0


""" Tests for is_angle_between() """


def test_between_basic1():
    # positive angles within shortest arc
    assert is_angle_between(0, 1, 2)
    assert is_angle_between(0, 45, 90)
    assert is_angle_between(10, 20, 50)
    assert is_angle_between(350, 0, 10)

    # positive angles outside shortest arc (reflex)
    assert not is_angle_between(45, 90, 270)
    assert not is_angle_between(0, 270, 90)
    assert not is_angle_between(10, 100, 50)

    # negative angles within shortest arc
    assert is_angle_between(-30, 0, 30)
    assert is_angle_between(-200, -150, -100)
    assert is_angle_between(-10, 5, 10)  # wrap-around

    # negative angles outside shortest arc
    assert not is_angle_between(-45, 90, -90)
    assert not is_angle_between(-100, -50, -150)
    assert not is_angle_between(-10, -20, 10)

    # mixed positive and negative
    assert is_angle_between(-30, 350, 30)
    assert is_angle_between(350, -10, 10)
    assert is_angle_between(-10, 20, 30)

    # on the boundaries
    assert is_angle_between(0, 0, 90)
    assert is_angle_between(0, 90, 90)
    assert is_angle_between(90, 0, 90)
    assert is_angle_between(-180, 180, 0)