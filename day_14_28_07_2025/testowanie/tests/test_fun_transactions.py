import fun_transactions as ft


def test_filter_transactions_income():
    expected_list = [
        {"id": 1, "type": "income", "amount": 1000, "currency": "USD"},
        {"id": 3, "type": "income", "amount": 500, "currency": "USD"},
        {"id": 5, "type": "income", "amount": 700, "currency": "USD"},
        {"id": 7, "type": "income", "amount": 100, "currency": "EUR"},
    ]

    assert ft.filter_transactions(ft.transactions, "income") == expected_list


def test_map_transactions_usd():
    result = [1000, 200, 500, 300, 700, 0, 0]
    assert ft.map_transactions(ft.transactions, "USD") == result


def test_reduce_transactions():
    assert ft.reduce_transactions([1000, 500, 700, 0]) == 2200


def test_process_transactions_expense_eur():
    assert ft.process_transactions(ft.transactions, "expense", "EUR")
# Testing started at 14:07 ...
# Launching pytest with arguments /Users/radoslawjaniak/PycharmProjects/Bootcamp-10-05-2025/day_14_28_07_2025/testowanie/tests/test_fun_transactions.py --no-header --no-summary -q in /Users/radoslawjaniak/PycharmProjects/Bootcamp-10-05-2025/day_14_28_07_2025/testowanie/tests
#
# ============================= test session starts ==============================
# collecting ... collected 4 items
#
# test_fun_transactions.py::test_filter_transactions_income PASSED         [ 25%]
# test_fun_transactions.py::test_map_transactions_usd PASSED               [ 50%]
# test_fun_transactions.py::test_reduce_transactions PASSED                [ 75%]
# test_fun_transactions.py::test_process_transactions_expense_eur PASSED   [100%]
#
# ============================== 4 passed in 0.01s ===============================
#
# Process finished with exit code 0
