import propagate_uncertainties as pru
import numpy as np


def test_add_zero_au():
    s, s_au = pru.add(x=1, x_au=0, y=1, y_au=0)
    assert s == 2
    assert s_au == 0


def test_add_1():
    s, s_au = pru.add(x=1, x_au=1, y=1, y_au=1)
    assert s == 2
    assert s_au == np.sqrt(2)


def test_add_2():
    s, s_au = pru.add(x=1, x_au=1, y=1, y_au=0)
    assert s == 2
    assert s_au == 1


def test_add_3():
    s, s_au = pru.add(x=0, x_au=1, y=0, y_au=1)
    assert s == 0
    assert s_au == np.sqrt(2)


def test_multiply_zero_au():
    s, s_au = pru.multiply(x=1, x_au=0, y=1, y_au=0)
    assert s == 1
    assert s_au == 0


def test_multiply_1():
    s, s_au = pru.multiply(x=0, x_au=1, y=0, y_au=1)
    assert s == 0
    assert s_au == 0


def test_multiply_2():
    s, s_au = pru.multiply(x=1, x_au=1, y=1, y_au=1)
    assert s == 1
    assert s_au == np.sqrt(2)


def test_multiply_3():
    s, s_au = pru.multiply(x=1, x_au=2, y=1, y_au=2)
    assert s == 1
    assert s_au == 2 * np.sqrt(2)


def test_multiply_4():
    s, s_au = pru.multiply(x=1, x_au=1, y=10, y_au=1)
    assert s == 10
    assert s_au == np.sqrt(1**2 + 10**2)


def test_devide_zero_au():
    s, s_au = pru.divide(x=1, x_au=0, y=1, y_au=0)
    assert s == 1
    assert s_au == 0


def test_devide_1():
    s, s_au = pru.divide(x=1, x_au=0, y=2, y_au=0)
    assert s == 0.5
    assert s_au == 0


def test_devide_2():
    s, s_au = pru.divide(x=7, x_au=1, y=2, y_au=1)
    assert s == 3.5
    assert s_au == np.sqrt((1 / 2) ** 2 + (7 / 2**2) ** 2)


def test_integrate_zero_au():
    s, s_au = pru.integrate(
        f=[1, 1, 1], f_au=[0, 0, 0], x_bin_edges=[0, 1, 2, 3]
    )
    assert s == 3
    assert s_au == 0


def test_integrate_zero_1():
    a = 0.1
    b = 0.2
    c = 0.3
    s, s_au = pru.integrate(
        f=[1, 1, 1], f_au=[a, b, c], x_bin_edges=[0, 1, 2, 3]
    )
    assert s == 3
    assert s_au == np.sqrt(a**2 + b**2 + c**2)


def test_elementwise_add_zero_au():
    s, s_au = pru.sum(x=[1, 1], x_au=[0, 0])
    assert s == 2
    assert s_au == 0


def test_elementwise_add_1():
    a = 1
    b = 2
    a_au = 0.2
    b_au = 0.55
    s1, s_au1 = pru.sum(x=[a, b], x_au=[a_au, b_au])
    s2, s_au2 = pru.add(x=a, x_au=a_au, y=b, y_au=b_au)
    assert s1 == s2
    assert s_au1 == s_au2


def test_elementwise_multiply_zero_au():
    s, s_au = pru.prod(x=[1, 1], x_au=[0, 0])
    assert s == 1
    assert s_au == 0


def test_elementwise_multiply_1():
    a = 1
    b = 2
    a_au = 0.2
    b_au = 0.55
    s1, s_au1 = pru.prod(x=[a, b], x_au=[a_au, b_au])
    s2, s_au2 = pru.multiply(x=a, x_au=a_au, y=b, y_au=b_au)
    assert s1 == s2
    assert s_au1 == s_au2


def test_sum_axis0():
    shape = (3, 25)

    x = np.ones(shape)
    x_au = 0.01 * np.ones(shape)

    snp = np.sum(x, axis=0)
    s, s_au = pru.sum_axis0(x=x, x_au=x_au)

    assert s.shape == s_au.shape
    assert s.shape == snp.shape
    assert s.shape[0] == 25
    assert s[0] == 3


def test_sum_axis0_2():
    x = [
        [10, 10, 10, 10, 10, 10],
        [10, 10, 10, 10, 10, 10],
    ]
    x_au = [
        [0.1, 0.1, 0.1, 0.1, 0.1, 0.1],
        [0.1, 0.1, 0.1, 0.1, 0.1, 0.1],
    ]
    snp = np.sum(x, axis=0)
    s, s_au = pru.sum_axis0(x=x, x_au=x_au)

    assert s.shape == snp.shape
    np.testing.assert_array_equal(s, snp)

    assert s.shape == s_au.shape

    assert s.shape[0] == 6
    assert s[0] == 20.0
    cs, cs_au = pru.sum(x=[10, 10], x_au=[0.1, 0.1])
    assert s[0] == cs
    assert s_au[0] == cs_au


def test_sqrt():
    s, s_au = pru.sqrt(x=4, x_au=0.0)
    assert s == 2.0
    assert s_au == 0.0


def test_sqrt_1():
    s, s_au = pru.sqrt(x=4, x_au=1.0)
    assert s == 2.0
    assert s_au == 0.25


def test_sqrt_2():
    s, s_au = pru.sqrt(x=4, x_au=4.0)
    assert s == 2.0
    assert s_au == 1.0
