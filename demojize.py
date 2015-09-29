# coding: utf-8

import sys
import os
import codecs
import emoji


def is_exist(fpath):
    if os.path.isfile(fpath):
        return True
    print "Error: File {} does not exist. Skipped.".format(fpath)
    return False


def run(infpath, outfpath):
    print "demojizing... {}".format(infpath)
    # read
    data = []
    with codecs.open(infpath, "r", "utf-8") as fp:
        for line in fp:
            line = emoji.demojize(line)
            data.append(line)
    # save
    with codecs.open(outfpath, "w", "utf-8") as fp:
        for line in data:
            fp.write(line)


if __name__ == "__main__":
    args = sys.argv
    if len(args) < 2:
        print "Usage: python demojize.py <path_to_file>"
        print "Usage: python demojize.py <path_to_dir> <file_name>..."
        sys.exit()

    if len(args) == 2:
        infpath = args[1]
        if is_exist(infpath):
            indir, fname = os.path.split(infpath)
            outfpath = os.path.join(indir, "demojized_{}".format(fname))
            run(infpath, outfpath)
    else:
        indir = args[1]
        for fname in args[2:]:
            fname = os.path.split(fname)[1]
            if "demojized_" in fname:
                continue
            infpath = os.path.join(indir, fname)
            if not is_exist(infpath):
                continue
            outfpath = os.path.join(indir, "demojized_{}".format(fname))
            run(infpath, outfpath)
