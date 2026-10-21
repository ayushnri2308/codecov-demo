from api.auth.login import login
from api.calculator.calculator import Calculator
from api.reports.summary import summarize
from lib.utils.numbers import clamp
from lib.utils.strings import slug


def test_calc():
    assert Calculator.add(1, 2) == 3


def test_login_ok():
    assert login('ayush') is True


def test_slug():
    assert slug('Hello World') == 'hello-world'


def test_summarize():
    assert summarize([1, 2])['count'] == 2


def test_clamp():
    assert clamp(5, 0, 10) == 5


# Intentionally leave api/billing, login.logout, and summary.unused_helper untested
# so folder/file coverage percentages differ for sort testing.
