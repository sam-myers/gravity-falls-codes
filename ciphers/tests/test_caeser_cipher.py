from ciphers.caeser import transform_text


def test_shift_zero():
    assert transform_text("abc", 0) == "abc"


def test_shift_one():
    assert transform_text("abc", 1) == "bcd"


def test_shift_negative_one():
    assert transform_text("abc", -1) == "zab"


def test_punctuation_unchanged():
    assert transform_text(", .!?", 1) == ", .!?"


def test_undoes_itself():
    text = "foo bar biz baz!"
    assert transform_text(transform_text(text, 1), -1) == text
