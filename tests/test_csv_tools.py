from utils.csv_tools import csv_mean

def test_csv_mean_ok(tmp_path):
    p = tmp_path / "data.csv"
    p.write_text(
        "name,score\nAlice,10\nBob,20\nCara,\nDan,30\n",
        encoding="utf-8",
    )
    count, mean = csv_mean(p, "score")
    assert count == 3
    assert abs(mean - 20.0) < 1e-9

def test_csv_mean_bad_column(tmp_path):
    p = tmp_path / "data.csv"
    p.write_text("x,y\n1,2\n", encoding="utf-8")
    try:
        csv_mean(p, "score")
        assert False, "Expected KeyError"
    except KeyError:
        pass

def test_csv_mean_skips_blanks(tmp_path):
    p = tmp_path / "data_mixed.csv"
    p.write_text("name,score\nAlice,10\nBlank,\nBob,20\n", encoding="utf-8")
    count, mean = csv_mean(p, "score")
    assert count == 2
    assert abs(mean - 15.0) < 1e-9