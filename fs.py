


import urllib.request
from rich.progress import Progress

url = "https://i.pinimg.com/736x/18/a0/ce/18a0ce75262459dc6ecc57233cc8d3b8.jpg"
file_name = url.split("/").pop()

print(file_name)

with urllib.request.urlopen(url) as data:
    file_size = int(data.getheader("Content-Length"))


with Progress() as progress_bar:
    task = progress_bar.add_task(f"[blue]Downloading {file_name}", total=file_size)

    def reporthook(block_num, block_size, total_size):
        progress_bar.update(task, advance=block_size)


    urllib.request.urlretrieve(url, file_name, reporthook)
