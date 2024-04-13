import pytest
from string_utils import StringUtils



string_utils = StringUtils()


@pytest.mark.parametrize("string, res_", [("skypro", "Skypro"), ("ivan", "Ivan"), ("samara", "Samara")])
def test_capitilize(string, res_):
    string_utils = StringUtils()
    res = string_utils.capitilize(string)
    assert res == res_

@pytest.mark.xfail
def test_capitilize_negative(): 
    string_utils = StringUtils()
    res = string_utils.capitilize("skypro")
    assert res == "skypro"


@pytest.mark.parametrize("string, res_", [("  skypro", "skypro"), ("   1234", "1234"), ("   Москва", "Москва")])
def test_trim(string, res_):
    string_utils = StringUtils()
    res = string_utils.trim(string)
    assert res == res_

@pytest.mark.xfail
def test_trim_negative(): 
    string_utils = StringUtils()
    res = string_utils.trim("   skypro")
    assert res == "   skypro"

@pytest.mark.parametrize("string, res_", [ ("a,b,c,d", ["a", "b", "c", "d"]), ("в,а,с,я", ["в", "а", "с", "я"]), ("a, ,c,d", ["a", " ", "c", "d"]) ])
def test_to_list(string, res_): 
    string_utils = StringUtils()
    res = string_utils.to_list(string)
    assert res == res_

@pytest.mark.xfail
def test_to_list_negative(): 
    string_utils = StringUtils()
    res = string_utils.to_list("a,b,c,d")
    assert res == "a,b,c,d"

@pytest.mark.parametrize("string, res_", [ ("SkyPro", "S"), ("Вася", "В") ])
def test_contains_true(string, res_): 
    string_utils = StringUtils()
    res = string_utils.contains(string, res_)
    assert res == True

@pytest.mark.parametrize("string, res_", [ ("SkyPro", "g"), ("Вася", "z") ])
def test_contains_false(string, res_): 
    string_utils = StringUtils()
    res = string_utils.contains(string, res_)
    assert res == False

@pytest.mark.xfail
def test_contains_negative_false(): 
    string_utils = StringUtils()
    res = string_utils.contains("SkyPro", "S")
    assert res == False

@pytest.mark.xfail
def test_contains_negative_true(): 
    string_utils = StringUtils()
    res = string_utils.contains("SkyPro", "c")
    assert res == True

@pytest.mark.parametrize("string, simbol, res_", [ ("SkyPro", "k", "SyPro"), ("1Вася", "1В", "ася"), ("Дуся", "д", "уся") ])
def test_delete_symbol(string, simbol, res_): 
    string_utils = StringUtils()
    res = string_utils.delete_symbol(string, simbol)
    assert res == res_

@pytest.mark.xfail
def test_delete_symbol_negative(): 
    string_utils = StringUtils()
    res = string_utils.delete_symbol("SkyPro", "k")
    assert res == "SkyPro"

@pytest.mark.parametrize("string, res_", [ ("SkyPro", "S"), ("Вася", "В"), (" Дуся", " ") ])
def test_starts_with_true(string, res_): 
    string_utils = StringUtils()
    res = string_utils.starts_with(string, res_)
    assert res == True

@pytest.mark.parametrize("string, res_", [ ("SkyPro", "P"), ("Вася", "a"), (" Дуся", "Д") ])
def test_starts_with_false(string, res_): 
    string_utils = StringUtils()
    res = string_utils.starts_with(string, res_)
    assert res == False

@pytest.mark.xfail
def test_starts_with_negative_false(): 
    string_utils = StringUtils()
    res = string_utils.starts_with("SkyPro", "S")
    assert res == False

@pytest.mark.xfail
def test_starts_with_negative_true(): 
    string_utils = StringUtils()
    res = string_utils.starts_with("SkyPro", "P")
    assert res == True

@pytest.mark.parametrize("string, res_", [ ("SkyPro", "o"), ("Вася", "я"), (" Дуся .", ".") ])
def test_end_with_true(string, res_): 
    string_utils = StringUtils()
    res = string_utils.end_with(string, res_)
    assert res == True

@pytest.mark.parametrize("string, res_", [ ("SkyPro", "y"), ("Вася", "В"), (" Дуся .", " ") ])
def test_end_with_false(string, res_): 
    string_utils = StringUtils()
    res = string_utils.end_with(string, res_)
    assert res == False        

@pytest.mark.xfail
def test_end_with_negative_true(): 
    string_utils = StringUtils()
    res = string_utils.end_with("SkyPro", "y")
    assert res == True

@pytest.mark.xfail
def test_end_with_negative_false(): 
    string_utils = StringUtils()
    res = string_utils.end_with("SkyPro", "o")
    assert res == False      

@pytest.mark.parametrize("string", [ ("  "), ("") ])
def test_is_empty_true(string): 
    string_utils = StringUtils()
    res = string_utils.is_empty(string)
    assert res == True    

@pytest.mark.parametrize("string", [ ("   ."), ("Вася") ])
def test_is_empty_false(string): 
    string_utils = StringUtils()
    res = string_utils.is_empty(string)
    assert res == False

@pytest.mark.xfail
def test_is_empty_negative_true(): 
    string_utils = StringUtils()
    res = string_utils.is_empty("Sky")
    assert res == True

@pytest.mark.xfail
def test_is_empty_negative_false(): 
    string_utils = StringUtils()
    res = string_utils.is_empty("")
    assert res == False

@pytest.mark.parametrize("string, simbol, res_", [ (["Sky", "Pro"], ".", "Sky.Pro"), (["Вася", "Дуся"], "+", "Вася+Дуся"), (["Мос", "ква"], "", "Москва") ])
def test_list_to_string(string, simbol, res_): 
    string_utils = StringUtils()
    res = string_utils.list_to_string(string, simbol)
    assert res == res_

@pytest.mark.xfail
def test_list_to_string_negative(): 
    string_utils = StringUtils()
    res = string_utils.list_to_string(["Sky", "Pro"], "+")
    assert res == "Sky-Pro" 