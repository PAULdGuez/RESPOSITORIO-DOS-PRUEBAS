"""Unit test stub for freddy sync mapping."""


def test_lookup_returns_none_for_empty_email():
    from sync_freddy_v3_2 import lookup_freddy_by_email
    assert lookup_freddy_by_email("") is None
