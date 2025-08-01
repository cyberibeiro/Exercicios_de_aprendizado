from exercicios_de_aprendizado.exercise_12 import translate

def test_single_word_vowel_start() -> None:
    assert translate("apple") == "appleay"

def test_single_word_consonant_start() -> None:
    assert translate("banana") == "ananabay"

def test_single_word_with_qu() -> None:
    assert translate("square") == "aresquay"
    assert translate("quiet") == "ietquay"

def test_single_word_xr_yt_start() -> None:
    assert translate("xray") == "xrayay"
    assert translate("yttria") == "yttriaay"

def test_y_as_vowel() -> None:
    assert translate("rhythm") == "ythmrhay"

def test_phrase_multiple_words() -> None:
    assert translate("quick fast run") == "ickquay astfay unray"
    assert translate("xray apple banana") == "xrayay appleay ananabay"
