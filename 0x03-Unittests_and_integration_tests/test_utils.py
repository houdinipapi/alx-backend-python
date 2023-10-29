#!/usr/bin/env python3

"""
Unit Test
"""

import unittest
import requests
from parameterized import parameterized
from unittest.mock import patch
from utils import (access_nested_map, get_json, memoize)


class TestAccessNestedMap(unittest.TestCase):
    """
    Class for Testing Access Nested Map
    """

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(self, nested_map, path, expected_result):
        """
        Test that the method returns what it is supposed to.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_execution(
        self, nested_map, path, expected_exception_message
    ):
        """
        Test that a KeyError is raised for the respective inputs
        """
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)
        self.assertEqual(f"KeyError('{expected_exception_message}')",
                         repr(e.exception))
