import tweepy
import time

auth = tweepy.OAuthHandler('TvzlJ7Q4WbvaKeoHC2HOkjX74', 'Ecj5ufDOkkSlSXRvcD8rvnZxBL0y8pz4oATuDPhOWTrpRMMMD7')
auth.set_access_token('1348643525479469056-UNMtNafDRQvzLVSZETQdcz3oE59BxK','eYr5moqfdv23a7NRvpavWsymYEeN4PJmcNc77ktDH1CBT')

api = tweepy.API(auth)
while True:
  user = api.get_user('ace27091')
  f = user.followers_count
  api.update_profile(name=f'ACE {f} Followers')
  print(f'ACE {f} Followers')
  time.sleep(10)
