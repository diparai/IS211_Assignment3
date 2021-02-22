import argparse
import urllib
import urllib.request
import logging
import datetime
import csv
import re

def downloadWeb(url):
    request = urllib.request(url)
    response = urllib.urlopen(url)
    return response.read().decode('utf-8')


def processImage(file):

    reader = file.reader(file)
    row_count = 0
    image_count = 0
    jpg_count = 0
    gif_count = 0
    png_count = 0
    REI = re.IGNORECASE

    for row in reader:
        row_count = row_count + 1
        filename = row[0]
        if re.search(r'(.JPG$|.PNG$|.GIF$|.)', filename, REI):
            image_count += 1
        elif re.search(r'.JPG$', filename, REI):
            jpg_count += 1
        elif re.search(r'.PNG$', filename, REI):
            png_count += 1
        else:
            gif_count += 1

    image_percent = round(float(image_count) / float(row_count) * 100)
    jpg_percent = round(float(jpg_count) / float(row_count) * 100)
    png_percent = round(float(png_count) / float(row_count) * 100)
    print("Total number of hits: {}.format(rowcount")
    print("Total number of image hits: {}.format(image_count")
    print("Total number of hits: {}.format(rowcount")
    print("Image request account for {}% of all requests. JPEG has {}%, PNG has {}% & GIF has {}% hits.'.format(image_percent,jpg_percent,png_percent)")

def processBrowser(file):
    reader = csv.reader((file))
    safaricount = 0
    chromecount = 0
    firefoxcount = 0
    iecount = 0
    linecount = 0
    REI = re.IGNORECASE

    for brow in reader:
        linecount += 1
        browser = brow[2]
        if re.search(r'Chrome+/\d{1,3}.\d{0,3}.\d{0,5}.\d\sSafari/537.36$', browser, REI):
            chromecount += 1
        elif re.search(r'Firefox/\d{0,2}.\d{0,2}$', browser, REI):
            firefoxcount += 1
        elif re.search(r'MSIE\s\d{0,2}.\d{0,2}', browser, REI):
            iecount += 1
        elif re.search(r'Safari/\d{0,4}.\d{0,4}$', browser, REI) != 'Safari/537.36':
            safaricount += 1
    safariper = round(float(safaricount) / float(linecount) * 100, 2)
    ieper = round(float(iecount) / float(linecount) * 100, 2)
    chromeper = round(float(chromecount) / float(linecount) * 100, 2)
    firefoxper = round(float(firefoxcount) / float(linecount) * 100, 2)

    print('\n')
    print('Total # of Chrome browser Used : {} that is {}% of total usage.'.format(chromecount, chromeper))
    print('Total # of Firefox browser Used : {} that is {}% of total usage.'.format(firefoxcount, firefoxper))
    print('Total # of Microsoft Internet Explorer browser Used : {} that is {}% of total usage.'.format(iecount, ieper))
    print('Total # of Safari browser Used : {} that is {}% of total usage.'.format(safaricount, safariper))


def hoursInfo(file):
    reader = csv.reader(file)
    hour_one = 0
    hour_two = 0
    hour_three = 0
    hour_four = 0
    hour_five = 0
    hour_six = 0
    totalCount = 0
    REI = re.IGNORECASE
    for hits in reader:
        totalCount += 1
        hour_hit = hits[1]
        if re.search(r'0:\d{0,2}$', hour_hit, REI):
            hour_one += 1
        elif re.search(r'1:\d{0,2}$', hour_hit, REI):
            hour_two += 1
        elif re.search(r' 2:\d{0,2}$', hour_hit, REI):
            hour_three += 1
        elif re.search(r' 3:\d{0,2}$', hour_hit, REI):
            hour_four += 1
        elif re.search(r' 4:\d{0,2}$', hour_hit, REI):
            hour_five += 1
        else:
            hour_six += 1
        total_hit = int(hour_one) + int(hour_two) + int(hour_three) + int(hour_four) + int(hour_five) + int(hour_six)
        print("Hour 12 has {} hits'.format(hour_one")
        print("Hour 1 has {} hits'.format(hour_one")
        print("Hour 2 has {} hits'.format(hour_one")
        print("Hour 3 has {} hits'.format(hour_one")
        print("Hour 4 has {} hits'.format(hour_one")
        print("Hour 5 has {} hits'.format(hour_one")
        print(" Total number of hits is: " + str(total_hit))


def main(url):
    print(f"Running main with URL = {url}...")
    if args.url:
        try:
            urlparse = downloadWeb(args.url)
            processBrowser(urlparse)
            hoursInfo(urlparse)
        except Exception as e:
            print("Check the log file")
    else:
        print("Please try again!")


if __name__ == "__main__":
    """Main entry point"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL to the datafile", type=str, required=False)
    args = parser.parse_args()
    logger = logging.getLogger("Assignment3 ")
    logging.basicConfig(filename='errors.log', level=logging.ERROR)
    main(args.url)
