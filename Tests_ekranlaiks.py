import pytest

from Programma_ekranlaiks import jautajumi

def test_aprekinat_punktus_minimalie():
    # Minimālie punkti
    punkti = ["2", "1", "1", "1", "1", "1"]
    assert jautajumi(punkti) == 6

def test_aprekinat_punktus_maksimalie():
    # Maksimālie punkti
    punkti = ["1", "6", "4", "5", "5", "4"]
    assert jautajumi(punkti) == 23

def test_aprekinat_punktus_1var():
    #1
    punkti = ["1", "3", "2", "3", "3", "2"]
    assert jautajumi(punkti) == 12

def test_aprekinat_punktus_2var():
    #2
    punkti = ["1", "7", "1", "1", "1", "1"]
    assert jautajumi(punkti) == 11

def test_aprekinat_punktus_3var():
    #3
    punkti = ["2", "2", "1", "1", "4", "1"]
    assert jautajumi(punkti) == 9

def test_aprekinat_punktus_4var():
    #4
    punkti = ["2", "2", "1", "1", "1", "4"]
    assert jautajumi(punkti) == 9
