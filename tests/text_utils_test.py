from utils import text_utils as tu


class TestTextProcessing:

    def test_normalize_text(self):
        assert tu.normalize_text('HELLO, world!') == 'hello world'
        assert tu.normalize_text('123 AB   C#!$') == '123 ab c'

    def test_remove_urls(self):
        assert tu.remove_urls('Example httpsAP https://www.test.au') == 'Example httpsAP '
        assert tu.remove_urls('Example http: http://test.es') == 'Example http: '
        assert tu.remove_urls('Example http: www.TesT.dm') == 'Example http: '
        assert tu.remove_urls('Example http: test.io') == 'Example http: test.io'
        assert tu.remove_urls('HTTPS://WWW.test.com') == ''
        assert tu.remove_urls('http://WWW.test.com') == ''
        assert tu.remove_urls('abcHTTP://WWW.TEST.au.er') == 'abc'

    def test_delete_words(self):
        assert tu.delete_words('hello hello!world world', ['world']) == 'hello hello!world'
        assert tu.delete_words('earth mars venus', ['earth', 'mars']) == 'venus'

    def test_count_words(self):
        assert tu.count_words(['star', 'galaxy', 'sun', 'galaxy']) == {'galaxy': 2, 'sun': 1, 'star': 1}

    def test_split_string(self):
        assert tu.split_string('hello world') == ['hello', 'world']
        assert tu.split_string('sun galaxy,star') == ['sun', 'galaxy,star']
