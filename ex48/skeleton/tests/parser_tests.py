from nose.tools import *
from ex48 import lexicon
from ex48 import parser
from ex48.parser import Sentence


def test_parse_sentence():
    result = lexicon.scan("the princess kill the bear")
    word_list = parser.parse_sentence(result)
    sample = Sentence(('noun', 'princess'), ('verb', 'kill'), ('noun', 'bear'))

    assert_equal(word_list.subject, sample.subject)
    assert_equal(word_list.verb, sample.verb)
    assert_equal(word_list.object, sample.object)

    # assert_raises(TypeError, parser.parse_verb, (('none', 'princess')))
