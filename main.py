"""
This DocumentCloud Add-On uses pdfkit https://pdfkit.org/ 
to create a PDF snapshot of a page and save the result to DocumentCloud
"""

from datetime import datetime
from documentcloud.addon import SoftTimeOutAddOn
import pdfkit


class Snapshot(SoftTimeOutAddOn):
    """Add-On that uses pdfkit to take a snapshot and save it to DocumentCloud"""

    def main(self):
        """Grabs datetime, runs pdfkit on the URL,
        and saves the document with that timestamp as the title"""
        now = datetime.now()
        for url in self.data["sites"]:
            pdfkit.from_url(url, f"{now}.pdf")
        if self.data.get("project_id"):
            self.client.documents.upload_directory(
                ".",
                project=self.data.get("project_id"),
                access=self.data["access_level"],
            )
        else:
            self.client.documents.upload_directory(
                ".", access=self.data["access_level"]
            )


if __name__ == "__main__":
    Snapshot().main()
