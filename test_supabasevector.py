# test_supabasevector.py
"""
Tests for SupabaseVector module.
"""

import unittest
from supabasevector import SupabaseVector

class TestSupabaseVector(unittest.TestCase):
    """Test cases for SupabaseVector class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SupabaseVector()
        self.assertIsInstance(instance, SupabaseVector)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SupabaseVector()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
