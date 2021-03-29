from python_hw_1 import addition_upto_palindrome


def test_example1():
    assert addition_upto_palindrome("abc") == 2


def test_example2():
    assert addition_upto_palindrome("aba") == 0


def test_example4():
    assert addition_upto_palindrome("bcba") == 1


def test_example5():
    assert addition_upto_palindrome("abb") == 1


def test_example6():
    assert addition_upto_palindrome("bba") == 1


def test_example7():
    assert addition_upto_palindrome("abracadabra") == 10


def test_example8():
    assert addition_upto_palindrome("abracarba") == 0


def test_example9():
    assert addition_upto_palindrome("abracarb") == 1


def test_example10():
    assert addition_upto_palindrome("abraca") == 3


def test_example11():
    assert addition_upto_palindrome("braccarba") == 1


def test_example12():
    assert (
        addition_upto_palindrome(
            "themajordivisionofthemechanicsdisciplineseparatesclassicalmechanics"
            "fromquantummechanicshistoricallyclassicalmechanicscamefirst"
            "whilequantummechanicsisacomparativelyrecentinventionclassicalmechanics"
            "originatedwithisaacnewtonslawsofmotioninprincipiamathematicaquantummechanics"
            "wasdiscoveredinbotharecommonlyheldtoconstitutethemostcertainknowledgethatexists"
            "aboutphysicalnatureclassicalmechanicshasespeciallyoftenbeenviewedasamodel"
            "forothersocalledexactsciencesessentialinthisrespectistherelentlessuseof"
            "mathematicsintheoriesaswellasthedecisiveroleplayedbyexperimentingenerat"
            "ingandtestingthemquantummechanicsisofawiderscopeasitencompassesclassical"
            "mechanicsasasubdisciplinewhichappliesundercertainrestrictedcircumstances"
            "accordingtothecorrespondenceprinciplethereisnocontradictionorconflict"
            "betweenthetwosubjectseachsimplypertainstospecificsituationsthecorrespondence"
            "principlestatesthatthebehaviorofsystemsdescribedbyquantumtheoriesreproduces"
            "classicalphysicsinthelimitoflargequantumnumbersquantummechanicshassupe"
        )
        == 999
    )
