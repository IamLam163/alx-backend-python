#!/usr/bin/env python3
"""
unit test for utils.access_nested_map
"""
from typing import Any, Dict, Mapping, Sequence, Union
import unittest
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
import requests
from unittest import mock


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

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence, res: Exception) -> Any:
        """this method raises a Key Error"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Class makes and tests Mock HTTP calls"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url: str, test_payload: dict) -> Any:
        """test get_json()"""
        with mock.patch("requests.get") as get_data:
            res = mock.Mock()
            res.json.return_value = test_payload
            get_data.return_value = res
            # url = get_json(test_url)
            self.assertEqual(get_json(test_url), test_payload)


class TestMemoize(unittest.TestCase):
    """Class implements memoization"""

    def test_memoize(self) -> None:
        """Test memoize"""
        class TestClass:
            """a method"""

            def a_method(self):
                """a method"""
                return 42

            @memoize
            def a_property(self):
                """return a_method"""
                return self.a_method()
        with mock.patch.object(TestClass, "a_method", return_value=lambda: 42) as func:
            test_obj = TestClass()
            self.assertEqual(test_obj.a_property(), 42)
            self.assertEqual(test_obj.a_property(), 42)
            func.assert_called_once()
