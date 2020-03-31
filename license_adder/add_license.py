#! /usr/bin/env python

import sys


shebang = '#!'


def get_lic(lic_filename = 'lic.txt'):
    with open(lic_filename) as f:
        lic = f.read()
    return lic


def prefix_lines(lic, line_prefix):
    return line_prefix + lic.replace('\n', '\n' + line_prefix)


def get_file_ext(filename):
    ext = filename.split('.')[-1]
    return ext


def get_comment_params(code_file_ext):
    ext = code_file_ext.lower()

    if ext in ('py', 'r', 'sh', 'yml'):
        comment_start=''
        comment_end=''
        line_prefix='# '
    elif ext in ('scala', 'sbt', 'java', 'sql'):
        comment_start='/*\n'
        comment_end=' */\n'
        line_prefix=' * '
    elif ext in ('xml'):
        comment_start='<!--\n'
        comment_end='-->\n'
        line_prefix=''
    else:
        comment_start = ''
        comment_end = ''
        line_prefix = ''

    return (comment_start, comment_end, line_prefix)


def get_lic_comment(code_file_ext):
    (comment_start, comment_end, comment_prefix) = get_comment_params(code_file_ext)
    lic = get_lic()
    lic_comment = (comment_start + prefix_lines(lic, comment_prefix) + '\n' +
            comment_end)
    return lic_comment


def add_lic(code_filename):
    # TODO: Skip unsupported file_ext (large files)

    with open(code_filename) as f:
        first_line = f.readline()
        remaining_lines = list(f.readlines())

    with open(code_filename, 'w') as f:
        lic_comment = get_lic_comment(get_file_ext(code_filename))
        if first_line.startswith(shebang):
            prefix = first_line + '\n' + lic_comment
        else:
            t = lic_comment + '\n' if lic_comment else lic_comment
            prefix = t + first_line
        f.write(prefix)
        f.writelines(remaining_lines)


if __name__ == '__main__':
    add_lic(sys.argv[1])

