import pytest
from romanizer import Romanizer

def romanize(text):
    r = Romanizer(text)
    return r.romanize()

def test_simple():
    assert romanize("안녕하세요") == "annyeonghaseyo"

def test_spaced_text():
    assert romanize("아이유 방탄소년단") == "aiyu bangtansonyeondan"

def test_onset_g_d_b():
    assert romanize("구미") == "gumi"
    assert romanize("영동") == "yeongdong"
    assert romanize("한밭") == "hanbat"

def test_coda_g_d_b():
    assert romanize("밝다") == "bakda"
    assert romanize("바닷가") == "badatga"
    assert romanize("없다") == "eopda"
    assert romanize("앞만") == "apman"

def test_r_l():
    assert romanize("구리") == "guri"
    assert romanize("설악") == "seorak"
    assert romanize("울릉") == "ulleung"
    assert romanize("대관령") == "daegwallyeong"
