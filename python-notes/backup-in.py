import shutil
import os
import datetime
source=r"C:\Users\ASUS\OneDrive\Desktop\docker files notes\python-notes"
destination=r"C:\Users\ASUS\OneDrive\Desktop\docker files notes\backup-python"
def backup(source, destination):
    today=datetime.date.today()
    data=os.path.join(destination, f"backup_{today}.tar.gz")
    shutil.make_archive(data.replace('.tar.gz', ''),'gztar', source)
backup(source,destination)