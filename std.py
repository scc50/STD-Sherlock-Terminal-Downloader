

print("""
____  _   _ _____ ____  _     ___   ____ _  __  _____ ____
/ ___|| | | | ____|  _ \| |   / _ \ / ___| |/ / |_   _|  _ \
\___ \| |_| |  _| | |_) | |  | | | | |   | ' /    | | | | | |
___) |  _  | |___|  _ <| |__| |_| | |___| . \    | | | |_| |
|____/|_| |_|_____|_| \_\_____\___/ \____|_|\_\   |_| |____/

""")


import urllib.request # Kugirango Dukore HTTP REQUEST
from rich.progress import Progress # Kwerekana Karia Ga Progress Bar

url = "https://i.pinimg.com/736x/18/a0/ce/18a0ce75262459dc6ecc57233cc8d3b8.jpg"
file_name = url.split("/").pop() # Kubitandukanya Ukoresheke / Then nkahita delete that part


with urllib.request.urlopen(url) as data:
    file_size = int(data.getheader("Content-Length")) # Kugirango Tubone File Sise


with Progress() as progress_bar:
    # Progress Bar WIth download
    task = progress_bar.add_task(f"[blue]Downloading {file_name}", total=file_size)

    # Call back function ya Ku Downloading no Kwa Updating value ya Progress Bar
    def reporthook(block_num, block_size, total_size):
        progress_bar.update(task, advance=block_size)


    urllib.request.urlretrieve(url, file_name, reporthook) # Calling it with callback
