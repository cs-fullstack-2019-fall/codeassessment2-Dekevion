# ### Problem 6
# Create a class called ClubMember 
# Each club member has a name and a role  
# Create ClubMember instances for the following people:
# ```
# Alfred - Club President
# Troy - Club Vice President
# Albert - Club Secretary
# Bob - Club Treasurer
# ```
# Add each member instance to a new club_members list that you create.
# Write the code needed to loop through the club member list and print the current number of members in the list, then the member’s name and club role, one per line using f strings.

# Example Output:
# ```
# There are currently 4 club members in the list!

# Club President: Alfred
# Club Vice President: Troy
# Club Secretary: Albert
# Club Treasurer: Bob
# ```


# Create a class called ClubMember
# Each club member has a name and a role
# Create ClubMember instances for the following people:


class ClubMember:
    def __init__(self, name,role):
        self.name = name
        self.role = role
    def __str__(self):
        return   f"{self.name}: his role is {self.role}"



# Alfred - Club President
# Troy - Club Vice President
# Albert - Club Secretary
# Bob - Club Treasurer

clubP = ClubMember('Alfred','Club President')
clubVP = ClubMember('Troy', 'Club Vice President')
clubS = ClubMember('Albert', 'Club Secretary')
clubT = ClubMember('Bob','Club Treasurer')


# Add each member instance to a new club_members list that you create.

memberList = [clubP,clubVP,clubS,clubT]


# Write the code needed to loop through the club member list and print the current number of members in the list,
# then the member’s name and club role, one per line using f strings.

for i in memberList:
    print(i)
