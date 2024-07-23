#
# This file is part of Glances.
#
# SPDX-FileCopyrightText: 2024 Nicolas Hennion <nicolas@nicolargo.com>
#
# SPDX-License-Identifier: LGPL-3.0-only
#

from typing import Any, Dict, Protocol, Tuple


class ContainersExtension(Protocol):
    def stop(self) -> None:
        raise NotImplementedError

    def update(self, all_tag) -> Tuple[Dict, list[Dict[str, Any]]]:
        raise NotImplementedError
