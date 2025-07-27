# unittesty - testy jednostkowe
# pytest - testowanie
# pip install pytest
# Asercje to instrukcje służace do sprawdzania poprawności założeń w kodzie
# pytest szuka plików z nazwą test_*.py i *_test.py
# pytest test1_unitesty.py
# pytest tests/   - katalog z testami
from unittest import TestCase


class TryTesting(TestCase):
    def test_always_passed(self):
        self.assertTrue(True)

    def test_uppercase(self):
        # sprawdzenie wyniku działania funkcji upper()
        assert 'python'.upper() == "PYTHON"

    def test_reversed(self):
        assert list(reversed([1, 2, 3])) == [3, 2, 1]

    def test_reversed_test_case_style(self):
        self.assertEqual(
            list(reversed([1, 2, 3])),
            [3, 2, 1],
            "Odwróćenie listy [1, 2, 3], powinno dać [3, 2, 1]"
        )

    def test_always_fail(self):
        self.assertTrue(False, "Ten test celowo zawsze nie przejdzie")
    # >       self.assertTrue(False)
    # E       AssertionError: False is not true

# (.venv) radoslawjaniak@mac testowanie % pytest test_1_unitesty.py
# ================================================================== test session starts ===================================================================
# platform darwin -- Python 3.13.2, pytest-8.4.1, pluggy-1.6.0
# rootdir: /Users/radoslawjaniak/PycharmProjects/Bootcamp-10-05-2025/day_14_28_07_2025/testowanie
# plugins: anyio-4.9.0
# collected 5 items
#
# test_1_unitesty.py F....                                                                                                                             [100%]
#
# ======================================================================== FAILURES ========================================================================
# ______________________________________________________________ TryTesting.test_always_fail _______________________________________________________________
#
# self = <zad1_unitesty.TryTesting testMethod=test_always_fail>
#
#     def test_always_fail(self):
# >       self.assertTrue(False, "Ten test celowo zawsze nie przejdzie")
# E       AssertionError: False is not true : Ten test celowo zawsze nie przejdzie
#
# test_1_unitesty.py:27: AssertionError
# ================================================================ short test summary info =================================================================
# FAILED test_1_unitesty.py::TryTesting::test_always_fail - AssertionError: False is not true : Ten test celowo zawsze nie przejdzie
# ============================================================== 1 failed, 4 passed in 0.03s ===============================================================
# (.venv) radoslawjaniak@mac testowanie %
