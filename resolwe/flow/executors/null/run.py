"""Local workflow executor."""
from __future__ import absolute_import, division, print_function, unicode_literals

import logging

from ..protocol import ExecutorProtocol  # pylint: disable=import-error
from ..run import BaseFlowExecutor

logger = logging.getLogger(__name__)  # pylint: disable=invalid-name


class FlowExecutor(BaseFlowExecutor):  # pylint: disable=abstract-method
    """Null dataflow executor proxy.

    This executor is intended to be used in tests where you want to save
    the object to the database but don't need to run it.
    """

    name = 'null'

    def run(self, data_id, script, verbosity=1):
        """Do nothing :)."""
        self._send_manager_command(ExecutorProtocol.FINISH)

    def terminate(self, data_id):
        """Do nothing :)."""
        pass
