from math import isnan as isNaN, floor, ceil
import json
import re


# /**
#  * Parse or format the given `val`.
#  *
#  * Options:
#  *
#  *  - `long` verbose formatting [false]
#  *
#  * @param {String|Number} val
#  * @param {Object} [options]
#  * @throws {Error} throw an error if val is not a non-empty string or a number
#  * @return {String|Number}
#  * @api public
#  */

def ms(val, options={'long': False}):
    # /**
    #  * Helpers.
    #  */

    s = 1000
    m = s * 60
    h = m * 60
    d = h * 24
    y = d * 365.25

    # /**
    #  * Parse the given `str` and return milliseconds.
    #  *
    #  * @param {String} str
    #  * @return {Number}
    #  * @api private
    #  */

    def parse(string):
        string = str(string)
        if (len(string) > 100):
            return

        match = re.match(
            r'^((?:\d+)?\.?\d+) *(milliseconds?|msecs?|ms|seconds?|secs?|s|minutes?|mins?|m|hours?|hrs?|h|days?|d|years?|yrs?|y)?$', string)
        if (not match):
            return 'undefined'
        n = float(match[1])
        t = (match[2] or 'ms').lower()
        if (t == 'years' or t == 'year' or t == 'yrs' or t == 'yr' or t == 'y'):
            return n * y
        if (t == 'days' or t == 'day' or t == 'd'):
            return n * d
        if (t == 'hours' or t == 'hour' or t == 'hrs' or t == 'hr' or t == 'h'):
            return n * h
        if (t == 'minutes' or t == 'minute' or t == 'mins' or t == 'min' or t == 'm'):
            return n * m
        if (t == 'seconds' or t == 'second' or t == 'secs' or t == 'sec' or t == 's'):
            return n * s
        if (t == 'milliseconds' or t == 'millisecond' or t == 'msecs' or t == 'msec' or t == 'ms'):
            return n
        return 'undefined'

    # /**
    #  * Short format for `ms`.
    #  *
    #  * @param {Number} ms
    #  * @return {String}
    #  * @api private
    #  */

    def fmtShort(ms):
        if (ms >= d):
            return str(int(round(ms / d))) + 'd'
        if (ms >= h):
            return str(int(round(ms / h))) + 'h'
        if (ms >= m):
            return str(int(round(ms / m))) + 'm'
        if (ms >= s):
            return str(int(round(ms / s))) + 's'
        return str(ms) + 'ms'

    # /**
    #  * Long format for `ms`.
    #  *
    #  * @param {Number} ms
    #  * @return {String}
    #  * @api private
    #  */

    def fmtLong(ms):
        return plural(ms, d, 'day') or \
            plural(ms, h, 'hour') or \
            plural(ms, m, 'minute') or \
            plural(ms, s, 'second') or \
            str(ms) + ' ms'

    # /**
    #  * Pluralization helper.
    #  */

    def plural(ms, n, name):
        if (ms < n):
            return
        if (ms < n * 1.5):
            return str(int(floor(ms / n))) + ' ' + str(name)
        return str(int(ceil(ms / n))) + ' ' + str(name) + 's'

    def main(val, options):
        valType = type(val)
        if (valType == str and len(val) > 0):
            return parse(val)
        elif (valType == int and not isNaN(val)):
            if (options['long']):
                return fmtLong(val)
            else:
                return fmtShort(val)

        raise Exception(
            'val is not a non-empty string or a valid number. val=' + json.dumps(val))

    return main(val, options)
