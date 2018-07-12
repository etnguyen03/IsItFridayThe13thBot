# IsItFridayThe13thBot
# http://www.reddit.com/r/IsItFridayThe13th
# Copyright 2018 Ethan Nguyen, all rights reserved

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

# Syntax for secret.txt
# Line 1: Reddit Client ID
# Line 2: Reddit Client Secret
# Line 3: Reddit Username
# Line 4: Reddit Password

import praw
import datetime

secretFile = open("secret.txt").read().split("\n")

reddit = praw.Reddit(user_agent='IsItFridayThe13thBot', client_id=secretFile[0], client_secret=secretFile[1], username=secretFile[2], password=secretFile[3])
subreddit = reddit.subreddit('IsItFridayThe13th')

today = datetime.date.today()
string = today.strftime("%A %d")
todoString = today.strftime("%A, %B %d, %Y")

# find the next Friday the 13th
Break = False
incrementDays = 1
while (Break == False):
    newDT = today + datetime.timedelta(days=incrementDays)
    stringThing = newDT.strftime("%A %d")
    if stringThing == "Friday 13":
        Break = True
    else:
        incrementDays += 1

print (incrementDays)

if (string == "Friday 13"):
    subreddit.submit(title="Is it Friday the 13th?", selftext="Yes.\n---\n^(Today is " + todoString + ". The next Friday the 13th is " + str(incrementDays) + " away. This message was posted by a bot. [source](https://github.com/etnguyen03/IsItFridayThe13thBot))")
else:
    subreddit.submit(title="Is it Friday the 13th?", selftext="No.\n---\n^(Today is " + todoString + ". The next Friday the 13th is " + str(incrementDays) + " away. This message was posted by a bot. [source](https://github.com/etnguyen03/IsItFridayThe13thBot))")
