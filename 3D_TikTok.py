import random as rd

class tic_tac_toe_3D():
    def prRed(self,skk): print("\033[91m {}\033[00m" .format(skk))
    def prGreen(self,skk): print("\033[92m {}\033[00m" .format(skk))
    def prPurple(self,skk): print("\033[95m {}\033[00m" .format(skk))
    def prLightPurple(self,skk): print("\033[94m {}\033[00m" .format(skk))
    def prCyan(self,skk): print("\033[96m {}\033[00m" .format(skk))
    def prYellow(self,skk): print("\033[93m {}\033[00m" .format(skk))
    def prLightGray(self,skk): print("\033[97m {}\033[00m" .format(skk))
    def prorange(self,skk): print("\033[90m {}\033[90m" .format(skk))
    '\033[43m'
    def prCyan(self,skk): print("\033[96m {}\033[00m" .format(skk))
    
    def get_player_names(self):
        self.prGreen('-' * 80)
        self.prGreen("                     ██████████████████████████████████████ ")
        self.prGreen("                     █ Welcome to our tic Tac Toe 3D game █ ")
        self.prGreen("                     █   by Gal, Lior, Hagai and Yoav    █ ")
        self.prGreen("                     ██████████████████████████████████████ ")
        self.prGreen('-' * 80)
        print()
        name1 = input(" player 1 enter your name: ")
        print('-' * 80)
        name2 = input(" player 2 enter your name: ")
        print('-' * 80)
        # print(f"{players[starter_index]['name']} is starting the game!")
        names = [name1, name2]
        return names

    def print_board(self,board):
        self.prPurple("                             ___________________________")
        self.prPurple("                            /        /        /        /")
        self.prPurple(
            f"                           /    {board[1]:2}  /    {board[2]:2}  /    {board[3]:2}  /")
        self.prPurple("                          /________/________/________/")
        self.prPurple("                         /        /        /        /")
        self.prPurple(
            f"                        /   {board[4]:2}   /   {board[5]:2}   /     {board[6]:2} /")
        self.prPurple("                       /________/________/________/")
        self.prPurple("                      /        /        /        /")
        self.prPurple(
            f"                     /    {board[7]:2}  /    {board[8]:2}  /     {board[9]:2} /")
        self.prPurple("                    /________/________/________/")

        self.prGreen("                             ___________________________")
        self.prGreen("                            /        /        /        /")
        self.prGreen(
            f"                           /   {board[10]:2}   /    {board[11]:2}  /    {board[12]:2}  /")
        self.prGreen("                          /________/________/________/")
        self.prGreen("                         /        /        /        /")
        self.prGreen(
            f"                        /   {board[13]:2}   /   {board[14]:2}   /    {board[15]:2}  /")
        self.prGreen("                       /________/________/________/")
        self.prGreen("                      /        /        /        /")
        self.prGreen(
            f"                     /   {board[16]:2}   /   {board[17]:2}   /    {board[18]:2}  /")
        self.prGreen("                    /________/________/________/")

        self.prYellow("                             ___________________________")
        self.prYellow("                            /        /        /        /")
        self.prYellow(
            f"                           /   {board[19]:2}   /   {board[20]:2}   /    {board[21]:2}  /")
        self.prYellow("                          /________/________/________/")
        self.prYellow("                         /        /        /        /")
        self.prYellow(
            f"                        /   {board[22]:2}   /   {board[23]:2}   /    {board[24]:2}  /")
        self.prYellow("                       /________/________/________/")
        self.prYellow("                      /        /        /        /")
        self.prYellow(
            f"                     /   {board[25]:2}   /   {board[26]:2}   /    {board[27]:2}  /")
        self.prYellow("                    /________/________/________/")

        
    def get_random_starter(self):
        starter_index = rd.randint(0, 1)
        return starter_index

    def create_players(self,names: list[str], starter_index):
        players = []

        for i in range(2):
            curr_player = {"name": names[i].title(), "num_of_wins": 0}
            if i == starter_index:
                curr_player["sign"] = "X"
            else:
                curr_player["sign"] = "O"
            players.append(curr_player)

        return players
