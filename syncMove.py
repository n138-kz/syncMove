#!/usr/bin/python3
import os
import sys
import argparse
import pathlib
import shutil
import time
import datetime
import threading

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

if args.debug == True:
    print(' !!>> ---------------------- <<!! ' + '')
    print(' !!>>  Debug mode is Active  <<!! ' + '')
    print(' !!>> ---------------------- <<!! ' + '\n\n')

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





def tran(srcDirs, dirDst):
    shutil.move(str(srcDirs), str(dirDst))

def elapsed_timer():
    pass



try:
    run3 = str(input('Is this OK [y/N]: '))
    run3 = run3.lower().strip()
    if run3 != 'y' and run3 != 'yes' :
        sys.exit(1)

    for srcDirs in (pathlib.Path(str(dirSrc)).iterdir()):
        #print(str(srcDirs) + ': ', end='')
        findDir = False
        findChildrenDir = False
        procTimer = datetime.datetime.now()
        transfer = ''

        if not srcDirs.is_dir():
            continue

        findDir = pathlib.Path(str(dirDst) + '/' + str(srcDirs.relative_to(dirSrc))).exists()

        if findDir != True:
            os.makedirs(str(dirDst) + '/' + str(srcDirs.relative_to(dirSrc)))

        if False:
            # cb94eaa2c2b7a439fcb0bb4f66a4204c704ba282
            if args.debug == True:
                logg_time=datetime.datetime.now()
                print(str(logg_time.hour).zfill(2) + ':' + str(logg_time.minute).zfill(2) + ':' + str(logg_time.second).zfill(2) + '.' + '{:0<3}'.format(int(logg_time.microsecond/1000)) + ' ', end='')
            print('Transferring... \'' + str(srcDirs.relative_to(dirSrc)) + '\'')

            if args.debug == True:
                print('   ' + 'From    ' + ': ' + str(srcDirs) )
                print('   ' + 'To      ' + ': ' + str(dirDst) )

            if __name__ == '__main__':
                thread1 = threading.Thread(target=tran, kwargs={'srcDirs': str(srcDirs), 'dirDst': str(dirDst)})
                thread1.start()
                thread1.join()

            if args.debug == True:
                print('   ' + 'Elapsed ' + ': ' + str((datetime.datetime.now() - procTimer).seconds) + 's' )

            continue
        else:
            for srcChildrenDirs in (pathlib.Path(str(srcDirs)).iterdir()):
                procTimer = datetime.datetime.now()

                if not srcChildrenDirs.is_dir():
                    continue

                findChildrenDir = pathlib.Path(str(dirDst) + '/' + str(srcDirs.relative_to(dirSrc)) + '/' + str(srcChildrenDirs.relative_to(dirSrc + '/' + str(srcDirs.relative_to(dirSrc)) ))).exists()

                if findChildrenDir != True:
                    if args.debug == True:
                        logg_time=datetime.datetime.now()
                        print(str(logg_time.hour).zfill(2) + ':' + str(logg_time.minute).zfill(2) + ':' + str(logg_time.second).zfill(2) + '.' + '{:0<3}'.format(int(logg_time.microsecond/1000)) + ' ', end='')
                    print('Transferring... \'' + str(srcChildrenDirs.relative_to(dirSrc)) + '\'')

                    if args.debug == True:
                        print('   ' + 'From    ' + ': ' + str(srcChildrenDirs) )
                        print('   ' + 'To      ' + ': ' + str(pathlib.Path(str(dirDst) + '/' + str(srcDirs.relative_to(dirSrc)) + '/' + str(srcChildrenDirs.relative_to(dirSrc + '/' + str(srcDirs.relative_to(dirSrc)) )))) )

                    if __name__ == '__main__':
                        thread1 = threading.Thread(target=tran, kwargs={'srcDirs': str(srcChildrenDirs), 'dirDst': str(pathlib.Path(str(dirDst) + '/' + str(srcDirs.relative_to(dirSrc)) + '/' + str(srcChildrenDirs.relative_to(dirSrc + '/' + str(srcDirs.relative_to(dirSrc)) ))))})
                        thread1.start()
                        thread1.join()

                    if args.debug == True:
                        print('   ' + 'Elapsed ' + ': ' + str((datetime.datetime.now() - procTimer).seconds) + 's' )

                else:
                    if args.debug == True:
                        logg_time=datetime.datetime.now()
                        print(str(logg_time.hour).zfill(2) + ':' + str(logg_time.minute).zfill(2) + ':' + str(logg_time.second).zfill(2) + '.' + '{:0<3}'.format(int(logg_time.microsecond/1000)) + ' ', end='')

                    print('Skipping....... \'' + str(srcChildrenDirs.relative_to(dirSrc)) + '\'')
                    if args.debug == True:

                        print('            ' + 'File count check: ',end='')
                        tmp_internal_filesCount=[0, 0];
                        for tmp_dirpath in [
                            [
                                'Src',
                                str(srcChildrenDirs),
                                0,
                            ],
                            [
                                'Dst',
                                str(pathlib.Path(str(dirDst) + '/' + str(srcDirs.relative_to(dirSrc)) + '/' + str(srcChildrenDirs.relative_to(dirSrc + '/' + str(srcDirs.relative_to(dirSrc)) )))),
                                0,
                            ],
                        ] :
                            tmp_dirpath[2]=sum(os.path.isfile(os.path.join(str(tmp_dirpath[1]), name)) for name in os.listdir(str(tmp_dirpath[1])))
                            if tmp_dirpath[0]=='Src':
                                tmp_internal_filesCount=[tmp_dirpath[2], 0]
                            else:
                                if tmp_dirpath[0]=='Dst':
                                    tmp_internal_filesCount[1]=tmp_dirpath[2]

                        if tmp_internal_filesCount[0]==tmp_internal_filesCount[1]:
                            print('The same as destination.')
                        else:
                            print('There isn\'t same as destination. ')
                            print('            ' + 'Src: '+str(tmp_internal_filesCount[0]))
                            print('            ' + 'Dst: '+str(tmp_internal_filesCount[1]))


            try:
                os.rmdir(str(srcDirs))
            except OSError as e:
                pass

        if args.debug == True:
            logg_time=datetime.datetime.now()
            print(str(logg_time.hour).zfill(2) + ':' + str(logg_time.minute).zfill(2) + ':' + str(logg_time.second).zfill(2) + '.' + '{:0<3}'.format(int(logg_time.microsecond/1000)) + ' ', end='')

except KeyboardInterrupt:
    print('^C')
    sys.exit(1)
