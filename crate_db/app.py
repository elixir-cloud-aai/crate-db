"""API server entry point."""

from pathlib import Path

from connexion import FlaskApp  # type: ignore
from foca import Foca

from crate_db.api.ga4gh.service_info import ServiceInfo  # type: ignore


def init_app() -> FlaskApp:
    """Initialize FOCA application.

    Returns:
        FOCA application.
    """
    foca = Foca(
        Path(__file__).parents[1] / 'deployment' / 'config.yaml',
    )
    app = foca.create_app()
    with app.app.app_context():
        service_info = ServiceInfo()
        service_info.init_service_info_from_config()
    return app


def run_app(app: FlaskApp) -> None:
    """Run FOCA application."""
    app.run(port=app.port)


if __name__ == "__main__":
    my_app = init_app()
    run_app(my_app)
