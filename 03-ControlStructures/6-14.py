###
# A program that checks whether a given person is a good influencer, that is, 
# whether the person has at least two of the following accounts: Facebook, Twitter or Instagram
#

facebook = True
twitter = False
instagram = False

if (facebook and twitter == True) or (facebook and instagram == True) or (twitter and instagram == True):
     print("You are a good influencer!")
else:
     print("You might need more social network accounts to be a good influencer!")