# MarkovianTweets
----
This is a project that makes use of Markov Chains to model tweets after different celebries.
The custom tweet generator will only run on a Unix based computer. 

Addtionally to make use of the custom tweet generator work you need to get signup for a twitter developer
account that will give you Oauth1 key and secret to give you access to the RESTful twitter 
API.


## Installation

1. Clone the repository
2. Install `pip install python-twitter`
3. Signup up for twitter account than login to the twitter devloper dash to get Oauth information
which gets added to the tweetGrabber.py script
4. Compile with `g++ -std=c++11 -o tweetGen tweetGen.cpp`
5. Run with `./tweetGen`


## Future Plans

* Make the Markov Chain degree of accuracy a variable
* Make it a backend for a Twitterbot


## Credits

Collaborators: Adam Karpowich and Mike Mizikar

