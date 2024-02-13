import pytest
from main import exercise_1, exercise_2, exercise_3, exercise_5


class TestPAC4:

    @pytest.fixture(autouse=True)
    def setUp(self):
        self.tweets_list = [
            {
                'sentiment': '0',
                'id': '1467836859',
                'date': 'Mon Apr 06 22:26:33 PDT 2009',
                'query': 'NO_QUERY',
                'user': 'willy_chaz',
                'text': 'A bad nite for the favorite teams: Astros and Spartans lose.  The nite out with T.W. was good.'
            },
            {
                'sentiment': '0',
                'id': '1467836873',
                'date': 'Mon Apr 06 22:26:33 PDT 2009',
                'query': 'NO_QUERY',
                'user': 'LeakySpoon',
                'text': ' Body Of Missing Northern Calif. Girl Found: Police have found the remains of a missing Northern California girl .. http://tr.im/imji'
            },
            {
                'sentiment': '0',
                'id': '1467837189',
                'date': 'Mon Apr 06 22:26:38 PDT 2009',
                'query': 'NO_QUERY', 'user': 'cityrat59',
                'text': '@mangaaa I hope they will increase the capacity fast, yesterday was such a pain. Got the fail whale +15 times in 2 hours.... '
            }
        ]

        self.cleaned_tweets = [
            {
                'sentiment': '0',
                'id': '1467836859',
                'date': 'Mon Apr 06 22:26:33 PDT 2009',
                'query': 'NO_QUERY',
                'user': 'willy_chaz',
                'text': 'bad nite favorite teams astros spartans lose nite tw good'
            },
            {
                'sentiment': '0',
                'id': '1467836873',
                'date': 'Mon Apr 06 22:26:33 PDT 2009',
                'query': 'NO_QUERY',
                'user': 'LeakySpoon',
                'text': 'body missing northern calif girl found police found remains missing northern california girl'
            },
            {
                'sentiment': '0',
                'id': '1467837189',
                'date': 'Mon Apr 06 22:26:38 PDT 2009',
                'query': 'NO_QUERY',
                'user': 'cityrat59',
                'text': 'mangaaa hope increase capacity fast yesterday pain got fail whale 15 times 2 hours'
            }
        ]

        self.freq_list = [{'bad': 1, 'nite': 2, 'favorite': 1, 'teams': 1,
                           'astros': 1, 'spartans': 1, 'lose': 1, 'tw': 1,
                           'good': 1},
                          {'body': 1, 'missing': 2, 'northern': 2, 'calif': 1,
                           'girl': 2, 'found': 2, 'police': 1, 'remains': 1,
                           'california': 1},
                          {'mangaaa': 1, 'hope': 1, 'increase': 1,
                           'capacity': 1, 'fast': 1, 'yesterday': 1,
                           'pain': 1, 'got': 1, 'fail': 1, 'whale': 1,
                           '15': 1, 'times': 1, '2': 1, 'hours': 1}]

        self.vocab = {
            'good', 'body', 'favorite', 'missing', 'astros', 'spartans', '15',
            'hours', 'whale', 'california', 'increase', 'hope', 'pain',
            'yesterday', 'girl', 'police', 'nite', 'fast', 'times', 'fail',
            'teams', 'found', 'remains', 'mangaaa', 'bad', 'tw', 'capacity',
            'got', '2', 'northern', 'lose', 'calif'}

    def test_exercise_1(self):
        result = exercise_1()
        assert isinstance(result, list)
        assert result[99:102] == self.tweets_list

    def test_exercise_2(self):
        result = exercise_2(self.tweets_list)
        assert isinstance(result, list)
        assert result == self.cleaned_tweets

    def test_exercise_3(self):
        result = exercise_3(self.cleaned_tweets)
        assert isinstance(result, tuple)
        assert isinstance(result[0], list)
        assert isinstance(result[1], list)
        assert set(result[1]) == self.vocab
        assert result[0] == self.freq_list

    def test_exercise_5(self):
        result = exercise_5()
        assert isinstance(result, dict)
        assert all(word in result[0] or word in result[4] for word in self.vocab)
