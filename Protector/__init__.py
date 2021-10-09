"""Initialize Framework for Protector"""
# Protector (A telegram bot project)
# Copyright (C) 2021 - Kunaldiwan All rights reserved. Source code available under the AGPL.

# This file is part of Protector.

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

import asyncio
import logging

import aiorun

from .core import Protector, setup_log

aiorun.logger.disabled = True
log = logging.getLogger("Main")
protector = Protector()

LOGGER = logging.getLogger("__name__").setLevel(logging.WARNING)

def start():
    """Main entry point"""
    setup_log()
    log.info("Loading code...")

    try:
        import uvloop  # pylint: disable=C0415
    except ImportError:
        log.warning("uvloop not installed! Skipping...")
        print(
            "\nuvloop not installed! "
            "bot will work the same, but in a bit slower speed.\n"
            'You may install it by "poetry install -E uvloop" or "pip install uvloop"\n'
        )
    else:
        uvloop.install()

    loop = asyncio.new_event_loop()
    aiorun.run(Protector.begin(loop=loop), loop=loop)
