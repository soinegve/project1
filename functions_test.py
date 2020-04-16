from functions import get_dekada

def test_dekada():
    assert get_dekada()[0] == 1




# Some more tests to show how to name tests (naming convention )


def test_get_dekada_first_number_should_be_one():
    assert get_dekada()[0] == 1

def test_get_dekada_last_number_should_be_ten():
    assert get_dekada()[-1] == 10










