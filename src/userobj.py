
class Utilisateur:
    def __init__(self,token=None,mail=None,mdp=None) -> None:
        self.token = token
        self.mail = mail 
        self.password = mdp
        self.id = None
        if(token):
            self