# Tutipleni

This project is to download all the books in "https://thetrove.net/Books/" maintaining the path structure of the web page.

## Getting Started

This is a simple "script" make it with scrapy, so, here you have install and running explanations.

### Prerequisites

Python3.7 -> https://www.python.org/downloads/release/python-373/

### Installing

The first step is install python in your computer(read the url in prerequisites)
After install python you need to install the requirements, for that we use pip.

```
pip install -r requirements.txt
```

And that's all!!!

###Configuration

In  ./tutipleni/settings.py you have all the configuration variables, the most important are:
 - FILES_STORE: folder where save the files.
 - DOWNLOAD_DELAY: delay between downloads.
 - CONCURRENT_REQUESTS_*: To set the concurrents requests at the same time.


###running
In the root folder of the project launch this command
```
scrapy crawl thetrhove
```
