import json
from abc import ABC

from collectors.base import Collector, get_wmi_values


class Processes(Collector, ABC):
    def collect(self) -> str:
        """
        Collector which collects Running Processes
        :return: json of all running processes in the system, in the format: [{PID, Name, Thread count}, ...]
        """
        wmi_processes = get_wmi_values("SELECT Handle,Caption,ThreadCount FROM Win32_Process", [r"Handle = \"(.+)\"",
                                                                                                r"Caption = \"(.+)\"",
                                                                                                r"ThreadCount = (\d+)"])

        # Compile the list of lists into a readable json
        output = list()
        for wmi_process in wmi_processes:
            process = dict({'Handle': wmi_process[0][0],
                            'Caption': wmi_process[1][0],
                            'ThreadCount': wmi_process[2][0]})
            output.append(process)

        return json.dumps(output)

    def header(self) -> str:
        return 'Running processses'
