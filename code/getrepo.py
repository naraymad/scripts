import argparse
import os
import tempfile

try:
    from git import Repo
except:
    from pip._internal import main
    main(['install', 'GitPython'])
    from git import Repo


def parse_args():
    parser = argparse.ArgumentParser(description='LightGBM example')
    parser.add_argument(
        '--repo',
        default="https://github.com/mrudulan/DevPlatv2Template",
        help='Git repo to clone',
    )
    parser.add_argument(
        '--storage',
        help='AzureStorageAccount',
    )
    parser.add_argument(
        '--share',
        help='azure share',
    )
    return parser.parse_args()


def main():
    # parse command-line arguments
    args = parse_args()
    dir = tempfile.gettempdir()
    gtdir = dir +"/" + "code"
    Repo.clone_from(args.repo, gtdir)
    command = "az storage copy -s "+ gtdir +" --destination-account-name "+ args.storage +" --destination-share " + args.share +" --recursive "
    os.system(command)

if __name__ == '__main__':
    main()
