import unittest, subprocess

from main import get_tree, replace_content

class TestMain(unittest.TestCase):
    def test_returns_directory_tree_structure(self):
        result = get_tree()
        self.assertIsInstance(result, str)
        self.assertNotEqual(result, "")
        self.assertTrue("├──" in result or "└──" in result)
    
    def test_returns_empty_string_when_ignore_list_contains_all_directories(self):
        ignore_list = ["README.md", "main.py", "tests", "__pycache__", "TEST.md", "exec.py", "temp_file.txt"]
        result = get_tree(ignore_list=ignore_list)
        self.assertEqual(result, "")
    def test_replace_content_replaces_content_between_comments(self):
        # Create a temporary file with initial content
        with open('temp_file.txt', 'w') as file:
            file.write('Initial content\n<!-- _TREE_ -->\nOld content\n<!-- _ENDTREE_ -->\nMore content')

        # Call the replace_content function
        replace_content('temp_file.txt', 'New content')

        # Read the modified file
        with open('temp_file.txt', 'r') as file:
            modified_content = file.read()

        # Check if the content between the comments has been replaced
        expected_content = 'Initial content\n<!-- _TREE_ -->\nNew content\n<!-- _ENDTREE_ -->\nMore content'
        self.assertEqual(modified_content, expected_content)

        # Remove the temporary file
        subprocess.run(['rm', 'temp_file.txt'])

if __name__ == '__main__':
    # Discover and run tests
    unittest.main()