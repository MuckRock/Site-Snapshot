"""
This DocumentCloud Add-On uses pdfkit https://pdfkit.org/ 
to create a PDF snapshot of a page and save the result to DocumentCloud
"""

from datetime import datetime
from documentcloud.addon import SoftTimeOutAddOn
import pdfkit
import uuid

class Snapshot(SoftTimeOutAddOn):
    """Add-On that uses pdfkit to take a snapshot and save it to DocumentCloud"""

    def main(self):
        """Grabs datetime, runs pdfkit on the URL,
        and saves the document with that timestamp as the title"""
        
        # For each URL given in the UI, pdfkit will capture the site as a PDF.
        for url in self.data["sites"]:
            # Captures the current datetime and a UUID to formulate as a title
            now = datetime.now()
            file_uuid = uuid.uuid4().hex
            file_name = f"{now} {file_uuid}.pdf"
            pdfkit.from_url(url, filename)
        # If a project ID is specified in the front end, upload to that project. 
        # Else it will just upload the captures to your documents in general. 
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
