import unittest
from unittest.mock import patch, MagicMock
from crate_db.api.elixircloud.controllers.crate_db import (
    createROC,
    listROCs,
    readROC,
    updateROC,
    deleteROC
)


class TestCrateDBAPIControllers(unittest.TestCase):

    @patch('crate_db.exceptions.NotImplemented')
    @patch('foca.utils.logging.log_traffic')
    def test_createROC(self, mock_log_traffic, mock_NotImplemented):
        # Mock data
        ro_crate_data = {
            'name': 'Test ROC',
            'description': 'A test ROC',
            'created_by': 'test_user',
        }
        ro_crate = {
            'id': '123',
            'name': 'Test Crate',
            'location': 'Test Location',
        }

        # Mock setup
        mock_log_instance = MagicMock()
        mock_log_traffic.return_value = mock_log_instance
        mock_NotImplemented.return_value = {'message': 'Not implemented'}

        # Call the function
        result = createROC(ro_crate_data, ro_crate)

        # Assertions
        mock_log_traffic.assert_called_once()
        mock_NotImplemented.assert_called_once()
        self.assertEqual(result, {'message': 'Not implemented'})

    @patch('crate_db.exceptions.NotImplemented')
    @patch('foca.utils.logging.log_traffic')
    def test_listROCs(self, mock_log_traffic, mock_NotImplemented):
        # Mock setup
        mock_log_instance = MagicMock()
        mock_log_traffic.return_value = mock_log_instance
        mock_NotImplemented.return_value = [
            {
                'id': '123',
                'name': 'Test Crate'
            }
        ]

        # Call the function
        result = listROCs()

        # Assertions
        mock_log_traffic.assert_called_once()
        mock_NotImplemented.assert_called_once()
        self.assertEqual(result, [{'id': '123', 'name': 'Test Crate'}])

    @patch('crate_db.exceptions.NotImplemented')
    @patch('foca.utils.logging.log_traffic')
    def test_readROC(self, mock_log_traffic, mock_NotImplemented):
        # Mock data
        ro_crate_id = "123"

        # Mock setup
        mock_log_instance = MagicMock()
        mock_log_traffic.return_value = mock_log_instance
        mock_NotImplemented.return_value = {'id': '123', 'name': 'Test Crate'}

        # Call the function
        result = readROC(ro_crate_id)

        # Assertions
        mock_log_traffic.assert_called_once()
        mock_NotImplemented.assert_called_once()
        self.assertEqual(result, {'id': '123', 'name': 'Test Crate'})

    @patch('crate_db.exceptions.NotImplemented')
    @patch('foca.utils.logging.log_traffic')
    def test_updateROC(self, mock_log_traffic, mock_NotImplemented):
        # Mock data
        ro_crate_id = "123"

        # Mock setup
        mock_log_instance = MagicMock()
        mock_log_traffic.return_value = mock_log_instance
        mock_NotImplemented.return_value = {'message': 'Not implemented'}

        # Call the function
        result = updateROC(ro_crate_id)

        # Assertions
        mock_log_traffic.assert_called_once()
        mock_NotImplemented.assert_called_once()
        self.assertEqual(result, {'message': 'Not implemented'})

    @patch('crate_db.exceptions.NotImplemented')
    @patch('foca.utils.logging.log_traffic')
    def test_deleteROC(self, mock_log_traffic, mock_NotImplemented):
        # Mock data
        ro_crate_id = "123"

        # Mock setup
        mock_log_instance = MagicMock()
        mock_log_traffic.return_value = mock_log_instance
        mock_NotImplemented.return_value = {'message': 'Not implemented'}

        # Call the function
        result = deleteROC(ro_crate_id)

        # Assertions
        mock_log_traffic.assert_called_once()
        mock_NotImplemented.assert_called_once()
        self.assertEqual(result, {'message': 'Not implemented'})


if __name__ == "__main__":
    unittest.main()
