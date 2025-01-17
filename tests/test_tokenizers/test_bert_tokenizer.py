import unittest
import pytest
from cybertron.tokenizers.bert_tokenizer import BertTokenizer

class TestBertTokenizer(unittest.TestCase):
    @pytest.mark.action
    def test_bert_tokenizer(self):
        tokenizer = BertTokenizer.load('bert-base-uncased')
        inputs = tokenizer.encode('hello world.')

        assert inputs == [7592, 2088, 1012]