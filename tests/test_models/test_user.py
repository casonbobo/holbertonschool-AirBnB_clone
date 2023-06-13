#!/usr/bin/python3
import unittest
from models.user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User()

    def test_inheritance(self):
        self.assertIsInstance(self.user, User)
        self.assertEqual(type(self.user).__name__, "User")
        self.assertTrue(hasattr(self.user, "id"))
        self.assertTrue(hasattr(self.user, "created_at"))
        self.assertTrue(hasattr(self.user, "updated_at"))

    def test_attributes(self):
        self.assertTrue(hasattr(self.user, "email"))
        self.assertEqual(self.user.email, "")
        self.assertTrue(hasattr(self.user, "password"))
        self.assertEqual(self.user.password, "")
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertEqual(self.user.first_name, "")
        self.assertTrue(hasattr(self.user, "last_name"))
        self.assertEqual(self.user.last_name, "")

    def test_to_dict(self):
        user_dict = self.user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertEqual(user_dict["email"], "")
        self.assertEqual(user_dict["password"], "")
        self.assertEqual(user_dict["first_name"], "")
        self.assertEqual(user_dict["last_name"], "")
        self.assertEqual(user_dict["__class__"], "User")
        self.assertTrue("created_at" in user_dict)
        self.assertTrue("updated_at" in user_dict)

if __name__ == "__main__":
    unittest.main()
