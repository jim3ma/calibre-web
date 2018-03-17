#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:  # py3
    from shlex import quote
except ImportError:  # py2
    from pipes import quote

import os
import subprocess
import epub


def get_meta_info(tmp_file_path, original_file_name, original_file_extension):
    ext = original_file_extension.lower()
    os.rename(tmp_file_path, tmp_file_path + ext)

    output = tmp_file_path + ".epub"
    cmd = "ebook-convert %s %s --output-profile tablet" % (quote(tmp_file_path + ext), quote(output))
    print cmd
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    com = p.communicate()
    out = com[0].strip()
    err = com[1].strip()
    status = p.returncode
    print status, out, err

    os.rename(tmp_file_path + ext, tmp_file_path)
    meta = epub.get_epub_info(output, original_file_name, ".epub")
    return meta
