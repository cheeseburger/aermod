"""
Created on Sun Jul 14 06:43:49 2024

@author: roelofburger
"""

class AERMOD:
    def __init__(self):
        self.domain_details = {}
        self.output_files = []
        self.aermet = self.AERMET()
        self.aermap = self.AERMAP()

    def run(self):
        if not self.check():
            print("Configuration incomplete. Please check the setup.")
            return
        print("Running AERMOD...")
        # Code to run AERMOD
        print("AERMOD run complete.")

    def check(self):
        # Check if all necessary configurations are set
        return True

    def create_domain(self, domain_details):
        self.domain_details = domain_details
        print("Domain created with details:", self.domain_details)

    def plot_concentration(self):
        print("Plotting concentration...")
        # Code to plot concentration

    def plot_wind_rose(self):
        print("Plotting wind rose...")
        # Code to plot wind rose

    class AERMET:
        def clean(self):
            print("Cleaning AERMET output files...")
            # Code to clean AERMET output files

        def create(self, config):
            self.config = config
            print("AERMET configuration created:", self.config)

        def show_config(self):
            print("AERMET configuration:", self.config)

        def run(self):
            print("Running AERMET...")
            # Code to run AERMET
            print("AERMET run complete.")

        def check_messages(self):
            print("Checking AERMET messages...")
            # Code to check AERMET messages

    class AERMAP:
        def run(self):
            print("Running AERMAP...")
            # Code to run AERMAP
            print("AERMAP run complete.")

        def create(self, config):
            self.config = config
            print("AERMAP configuration created:", self.config)

        def create_receptor_file(self, receptors):
            self.receptors = receptors
            print("Receptor file created with receptors:", self.receptors)