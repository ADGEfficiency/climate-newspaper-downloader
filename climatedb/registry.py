import random

from climatedb.newspapers.guardian import guardian
from climatedb.newspapers.fox import fox
from climatedb.newspapers.skyau import check_sky_au_url, parse_sky_au_url
from climatedb.newspapers.nytimes import nytimes

from climatedb.newspapers.cnn import cnn
from climatedb.newspapers.economist import economist
from climatedb.newspapers.newshub import newshub
from climatedb.newspapers.nzherald import nzherald
from climatedb.newspapers.stuff import stuff
from climatedb.newspapers.aljazeera import aljazeera
from climatedb.newspapers.atlantic import atlantic
from climatedb.newspapers.washington_post import washington_post
from climatedb.newspapers.dw import dw
from climatedb.newspapers.bbc import bbc
from climatedb.newspapers.independent import independent
from climatedb.newspapers.dailymail import dailymail


def find_newspaper_from_url(url):
    for paper in registry:
        if paper["newspaper_url"] in url:
            return paper


registry = [
    guardian,
    bbc,
    nzherald,
    stuff,
    newshub,
    economist,
    aljazeera,
    atlantic,
    washington_post,
    cnn,
    dw,
    independent,
    dailymail,
    fox,
    nytimes,
    {
        "newspaper_id": "skyau",
        "newspaper": "Sky News Australia",
        "newspaper_url": "skynews.com.au",
        "checker": check_sky_au_url,
        "parser": parse_sky_au_url,
    },
]


def get_newspaper(newspaper):
    for paper in registry:
        if paper["newspaper_id"] == newspaper:
            return paper
    raise ValueError(f"{newspaper} not in registry")


def get_newspapers_from_registry(newspapers=None):
    if (newspapers == ("all",)) or (newspapers is None):
        papers = registry
    else:
        if isinstance(newspapers, str):
            newspapers = [newspapers, ]
        papers = [n for n in registry if n["newspaper_id"] in newspapers]
    random.shuffle(papers)
    return papers