#!/usr/bin/env python
import sys

base_url = 'https://cc3001.dmm.co.jp/litevideo/freepv/'

# serial number dictionary
sn_dicts = {
        'avsa' : 2,
        'bbtu' : 0,
        'blk'  : 2,
        'fcdc' : 2,
        'genu' : 0,
        'gvh'  : 0,
        'jufe' : 2,
        'juq'  : 2,
        'meyd' : 2,
        'miaa' : 5,
        'roe'  : 2,
        'waaa' : 2,
        'vec'  : 0,
        }

def parse(sn):
    prefix, number = sn.lower().split('-')
    if prefix in sn_dicts:
        pad_len = sn_dicts[prefix]
    else:
        pad_len = 2
        print("WARNING: no records for prefix", prefix, ", using default pad length, to be validated!")
    pad = pad_len * '0'
    return prefix, pad, number

def get_preview_url(sn):
    # Parse to get elements to assemble the URL.
    prefix, pad, number = parse(sn)
    full_sn = prefix + pad + number
    suffix = prefix[0] + '/' + prefix[0:3] + '/' + full_sn + '/' + full_sn + '_mhb_w.mp4'
    print(base_url + suffix)


def main(argv):
    # check arguments before work
    if len(argv) == 1:
        print("Please add serial number(s)!")
        print("Example usage: ./dmm_preview.py JUFE-440")
    else:
        for sn in argv[1::]:
            get_preview_url(sn)

if __name__ == '__main__':
    main(sys.argv)
