# Vedic Mathematics

Python helpers for learning and applying Vedic mathematics techniques. The
library focuses on two things:

- returning correct arithmetic results as simple Python values
- exposing step-by-step workings that teachers, students, notebooks, and apps
  can display

This project is early-stage and intended to grow into an open-source package of
well-tested Vedic mathematics methods.

The first implementation pass is guided by the parsed source chunks in the
larger Mr Rishi project, especially
`data/processed/Vedic_mathematics_chunks.jsonl`.

## Install for Development

```powershell
git clone https://github.com/ksriniv2/vedicmaths.git
cd vedicmaths
python -m pip install -e ".[dev]"
```

If you are working from this local starter folder:

```powershell
cd C:\Users\KARTH\OneDrive\Documents\vedicmathematics
python -m pip install -e ".[dev]"
```

## Quick Start

```python
from vedicmathematics import (
    nikhilam_multiply,
    nikhilam_steps,
    square_ending_in_5,
    urdhva_tiryagbhyam_multiply,
)

print(nikhilam_multiply(98, 97))
# 9506

print(urdhva_tiryagbhyam_multiply(123, 456))
# 56088

print(square_ending_in_5(35))
# 1225

trace = nikhilam_steps(98, 97)
for step in trace.steps:
    print(step.title, step.expression, "=>", step.value)
```

You can also use the shorter package alias:

```python
from vedicmaths import nikhilam_multiply
```

## Available Functions

| Function | Purpose |
|---|---|
| `digit_sum(number)` | Sums the decimal digits of a number. |
| `sum_digits_until_single(number)` | Repeated digit sum, equivalent to digital root. |
| `nikhilam_multiply(a, b, base=None)` | Multiplies numbers using a nearby base, commonly a power of ten. |
| `nikhilam_steps(a, b, base=None)` | Returns the worked steps for Nikhilam multiplication. |
| `anurupyena_multiply(a, b, working_base, theoretical_base=None)` | Proportionate-base multiplication when a multiple or sub-multiple is more convenient. |
| `anurupyena_steps(a, b, working_base, theoretical_base=None)` | Worked steps for proportionate-base multiplication. |
| `urdhva_tiryagbhyam_multiply(a, b)` | General multiplication using the vertically-and-crosswise digit method. |
| `urdhva_tiryagbhyam_steps(a, b)` | Returns the worked steps for vertically-and-crosswise multiplication. |
| `left_to_right_add(a, b)` | Addition with a trace-friendly column process. |
| `left_to_right_add_steps(a, b)` | Worked steps for addition. |
| `subtract_using_complement(a, b)` | Subtraction by complementing the subtrahend from a power of ten. |
| `subtract_using_complement_steps(a, b)` | Worked steps for complement subtraction. |
| `complement(number, base=None)` | Complement from a supplied base or next power of ten. |
| `all_from_9_last_from_10(number)` | Nikhilam-style complement helper. |
| `vinculum_digits(number)` | Signed digit representation for digits above 5. |
| `multiply_by_5(number)` | Shortcut for multiplication by 5. |
| `multiply_by_9(number)` | Shortcut for multiplication by 9. |
| `multiply_by_11(number)` | Adjacent-sum shortcut for multiplication by 11. |
| `multiply_by_11_steps(number)` | Worked steps for multiplication by 11. |
| `multiply_by_12(number)` | Shortcut for multiplication by 12. |
| `multiply_by_15(number)` | Shortcut for multiplication by 15. |
| `multiply_by_25(number)` | Shortcut for multiplication by 25. |
| `multiply_by_50(number)` | Shortcut for multiplication by 50. |
| `multiply_by_75(number)` | Shortcut for multiplication by 75. |
| `multiply_by_99(number)` | Shortcut for multiplication by 99. |
| `multiply_by_125(number)` | Shortcut for multiplication by 125. |
| `multiply_by_999(number)` | Shortcut for multiplication by 999. |
| `multiply_by_repeated_9(number, count)` | Multiply by 9, 99, 999, etc. |
| `square_ending_in_5(number)` | Squares numbers ending in 5 using the "one more than the previous" pattern. |
| `square_ending_in_5_steps(number)` | Returns the worked steps for squaring a number ending in 5. |
| `square_near_base(number, base=None)` | Squares numbers close to a power-of-ten base. |
| `square_near_base_steps(number, base=None)` | Worked steps for near-base squaring. |
| `square_near_50(number)` | Shortcut for squaring values near 50. |
| `cube_ending_in_5(number)` | Cubes numbers ending in 5. |
| `divide_by_5(number)` | Division by 5 as doubling then dividing by 10. |
| `divide_by_25(number)` | Division by 25 as multiplying by 4 then dividing by 100. |
| `recurring_decimal_unit_fraction(denominator, limit=None)` | Decimal expansion of `1 / denominator`, with repeating cycles in parentheses. |
| `osculator_for_ending_9(divisor)` | Ekadhika-style osculator for divisors ending in 9. |
| `fraction_to_percent(numerator, denominator)` | Converts fractions to percentages. |
| `percent_of(percent, number)` | Calculates percent of a number. |
| `transpose_percent(percent, number)` | Uses `a% of b = b% of a`. |
| `is_divisible_by_3(number)` | Divisibility by 3 using digit sum. |
| `is_divisible_by_9(number)` | Divisibility by 9 using digit sum. |
| `is_divisible_by_11(number)` | Divisibility by 11 using alternating digit sums. |
| `square_root_if_perfect(number)` | Returns the integer square root for perfect squares, otherwise `None`. |
| `cube_root_if_perfect(number)` | Returns the integer cube root for perfect cubes, otherwise `None`. |
| `digital_root(number)` | Computes a number's digital root. |
| `casting_out_nines_check(a, b, result, operator="*")` | Verifies `+`, `-`, or `*` results using digital roots. |

## Example Step Trace

```python
from vedicmathematics import nikhilam_steps

trace = nikhilam_steps(98, 97)
print(trace.result)
# 9506

for step in trace.steps:
    print(f"{step.title}: {step.expression} = {step.value}")
```

Output:

```text
Choose base: base = 100 = 100
Find deviations: 98 - 100, 97 - 100 = -2, -3
Cross subtract: 98 + (-3) = 95
Multiply deviations: (-2) * (-3) = 6
Combine: (95 * 100) + (6) = 9506
```

## Roadmap

Good next functions to add:

- division using Paravartya Yojayet
- multiplication by 9, 99, 999, and related bases
- straight division and auxiliary fractions
- simple and complex oscillators for divisibility
- cube-root techniques
- fraction simplification and recurring decimal patterns
- richer renderers for traces, such as Markdown and HTML

## Development

Run tests:

```powershell
python -m pytest
```

Project structure:

```text
vedicmathematics/
  vedicmathematics/
    __init__.py
    arithmetic.py
  tests/
    test_arithmetic.py
  pyproject.toml
  README.md
```

## Contributing

Contributions are welcome. Please include:

- a clear function name and docstring
- tests for regular cases and edge cases
- a `*_steps` variant when the method is teachable step by step
- examples in the README when adding a major new method

## License

MIT
