# IMPORTANT!
# You don't need to do anything with this file
# It is only to provide some automated testing
# to give you feedback on if your code is working
# correctly! Please do not change!


from Card import Card
from Prob1 import Deck
from Prob2 import cryptocurrency_calculator

class Test_Prob1:

    def test_str_or_repr_method_defined(self):
        student = Deck()
        assert '__main__' not in str(student), "Did you define a __str__ or __repr__ method that returns something?"

    def test_str_or_repr_prints_nice_reps(self):
        student = Deck()
        assert len(str(student)) < 52*5, "All the cards in your deck should be printed with their two character codes, and that does not seem to be the case here?"

    def test_get_deck_exists(self):
        student = Deck()
        assert 'get_deck' in dir(student), "Did you create a get_deck method?"

    def test_get_deck_functions_correctly(self):
        student = Deck()
        assert type(student.get_deck()) == list, "get_deck is not returning a list?"
        assert type(student.get_deck()[0]) == Card, "The elements of get_deck are not card elements?"
        deck = student.get_deck()
        deck.pop(0)
        assert deck != student.get_deck(), "It looks like you returned a reference to your deck attribute instead of a copy of it."

    def test_initial_deck(self):
        student = Deck()
        assert len(student.get_deck()) == 52, f"Your initial deck size should be 52 but instead is {len(student.get_deck())}. Or your get_deck method is broken."
        deck = student.get_deck()
        for suit in range(3):
            assert 13 == sum([1 for card in deck if card.get_suit()==suit]), "You don't seem to have 13 cards of each suit in your deck initially. Or your get_deck method is broken."

    def test_shuffle_exists(self):
        student = Deck()
        assert 'shuffle' in dir(student), "Did you create a shuffle method?"

    def test_shuffle_works(self):
        student = Deck()
        d1 = student.get_deck()
        student.shuffle()
        d2 = student.get_deck()
        assert d1 != d2, "Is your shuffle method properly scrambling the card order? Or your get_deck is not returning a copy."

    def test_draw_exists(self):
        student = Deck()
        assert 'draw' in dir(student), "Did you create a draw method?"

    def test_draw_functions_correctly(self):
        student = Deck()
        curdeck = student.get_deck()
        to_draw = 5
        topcards = curdeck[:to_draw]
        assert student.draw(to_draw) == topcards, "You are not returning the top n cards of your deck when you draw?"
        assert len(student.get_deck()) == len(curdeck)-to_draw, "Your deck size is not decreasing by the number of cards you drew? Or your get_deck is not returning a copy."
        for card in topcards:
            assert card not in student.get_deck(), "A drawn card is still within your deck for some reason? Are you cheating at cards?!"


class Test_Prob2:
    def test_example1(self, monkeypatch, capsys):
        entries = ['Bitcoin', '1', '1-Mar-22', '1-Dec-22']
        monkeypatch.setattr('builtins.input', lambda _: entries.pop(0))
        cryptocurrency_calculator()
        captured = capsys.readouterr().out.splitlines()
        assert 'loss' in captured[-1].lower()
        assert '27,387.51' in captured[-1]

    def test_example2(self, monkeypatch, capsys):
        entries = ['DogeCoin', '1000', '1-Jun-22', '1-Dec-22']
        monkeypatch.setattr('builtins.input', lambda _: entries.pop(0))
        cryptocurrency_calculator()
        captured = capsys.readouterr().out.splitlines()
        assert 'profit' in captured[-1].lower()
        assert '20.54' in captured[-1]

    def test_other_situations(self, monkeypatch, capsys):
        totest = [
            {'inputs': ['Binance', '50', '10-Feb-22', '1-Nov-22'],
             'outputs': ('loss', '74,889.00')},
            {'inputs': ['Bitcoin', '100', '1-Jan-22', '1-Dec-22'],
             'outputs': ('loss', '3,071,968.00')},
            {'inputs': ['DogeCoin', '5000', '17-Mar-22', '1-Nov-22'],
             'outputs': ('profit', '130.50')}
        ]
        for entry in totest:
            icopy = entry['inputs'].copy()
            monkeypatch.setattr('builtins.input', lambda _: entry['inputs'].pop(0))
            cryptocurrency_calculator()
            captured = capsys.readouterr().out.splitlines()
            for out in entry['outputs']:
                assert out in captured[-1].lower(), f"With inputs of {icopy}, your function should have printed {out} and didn't?"

