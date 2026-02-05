import unittest
from hw2 import Profile, Activity, Post, Message, User

class TestProfile(unittest.TestCase):
    """Test cases for the Profile class."""
    prof = Profile('1','2','3','4')
    print(prof)
    print(f'{prof.username}, {prof.password}, {prof.screen_name}, {prof.email}')
    prof.modify_profile('a','b','c')
    print(prof)
    print(f'{prof.username}, {prof.password}, {prof.screen_name}, {prof.email}')

    

class TestActivity(unittest.TestCase):
    """Test cases for the Activity class."""
    test = User('abc','2','3','4')
    act = Activity(test,'CONTENT')
    print(act)
    print(f'FULL USER VAR:\n{act.user},\nCONTENTS:\n{act.content}')

class TestPost(unittest.TestCase):
    """Test cases for the Post class."""
    test = User('abc','2','3','4')
    postvar = Post(test,'CONTENT')
        

class TestMessage(unittest.TestCase):
    """Test cases for the Message class."""
    test_user1 = User('abc1','2','3','4')
    test_user2 = User('abc2','2','3','4')
    message = Message(test_user1,'CONTENT', test_user2)
    print(message)

class TestUser(unittest.TestCase):
    """Test cases for the User class."""
    # Add more test cases for other methods and classes
    
    def setUp(self):
        self.user = User("user1", "password1", "User One", "user1@example.com")
        self.user2 = User("user2", "password1", "User Two", "user2@example.com")
        
    def test_create_post(self):
        """Test creating a post for a user."""
        
        post = self.user.create_post("Test Post Content")

        # Check if the post is added to the user's posts list
        self.assertIn(post, self.user.posts)
        # Check if the user is correct
        self.assertEqual(post.user, self.user)
        # Check if the content of the post is correct
        self.assertEqual(post.content, "Test Post Content")
    
    def test_create_message(self):

        mess = self.user.send_message(self.user2,"Test Message Content")

        # Check if the post is added to the user's posts list
        self.assertIn(mess, self.user.messages)
        # Check if the user is correct
        self.assertEqual(mess.user, self.user)
        # Check if the content of the post is correct
        self.assertEqual(mess.content, "Test Message Content")
    

    

if __name__ == "__main__":
    unittest.main()

