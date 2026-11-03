import unittest
from app import hello_world, welcome_message


class TestHelloWorld(unittest.TestCase):
    def test_hello_world_message(self):
        self.assertEqual(
            hello_world(),
            "Hello, DevOps Wrong!"
        )
        
    def test_hello_world_return_type(self):
        self.assertIsInstance(hello_world(), str)


    def test_welcome_message_ritesh(self):
        self.assertEqual(
            welcome_message("Ritesh"),
            "Welcome to DevOps, Ritesh!"
        )

    def test_welcome_message_vedant(self):
        self.assertEqual(
            welcome_message("Dhruv"),
            "Welcome to DevOps, Dhruv!"
        )
    
    
if __name__ == "__main__":
    unittest.main()
