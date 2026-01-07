import builtins
import pytest

from keywait.key_wait import KEYWAIT


def test_continue_input(monkeypatch):
    monkeypatch.setattr(builtins, "input", lambda _: "c")

    # Should return normally (not exit)
    KEYWAIT.wait_for_key()


def test_quit_input(monkeypatch):
    monkeypatch.setattr(builtins, "input", lambda _: "q")

    with pytest.raises(SystemExit):
        KEYWAIT.wait_for_key()


def test_invalid_then_continue(monkeypatch):
    inputs = iter(["x", "c"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    # Should loop once, then continue
    KEYWAIT.wait_for_key()


def test_whitespace_and_case(monkeypatch):
    monkeypatch.setattr(builtins, "input", lambda _: "  C ")

    KEYWAIT.wait_for_key()

