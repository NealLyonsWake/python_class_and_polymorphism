# Inheritance

class Phone():

    def __init__(self, manufacturer="generic", owner="public"):
        self.manufacturer=manufacturer
        self.owner= owner
        self.UUID = "1234-12345-123456X"


    def call(self, number):
        print (f'I am calling on my {self.manufacturer} to {number}, ring ring')


# a mobile phone is a phone class
class MobilePhone(Phone):

    def __init__ (self, manufacturer="generic", owner="public", contact_list =[], credit=0.0, games=["snake"]):
        super().__init__(manufacturer, owner)
        self.contacts = contact_list
        self.credit = credit
        self.games = games
        
    def sms(self, number):
        print (f'I am sending am SMS to {number}, beep beep')

mobilePhoneA = MobilePhone(manufacturer="Nokia", owner="unknown", contact_list=["01923432432"], credit=10.0)

# print(mobilePhoneA.manufacturer)
# mobilePhoneA.call("01234")
# print(mobilePhoneA.UUID)


# a mobile phone is a phone class
class SmartPhone(MobilePhone):
    """  
    self, manufacturer="generic", owner="public", contact_list =[], credit=0.0, games=["snake"])
    """

    def __init__(self, manufacturer="generic", owner="public", contact_list =[], credit=0.0, games=["snake"], browser="Chrome", touchscreen=True, apps={"games":["snake"],"util":[]}):
        super().__init__(manufacturer, owner, contact_list, credit, apps["games"])
        
        self.browser = browser
        self.touchscreen = touchscreen
        self.apps = apps
        
    def browse(self, url):
        print(f'I am browsing {url} website!!')

    def launch_app(self, app):
        print(f'I am using mu new app {app}.')

    def call(self, number):
        app = input("what app do you want to use to make the call?")
        print (f'I am calling {number} using {app}')



iPhone = SmartPhone(manufacturer="Apple", owner="unknown", contact_list=[], credit=100.0, browser="Safari", touchscreen=True)

mobilePhoneA.call("0943874")
print("\n\n\n")
iPhone.call("0987673")
# iPhone.sms("7687484")