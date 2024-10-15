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
def readROCs() -> list:
    return NotImplemented


@log_traffic
def readROC(rocId: str) -> dict:
    return NotImplemented


@log_traffic
def updateROC(rocId: str) -> dict:
    return NotImplemented


@log_traffic
def deleteROC(rocId: str) -> dict:
    return NotImplemented


@log_traffic
def createServiceInfo(service_info) -> dict:
    return NotImplemented


@log_traffic
def readServiceInfo() -> dict:
    return NotImplemented


@log_traffic
def updateServiceInfo(service_info) -> dict:
    return NotImplemented
