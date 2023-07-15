# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import cursors_untyped as module_0


def test_case_0():
    bool_0 = True
    s_c_i_m_cursor_0 = module_0.SCIMCursor(bool_0, is_prev=bool_0, has_results=bool_0)
    assert s_c_i_m_cursor_0.offset == 0
    assert (
        f"{type(module_0.SCIMCursor.from_string).__module__}.{type(module_0.SCIMCursor.from_string).__qualname__}"
        == "builtins.method"
    )
    list_0 = []
    var_0 = s_c_i_m_cursor_0.__eq__(s_c_i_m_cursor_0)
    assert var_0 is True
    var_1 = module_0.build_cursor(list_0, list_0)
    assert (
        f"{type(var_1).__module__}.{type(var_1).__qualname__}"
        == "cursors_untyped.CursorResult"
    )
    assert len(var_1) == 0
    cursor_0 = module_0.Cursor(s_c_i_m_cursor_0, bool_0)
    assert (
        f"{type(module_0.Cursor.from_string).__module__}.{type(module_0.Cursor.from_string).__qualname__}"
        == "builtins.method"
    )
    var_2 = module_0.build_cursor(var_1, var_1, cursor=s_c_i_m_cursor_0, hits=list_0)
    assert (
        f"{type(var_2).__module__}.{type(var_2).__qualname__}"
        == "cursors_untyped.CursorResult"
    )
    assert len(var_2) == 0


def test_case_1():
    list_0 = []
    var_0 = module_0.build_cursor(list_0, list_0)
    assert (
        f"{type(var_0).__module__}.{type(var_0).__qualname__}"
        == "cursors_untyped.CursorResult"
    )
    assert len(var_0) == 0


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    module_0.build_cursor(bool_0, bool_0, is_desc=bool_0, cursor=bool_0, hits=bool_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    module_0.KeyCallable()


def test_case_4():
    int_0 = -2453
    s_c_i_m_cursor_0 = module_0.SCIMCursor(int_0, is_prev=int_0)
    assert s_c_i_m_cursor_0.offset == 0
    assert (
        f"{type(module_0.SCIMCursor.from_string).__module__}.{type(module_0.SCIMCursor.from_string).__qualname__}"
        == "builtins.method"
    )


def test_case_5():
    bool_0 = True
    s_c_i_m_cursor_0 = module_0.SCIMCursor(bool_0, is_prev=bool_0, has_results=bool_0)
    assert s_c_i_m_cursor_0.offset == 0
    assert (
        f"{type(module_0.SCIMCursor.from_string).__module__}.{type(module_0.SCIMCursor.from_string).__qualname__}"
        == "builtins.method"
    )
    list_0 = []
    var_0 = module_0.build_cursor(list_0, list_0)
    assert (
        f"{type(var_0).__module__}.{type(var_0).__qualname__}"
        == "cursors_untyped.CursorResult"
    )
    assert len(var_0) == 0
    var_1 = module_0.build_cursor(var_0, var_0, cursor=s_c_i_m_cursor_0, hits=list_0)
    assert (
        f"{type(var_1).__module__}.{type(var_1).__qualname__}"
        == "cursors_untyped.CursorResult"
    )
    assert len(var_1) == 0
    var_2 = s_c_i_m_cursor_0.__str__()
    assert var_2 == "True:0:1"


def test_case_6():
    bool_0 = True
    s_c_i_m_cursor_0 = module_0.SCIMCursor(bool_0, is_prev=bool_0, has_results=bool_0)
    assert s_c_i_m_cursor_0.offset == 0
    assert (
        f"{type(module_0.SCIMCursor.from_string).__module__}.{type(module_0.SCIMCursor.from_string).__qualname__}"
        == "builtins.method"
    )
    list_0 = []
    var_0 = module_0.build_cursor(list_0, list_0)
    assert (
        f"{type(var_0).__module__}.{type(var_0).__qualname__}"
        == "cursors_untyped.CursorResult"
    )
    assert len(var_0) == 0
    var_1 = module_0.build_cursor(var_0, var_0, cursor=s_c_i_m_cursor_0, hits=list_0)
    assert (
        f"{type(var_1).__module__}.{type(var_1).__qualname__}"
        == "cursors_untyped.CursorResult"
    )
    assert len(var_1) == 0
    var_2 = s_c_i_m_cursor_0.__repr__()
    assert var_2 == "<SCIMCursor: value=True offset=0 is_prev=1>"


def test_case_7():
    bool_0 = True
    s_c_i_m_cursor_0 = module_0.SCIMCursor(bool_0, is_prev=bool_0, has_results=bool_0)
    assert s_c_i_m_cursor_0.offset == 0
    assert (
        f"{type(module_0.SCIMCursor.from_string).__module__}.{type(module_0.SCIMCursor.from_string).__qualname__}"
        == "builtins.method"
    )
    list_0 = []
    var_0 = s_c_i_m_cursor_0.__bool__()
    var_1 = module_0.build_cursor(list_0, list_0)
    assert (
        f"{type(var_1).__module__}.{type(var_1).__qualname__}"
        == "cursors_untyped.CursorResult"
    )
    assert len(var_1) == 0
    var_2 = module_0.build_cursor(var_1, var_1, cursor=s_c_i_m_cursor_0, hits=list_0)
    assert (
        f"{type(var_2).__module__}.{type(var_2).__qualname__}"
        == "cursors_untyped.CursorResult"
    )
    assert len(var_2) == 0


def test_case_8():
    bool_0 = True
    cursor_result_0 = module_0.CursorResult(bool_0, bool_0, bool_0, bool_0, bool_0)
    assert (
        f"{type(cursor_result_0).__module__}.{type(cursor_result_0).__qualname__}"
        == "cursors_untyped.CursorResult"
    )
    assert cursor_result_0.results is True
    assert cursor_result_0.next is True
    assert cursor_result_0.prev is True
    assert cursor_result_0.hits is True
    assert cursor_result_0.max_hits is True


def test_case_9():
    bool_0 = True
    s_c_i_m_cursor_0 = module_0.SCIMCursor(bool_0, is_prev=bool_0, has_results=bool_0)
    assert s_c_i_m_cursor_0.offset == 0
    assert (
        f"{type(module_0.SCIMCursor.from_string).__module__}.{type(module_0.SCIMCursor.from_string).__qualname__}"
        == "builtins.method"
    )
    list_0 = []
    var_0 = module_0.build_cursor(list_0, list_0)
    assert (
        f"{type(var_0).__module__}.{type(var_0).__qualname__}"
        == "cursors_untyped.CursorResult"
    )
    assert len(var_0) == 0
    var_1 = module_0.build_cursor(var_0, var_0, cursor=s_c_i_m_cursor_0, hits=list_0)
    assert (
        f"{type(var_1).__module__}.{type(var_1).__qualname__}"
        == "cursors_untyped.CursorResult"
    )
    assert len(var_1) == 0


@pytest.mark.xfail(strict=True)
def test_case_10():
    bool_0 = False
    none_type_0 = None
    cursor_result_0 = module_0.CursorResult(
        bool_0, bool_0, none_type_0, max_hits=bool_0
    )
    assert (
        f"{type(cursor_result_0).__module__}.{type(cursor_result_0).__qualname__}"
        == "cursors_untyped.CursorResult"
    )
    assert cursor_result_0.results is False
    assert cursor_result_0.next is False
    assert cursor_result_0.prev is None
    assert cursor_result_0.hits is None
    assert cursor_result_0.max_hits is False
    cursor_result_0.__iter__()


def test_case_11():
    list_0 = []
    var_0 = module_0.build_cursor(list_0, list_0)
    assert (
        f"{type(var_0).__module__}.{type(var_0).__qualname__}"
        == "cursors_untyped.CursorResult"
    )
    assert len(var_0) == 0
    var_1 = var_0.__str__()
    assert var_1 == "<CursorResult: results=0>"


@pytest.mark.xfail(strict=True)
def test_case_12():
    bytes_0 = b"O\x1f\xca\x17\xaae\rxw\x14\x04\x08P+\xb85\xcc\x92"
    module_0.build_cursor(bytes_0, bytes_0, max_hits=bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_13():
    bool_0 = True
    cursor_result_0 = module_0.CursorResult(bool_0, bool_0, bool_0, bool_0, bool_0)
    assert (
        f"{type(cursor_result_0).__module__}.{type(cursor_result_0).__qualname__}"
        == "cursors_untyped.CursorResult"
    )
    assert cursor_result_0.results is True
    assert cursor_result_0.next is True
    assert cursor_result_0.prev is True
    assert cursor_result_0.hits is True
    assert cursor_result_0.max_hits is True
    cursor_result_0.__getitem__(cursor_result_0)


@pytest.mark.xfail(strict=True)
def test_case_14():
    bool_0 = True
    s_c_i_m_cursor_0 = module_0.SCIMCursor(bool_0, is_prev=bool_0, has_results=bool_0)
    assert s_c_i_m_cursor_0.offset == 0
    assert (
        f"{type(module_0.SCIMCursor.from_string).__module__}.{type(module_0.SCIMCursor.from_string).__qualname__}"
        == "builtins.method"
    )
    list_0 = []
    var_0 = module_0.build_cursor(list_0, list_0)
    assert (
        f"{type(var_0).__module__}.{type(var_0).__qualname__}"
        == "cursors_untyped.CursorResult"
    )
    assert len(var_0) == 0
    var_1 = module_0.build_cursor(var_0, var_0, cursor=s_c_i_m_cursor_0, hits=list_0)
    assert (
        f"{type(var_1).__module__}.{type(var_1).__qualname__}"
        == "cursors_untyped.CursorResult"
    )
    assert len(var_1) == 0
    module_0.build_cursor(
        list_0, var_0, is_desc=var_0, hits=list_0, on_results=s_c_i_m_cursor_0
    )


def test_case_15():
    bool_0 = True
    s_c_i_m_cursor_0 = module_0.SCIMCursor(bool_0, is_prev=bool_0, has_results=bool_0)
    assert s_c_i_m_cursor_0.offset == 0
    assert (
        f"{type(module_0.SCIMCursor.from_string).__module__}.{type(module_0.SCIMCursor.from_string).__qualname__}"
        == "builtins.method"
    )
    list_0 = []
    var_0 = module_0.build_cursor(list_0, list_0, cursor=s_c_i_m_cursor_0, hits=list_0)
    assert (
        f"{type(var_0).__module__}.{type(var_0).__qualname__}"
        == "cursors_untyped.CursorResult"
    )
    assert len(var_0) == 0


@pytest.mark.xfail(strict=True)
def test_case_16():
    int_0 = -2358
    string_cursor_0 = module_0.StringCursor(int_0)
    assert string_cursor_0.offset == 0
    assert (
        f"{type(module_0.StringCursor.from_string).__module__}.{type(module_0.StringCursor.from_string).__qualname__}"
        == "builtins.method"
    )
    var_0 = string_cursor_0.__str__()
    assert var_0 == "-2358:0:0"
    list_0 = []
    var_1 = module_0.build_cursor(list_0, list_0)
    assert (
        f"{type(var_1).__module__}.{type(var_1).__qualname__}"
        == "cursors_untyped.CursorResult"
    )
    assert len(var_1) == 0
    module_0.build_cursor(
        var_0, int_0, cursor=string_cursor_0, hits=var_0, on_results=int_0
    )


@pytest.mark.xfail(strict=True)
def test_case_17():
    bool_0 = True
    int_0 = -2370
    string_cursor_0 = module_0.StringCursor(bool_0)
    assert string_cursor_0.offset == 0
    assert (
        f"{type(module_0.StringCursor.from_string).__module__}.{type(module_0.StringCursor.from_string).__qualname__}"
        == "builtins.method"
    )
    var_0 = module_0.CursorResult(int_0, int_0, string_cursor_0)
    assert (
        f"{type(var_0).__module__}.{type(var_0).__qualname__}"
        == "cursors_untyped.CursorResult"
    )
    assert var_0.results == -2370
    assert var_0.next == -2370
    assert (
        f"{type(var_0.prev).__module__}.{type(var_0.prev).__qualname__}"
        == "cursors_untyped.StringCursor"
    )
    assert var_0.hits is None
    assert var_0.max_hits is None
    var_1 = int_0.__repr__()
    var_2 = string_cursor_0.__bool__()
    list_0 = []
    var_3 = module_0.build_cursor(list_0, list_0)
    assert (
        f"{type(var_3).__module__}.{type(var_3).__qualname__}"
        == "cursors_untyped.CursorResult"
    )
    assert len(var_3) == 0
    var_4 = string_cursor_0.__str__()
    assert var_4 == "True:0:0"
    var_5 = string_cursor_0.__str__()
    assert var_5 == "True:0:0"
    module_0.build_cursor(
        list_0, int_0, cursor=string_cursor_0, hits=list_0, on_results=int_0
    )


@pytest.mark.xfail(strict=True)
def test_case_18():
    bool_0 = True
    int_0 = -2370
    string_cursor_0 = module_0.StringCursor(int_0, bool_0, int_0)
    assert (
        f"{type(module_0.StringCursor.from_string).__module__}.{type(module_0.StringCursor.from_string).__qualname__}"
        == "builtins.method"
    )
    var_0 = string_cursor_0.__repr__()
    assert var_0 == "<StringCursor: value=-2370 offset=1 is_prev=1>"
    var_1 = var_0.__repr__()
    assert var_1 == "'<StringCursor: value=-2370 offset=1 is_prev=1>'"
    module_0.build_cursor(
        var_0, int_0, cursor=string_cursor_0, hits=var_0, on_results=int_0
    )


@pytest.mark.xfail(strict=True)
def test_case_19():
    bool_0 = True
    s_c_i_m_cursor_0 = module_0.SCIMCursor(bool_0, is_prev=bool_0, has_results=bool_0)
    assert s_c_i_m_cursor_0.offset == 0
    assert (
        f"{type(module_0.SCIMCursor.from_string).__module__}.{type(module_0.SCIMCursor.from_string).__qualname__}"
        == "builtins.method"
    )
    list_0 = []
    var_0 = module_0.build_cursor(list_0, list_0)
    assert (
        f"{type(var_0).__module__}.{type(var_0).__qualname__}"
        == "cursors_untyped.CursorResult"
    )
    assert len(var_0) == 0
    float_0 = -31.0
    var_1 = module_0.build_cursor(
        var_0, var_0, float_0, cursor=s_c_i_m_cursor_0, hits=list_0, max_hits=var_0
    )
    assert (
        f"{type(var_1).__module__}.{type(var_1).__qualname__}"
        == "cursors_untyped.CursorResult"
    )
    assert len(var_1) == 0
    var_2 = var_0.__contains__(var_1)
    var_2.__getitem__(var_1)