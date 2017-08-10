import turtle
import math

class User:

    #Sets the attributes for a new User object.
    def _init_(self, user_name, user_id):
        self.user_name = user_name
        self.user_id = user_id
        self.connections = []

    #Returns user_name
    def getUserName(self):
        return self.user_name

    #Returns user_id
    def getUserId(self):
        return self.user_id

    #Lists connections
    def getUserConnections(self):
        return self.connections

    #Adds a connection (passed in as a parameter) to the user's list of connections
    def addConnection(self, connection_id):
        self.connections.append(connection_id)


class Network:

    #Initialize network
    def _init_(self):
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


    #Return userId connected to given username
    ##If username does not exist,
    ## set user_id = -1 which means that the username is not there
    def getUserId(self, username):

        #4 conditionals

        user_id = -1

        for user in self.users:
            if username == user.getUserName():  #Is "user" in user.getUserName() the parameter? And how are you passing it in if the User class function only has "self" as a parameter...?
                user_id = user.getUserId()


        return user_id

    #Create connection between two users
    def addConnections(self, user1, user2):
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
        user2 = self.users[user1_id]



    #Print out all user in the network
    def printUsers(self):

    #Print out all the connections of the given username
    def printConnections(self, username):





def main():
    # Define the program flow for your user interface here.


# Runs your program.
if __name__ == '__main__':
    main():
