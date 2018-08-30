#!/usr/bin/env python3

# 2018 Luther Thompson
# This program is public domain. See COPYING for details.

import datetime
import os
import sys

dayDelta = datetime.timedelta(1)


def minDate(data):
  """Find the minimum date represented in the data dict."""
  minYear = min(data.keys())
  yearData = data[minYear]
  minMonth = min(yearData.keys())
  monthData = yearData[minMonth]
  minDay = min(monthData.keys())
  return datetime.date(minYear, minMonth, minDay)


def thenUntilToday(date):
  """Yield every date from the argument up to and including today."""
  today = datetime.date.today()
  while date <= today:
    yield date
    date = date + dayDelta


def estimateLevels(retention, data):
  """Iterate through days, showing the expected drug levels.

  Yield a tuple containing the date, that day's dose, and the expected drug
  level for that day. retention is the percentage of the drug that the body
  retains each day. data is a nested dict with keys representing years -> months
  -> days. The innermost values are the dose for the day.
  """
  level = 0
  for date in thenUntilToday(minDate(data)):
    dose = data.get(date.year, {}).get(date.month, {}).get(date.day, 0)
    level = level * retention + dose
    yield date, dose, level


def main(argv, environ):
  sys.path.append(environ.get('HOME', ''))
  try:
    import mydoses
  except ModuleNotFoundError:
    return "Can't find mydoses.py in home directory."
  try:
    retention = float(argv[1])
  except (IndexError, ValueError):
    print('doses takes one numerical argument', file=stderr)
    return 2
  for day in estimateLevels(retention, mydoses.doses):
    print(f'{day[0]} {day[1]:<4} {day[2]:.3}')


if __name__ == '__main__':
  exit(main(sys.argv, os.environ))
