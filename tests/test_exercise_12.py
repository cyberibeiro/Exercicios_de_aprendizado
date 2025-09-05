from exercicios_de_aprendizado.exercise_12 import PigLatin


def test_palavras_que_comecam_com_vogal():
    pig = PigLatin()
    assert pig.translate("apple") == "appleay"
    assert pig.translate("ear") == "earay"
    assert pig.translate("igloo") == "iglooay"
    assert pig.translate("object") == "objectay"
    assert pig.translate("under") == "underay"


def test_palavras_com_prefixos_especiais():
    pig = PigLatin()
    assert pig.translate("xray") == "xrayay"
    assert pig.translate("yttria") == "yttriaay"


def test_palavras_com_qu():
    pig = PigLatin()
    assert pig.translate("quick") == "ickquay"
    assert pig.translate("square") == "aresquay"


def test_palavras_com_consoantes_no_inicio():
    pig = PigLatin()
    assert pig.translate("pig") == "igpay"
    assert pig.translate("koala") == "oalakay"
    assert pig.translate("yellow") == "ellowyay"
    assert pig.translate("rhythm") == "ythmrhay"


def test_frase_completa():
    pig = PigLatin()
    assert pig.translate("quick fast run") == "ickquay astfay unray"
