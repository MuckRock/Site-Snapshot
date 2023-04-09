"""
This DocumentCloud Add-On uses pdfkit https://pdfkit.org/ to create a PDF snapshot of a page and save the result to DocumentCloud
"""

from documentcloud.addon import SoftTimeOutAddOn
import pdfkit
from datetime import datetime

class Snapshot(SoftTimeOutAddOn):
    """Add-On that uses pdfkit to take a snapshot and save it to DocumentCloud"""

    def main(self):
        now = datetime.now()
        for url in self.data["sites"]:
            print(url)
            pdfkit.from_url(url, 'out.pdf')
            self.client.documents.upload("out.pdf")

if __name__ == "__main__":
    Snapshot().main()
    
