class NetworkDevice:
    """
    Base class for all Network devices- Switch, Router and WirelessAP
    """

    def __init__(self, hostname, device_type):
        self.hostname = hostname  # The name of the device
        self.device_type = device_type  # Saved as "Switch", "Router", or "AP"

        """
        CLI state
        A mode stack is used, the current mode is always the last item on the list
        Always start of user exec mode!
        """
        self.mode_stack = ["user_exec"]

        self.current_interface = None  # current interface

        """
        Running-config, saved as a dictionary
        """
        self.running_config = {
            "hostname":     hostname,
            "enable_secret":    None,
            "banner_motd":  None,
        }

        """
        The actual interfaces on the device
        Subclasses for all config modes in order to change the hostname 
        """
        self.interfaces = {}

        print(f"{device_type.capitalize()} '{hostname}' initialised.")

    def get_prompt(self):
        """
        Returns the correct CLI mode based on the prompt 
        """
        mode = self.mode_stack[-1]  # -1 in order to get the last item on the list

        if mode == "user_exec":
            return f"{self.hostname}>"
        elif mode == "privileged_exec":
            return f"{self.hostname}#"
        elif mode == "global_config":
            return f"{self.hostname}(config)#"
        elif mode == "interface_config":
            return f"{self.hostname}(config-if)#"
        elif mode == "vlan_config":
            return f"{self.hostname}(config-vlan)"
        elif mode == "line_config":
            return f"{self.hostname}(config-line)#"
        else:
            return f"{self.hostname}>"

    def __repr__(self):
        return f"<{self.device_type.capitalize()} hostname= '{self.hostname}'>"

# Test


d1 = NetworkDevice("SW1", "switch")
d2 = NetworkDevice("R1", "router")

print(d1)
print(d2.hostname)
print(d1.get_prompt())
print(d1.mode_stack)
