import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card1 = Card('heart', 9)
        self.card2 = Card('heart', 10)
        self.cardgame = CardGame()

    def test_check_for_ace(self):
        actual_outcome = self.cardgame.check_for_ace(self.card1)
        expected_outcome = False
        self.assertEqual(expected_outcome, actual_outcome)

    def test_highest_card(self):
        actual_outcome = self.cardgame.highest_card(self.card1, self.card2)
        expected_outcome = self.card2
        self.assertEqual(expected_outcome, actual_outcome)

    def test_cards_total(self):
        cards = [self.card1, self.card2]
        actual_outcome = self.cardgame.cards_total(cards)
        expected_outcome = ('You have a total of 19')
        self.assertEqual(expected_outcome, actual_outcome)