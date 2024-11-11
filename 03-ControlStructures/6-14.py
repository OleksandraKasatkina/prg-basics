###
# A program that checks whether a given person is a good influencer, that is, 
# whether the person has at least two of the following accounts: Facebook, Twitter or Instagram
#

facebook = input('Do you have account on Facebook?(y/n): ')
twitter = input('Do you have account on Twitter?(y/n): ')
instagram = input('Do you have account on Instagram?(y/n): ')

if (facebook and twitter == 'y') or (facebook and instagram == 'y') or (twitter and instagram == 'y'):
     print("You are a good influencer!")
else:
     print("You might need more social network accounts to be a good influencer!")