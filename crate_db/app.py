"""API server entry point."""

from pathlib import Path

from connexion import FlaskApp  # type: ignore
from foca import Foca


def init_app() -> FlaskApp:
    """Initialize FOCA application.

    Returns:
        FOCA application.
    """
    foca = Foca(
        Path(__file__).parents[1] / 'deployment' / 'config.yaml',
    )
    app = foca.create_app()
    return app


def run_app(app: FlaskApp) -> None:
    """Run FOCA application."""
    app.run(port=app.port)


if __name__ == "__main__":
    my_app = init_app()
    run_app(my_app)
