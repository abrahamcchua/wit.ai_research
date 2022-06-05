from wit import Wit

'''
Simple demo for gcash chatbot, intents taken from https://www.gcash.com/gcashfaqseries
:Date: June, 06, 2022
:Author/s: 
    - Chua, Abraham <abrahamcchua@gmail.com>
'''


class WitDemo():
    def __init__(self):
        self.access_token = "UVOZ4V3MXO42D6UXQBRXXZNWYUU3BMZE"
        self.client = Wit(access_token = self.access_token)
    
    
    def frame(self, message):
        """Main highlight of function "frame"
        Summary:
        This function acts as the frame of the code
        output of the function:
        -Message of the chatbot
        """
        #Used a dictionary instead of if/elif statements for computational efficiency in case intents get significantly large
        response_dict = {"cash_in_location":self.cash_in_location,
                         "cash_out_location":self.cash_out_lcoation,
                         "mpin_concern":self.mpin_concern,
                         "penalty_waiver":self.penalty_waiver
        }
        resp = self.client.message(message)
        intent = resp["intents"][0]["name"]
        return response_dict.get(intent)()
        
        
    def cash_in_location(self):
        """Main highlight of function "cash_in_location"
        Summary:
        This function returns a certain string given that the intent detected by the chatbot is "cash_in_location"
        output of the function:
        -String message
        """
        return "You can cash-in through online banking or over-the-counter at Puregold, 7-Eleven, Palawan Pawnshop, or Villarica Pawnshop."
        
    
    def cash_out_lcoation(self):
        """Main highlight of function "cash_in_location"
        Summary:
        This function returns a certain string given that the intent detected by the chatbot is "cash_out_location"
        output of the function:
        -String message
        """
        return "You can cash-out at Puregold, Palawan Pawnshop, or Villarica Pawnshop."
        
        
    def mpin_concern(self):
        """Main highlight of function "mpin_concern"
        Summary:
        This function returns a certain string given that the intent detected by the chatbot is "mpin_concern"
        output of the function:
        -String message
        """
        return "If you have previously nominated your security questions, simply tap Forgot MPIN on the GCash login screen. You will receive an authentication code to access your security questions. After answering them correctly, you will be able to change your MPIN."
    
   
    def penalty_waiver(self):
        """Main highlight of function "penalty_waiver"
        Summary:
        This function returns a certain string given that the intent detected by the chatbot is "penalty_waiver"
        output of the function:
        -String message
        """
        return "Yes! If your due date is within March 17 to April 12, you are eligible for a penalty fee waiver if you are unable to pay or cash-in on your GCash account by your due date."


            
