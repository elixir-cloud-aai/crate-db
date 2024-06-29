"""Crate exceptions."""

from foca.errors.exceptions import (
    ExtraParameterProblem,
    Forbidden,
    Unauthorized,
    OAuthProblem,
    BadRequest,
    InternalServerError,
    NotFound,
)

from werkzeug.exceptions import NotImplemented

exceptions = {
    Exception: {
        "message": "An unexpected error occurred.",
        "code": "500",
    },
    BadRequest: {
        "message": "The request is malformed.",
        "code": "400",
    },
    ExtraParameterProblem: {
        "message": "The request is malformed.",
        "code": "400",
    },
    Unauthorized: {
        "message": " The request is unauthorized.",
        "code": "401",
    },
    OAuthProblem: {
        "message": (
            "Unauthorized! You need to be logged in to"
            "perform this action."
        ),
        "code": 401,
    },
    Forbidden: {
        "message": "The requester is not authorized to perform this action.",
        "code": "403",
    },
    NotFound: {
        "message": "The requested resource wasn't found.",
        "code": "404",
    },
    InternalServerError: {
        "message": "An unexpected error occurred.",
        "code": "500",
    },
    NotImplemented: {
        "message": "The requested functionality is not implemented.",
        "code": "501",
    },
}
