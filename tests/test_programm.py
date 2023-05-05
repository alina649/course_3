from utils.programm import date, operation_list, operation_sort_acoompl, sort_date, sort_list,changing_from, changing_to
import os.path




def test_operation_list():
    assert operation_list(os.path.join('tests', 'test_programm.json'))
    assert operation_list("") == None
def test_operation_sort_acoompl():
    assert operation_sort_acoompl(os.path.join('tests', 'test_programm.json'))
    assert operation_sort_acoompl("") == None

def test_sort_date():
    assert sort_date(os.path.join('tests', 'test_programm.json'))

def test_sort_list():
    assert sort_list(os.path.join('tests', 'test_programm.json'))

def test_changing_from():
    assert changing_from(os.path.join('tests', 'test_programm.json'))

def test_changing_to():

    assert changing_to(os.path.join('tests', 'test_programm.json'))

def test_date():
    assert date(os.path.join('tests', 'test_programm.json'))