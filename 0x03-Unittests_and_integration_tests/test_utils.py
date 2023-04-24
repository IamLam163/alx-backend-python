#!/usr/bin/env python3
"""
unit test for utils.access_nested_map
"""
from typing import Any, Dict, Mapping, Sequence, Union
import unittest
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """unittest class"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence,
                               expected: Union[Dict, int, str]) -> Any:
        """test access_nested_map()"""
        # self.assertEqual(access_nested_map(nested_map, path), expected)
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)
