from exercicios_de_aprendizado.pig_latin import PigLatin


def test_words_starting_with_vowel() -> None:
    pig = PigLatin()
    assert pig.translate("apple") == "appleay"
    assert pig.translate("ear") == "earay"
    assert pig.translate("igloo") == "iglooay"
    assert pig.translate("object") == "objectay"
    assert pig.translate("under") == "underay"


def test_words_with_special_prefixes() -> None:
    pig = PigLatin()
    assert pig.translate("xray") == "xrayay"
    assert pig.translate("yttria") == "yttriaay"


def test_words_with_qu() -> None:
    pig = PigLatin()
    assert pig.translate("quick") == "ickquay"
    assert pig.translate("square") == "aresquay"


def test_words_with_initial_consonants() -> None:
    pig = PigLatin()
    assert pig.translate("pig") == "igpay"
    assert pig.translate("koala") == "oalakay"
    assert pig.translate("yellow") == "ellowyay"
    assert pig.translate("rhythm") == "ythmrhay"


def test_full_sentence() -> None:
    pig = PigLatin()
    assert pig.translate("quick fast run") == "ickquay astfay unray"
