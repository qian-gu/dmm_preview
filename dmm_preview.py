#!/usr/bin/env python
import sys

def parse(sn):
    prefix, number = sn.lower().split('-')
    if prefix in ['gvh', 'bbtu']:
        pad_len = 0
    else:
        pad_len = 5 - len(number)
    pad = pad_len * '0'
    return prefix, pad, number

def get_preview_url(sn):
    base_url = 'https://cc3001.dmm.co.jp/litevideo/freepv/'
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
