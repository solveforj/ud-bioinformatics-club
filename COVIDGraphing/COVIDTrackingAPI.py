import json
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.dates import date2num, DayLocator, DateFormatter
import matplotlib.ticker as mticker
import datetime as dt
from matplotlib.patches import Ellipse

def usaCOVIDTestingStats(x_axis='date',y_scale="linear",y_label = "Number of tests", y_axis='total',y1_label = "Positive cases",y1_axis='positive'):
    response = requests.get("https://covidtracking.com/api/us/daily")
    text = json.loads(response.text)
    df = pd.DataFrame.from_records(text)
    df['date'] = date2num(pd.to_datetime(df['date'], format='%Y%m%d').tolist())
    print df
    x = df[x_axis]
    y = df[y_axis]
    y1 = df[y1_axis]

    fig, ax = plt.subplots()
    plt.rcParams["font.family"] = "Arial"
    plt.xlabel("Date", fontname="Arial Rounded MT Bold")
    plt.ylabel("People (" + y_scale +")" , fontname="Arial Rounded MT Bold")
    plt.grid(color='grey', linestyle='-', linewidth=0.5, alpha=0.5)
    plt.xticks(fontsize=8, fontname="Arial")
    plt.yticks(fontsize=8, fontname="Arial")
    ax.set_yscale(y_scale)

    plt.gca().xaxis.set_major_locator(DayLocator())
    plt.gca().xaxis.set_major_formatter(DateFormatter('%m/%d'))

    line1, = plt.plot(x, y, label=y_label, marker='o', color='blue', mfc='white', mec="black", alpha=0.8, ms=3)
    line2, = plt.plot(x, y1, label = y1_label, marker='o', color='orange', mfc='white', mec="black", alpha=0.8, ms=3)
    plt.legend(handles=[line1, line2], fontsize=10)
    plt.gcf().autofmt_xdate()
    ax.set_xticks(ax.get_xticks()[::2])
    plt.title("USA COVID-19 Testing Response", fontname="Arial Rounded MT Bold")
    plt.savefig("COVIDFigure.png", dpi=400)

def stateCOVIDTestingStats(x_axis='date',y_scale='linear',y_axis='total',y1_axis='positive', state='NY'):
    response = requests.get("https://covidtracking.com/api/states/daily?state=" + state)
    text = json.loads(response.text)
    df = pd.DataFrame.from_records(text)
    df = df.sort_values('date')
    df['date'] = date2num(pd.to_datetime(df['date'], format='%Y%m%d').tolist())
    print df

    x = df[x_axis]
    y = df[y_axis]
    y1 = df[y1_axis]

    fig, ax = plt.subplots()
    plt.rcParams["font.family"] = "Arial"
    plt.xlabel("Date", fontname="Arial Rounded MT Bold")
    plt.ylabel("People (" + y_scale + ")" , fontname="Arial Rounded MT Bold")
    plt.grid(color='grey', linestyle='-', linewidth=0.5, alpha=0.5)
    plt.xticks(fontsize=8, fontname="Arial")
    plt.yticks(fontsize=8, fontname="Arial")
    ax.set_yscale(y_scale)

    plt.gca().xaxis.set_major_locator(DayLocator())
    plt.gca().xaxis.set_major_formatter(DateFormatter('%m/%d'))

    line1, = plt.plot(x, y, label="Number of tests", marker='o', color='blue', mfc='white', mec="black", alpha=0.8, ms=3)
    line2, = plt.plot(x, y1, label = "Positive cases", marker='o', color='orange', mfc='white', mec="black", alpha=0.8, ms=3)
    plt.legend(handles=[line1, line2], fontsize=10)
    plt.gcf().autofmt_xdate()
    ax.set_xticks(ax.get_xticks()[::2])
    plt.title(state + " COVID-19 Testing Response", fontname="Arial Rounded MT Bold")
    plt.savefig(state+".png", dpi=400)
