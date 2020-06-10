# Climate Newspaper Downloader

CLI to download climate change news articles.

## Setup

Python 3.7+ (we use f-strings)

```bash
$ pip install -r requirements.txt
```

## Use

```bash
$ python download.py --newspapers all --n 50
```

This will download files into `$HOME`:

```bash
/Users/adam/climate-nlp
├── final
│   └── yellowstones-geysers-are-getting-more-active-and-nobody-knows-why.json
└── raw
    └── yellowstones-geysers-are-getting-more-active-and-nobody-knows-why.html
```

The interim data has the schema:
```json
{
TODO
}
```

## Useful commands

See how many articles you have:

```bash
$ ls ~/climate-nlp/final | wc -l
```
