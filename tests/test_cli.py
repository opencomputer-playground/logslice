from logslice.cli import parse_ts


def test_parse_ts():
    assert parse_ts("2026-01-01T10:00:00 hello").hour == 10
