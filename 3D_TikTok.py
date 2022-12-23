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

    def update_num_of_wins(self,players: list[dict], winner_index: int):
        players[winner_index]["num_of_wins"] += 1



    def make_move(self,board, players, turn_index):
        move = self.get_player_move(board, players, turn_index)
        board[int(move)] = players[turn_index]["sign"] 

    def is_move_valid(self,board: list[dict], player_move: str):
        answer = False
        if player_move.isdigit():
            #print(" board.values()",  board.values())
            if player_move in board.values():  # check if move is possible in board
                answer = True
            else:
                self.prRed(
                    "     ______________________________________________________________________")
                self.prRed(
                    "    |                                                                      |")
                self.prRed(
                    "    | Invalid move, your move is out of range or cell is taken, try again. |")
                self.prRed(
                    "    |______________________________________________________________________|")
        else:
            self.prRed("                     ____________________________________")
            self.prRed("                    |                                    |")
            self.prRed("                    | Invalid input, insert numbers only.|")
            self.prRed("                    |____________________________________|")

        return answer

    def change_turn(self,turn_i):
        next_turn = turn_i + 1
        return next_turn % 2    

    def get_player_move(self,board, players, turn_index) -> str:
        is_valid = False
        name = players[turn_index]['name']
        sign = players[turn_index]['sign']
        while not is_valid:
            print()
            player_move = input(
                f"{name}, choose a number from the board to put your {sign} in: ")
            is_valid = self.is_move_valid(board, player_move)

        return player_move

    def turn(self,board, players, turn_index):
        self.print_board(board)
        self.make_move(board, players, turn_index)
        is_finished = self.is_game_over(board)
        return is_finished

    def init(self):
        board = {num: str(num) for num in range(1, 28)}
        return board
    
    def is_answer_valid(self,answer):
        return answer == "y" or answer == "n"
    
    def is_repeat_game(self):
        valid = False
        counter = 0

        while valid == False and counter < 3:
            print()
            answer = input("Would you like to play another game? prass y or n: ")
            print()
            if (answer == 'y') or (answer == 'yes'):
                print()
                self.prGreen("                     ██████████████████████████████████████ ")
                self.prGreen("                     █████ Let\'s play another game!! ██████ ")
                self.prGreen("                     ██████████████████████████████████████ ")
                print()
                valid = True
                answer = True
            elif (answer == 'n') or (answer == 'no'):
                self.prGreen("-" * 80)
                print()
                self.prGreen('                        See you next time! Bye...')
                print()

                valid = True
                answer = False

            else:
                print("Invalid input")
                counter += 1

        return answer
    
    def check_draw(self,board):
        for val in board.values():
            if val.isdigit():
                return False
        return True
    
    def print_end_message(self,players):
        self.prGreen("-" * 80)
        print()
        self.prGreen("                        Hope you enjoyed the game")
        print()
        self.prGreen(
            f"                            {players[0]['name']} is with {players[0]['num_of_wins']} wins")
        print()
        self.prGreen(
            f"                            {players[1]['name']} is with {players[1]['num_of_wins']} wins")
        print()
        self.prGreen("-" * 80)
        
    def print_game_winner(self,players, turn_index):
        print()
        self.prGreen('-' * 80)

        self.prGreen(
            f"                     {players[turn_index]['name']} is the winner! with the sign {players[turn_index]['sign']}")
        self.prGreen('-' * 80)
        


    def tic_tac_toe_3D(self):
        another_game = True
        names = self.get_player_names()
        turn_index = self.get_random_starter()
        players = self.create_players(names, turn_index)

        while another_game == True:
            board = self.init()
            is_finished = False

            turn_index = self.get_random_starter()
            is_draw = False
            while not is_finished:
                is_there_a_winner = self.turn(board, players, turn_index)
                is_draw = self.check_draw(board)
                # the game ends if there is a winner or draw
                is_finished = is_there_a_winner or is_draw
                if is_there_a_winner == True:
                    self.update_num_of_wins(players, turn_index)
                    self.print_board(board)
                    self.print_game_winner(players, turn_index)
                
                turn_index = self.change_turn(turn_index)
            another_game = self.is_repeat_game()

        self.print_end_message(players)
