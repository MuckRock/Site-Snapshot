"""
This DocumentCloud Add-On uses pdfkit https://pdfkit.org/ to create a PDF snapshot of a page and save the result to DocumentCloud
"""

from documentcloud.addon import SoftTimeOutAddOn
import pdfkit
import os

class Snapshot(SoftTimeOutAddOn):
    """Add-On that uses pdfkit to take a snapshot and save it to DocumentCloud"""

    def main(self):
        os.makedirs(os.path.dirname("./out/"), exist_ok=True)
        os.chdir("./out/")
        test=self.data.get("sites")
        for url in self.data["sites"]:
            doc = pdfkit.from_url(url)
            self.client.documents.upload(doc)

if __name__ == "__main__":
    Snapshot().main()
    
