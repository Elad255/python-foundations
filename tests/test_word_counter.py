
from utils.word_counter import count_words, top_n

def test_count_words_and_top_n(tmp_path):
    p=tmp_path/"sample.txt"
    p.write_text("Hello hello world! Don't stop, world.", encoding="utf-8")

    total,freqs=count_words(p)
    assert total==6
    assert freqs["hello"] == 2
    assert freqs["world"] == 2
    assert ("world", 2) in top_n(freqs, 2)


def test_invalid_file_raises(tmp_path):
    missing = tmp_path / "nope.txt"
    try:
        count_words(missing)
        assert False, "Expected FileNotFoundError"
    except FileNotFoundError:
        pass
