# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ActivitatsEconomiques
                                 A QGIS plugin
 ActivitatsEconomiques
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2018-11-14
        copyright            : (C) 2018 by CCU
        email                : jlopez@tecnocampus.cat
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load ActivitatsEconomiques class from file ActivitatsEconomiques.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .ActivitatsEconomiques import ActivitatsEconomiques
    return ActivitatsEconomiques(iface)
