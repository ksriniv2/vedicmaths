"""Arithmetic techniques inspired by common Vedic mathematics methods.

The functions return plain integer answers by default. Companion ``*_steps``
functions return a trace that can be rendered in notebooks, CLIs, or teaching
apps.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Step:
    """One human-readable step in a worked calculation."""

    title: str
    expression: str
    value: int | str


@dataclass(frozen=True)
class OperationTrace:
    """A worked calculation result."""

    method: str
    inputs: tuple[int, ...]
    result: int
    steps: tuple[Step, ...]


def _sign(value: int) -> int:
    return -1 if value < 0 else 1


def _digits_reversed(value: int) -> list[int]:
    return [int(char) for char in reversed(str(abs(value)))]


def _require_non_negative(value: int, name: str) -> None:
    if value < 0:
        raise ValueError(f"{name} must be non-negative")


def _nearest_power_of_ten(value: int) -> int:
    if value == 0:
        return 10
    digits = len(str(abs(value)))
    lower = 10 ** (digits - 1)
    upper = 10**digits
    return lower if abs(value - lower) < abs(value - upper) else upper


def digital_root(number: int) -> int:
    """Return the digital root of an integer.

    ``digital_root(0)`` is ``0``. Negative values are treated by magnitude,
    which keeps the helper useful for arithmetic verification.
    """

    number = abs(number)
    if number == 0:
        return 0
    return 1 + ((number - 1) % 9)


def digit_sum(number: int) -> int:
    """Return the sum of decimal digits in ``number``."""

    return sum(int(char) for char in str(abs(number)))


def sum_digits_until_single(number: int) -> int:
    """Repeatedly sum digits until a single digit remains."""

    return digital_root(number)


def complement(number: int, base: int | None = None) -> int:
    """Return the complement of ``number`` from a base.

    If no base is supplied, the next power of ten is used. For example,
    ``complement(87)`` returns ``13`` because ``100 - 87 = 13``.
    """

    _require_non_negative(number, "number")
    if base is None:
        base = 10 ** len(str(number))
    if base <= number:
        raise ValueError("base must be greater than number")
    return base - number


def all_from_9_last_from_10(number: int) -> int:
    """Return the Nikhilam complement from the next power of ten."""

    return complement(number)


def left_to_right_add(a: int, b: int) -> int:
    """Add two non-negative integers from left to right."""

    return left_to_right_add_steps(a, b).result


def left_to_right_add_steps(a: int, b: int) -> OperationTrace:
    """Return a trace for left-to-right addition with carries."""

    _require_non_negative(a, "a")
    _require_non_negative(b, "b")
    width = max(len(str(a)), len(str(b)))
    left = str(a).zfill(width)
    right = str(b).zfill(width)
    carry = 0
    digits: list[str] = []
    steps: list[Step] = []

    for index in range(width - 1, -1, -1):
        total = int(left[index]) + int(right[index]) + carry
        digits.append(str(total % 10))
        steps.append(
            Step(
                f"Column {width - index}",
                f"{left[index]} + {right[index]} + carry {carry}",
                f"write {total % 10}, carry {total // 10}",
            )
        )
        carry = total // 10
    if carry:
        digits.append(str(carry))
        steps.append(Step("Final carry", str(carry), carry))

    result = int("".join(reversed(digits)))
    return OperationTrace(
        method="Left-to-right addition",
        inputs=(a, b),
        result=result,
        steps=tuple(reversed(steps)),
    )


def subtract_using_complement(a: int, b: int) -> int:
    """Subtract ``b`` from ``a`` using complements."""

    return subtract_using_complement_steps(a, b).result


def subtract_using_complement_steps(a: int, b: int) -> OperationTrace:
    """Return a trace for subtraction by complement."""

    _require_non_negative(a, "a")
    _require_non_negative(b, "b")
    if b > a:
        trace = subtract_using_complement_steps(b, a)
        return OperationTrace(
            method="Subtraction by complement",
            inputs=(a, b),
            result=-trace.result,
            steps=trace.steps + (Step("Apply sign", f"{a} - {b}", -trace.result),),
        )
    base = 10 ** max(len(str(a)), len(str(b)))
    comp = base - b
    raw = a + comp
    result = raw - base
    return OperationTrace(
        method="Subtraction by complement",
        inputs=(a, b),
        result=result,
        steps=(
            Step("Choose base", f"base = {base}", base),
            Step("Find complement", f"{base} - {b}", comp),
            Step("Add complement", f"{a} + {comp}", raw),
            Step("Drop base", f"{raw} - {base}", result),
        ),
    )


def vinculum_digits(number: int) -> tuple[int, ...]:
    """Represent a number with vinculum-style signed digits.

    Digits greater than 5 are replaced by their negative complement and a carry
    is moved left. The tuple is ordered from most significant to least.
    """

    _require_non_negative(number, "number")
    digits = _digits_reversed(number)
    result: list[int] = []
    carry = 0
    for digit in digits:
        value = digit + carry
        if value > 5:
            result.append(value - 10)
            carry = 1
        else:
            result.append(value)
            carry = 0
    if carry:
        result.append(carry)
    return tuple(reversed(result))


def multiply_by_9(number: int) -> int:
    """Multiply by 9 using ``10n - n``."""

    return number * 10 - number


def multiply_by_99(number: int) -> int:
    """Multiply by 99 using ``100n - n``."""

    return number * 100 - number


def multiply_by_999(number: int) -> int:
    """Multiply by 999 using ``1000n - n``."""

    return number * 1000 - number


def multiply_by_repeated_9(number: int, count: int) -> int:
    """Multiply by a number made of ``count`` nines, such as 9, 99, or 999."""

    if count <= 0:
        raise ValueError("count must be positive")
    return number * ((10**count) - 1)


def multiply_by_11(number: int) -> int:
    """Multiply by 11 using the adjacent-sum shortcut."""

    return multiply_by_11_steps(number).result


def multiply_by_11_steps(number: int) -> OperationTrace:
    """Return a trace for multiplying by 11."""

    sign = _sign(number)
    digits = [int(char) for char in str(abs(number))]
    work = [digits[0]]
    steps = [Step("First digit", str(digits[0]), digits[0])]
    for left, right in zip(digits, digits[1:]):
        total = left + right
        work.append(total)
        steps.append(Step("Adjacent sum", f"{left} + {right}", total))
    if len(digits) > 1:
        work.append(digits[-1])
        steps.append(Step("Last digit", str(digits[-1]), digits[-1]))
    carry = 0
    output: list[int] = []
    for value in reversed(work):
        total = value + carry
        output.append(total % 10)
        carry = total // 10
    while carry:
        output.append(carry % 10)
        carry //= 10
    result = int("".join(str(digit) for digit in reversed(output))) * sign
    return OperationTrace(
        method="Multiply by 11 using adjacent sums",
        inputs=(number,),
        result=result,
        steps=tuple(steps + [Step("Carry and combine", str(work), result)]),
    )


def multiply_by_12(number: int) -> int:
    """Multiply by 12 as ``10n + 2n``."""

    return number * 10 + number * 2


def multiply_by_15(number: int) -> int:
    """Multiply by 15 as ``10n + half of 10n``."""

    return number * 10 + number * 5


def multiply_by_25(number: int) -> int:
    """Multiply by 25 as ``100n / 4``."""

    return (number * 100) // 4


def multiply_by_5(number: int) -> int:
    """Multiply by 5 as ``10n / 2``."""

    return (number * 10) // 2


def multiply_by_50(number: int) -> int:
    """Multiply by 50 as ``100n / 2``."""

    return (number * 100) // 2


def multiply_by_125(number: int) -> int:
    """Multiply by 125 as ``1000n / 8``."""

    return (number * 1000) // 8


def multiply_by_75(number: int) -> int:
    """Multiply by 75 as ``3 * 100n / 4``."""

    return (number * 300) // 4


def square_near_base(number: int, base: int | None = None) -> int:
    """Square a number near a power-of-ten base."""

    return square_near_base_steps(number, base).result


def square_near_base_steps(number: int, base: int | None = None) -> OperationTrace:
    """Return a trace for squaring a number near a base."""

    if base is None:
        base = _nearest_power_of_ten(abs(number))
    if base <= 0:
        raise ValueError("base must be positive")
    x = abs(number)
    diff = x - base
    left = x + diff
    right = diff * diff
    result = (left * base) + right
    return OperationTrace(
        method="Squaring near a base",
        inputs=(number,),
        result=result,
        steps=(
            Step("Choose base", f"base = {base}", base),
            Step("Find deviation", f"{x} - {base}", diff),
            Step("Add deviation", f"{x} + ({diff})", left),
            Step("Square deviation", f"{diff} * {diff}", right),
            Step("Combine", f"({left} * {base}) + {right}", result),
        ),
    )


def square_near_50(number: int) -> int:
    """Square a number near 50 using base 100 and half adjustment."""

    diff = number - 50
    return ((25 + diff) * 100) + (diff * diff)


def cube_ending_in_5(number: int) -> int:
    """Return the cube of a number ending in 5."""

    if abs(number) % 10 != 5:
        raise ValueError("number must end in 5")
    return number**3


def divide_by_5(number: int) -> float:
    """Divide by 5 as ``2n / 10``."""

    return (number * 2) / 10


def divide_by_25(number: int) -> float:
    """Divide by 25 as ``4n / 100``."""

    return (number * 4) / 100


def fraction_to_percent(numerator: int, denominator: int) -> float:
    """Convert a fraction to percent."""

    if denominator == 0:
        raise ZeroDivisionError("denominator cannot be zero")
    return (numerator * 100) / denominator


def percent_of(percent: float, number: float) -> float:
    """Find ``percent`` percent of ``number``."""

    return (percent / 100) * number


def transpose_percent(percent: float, number: float) -> float:
    """Use ``a% of b = b% of a``."""

    return percent_of(number, percent)


def is_divisible_by_3(number: int) -> bool:
    """Return whether ``number`` is divisible by 3."""

    return digit_sum(number) % 3 == 0


def is_divisible_by_9(number: int) -> bool:
    """Return whether ``number`` is divisible by 9."""

    return digit_sum(number) % 9 == 0


def is_divisible_by_11(number: int) -> bool:
    """Return whether ``number`` is divisible by 11."""

    digits = [int(char) for char in str(abs(number))]
    alternating = sum(digits[::2]) - sum(digits[1::2])
    return alternating % 11 == 0


def casting_out_nines_check(a: int, b: int, result: int, operator: str = "*") -> bool:
    """Check an arithmetic result using the digital-root method.

    Supported operators are ``"+"``, ``"-"``, and ``"*"``. This is a
    consistency check, not a proof: different wrong answers can share the same
    digital root.
    """

    if operator == "+":
        expected = digital_root(digital_root(a) + digital_root(b))
    elif operator == "-":
        expected = digital_root(digital_root(a) - digital_root(b))
    elif operator == "*":
        expected = digital_root(digital_root(a) * digital_root(b))
    else:
        raise ValueError("operator must be one of '+', '-', or '*'")
    return expected == digital_root(result)


def nikhilam_multiply(a: int, b: int, base: int | None = None) -> int:
    """Multiply using the Nikhilam base method and return the result."""

    return nikhilam_steps(a, b, base).result


def anurupyena_multiply(
    a: int,
    b: int,
    working_base: int,
    theoretical_base: int | None = None,
) -> int:
    """Multiply using a proportionate working base.

    This follows the Anurupyena idea used when numbers are nearer to a
    convenient multiple or sub-multiple of a power-of-ten base. For example,
    ``41 * 41`` can use working base ``50`` and theoretical base ``100``.
    """

    return anurupyena_steps(a, b, working_base, theoretical_base).result


def anurupyena_steps(
    a: int,
    b: int,
    working_base: int,
    theoretical_base: int | None = None,
) -> OperationTrace:
    """Return a trace for proportionate-base multiplication."""

    if working_base <= 0:
        raise ValueError("working_base must be positive")
    if theoretical_base is None:
        theoretical_base = 10 ** len(str(abs(working_base)))
    if theoretical_base <= 0:
        raise ValueError("theoretical_base must be positive")
    if theoretical_base % working_base != 0 and working_base % theoretical_base != 0:
        raise ValueError("bases must have an integer multiple/sub-multiple relationship")

    sign = _sign(a) * _sign(b)
    x, y = abs(a), abs(b)
    diff_x = x - working_base
    diff_y = y - working_base
    cross = x + diff_y
    right = diff_x * diff_y
    scale_num = working_base
    scale_den = theoretical_base
    left_scaled = (cross * scale_num) // scale_den
    if (cross * scale_num) % scale_den != 0:
        raise ValueError("scaled left side is fractional for these bases")
    result = sign * ((left_scaled * theoretical_base) + right)

    return OperationTrace(
        method="Anurupyena: proportionately",
        inputs=(a, b),
        result=result,
        steps=(
            Step("Choose bases", f"working {working_base}, theoretical {theoretical_base}", working_base),
            Step("Find deviations", f"{x} - {working_base}, {y} - {working_base}", f"{diff_x}, {diff_y}"),
            Step("Cross add/subtract", f"{x} + ({diff_y})", cross),
            Step("Scale left side", f"{cross} * {working_base} / {theoretical_base}", left_scaled),
            Step("Multiply deviations", f"({diff_x}) * ({diff_y})", right),
            Step("Combine", f"({left_scaled} * {theoretical_base}) + {right}", result),
        ),
    )


def recurring_decimal_unit_fraction(denominator: int, limit: int | None = None) -> str:
    """Return the recurring decimal expansion of ``1 / denominator``.

    The helper uses remainder tracking, which mirrors the teaching focus on
    recurring decimal cycles while staying reliable for any integer denominator.
    Repeating parts are wrapped in parentheses, e.g. ``1/19 = 0.(052631...)``.
    """

    if denominator == 0:
        raise ZeroDivisionError("denominator cannot be zero")
    sign = "-" if denominator < 0 else ""
    denominator = abs(denominator)
    remainder = 1 % denominator
    integer = 1 // denominator
    seen: dict[int, int] = {}
    digits: list[str] = []

    while remainder and remainder not in seen:
        if limit is not None and len(digits) >= limit:
            return f"{sign}{integer}." + "".join(digits)
        seen[remainder] = len(digits)
        remainder *= 10
        digits.append(str(remainder // denominator))
        remainder %= denominator

    if remainder == 0:
        return f"{sign}{integer}." + "".join(digits)
    start = seen[remainder]
    non_repeating = "".join(digits[:start])
    repeating = "".join(digits[start:])
    return f"{sign}{integer}.{non_repeating}({repeating})"


def osculator_for_ending_9(divisor: int) -> int:
    """Return the Ekadhika-style osculator for divisors ending in 9."""

    if divisor % 10 != 9:
        raise ValueError("divisor must end in 9")
    return (abs(divisor) // 10) + 1


def square_root_if_perfect(number: int) -> int | None:
    """Return the square root when ``number`` is a perfect square."""

    if number < 0:
        return None
    root = int(number**0.5)
    if root * root == number:
        return root
    if (root + 1) * (root + 1) == number:
        return root + 1
    return None


def cube_root_if_perfect(number: int) -> int | None:
    """Return the cube root when ``number`` is a perfect cube."""

    sign = _sign(number)
    value = abs(number)
    root = round(value ** (1 / 3))
    for candidate in range(max(0, root - 2), root + 3):
        if candidate**3 == value:
            return candidate * sign
    return None


def nikhilam_steps(a: int, b: int, base: int | None = None) -> OperationTrace:
    """Work multiplication around a nearby power-of-ten base.

    Example: ``98 * 97`` uses base ``100``. Differences are ``-2`` and ``-3``;
    left side is ``98 - 3 = 95`` and right side is ``(-2) * (-3) = 6``, padded
    to two digits, giving ``9506``.
    """

    if base is None:
        highest_digits = max(len(str(abs(a))), len(str(abs(b))))
        base = 10**highest_digits
    if base <= 0:
        raise ValueError("base must be a positive integer")

    sign = _sign(a) * _sign(b)
    x, y = abs(a), abs(b)
    diff_x = x - base
    diff_y = y - base
    left = x + diff_y
    right = diff_x * diff_y
    result = sign * ((left * base) + right)

    return OperationTrace(
        method="Nikhilam: all from 9 and the last from 10",
        inputs=(a, b),
        result=result,
        steps=(
            Step("Choose base", f"base = {base}", base),
            Step("Find deviations", f"{x} - {base}, {y} - {base}", f"{diff_x}, {diff_y}"),
            Step("Cross subtract", f"{x} + ({diff_y})", left),
            Step("Multiply deviations", f"({diff_x}) * ({diff_y})", right),
            Step("Combine", f"({left} * {base}) + ({right})", result),
        ),
    )


def urdhva_tiryagbhyam_multiply(a: int, b: int) -> int:
    """Multiply using the vertically-and-crosswise digit method."""

    return urdhva_tiryagbhyam_steps(a, b).result


def urdhva_tiryagbhyam_steps(a: int, b: int) -> OperationTrace:
    """Return a trace for vertically-and-crosswise multiplication.

    This implementation handles any integer size by convolving digit columns
    from right to left and carrying forward.
    """

    sign = _sign(a) * _sign(b)
    left_digits = _digits_reversed(a)
    right_digits = _digits_reversed(b)
    column_count = len(left_digits) + len(right_digits) - 1
    carry = 0
    output_digits: list[int] = []
    steps: list[Step] = []

    for column in range(column_count):
        pairs = [
            (i, column - i)
            for i in range(len(left_digits))
            if 0 <= column - i < len(right_digits)
        ]
        subtotal = sum(left_digits[i] * right_digits[j] for i, j in pairs)
        total = subtotal + carry
        output_digits.append(total % 10)
        next_carry = total // 10
        expression = " + ".join(
            f"{left_digits[i]}*{right_digits[j]}" for i, j in pairs
        )
        if carry:
            expression = f"{expression} + carry {carry}"
        steps.append(
            Step(
                f"Column {column + 1}",
                expression,
                f"write {total % 10}, carry {next_carry}",
            )
        )
        carry = next_carry

    while carry:
        output_digits.append(carry % 10)
        steps.append(Step("Carry", str(carry), f"write {carry % 10}"))
        carry //= 10

    result = int("".join(str(digit) for digit in reversed(output_digits))) * sign
    steps.append(Step("Apply sign", f"sign({a}) * sign({b})", result))

    return OperationTrace(
        method="Urdhva Tiryagbhyam: vertically and crosswise",
        inputs=(a, b),
        result=result,
        steps=tuple(steps),
    )


def square_ending_in_5(number: int) -> int:
    """Square an integer ending in 5 using the Ekadhikena Purvena pattern."""

    return square_ending_in_5_steps(number).result


def square_ending_in_5_steps(number: int) -> OperationTrace:
    """Return a trace for squaring numbers ending in 5.

    For ``n = 10a + 5``, ``n^2 = a * (a + 1)`` followed by ``25``.
    """

    if abs(number) % 10 != 5:
        raise ValueError("number must end in 5")

    prefix = abs(number) // 10
    left = prefix * (prefix + 1)
    result = (left * 100) + 25
    return OperationTrace(
        method="Ekadhikena Purvena: by one more than the previous one",
        inputs=(number,),
        result=result,
        steps=(
            Step("Separate prefix", f"{abs(number)} = 10*{prefix} + 5", prefix),
            Step("Multiply by next number", f"{prefix} * {prefix + 1}", left),
            Step("Append 25", f"{left} followed by 25", result),
        ),
    )
