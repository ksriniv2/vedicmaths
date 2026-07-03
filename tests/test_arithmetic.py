import pytest

from vedicmathematics import (
    all_from_9_last_from_10,
    anurupyena_multiply,
    casting_out_nines_check,
    complement,
    cube_ending_in_5,
    cube_root_if_perfect,
    digit_sum,
    digital_root,
    divide_by_5,
    divide_by_25,
    fraction_to_percent,
    is_divisible_by_3,
    is_divisible_by_9,
    is_divisible_by_11,
    left_to_right_add,
    multiply_by_5,
    multiply_by_9,
    multiply_by_11,
    multiply_by_12,
    multiply_by_15,
    multiply_by_25,
    multiply_by_50,
    multiply_by_75,
    multiply_by_99,
    multiply_by_125,
    multiply_by_999,
    multiply_by_repeated_9,
    nikhilam_multiply,
    nikhilam_steps,
    osculator_for_ending_9,
    percent_of,
    recurring_decimal_unit_fraction,
    square_ending_in_5,
    square_near_50,
    square_near_base,
    square_root_if_perfect,
    subtract_using_complement,
    sum_digits_until_single,
    transpose_percent,
    urdhva_tiryagbhyam_multiply,
    vinculum_digits,
)


@pytest.mark.parametrize(
    ("number", "expected"),
    [(0, 0), (9, 9), (10, 1), (99, 9), (12345, 6), (-987, 6)],
)
def test_digital_root(number, expected):
    assert digital_root(number) == expected


def test_digit_sum_helpers():
    assert digit_sum(98765) == 35
    assert sum_digits_until_single(98765) == 8


def test_casting_out_nines_check():
    assert casting_out_nines_check(98, 97, 9506)
    assert casting_out_nines_check(45, 17, 62, "+")
    assert not casting_out_nines_check(45, 17, 63, "+")


@pytest.mark.parametrize(
    ("a", "b"),
    [(98, 97), (104, 103), (1002, 1005), (-98, 97), (98, -97)],
)
def test_nikhilam_multiply(a, b):
    assert nikhilam_multiply(a, b) == a * b


def test_nikhilam_steps_exposes_working():
    trace = nikhilam_steps(98, 97)
    assert trace.result == 9506
    assert trace.steps[0].title == "Choose base"
    assert trace.steps[-1].title == "Combine"


def test_anurupyena_multiply():
    assert anurupyena_multiply(41, 41, 50, 100) == 1681
    assert anurupyena_multiply(46, 44, 50, 100) == 46 * 44


@pytest.mark.parametrize(
    ("a", "b"),
    [(12, 13), (123, 456), (999, 999), (1001, 77), (-321, 45), (-321, -45)],
)
def test_urdhva_tiryagbhyam_multiply(a, b):
    assert urdhva_tiryagbhyam_multiply(a, b) == a * b


@pytest.mark.parametrize("number", [5, 15, 25, 105, 9995, -35])
def test_square_ending_in_5(number):
    assert square_ending_in_5(number) == number * number


def test_square_ending_in_5_rejects_other_numbers():
    with pytest.raises(ValueError):
        square_ending_in_5(42)


def test_complements():
    assert complement(87) == 13
    assert complement(887, 1000) == 113
    assert all_from_9_last_from_10(76) == 24


def test_left_to_right_add():
    assert left_to_right_add(987, 654) == 1641


@pytest.mark.parametrize(("a", "b"), [(1000, 348), (348, 1000), (12345, 9876)])
def test_subtract_using_complement(a, b):
    assert subtract_using_complement(a, b) == a - b


def test_vinculum_digits():
    assert vinculum_digits(18) == (2, -2)
    assert vinculum_digits(76) == (1, -2, -4)
    assert vinculum_digits(576) == (6, -2, -4)


@pytest.mark.parametrize("number", [0, 1, 7, 42, 1234, -56])
def test_multiplication_shortcuts(number):
    assert multiply_by_5(number) == number * 5
    assert multiply_by_9(number) == number * 9
    assert multiply_by_11(number) == number * 11
    assert multiply_by_12(number) == number * 12
    assert multiply_by_15(number) == number * 15
    assert multiply_by_25(number) == number * 25
    assert multiply_by_50(number) == number * 50
    assert multiply_by_75(number) == number * 75
    assert multiply_by_99(number) == number * 99
    assert multiply_by_125(number) == number * 125
    assert multiply_by_999(number) == number * 999
    assert multiply_by_repeated_9(number, 4) == number * 9999


@pytest.mark.parametrize("number", [98, 102, 1004, 47, -103])
def test_square_near_base(number):
    assert square_near_base(number) == number * number


@pytest.mark.parametrize("number", [47, 49, 51, 56])
def test_square_near_50(number):
    assert square_near_50(number) == number * number


def test_cube_ending_in_5():
    assert cube_ending_in_5(15) == 15**3
    assert cube_ending_in_5(-25) == (-25) ** 3
    with pytest.raises(ValueError):
        cube_ending_in_5(24)


def test_division_and_percent_helpers():
    assert divide_by_5(125) == 25
    assert divide_by_25(125) == 5
    assert fraction_to_percent(1, 8) == 12.5
    assert percent_of(12.5, 80) == 10
    assert transpose_percent(12.5, 80) == percent_of(80, 12.5)


def test_divisibility_helpers():
    assert is_divisible_by_3(123)
    assert is_divisible_by_9(729)
    assert is_divisible_by_11(121)
    assert not is_divisible_by_11(123)


def test_recurring_decimal_unit_fraction():
    assert recurring_decimal_unit_fraction(2) == "0.5"
    assert recurring_decimal_unit_fraction(3) == "0.(3)"
    assert recurring_decimal_unit_fraction(19) == "0.(052631578947368421)"


def test_osculator_for_ending_9():
    assert osculator_for_ending_9(19) == 2
    assert osculator_for_ending_9(29) == 3
    with pytest.raises(ValueError):
        osculator_for_ending_9(21)


def test_perfect_roots():
    assert square_root_if_perfect(144) == 12
    assert square_root_if_perfect(145) is None
    assert cube_root_if_perfect(15625) == 25
    assert cube_root_if_perfect(-15625) == -25
    assert cube_root_if_perfect(15626) is None


def test_vedicmaths_alias():
    from vedicmaths import nikhilam_multiply as alias_nikhilam_multiply

    assert alias_nikhilam_multiply(98, 97) == 9506
