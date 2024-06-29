"""Crate DB API controllers."""

import logging
from foca.utils.logging import log_traffic  # type: ignore
from crate_db.exceptions import NotImplemented

# Get logger instance
logger = logging.getLogger(__name__)


@log_traffic
def createROC(ro_crate_data, ro_crate) -> dict:
    return NotImplemented


@log_traffic
def listROCs() -> list:
    return NotImplemented


@log_traffic
def readROC(ro_crate_id: str) -> dict:
    return NotImplemented


@log_traffic
def updateROC(ro_crate_id: str) -> dict:
    return NotImplemented


@log_traffic
def deleteROC(ro_crate_id: str) -> dict:
    return NotImplemented
