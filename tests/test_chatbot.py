import unittest
from src import chatbot

class TestChatbot(unittest.TestCase):
    def test_suicidal_detection(self):
        text = "I want to die"
        self.assertTrue(chatbot.contains_suicidal_thoughts(text))
        reply = chatbot.bot_reply(1, text)
        self.assertIn("emergency", reply.lower())

    def test_anxiety_reply(self):
        text = "I feel anxious before exams"
        reply = chatbot.bot_reply(1, text)
        self.assertIn("anxiety", reply.lower() or "breathing" in reply.lower())

if __name__ == '__main__':
    unittest.main()
