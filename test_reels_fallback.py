import json
import unittest
from unittest.mock import patch, mock_open
import server

class ReelsFallbackTest(unittest.TestCase):
    def test_failed_fetch_preserves_observation_time_and_filters_removed_accounts(self):
        snapshot = {'fetchedAt': 123, 'reels': [
            {'account': 'go_with_iru', 'url': 'https://www.instagram.com/reel/real/'},
            {'account': 'removed_account', 'url': 'https://www.instagram.com/reel/other/'}]}
        with patch.object(server, 'load_accounts', return_value=['go_with_iru']), \
             patch.object(server, 'cached', return_value=([], 999)), \
             patch('builtins.open', mock_open(read_data=json.dumps(snapshot))):
            reels, accounts, at = server.get_reels(False)
        self.assertEqual(at, 123)
        self.assertEqual([r['account'] for r in reels], ['go_with_iru'])

    def test_live_results_win(self):
        live = [{'account': 'go_with_iru'}]
        with patch.object(server, 'load_accounts', return_value=['go_with_iru']), \
             patch.object(server, 'cached', return_value=(live, 999)), \
             patch('builtins.open', side_effect=AssertionError('must not read old snapshot')):
            self.assertEqual(server.get_reels(False), (live, ['go_with_iru'], 999))

if __name__ == '__main__':
    unittest.main()
