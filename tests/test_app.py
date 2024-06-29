import unittest
from unittest.mock import patch, MagicMock
from pathlib import Path
from connexion import FlaskApp
from crate_db.app import init_app, run_app


class TestAppFunctions(unittest.TestCase):

    @patch('foca.Foca')
    @patch('connexion.FlaskApp')
    def test_init_app(self, MockFlaskApp, MockFoca):
        # Mock the return values
        mock_foca_instance = MagicMock()
        MockFoca.return_value = mock_foca_instance
        mock_app_instance = MagicMock(spec=FlaskApp)
        MockFlaskApp.return_value = mock_app_instance

        # Call the function
        app = init_app()

        # Assertions
        MockFoca.assert_called_once_with(
            Path(__file__).parents[1] / 'deployment' / 'config.yaml'
        )
        mock_foca_instance.create_app.assert_called_once()
        self.assertEqual(app, mock_app_instance)

    @patch('connexion.FlaskApp.run')
    def test_run_app(self, mock_run):
        # Mock setup
        mock_app_instance = MagicMock(spec=FlaskApp)

        # Call the function
        run_app(mock_app_instance)

        # Assertions
        mock_run.assert_called_once_with(port=mock_app_instance.port)


if __name__ == "__main__":
    unittest.main()
