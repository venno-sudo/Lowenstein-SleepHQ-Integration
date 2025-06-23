import os
import datetime
import shutil

def create_year_month_folders():
    """Creates folders for the current year and month."""
    base_path = "/home/USER/prisma/archive/"
    mount_path = "/media/USER/Weinmann"
    data_path = "/home/USER/prisma/data"
    now = datetime.datetime.now()
    year_folder = str(now.year)
    month_folder = now.strftime("%m")  # Get month
    day_folder = now.strftime("%d") # get day
    # Create year folder if it doesn't exist
    year_path = os.path.join(base_path ,year_folder)
    if not os.path.exists(year_path):
        os.makedirs(year_path)

    # Create month folder inside the year folder
    month_path = os.path.join(base_path, year_folder, month_folder)
    if not os.path.exists(month_path):
        os.makedirs(month_path)

    # Create day folder inside the year folder
    day_path = os.path.join(base_path, year_folder, month_folder, day_folder)
    if not os.path.exists(day_path):
        os.makedirs(day_path)

    # Copy data from SD card
    files = ["config.pcfg", "therapy.pdat",]
    for myfile in files:
        destination = os.path.join(base_path, year_folder, month_folder, day_folder, myfile)
        source = os.path.join(mount_path, myfile)
        pdata = os.path.join(data_path, myfile)
        shutil.copyfile(source, destination)
        shutil.copyfile(source, pdata)

if __name__ == "__main__":
    create_year_month_folders()

