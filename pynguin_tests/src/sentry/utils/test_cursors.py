# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import cursors as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 1498
    none_type_0 = None
    cursor_0 = module_0.Cursor(int_0, int_0, has_results=none_type_0)
    assert (
        f"{type(module_0.Cursor.from_string).__module__}.{type(module_0.Cursor.from_string).__qualname__}"
        == "builtins.method"
    )
    int_1 = -889
    cursor_1 = module_0.Cursor(none_type_0, int_1, none_type_0)
    bool_0 = cursor_0.__bool__()
    cursor_0.__eq__(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    cursor_0 = module_0.Cursor(bool_0, bool_0, has_results=bool_0)
    assert (
        f"{type(module_0.Cursor.from_string).__module__}.{type(module_0.Cursor.from_string).__qualname__}"
        == "builtins.method"
    )
    bool_1 = cursor_0.__eq__(cursor_0)
    assert bool_1 is True
    s_c_i_m_cursor_0 = module_0.SCIMCursor(cursor_0)
    assert s_c_i_m_cursor_0.offset == 0
    assert (
        f"{type(module_0.SCIMCursor.from_string).__module__}.{type(module_0.SCIMCursor.from_string).__qualname__}"
        == "builtins.method"
    )
    str_0 = cursor_0.__repr__()
    assert str_0 == "<Cursor: value=True offset=1 is_prev=0>"
    bool_2 = cursor_0.__bool__()
    none_type_0 = None
    module_0.build_cursor(
        none_type_0, none_type_0, is_desc=bool_2, hits=s_c_i_m_cursor_0
    )


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = ""
    module_0.build_cursor(str_0, str_0, str_0)


def test_case_3():
    str_0 = ""
    none_type_0 = None
    cursor_result_0 = module_0.build_cursor(str_0, str_0, none_type_0)
    assert (
        f"{type(cursor_result_0).__module__}.{type(cursor_result_0).__qualname__}"
        == "cursors.CursorResult"
    )
    assert len(cursor_result_0) == 0


def test_case_4():
    str_0 = ""
    int_0 = -5060
    string_cursor_0 = module_0.StringCursor(str_0, int_0, int_0, str_0)
    assert (
        f"{type(module_0.StringCursor.from_string).__module__}.{type(module_0.StringCursor.from_string).__qualname__}"
        == "builtins.method"
    )
    cursor_result_0 = module_0.build_cursor(
        str_0, string_cursor_0, cursor=string_cursor_0, hits=int_0
    )
    assert (
        f"{type(cursor_result_0).__module__}.{type(cursor_result_0).__qualname__}"
        == "cursors.CursorResult"
    )
    assert len(cursor_result_0) == 0


@pytest.mark.xfail(strict=True)
def test_case_5():
    module_0.KeyCallable()


@pytest.mark.xfail(strict=True)
def test_case_6():
    none_type_0 = None
    string_cursor_0 = module_0.StringCursor(none_type_0)
    assert string_cursor_0.offset == 0
    assert (
        f"{type(module_0.StringCursor.from_string).__module__}.{type(module_0.StringCursor.from_string).__qualname__}"
        == "builtins.method"
    )
    str_0 = string_cursor_0.__repr__()
    assert str_0 == "<StringCursor: value=None offset=0 is_prev=0>"
    str_1 = string_cursor_0.__str__()
    assert str_1 == "None:0:0"
    cursor_result_0 = module_0.CursorResult(
        none_type_0, string_cursor_0, str_0, max_hits=none_type_0
    )
    assert (
        f"{type(cursor_result_0).__module__}.{type(cursor_result_0).__qualname__}"
        == "cursors.CursorResult"
    )
    assert cursor_result_0.results is None
    assert (
        f"{type(cursor_result_0.next).__module__}.{type(cursor_result_0.next).__qualname__}"
        == "cursors.StringCursor"
    )
    assert cursor_result_0.prev == "<StringCursor: value=None offset=0 is_prev=0>"
    assert cursor_result_0.hits is None
    assert cursor_result_0.max_hits is None
    cursor_result_0.__contains__(str_0)


def test_case_7():
    str_0 = ""
    int_0 = -5060
    string_cursor_0 = module_0.StringCursor(str_0, int_0, int_0, str_0)
    assert (
        f"{type(module_0.StringCursor.from_string).__module__}.{type(module_0.StringCursor.from_string).__qualname__}"
        == "builtins.method"
    )
    str_1 = string_cursor_0.__repr__()
    assert str_1 == "<StringCursor: value= offset=-5060 is_prev=1>"
    cursor_result_0 = module_0.build_cursor(
        str_0, string_cursor_0, cursor=string_cursor_0, hits=int_0
    )
    assert (
        f"{type(cursor_result_0).__module__}.{type(cursor_result_0).__qualname__}"
        == "cursors.CursorResult"
    )
    assert len(cursor_result_0) == 0
    cursor_result_1 = module_0.build_cursor(cursor_result_0, str_1, is_desc=int_0)
    assert (
        f"{type(cursor_result_1).__module__}.{type(cursor_result_1).__qualname__}"
        == "cursors.CursorResult"
    )
    assert len(cursor_result_1) == 0


def test_case_8():
    str_0 = ""
    int_0 = -5060
    string_cursor_0 = module_0.StringCursor(str_0, int_0, int_0, str_0)
    assert (
        f"{type(module_0.StringCursor.from_string).__module__}.{type(module_0.StringCursor.from_string).__qualname__}"
        == "builtins.method"
    )
    cursor_result_0 = module_0.build_cursor(
        str_0, string_cursor_0, cursor=string_cursor_0, hits=int_0
    )
    assert (
        f"{type(cursor_result_0).__module__}.{type(cursor_result_0).__qualname__}"
        == "cursors.CursorResult"
    )
    assert len(cursor_result_0) == 0
    cursor_result_1 = module_0.build_cursor(cursor_result_0, str_0, is_desc=int_0)
    assert (
        f"{type(cursor_result_1).__module__}.{type(cursor_result_1).__qualname__}"
        == "cursors.CursorResult"
    )
    assert len(cursor_result_1) == 0


@pytest.mark.xfail(strict=True)
def test_case_9():
    none_type_0 = None
    int_0 = -2413
    cursor_0 = module_0.Cursor(none_type_0, int_0, int_0, int_0)
    assert (
        f"{type(module_0.Cursor.from_string).__module__}.{type(module_0.Cursor.from_string).__qualname__}"
        == "builtins.method"
    )
    cursor_result_0 = module_0.CursorResult(none_type_0, cursor_0, cursor_0)
    assert (
        f"{type(cursor_result_0).__module__}.{type(cursor_result_0).__qualname__}"
        == "cursors.CursorResult"
    )
    assert cursor_result_0.results is None
    assert (
        f"{type(cursor_result_0.next).__module__}.{type(cursor_result_0.next).__qualname__}"
        == "cursors.Cursor"
    )
    assert (
        f"{type(cursor_result_0.prev).__module__}.{type(cursor_result_0.prev).__qualname__}"
        == "cursors.Cursor"
    )
    assert cursor_result_0.hits is None
    assert cursor_result_0.max_hits is None
    cursor_result_0.__iter__()


@pytest.mark.xfail(strict=True)
def test_case_10():
    int_0 = 371
    string_cursor_0 = module_0.StringCursor(int_0, has_results=int_0)
    assert string_cursor_0.offset == 0
    assert (
        f"{type(module_0.StringCursor.from_string).__module__}.{type(module_0.StringCursor.from_string).__qualname__}"
        == "builtins.method"
    )
    bool_0 = False
    s_c_i_m_cursor_0 = module_0.SCIMCursor(bool_0)
    assert s_c_i_m_cursor_0.offset == 0
    assert (
        f"{type(module_0.SCIMCursor.from_string).__module__}.{type(module_0.SCIMCursor.from_string).__qualname__}"
        == "builtins.method"
    )
    cursor_result_0 = module_0.CursorResult(int_0, string_cursor_0, bool_0)
    assert (
        f"{type(cursor_result_0).__module__}.{type(cursor_result_0).__qualname__}"
        == "cursors.CursorResult"
    )
    assert cursor_result_0.results == 371
    assert (
        f"{type(cursor_result_0.next).__module__}.{type(cursor_result_0.next).__qualname__}"
        == "cursors.StringCursor"
    )
    assert cursor_result_0.prev is False
    assert cursor_result_0.hits is None
    assert cursor_result_0.max_hits is None
    none_type_0 = None
    cursor_result_1 = module_0.CursorResult(bool_0, none_type_0, bool_0)
    cursor_result_2 = module_0.CursorResult(
        cursor_result_0, string_cursor_0, string_cursor_0
    )
    cursor_result_0.__repr__()


@pytest.mark.xfail(strict=True)
def test_case_11():
    str_0 = "(\nAHp<N((^\rD*G(nhh<N"
    none_type_0 = None
    module_0.build_cursor(str_0, str_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_12():
    str_0 = ""
    str_1 = "slack.client-secret"
    none_type_0 = None
    string_cursor_0 = module_0.StringCursor(str_0, is_prev=none_type_0)
    assert string_cursor_0.offset == 0
    assert (
        f"{type(module_0.StringCursor.from_string).__module__}.{type(module_0.StringCursor.from_string).__qualname__}"
        == "builtins.method"
    )
    none_type_1 = None
    cursor_0 = module_0.Cursor(none_type_1, is_prev=none_type_1)
    assert cursor_0.offset == 0
    assert (
        f"{type(module_0.Cursor.from_string).__module__}.{type(module_0.Cursor.from_string).__qualname__}"
        == "builtins.method"
    )
    str_2 = string_cursor_0.__repr__()
    assert str_2 == "<StringCursor: value= offset=0 is_prev=0>"
    module_0.build_cursor(str_0, str_0, on_results=str_1)


def test_case_13():
    str_0 = ""
    str_1 = "i_%{':=jIKl\"}daPU}"
    int_0 = -5060
    string_cursor_0 = module_0.StringCursor(str_1, int_0, int_0, str_0)
    assert (
        f"{type(module_0.StringCursor.from_string).__module__}.{type(module_0.StringCursor.from_string).__qualname__}"
        == "builtins.method"
    )
    none_type_0 = None
    str_2 = string_cursor_0.__repr__()
    assert str_2 == "<StringCursor: value=i_%{':=jIKl\"}daPU} offset=-5060 is_prev=1>"
    cursor_result_0 = module_0.build_cursor(
        str_0, string_cursor_0, cursor=string_cursor_0, hits=none_type_0
    )
    assert (
        f"{type(cursor_result_0).__module__}.{type(cursor_result_0).__qualname__}"
        == "cursors.CursorResult"
    )
    assert len(cursor_result_0) == 0
    cursor_result_1 = module_0.build_cursor(cursor_result_0, str_1, is_desc=int_0)
    assert (
        f"{type(cursor_result_1).__module__}.{type(cursor_result_1).__qualname__}"
        == "cursors.CursorResult"
    )
    assert len(cursor_result_1) == 0


@pytest.mark.xfail(strict=True)
def test_case_14():
    str_0 = ""
    str_1 = ""
    str_2 = "slack.client-secret"
    none_type_0 = None
    string_cursor_0 = module_0.StringCursor(str_1)
    assert string_cursor_0.offset == 0
    assert (
        f"{type(module_0.StringCursor.from_string).__module__}.{type(module_0.StringCursor.from_string).__qualname__}"
        == "builtins.method"
    )
    cursor_0 = module_0.Cursor(str_2)
    assert cursor_0.offset == 0
    assert (
        f"{type(module_0.Cursor.from_string).__module__}.{type(module_0.Cursor.from_string).__qualname__}"
        == "builtins.method"
    )
    string_cursor_1 = module_0.StringCursor(str_0, has_results=none_type_0)
    assert string_cursor_1.offset == 0
    str_3 = string_cursor_0.__repr__()
    assert str_3 == "<StringCursor: value= offset=0 is_prev=0>"
    none_type_1 = None
    module_0.build_cursor(str_2, none_type_1, cursor=cursor_0)


@pytest.mark.xfail(strict=True)
def test_case_15():
    str_0 = ""
    none_type_0 = None
    string_cursor_0 = module_0.StringCursor(str_0, is_prev=none_type_0)
    assert string_cursor_0.offset == 0
    assert (
        f"{type(module_0.StringCursor.from_string).__module__}.{type(module_0.StringCursor.from_string).__qualname__}"
        == "builtins.method"
    )
    none_type_1 = None
    cursor_0 = module_0.Cursor(none_type_1, is_prev=none_type_1)
    assert cursor_0.offset == 0
    assert (
        f"{type(module_0.Cursor.from_string).__module__}.{type(module_0.Cursor.from_string).__qualname__}"
        == "builtins.method"
    )
    str_1 = string_cursor_0.__repr__()
    assert str_1 == "<StringCursor: value= offset=0 is_prev=0>"
    none_type_2 = None
    bool_0 = False
    cursor_1 = module_0.Cursor(str_1, is_prev=bool_0)
    assert cursor_1.value == "<StringCursor: value= offset=0 is_prev=0>"
    assert cursor_1.offset == 0
    cursor_result_0 = module_0.build_cursor(str_0, none_type_1, cursor=cursor_1)
    assert (
        f"{type(cursor_result_0).__module__}.{type(cursor_result_0).__qualname__}"
        == "cursors.CursorResult"
    )
    assert len(cursor_result_0) == 0
    var_0 = cursor_result_0.count(cursor_result_0)
    module_0.StringCursor(string_cursor_0, none_type_2, var_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_16():
    str_0 = "i_%{':=jIKl\"}daPU}"
    int_0 = 60
    string_cursor_0 = module_0.StringCursor(str_0, int_0, int_0)
    assert (
        f"{type(module_0.StringCursor.from_string).__module__}.{type(module_0.StringCursor.from_string).__qualname__}"
        == "builtins.method"
    )
    int_1 = -5060
    string_cursor_1 = module_0.StringCursor(str_0, int_1, int_1, str_0)
    str_1 = string_cursor_1.__repr__()
    assert str_1 == "<StringCursor: value=i_%{':=jIKl\"}daPU} offset=-5060 is_prev=1>"
    none_type_0 = None
    str_2 = string_cursor_1.__repr__()
    assert str_2 == "<StringCursor: value=i_%{':=jIKl\"}daPU} offset=-5060 is_prev=1>"
    module_0.build_cursor(
        str_2, string_cursor_1, cursor=string_cursor_1, hits=none_type_0
    )


@pytest.mark.xfail(strict=True)
def test_case_17():
    str_0 = "db spans are equivalent if their ops and hashes match. Other spans are\n        equivalent if their ops match."
    str_1 = "]f3"
    int_0 = 60
    string_cursor_0 = module_0.StringCursor(str_0, int_0, int_0)
    assert (
        f"{type(module_0.StringCursor.from_string).__module__}.{type(module_0.StringCursor.from_string).__qualname__}"
        == "builtins.method"
    )
    none_type_0 = None
    s_c_i_m_cursor_0 = module_0.SCIMCursor(none_type_0)
    assert s_c_i_m_cursor_0.offset == 0
    assert (
        f"{type(module_0.SCIMCursor.from_string).__module__}.{type(module_0.SCIMCursor.from_string).__qualname__}"
        == "builtins.method"
    )
    bool_0 = s_c_i_m_cursor_0.__bool__()
    int_1 = -5088
    string_cursor_1 = module_0.StringCursor(str_1, int_1, int_1, str_0)
    str_2 = string_cursor_1.__repr__()
    assert str_2 == "<StringCursor: value=]f3 offset=-5088 is_prev=1>"
    none_type_1 = None
    str_3 = string_cursor_1.__repr__()
    assert str_3 == "<StringCursor: value=]f3 offset=-5088 is_prev=1>"
    module_0.build_cursor(
        str_0, string_cursor_1, cursor=string_cursor_1, hits=none_type_1
    )


@pytest.mark.xfail(strict=True)
def test_case_18():
    str_0 = ""
    str_1 = "]f3"
    int_0 = 60
    string_cursor_0 = module_0.StringCursor(str_0, int_0, int_0)
    assert (
        f"{type(module_0.StringCursor.from_string).__module__}.{type(module_0.StringCursor.from_string).__qualname__}"
        == "builtins.method"
    )
    none_type_0 = None
    str_2 = string_cursor_0.__repr__()
    assert str_2 == "<StringCursor: value= offset=60 is_prev=1>"
    s_c_i_m_cursor_0 = module_0.SCIMCursor(none_type_0)
    assert s_c_i_m_cursor_0.offset == 0
    assert (
        f"{type(module_0.SCIMCursor.from_string).__module__}.{type(module_0.SCIMCursor.from_string).__qualname__}"
        == "builtins.method"
    )
    bool_0 = s_c_i_m_cursor_0.__bool__()
    int_1 = -5060
    string_cursor_1 = module_0.StringCursor(str_1, int_1, int_1, str_0)
    str_3 = string_cursor_1.__repr__()
    assert str_3 == "<StringCursor: value=]f3 offset=-5060 is_prev=1>"
    none_type_1 = None
    str_4 = string_cursor_1.__repr__()
    assert str_4 == "<StringCursor: value=]f3 offset=-5060 is_prev=1>"
    cursor_result_0 = module_0.build_cursor(
        str_0, string_cursor_1, int_1, cursor=string_cursor_1, hits=none_type_1
    )
    assert (
        f"{type(cursor_result_0).__module__}.{type(cursor_result_0).__qualname__}"
        == "cursors.CursorResult"
    )
    assert len(cursor_result_0) == 0
    var_0 = cursor_result_0.__contains__(string_cursor_1)
    var_0.__getitem__(var_0)