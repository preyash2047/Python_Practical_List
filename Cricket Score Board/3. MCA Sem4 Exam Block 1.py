#!/usr/bin/env python
# coding: utf-8

# # Cricket Batting Score Board Program

# In[1]:


class Cricket:
    #defing class variable
    teamDic = {} # team id and team name
    teamPlayers = {} #team id and team player list
    matchDic = {} #match id and team list
    matchScore = {} #match id and list of runs as list [totalScore,noOf4,noOf6,[player,player] score] 
    
    def addTeam(self):
        if len(Cricket.teamDic) > 0:
            print("List of Teams")
            for i in Cricket.teamDic:
                print(f'Team ID: {i} Team Name: {Cricket.teamDic[i]}')

        print("Enter Team Details")
        tempId = int(input('Team ID: '))
        Cricket.teamDic[tempId] = input('Team Name: ').upper()
        Cricket.teamPlayers[tempId] = []
        print("Best of luck for the Match!")
        print("Would you like to add Players in Team Right now?\nYou can do it latter.")
        choice = str(input("To add Playes Enter 'y' else 'n'")).lower()
        if choice == 'y': Cricket.addPlayer(self)
    
    def addPlayer(self):
        print("List of Teams")
        for i in Cricket.teamDic:
            print(f'Team ID: {i} Team Name: {Cricket.teamDic[i]}')
        selectTeam = int(input("Enter Team ID: "))
        
        #entering the player names
        choice = int(input("Enter no of Player you wish to add: "))
        for i in range(choice):
            Cricket.teamPlayers[selectTeam].append(input("Enter Name: ").upper())
        print("Team players added Succesfully")
    
    def viewPlayer(self):
        print("List of Teams")
        for i in Cricket.teamDic:
            print(f'Team ID: {i} Team Name: {Cricket.teamDic[i]}')
        selectTeam = int(input("Enter Team ID you wish to view List of Player: "))
        print(f"List of Players in {Cricket.teamDic[selectTeam]} Team")
        for i in range(len(Cricket.teamPlayers[selectTeam])):
            print(f'{i+1} Player Name: {Cricket.teamPlayers[selectTeam][i]}')
            
    def startMatch(self):
        print("List of Teams")
        for i in Cricket.teamDic:
            print(f'Team ID: {i} Team Name: {Cricket.teamDic[i]}')
        selectTeam1 = int(input("Enter First Team ID: "))
        selectTeam2 = int(input("Enter Second Team ID: "))
        self.matchNo = int(input("Enter Match No: "))
        Cricket.matchDic[self.matchNo] = str(Cricket.teamDic[selectTeam1] + ' vs ' + Cricket.teamDic[selectTeam2])
        
        print(f"Team ID {selectTeam1} will go for batting")
        self.PresentTeam = selectTeam1
        Cricket.throwBall(self)

        print(f"Now {selectTeam2} will go for batting")
        self.PresentTeam = selectTeam2
        Cricket.throwBall(self)

    def throwBall(self):
        noOfOver = 1 #int(input("Enter No of Overs: "))
        noOfBallInOver = 6 * noOfOver
        
        totalScore = 0
        noOf4 = 0
        noOf6 = 0
        individualPlayerscore = {} #player id and score 
        Player1 = int(input(f"Enter Player 1 ID: "))
        Player2 = int(input(f"Enter Player 2 ID: "))
        presentPlayerID = Player1
        individualPlayerscore[Player1] = 0
        individualPlayerscore[Player2] = 0
        for i in range(noOfBallInOver):
            
            if input(f"Player position changed ?\nif yes enter y else n: ").lower() == 'y':
                if presentPlayerID == Player1:
                    presentPlayerID = Player2
                else: presentPlayerID = Player1
                    
            run = int(input(f"Enter Run Secured in {i+1} no ball: "))
            totalScore += run
            individualPlayerscore[presentPlayerID] += run 
            if run == 4: noOf4 += 1
            elif run == 6: noOf6 += 1
            elif run == 0:
                print(f"Player {Cricket.teamPlayers[self.PresentTeam][presentPlayerID]} is out")
                if Player1 == presentPlayerID:
                    print(f"List of Players in {Cricket.teamDic[self.PresentTeam]} Team")
                    for i in range(len(Cricket.teamPlayers[self.PresentTeam])):
                        print(f'{i+1} Player Name: {Cricket.teamPlayers[self.PresentTeam][i]}')
                    Player1 = int(input(f"Enter Player 1 ID: "))
                    individualPlayerscore[Player1] = 0
                else:
                    print(f"List of Players in {Cricket.teamDic[self.PresentTeam]} Team")
                    for i in range(len(Cricket.teamPlayers[self.PresentTeam])):
                        print(f'{i+1} Player Name: {Cricket.teamPlayers[self.PresentTeam][i]}')
                    Player2 = int(input(f"Enter Player 2 ID: "))
                    individualPlayerscore[Player2] = 0
        
        #match id and list of runs as list [totalScore,noOf4,noOf6,[player,player] score] 
        Cricket.matchScore[self.matchNo] = [totalScore,noOf4,noOf6,individualPlayerscore] 
        
    def scoreBoard(self):
        if len(Cricket.matchDic) > 0:
            print("List of Matches happed till now")
            for i in Cricket.matchDic:
                print(f"Match ID: {i} Match Name: {Cricket.matchDic[i]}")
            selectMatch = int(input("Enter Match No to Show Score: "))
            print(f"Total Score: {Cricket.matchScore[selectMatch][0]}\nNo of Fours: {Cricket.matchScore[selectMatch][1]}\nNo of Six: {Cricket.matchScore[selectMatch][2]}")
            print("Individual Plahyer Score:")
            for j in Cricket.matchScore[selectMatch][3]:
                print(f"Player ID: {j} Score: {Cricket.matchScore[selectMatch][3][j]}")        
        else: print("No Matches Played yet")


# In[2]:


#creating object
obj = Cricket()


# ## calling methods

# ### Add Team

# In[4]:


obj.addTeam()


# ### Add Players

# In[5]:


obj.addPlayer()


# ### View Player

# In[7]:


obj.viewPlayer()


# ### Start Match

# In[8]:


obj.startMatch()


# ### View Score Board

# In[9]:


obj.scoreBoard()


# In[ ]:




