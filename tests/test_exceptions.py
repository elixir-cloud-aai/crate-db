import unittest
from crate_db.exceptions import (
    ExtraParameterProblem,
    Forbidden,
    Unauthorized,
    OAuthProblem,
    BadRequest,
    InternalServerError,
    NotFound,
    NotImplemented
)
from crate_db import exceptions


class TestExceptions(unittest.TestCase):

    def test_exception_messages(self):
        test_cases = [
            (
                Exception,
                "An unexpected error occurred.",
                500
            ),
            (
                BadRequest,
                "The request is malformed.",
                400
            ),
            (
                ExtraParameterProblem,
                "The request is malformed.",
                400
            ),
            (
                Unauthorized,
                " The request is unauthorized.",
                401
            ),
            (
                OAuthProblem,
                "Unauthorized! You need to be logged in to"
                "perform this action.",
                401
            ),
            (
                Forbidden,
                "The requester is not authorized to perform this action.",
                "403",
            ),
            (
                NotFound,
                "The requested resource wasn't found.",
                "404"
            ),
            (
                InternalServerError,
                "An unexpected error occurred.",
                500
            ),
            (
                NotImplemented,
                "The requested functionality is not implemented.",
                501
            ),
        ]

        for exception, expected_message, expected_code in test_cases:
            with self.subTest(exception=exception):
                self.assertEqual(
                    exceptions[exception]["message"], expected_message
                )
                self.assertEqual(
                    exceptions[exception]["code"], expected_code
                )


if __name__ == '__main__':
    unittest.main()
