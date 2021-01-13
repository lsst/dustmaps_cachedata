"""Sphinx configuration file for an LSST stack package.

This configuration only affects single-package Sphinx documentation builds.
"""

from documenteer.sphinxconfig.stackconf import build_package_configs
import lsst.dustmaps.cachedata


_g = globals()
_g.update(build_package_configs(
    project_name='dustmaps_cachedata',
    version=lsst.dustmaps.cachedata.version.__version__))
