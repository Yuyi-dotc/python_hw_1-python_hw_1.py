from python_hw_1 import caesar_encrypt


def test_example():
    input = "This is stupid song stupid stupid stupid song"
    output = "Drsc sc cdezsn cyxq cdezsn cdezsn cdezsn cyxq"
    assert caesar_encrypt(input, 10) == output


def test_example3():
    actual = caesar_encrypt("Roses are Red, Violets are blue", 4)
    expected = "Vswiw evi Vih, Zmspixw evi fpyi"
    assert actual == expected


def test_example4():
    actual = caesar_encrypt("A", 1)
    expected = "B"
    assert actual == expected


def test_example5():
    actual = caesar_encrypt("XYZ", 5)
    expected = "CDE"
    assert actual == expected


def test_example6():
    actual = caesar_encrypt(
        "I havent slept for three days, because that would be too long.", 2
    )
    expected = "K jcxgpv ungrv hqt vjtgg fcau, dgecwug vjcv yqwnf dg vqq nqpi."
    assert actual == expected


def test_example7():
    actual = caesar_encrypt("AbCdEfGhIjKlMnOp", -2)
    expected = "YzAbCdEfGhIjKlMn"
    assert actual == expected


def test_example8():
    actual = caesar_encrypt(
        "You can never lose a homing pigeon - "
        "if your homing pigeon doesn't come back, "
        "what you've lost is a pigeon.",
        20,
    )
    expected = (
        "Sio wuh hypyl fimy u bigcha jcayih - "
        "cz siol bigcha jcayih xiymh'n wigy vuwe, "
        "qbun sio'py fimn cm u jcayih."
    )
    assert actual == expected


def test_example9():
    actual = caesar_encrypt("This is stupid song stupid stupid stupid song", 10)
    expected = "Drsc sc cdezsn cyxq cdezsn cdezsn cdezsn cyxq"
    assert actual == expected


def test_example10():
    query = "This is stupid song stupid stupid stupid song"
    actual = caesar_encrypt(caesar_encrypt(query, 10), -10)
    assert actual == query
