# 17-3 -> this can be run only from console and from tests dir
import unittest

import sys
sys.path.insert(1, '../api')

import python_repos as pr



class PythonReposTest(unittest.TestCase):

    BASE_URL = 'https://api.github.com/search/' \
               'repositories?q=language:python&sort=stars'

    def setUp(self):
        url = self.BASE_URL
        self.response = pr.make_api_call(url)

    def test_status_code_correct(self):
        self.assertEqual(self.response.status_code, 200)

    def test_status_code_incorrect(self):
        url = 'https://api.github.com/search/repositories?q=language:pysdcsdcs'
        response = pr.make_api_call(url)
        self.assertNotEqual(response.status_code, 200)

    def test_repo_dicts_len(self):
        dict = pr.make_repo_dicts(self.response)
        result = len(dict)
        self.assertEqual(result, 30)

    def test_total_repos(self):
        response_dict = self.response.json()
        total_repos = int(response_dict['total_count'])
        self.assertGreater(total_repos, 7_000_000)


if __name__ == '__main__':
    unittest.main()
