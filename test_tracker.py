import pytest
import os
from datetime import date, timedelta
import tracker 

@pytest.fixture
def active():
    t = date.today()
    return [str(t - timedelta(days=2)), str(t - timedelta(days=1)), str(t)]

@pytest.fixture
def dead():
    t = date.today()
    return [str(t - timedelta(days=4)), str(t - timedelta(days=3))]

def test_streak_active(active):
    assert tracker.calculate_streak(active) == 3

def test_streak_dead(dead):
    assert tracker.calculate_streak(dead) == 0

def test_streak_empty():
    assert tracker.calculate_streak([]) == 0

def test_io(tmp_path, monkeypatch):
    f = tmp_path / "test.json"
    monkeypatch.setattr(tracker, "DATA_FILE", str(f))
    
    data = {"Gym": ["2026-01-01"], "Code": []}
    tracker.save_data(data)
    
    assert os.path.exists(f)
    assert tracker.load_data() == data
