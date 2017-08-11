import turtle
import math
import time

class User:

    #Sets the attributes for a new User object.
    def __init__(self, user_name, user_id, update):
        self.user_name = user_name
        self.user_id = user_id
        self.connections = []
        # self.status_update = update

    #Returns user_name
    def getUserName(self):
        return self.user_name

    #Returns user_id
    def getUserId(self):
        return self.user_id

    #Lists connections
    def getConnections(self):
        return self.connections

    #Adds a connection (passed in as a parameter) to the user's list of connections
    def addConnection(self, connection_id):
        self.connections.append(connection_id)
    #
    # def getStatusUpdate(self):
    #     return self.update


class Network:

    #Initialize network
    def __init__(self):
        self.users = []

    #Gives you the number of total users in the network
    def numUsers(self):
        return len(self.users)

    #Check if passed username is taken, and if not, add username to Network
    def addUser(self, username):

        for user in self.users:
            if username == user.getUserName():
                print("Sorry, that name is taken. Try again.")
                return

        user_id = len(self.users)

        self.users.append(User(username, user_id))
        time.sleep(0.5)
        print("A new user, \"" + username + ",\" has been created!")


    #Return userId connected to given username
    ##If username does not exist,
    ## set user_id = -1 which means that the username is not there
    def getUserId(self, username):

        #4 conditionals

        user_id = -1

        for user in self.users:
            if username == user.getUserName():  #"user" is referring to the current username in self.users
                user_id = user.getUserId()


        return user_id

    #Create connection between two users
    def addConnection(self, user1, user2):
        #4 cases to check:
        ##1. If users are both in the network
        ##2. If users are already connected
        ##3. If user is trying to connect to self
        ##4. Connect them

        ## maybe later-- if blocked?

        #Creates new variables to hold user 1 and user 2's IDs
        user1_id = self.getUserId(user1)
        user2_id = self.getUserId(user2)

        user1 = self.users[user1_id]
        user2 = self.users[user2_id]

        #A conditional to check if user1 and/or user2 exist
        if user1_id == user2_id:
            print("You can't connect to yourself. Please try again.")
            return

        if user1_id == -1 or user2_id == -1:
            print ("One or two of the users do not exist. Please try again.")
            return

        if user1_id in user2.getConnections(): #Does it matter whether user1_id is user1_id or "user1"
            print("Those users are already connected!")
            return

        else:
            user1.addConnection(user2_id)
            user2.addConnection(user1_id)
            return

    #Prints out existing users
    def printUsers(self):
        print("Network Users:")
        for user in self.users:
            print("\tUser {}: {}".format(user.getUserId()+1,user.getUserName()))


    #Print out all the connections of the given username
    def printConnections(self, username):
        user =  self.users[self.getUserId(username)]
        connections =  user.getConnections()
        print("{}'s connections:".format(user.getUserName()))
        for friendID in connections:
            friend = self.users[friendID]
            print("\t{}".format(friend.getUserName()))


    # def addStatusUpdate(self, update):
    #

def main():
    # Define the program flow for your user interface here.

    #Creates new "myNetwork" object in the "Network" class
    myNetwork = Network()
    done = False
    while not done:

        action = input("\n~~~\nWhat would you like to do?\n(Type \"show\" to display instructions)\n")

        #1. Print a user
        #2. Add a user
        #3. Add a connection
        #4. Print connections
        #5. Print users
        #6. Be able to quit the program
        #7. Deals with anything else (such as input you haven't defined)

        if action == "show":
            print("""\n

                USERS
                -----
                Make a new user account (make)
                Print existing users (print users)

                CONNECTIONS
                -----------
                Add a connection to an existing user account (add c)
                Print a user\'s connections (print c)

                QUIT
                ----
                Quit the program (q)
                """)
        if action == "make":
            userInput = input("Choose a username: ")
            print("\n")
            myNetwork.addUser(userInput)

        if action == "print users":
            print("\n")
            myNetwork.printUsers()
            time.sleep(1)


        if action == "add c":
            user1 = input("Please print your username: ")
            user2 = input("Who would you like to connect to? ")
            print("\n")
            myNetwork.addConnection(user1, user2)
            print("Connection made!")
            time.sleep(1)


        if action == "print c":
            userInput = input("Whose connections would you like to see? ")
            print("\n")
            myNetwork.printConnections(userInput)
            time.sleep(1)


        if action == "q":
            done = True

        else:
            print("Sorry, I don't understand that. Please try again.")
            time.sleep(1)




# Runs your program.
if __name__ == '__main__':
    main()
