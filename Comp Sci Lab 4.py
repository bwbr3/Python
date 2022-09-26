#Braniyah Webb

import unittest
from unittest.mock import patch
from io import StringIO
class TestLabFunctions(unittest.TestCase):

#play again code    

 def play_again() -> bool:

    user_input = ['Yes']
    with patch('sys.stdout', new_callable=StringIO):
        with patch('builtins,input', side_effect = user_input):
            results = lab05.play_again()
        self.assertTrue(results, 'When input is yes the function is return True')
    return True

# questions you can ask the program
     
def get_wager(bank : int) -> int:
    print(input('How many chips do you want to start with?'))
   
    return 1            
def get_slot_results() -> tuple:
    ''' Returns the result of the slot pull '''
    return 1, 2, 3
def get_matches(reela, reelb, reelc) -> int:
    ''' Returns 3 for all 3 match, 2 for 2 alike, and 0 for none alike. '''
    return 0
def get_bank() -> int:
    ''' Returns how many chips the user wants to play with.  Loops until a value 
greater than 0 and less than 101 '''
    return 0
def get_payout(wager, matches):
    ''' Returns how much the payout is.. 10 times the wager if 3 matched, 3 times 
the wager if 2 match, and negative wager if 0 match '''
    return wager * -1     
if __name__ == "__main__":
    
    
 value = int(input('How many chips do you want to start with? ==>'))

        

 def returns_True(self):
    user_input = ["YeS"]
    with patch('sys.stdout', new_callable=StringIO) as es:
        with patch('builtins.input', side_effect = user_input):
            results = lab05.play_again()
            self.assertTrue(results,"When input is yes the function should return True")
    
        
def returns_False_with_N_or_NO(self):
    user_input = ["nO"]
    with patch('sys.stdout', new_callable=StringIO) as es:
        with patch('builtins.input', side_effect=user_input):
            results = lab05.play_again()
            self.assertFalse(results, "When input is No play_again should return False")

def test_get_slot_results_returns_a_tuple_of_integers(self):
    results = lab05.get_slot_results()
    self.assertIsInstance(results, tuple, "get_slot_results should return a tuple")
    
    self.assertEqual(3, len(results), "get_slot_results should return 3 items")
    self.assertIsInstance(results[0], int, "Item at index 0 was not an integer")
        
    self.assertIsInstance(results[1], int, "Item at index 1 was not aninteger")
        
    self.assertIsInstance(results[2], int, "Item at index 2 was not an integer")
    
def test_get_matches_returns_correct_number_of_matches(self):
    results = lab05.get_matches(3, 3, 3)
    self.assertEqual(3, results, "get_matches returns 3 when given 3 matching values")
    results = lab05.get_matches(4, 4, 4)
    self.assertEqual(3, results, "get_matches returns 3 when given 3 matching values")
    results = lab05.get_matches(4, 4, 5)
    self.assertEqual(2, results, "get_matches returns 2 when given 2 matching values")
    results = lab05.get_matches(8, 4, 4)
    self.assertEqual(2, results, "get_matches returns 2 when given 2 matching values")
    results = lab05.get_matches(8, 4, 8)
    self.assertEqual(2, results, "get_matches returns 2 when given 2 matching values")
    results = lab05.get_matches(8, 4, 3)
    self.assertEqual(0, results, "get_matches returns 0 when given 0 matching values")
def test_get_payout_returns_correct_results(self):
    results = lab05.get_payout(3, 0)
    self.assertEqual(-3, results, "get_payout returns -3 when given 3 and no matches.")
    results = lab05.get_payout(2, 3)
    self.assertEqual(18, results, "get_payout returns 8 when given 2 and 3 matches.")
    results = lab05.get_payout(5, 2)
    self.assertEqual(10, results, "get_payout returns 10 when given 5 and 2 matches.")
        
if __name__ == "__main__":
    __unittest = True
    unittest.main()

playing = True
while playing:
    bank = get_bank()
while True:
     wager = get_wager(bank)
     reel1, reel2, reel3 = get_slot_results()
     matches = get_matches(reel1, reel2, reel3)
     payout = get_payout(wager, matches)
     bank = bank + payout
     print("Your spin", reel1, reel2, reel3)
     print("You matched", matches, "reels")
     print("You won/lost", payout)
     print("Current bank", bank)
     print()
           
     print("You lost all", 0, "in", 0, "spins")
     print("The most chips you had was", 0)
     playing = play_again()

            
           
