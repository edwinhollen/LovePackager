import argparse
import json
from distutils import dir_util
import shutil
import os
import tempfile
import glob
import subprocess


def build(config):
    print("building...")
    # make output dir
    output_dir = config["output"] or "build/"
    print("preparing output directory...")
    os.makedirs(output_dir, exist_ok=True)
    # make temp dir
    with tempfile.TemporaryDirectory() as temp_dir:
        # copy files from source paths
        print("copying source files...")
        for source_path_str in config["sources"]:
            for source_glob in glob.glob(source_path_str):
                if os.path.isdir(source_glob):
                    dir_util.copy_tree(os.path.realpath(source_glob), os.path.join(temp_dir, os.path.dirname(source_glob)))
                else:
                    shutil.copy(source_glob, temp_dir)
        # zip up temp dir
        print("zipping everything up...")
        zip = shutil.make_archive(os.path.join(output_dir, config["name"]), "zip", temp_dir)
        # move to love
        print("making .love...")
        return shutil.move(zip, os.path.splitext(zip)[0]+".love")

    pass


def run(config, love_file):
    print("running...")
    love = config["love"] if ("love" in config) else shutil.which("love")
    process = subprocess.Popen([love, love_file])
    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True, help="Path to config file (json)")
    parser.add_argument("--run", action="store_true", default=False, help="Run after build")
    args = parser.parse_args()

    # check for config
    if not os.path.isfile(args.config):
        print("Couldn't find specified config file", args.config)
        exit(1)

    # load config
    config = None
    with open(args.config) as json_data:
        config = json.load(json_data)
        # set working dir
        os.chdir(os.path.dirname(os.path.realpath(json_data.name)))

    # build
    love_file = build(config)

    if args.run:
        run(config, love_file)