# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import common_untyped as module_0


def test_case_0():
    pass


@pytest.mark.xfail(strict=True)
def test_case_1():
    dict_0 = {}
    module_0.has_region_name(dict_0, dict_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\x85R\xa5\xc4\xe0\xf4\x1d\xbf"
    module_0.apply_decorators(bytes_0, bytes_0, bytes_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = " Jzi}R{KW8_5y"
    keywords_0 = module_0.Keywords(str_0)
    none_type_0 = None
    keywords_0.check(none_type_0)


def test_case_4():
    bytes_0 = b""
    var_0 = module_0.apply_decorators(bytes_0, bytes_0, bytes_0, bytes_0)


def test_case_5():
    bytes_0 = b""
    keywords_0 = module_0.Keywords(bytes_0)
    var_0 = keywords_0.check(keywords_0)
    assert var_0 is False


@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = " Jzi}R{KW8_5y"
    keywords_0 = module_0.Keywords(str_0)
    var_0 = keywords_0.check(str_0)
    assert var_0 is True
    none_type_0 = None
    keywords_0.check(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_7():
    bytes_0 = b""
    bytes_1 = b"."
    module_0.apply_decorators(bytes_0, bytes_1, bytes_0, bytes_1)
