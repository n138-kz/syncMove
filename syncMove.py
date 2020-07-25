#!/usr/bin/python3
import os
import sys
import argparse
import pathlib
import shutil

for c in range((shutil.get_terminal_size().columns-1)):
    print('-', end='')
print('')

parser = argparse.ArgumentParser(
                                 prog=os.path.basename(__file__),
                                 description=''
                                )

parser.add_argument('--debug',
                    help='Turn on of the debug mode.',
                    action='store_true',
                   )

parser.add_argument('dirSrc',
                    nargs=1,
                    default=None,
                    metavar='SOURCE',
                    help='',
                   )

parser.add_argument('dirDst',
                    nargs=1,
                    default=None,
                    metavar='DEST',
                    help='',
                   )

args = parser.parse_args()

# Is Exist
dirSrc = str(args.dirSrc[0])
if not pathlib.Path(str(dirSrc)).exists():
    print('[ERROR]>> No such a directory.')
    print('          ' + str(dirSrc))
    parser.print_usage()
    sys.exit(1)

# Is Dir
if not pathlib.Path(str(dirSrc)).is_dir():
    print('[ERROR]>> Is a not directory.')
    print('          ' + str(dirSrc))
    parser.print_usage()
    sys.exit(1)

dirDst = str(args.dirDst[0])
# Is Exist
if not pathlib.Path(str(dirDst)).exists():
    print('[ERROR]>> No such a directory.')
    print('          ' + str(dirDst))
    parser.print_usage()
    sys.exit(1)

# Is Dir
if not pathlib.Path(str(dirDst)).is_dir():
    print('[ERROR]>> Is a not directory.')
    print('          ' + str(dirDst))
    parser.print_usage()
    sys.exit(1)

print('Src: ' + str(pathlib.Path(str(dirSrc)).resolve()))
print('Dst: ' + str(pathlib.Path(str(dirDst)).resolve()))

run3 = str(input('Is this OK [y/N]: '))
run3 = run3.lower().strip()
if run3 != 'y' and run3 != 'yes' :
    sys.exit(1)

for srcDirs in (pathlib.Path(str(dirSrc)).iterdir()):
    #print(str(srcDirs) + ': ', end='')
    findDir = False

    if not srcDirs.is_dir():
        continue

    findDir = pathlib.Path(str(dirDst) + '/' + str(srcDirs.relative_to(dirSrc))).exists()

    if findDir != True:
        print('Transferring... \'' + str(srcDirs.relative_to(dirSrc)) + '\'')
        shutil.move(str(srcDirs), str(dirDst))
