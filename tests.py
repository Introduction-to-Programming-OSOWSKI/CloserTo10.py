#DO NOT TAMPER WITH THIS FILE
#ANY EDITS YOU MAKE TO THIS FILE WILL BE SAVED TO YOUR PUBLIC GITHUB HISTORY
#TAMPERING WITH THIS FILE WILL BE OBVIOUS AND WILL RESULT IN A ZERO

import main;
import datetime;

year = 2022
month = 9
day = 24

def test_code():
    assert main.close10(5, 13) == 13, "close10(5, 13)  == 13 failed"
    assert main.close10(5, 15) == 0, "close10(5, 15) == 0 failed"
    assert main.close10(1, 135) == 1, "close10(1, 135) == 1 failed"
    

def test_late():
    assert datetime.datetime.now() < datetime.datetime(year, month, day + 1, 4, 0), "Submitted Late"
