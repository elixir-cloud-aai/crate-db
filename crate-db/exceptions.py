"""Petstore exceptions."""

from connexion.exceptions import (
    BadRequestProblem,
    ExtraParameterProblem,
    Forbidden,
    Unauthorized,
    OAuthProblem,
)
from werkzeug.exceptions import (
    BadRequest,
    InternalServerError,
    NotFound,
)

exceptions = {
    Exception: {
        "message": "Oops, something unexpected happened.",
        "code": 500,
    },
    BadRequestProblem: {
        "message": "We don't quite understand what it is you are looking for.",
        "code": 400,
    },
    BadRequest: {
        "message": "We don't quite understand what it is you are looking for.",
        "code": 400,
    },
    ExtraParameterProblem: {
        "message": "We don't quite understand what it is you are looking for.",
        "code": 400,
    },
    OAuthProblem: {
        "message": (
            "Unauthorized! You need to be logged in to"
            "perform this action."
        ),
        "code": 401,
    },
    Unauthorized: {
        "message": (
            "Unauthorized!"
        ),
        "code": 401,
    },
    Forbidden: {
        "message": (
            "Not authorized to perform this action."
        ),
        "code": 403,
    },
    NotFound: {
        "message": "Not sure what you are looking for, but it's not here.",
        "code": 404,
    },
    InternalServerError: {
        "message": "Oops, something unexpected happened.",
        "code": 500,
    },
}