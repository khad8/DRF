import os
import uuid
from datetime import datetime

def file_uploader(instance,filename):
    ext= filename.split(".")[-1]
    date_str=datetime.now().strftime("%Y/%m/%d")
    #date_str/uuid.ext
    new_filename=f"{date_str/uuid.uuid4()}.{ext}"
    return os.path.join(new_filename)