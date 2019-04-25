from ciphers.atbash import transform_text


def test_sample_phrase():
    assert transform_text("abc") == "zyx"


def test_punctuation_unchanged():
    assert transform_text(", .!?") == ", .!?"


def test_undoes_itself():
    text = "foo bar biz baz!"
    assert transform_text(transform_text(text)) == text
