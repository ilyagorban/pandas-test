#!/usr/bin/env python
import os

import yaml
import argparse
import vagrant


def read_yaml(name):
    with open('{}.yml'.format(name)) as f:
        content = yaml.load(f.read())
    return content


def save_yaml(name, addition):
    content = read_yaml('automatic_deploy_{}'.format(name))
    content.extend(addition)
    with open('{}.yml'.format(name), 'w') as f:
        yaml.dump(content, f)


def launch_redeploy():
    v = vagrant.Vagrant()
    v.halt('base') # of course here can be a more advanced logic to reduce vagrant machine downtime
    v.up(vm_name='base', provision=True)


def sync_git():
    print("Git fetching")
    os.system('git fetch')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Automated deploy')
    parser.add_argument('-b', '--add-bamboo', help='Enable bamboo service', action='store_true')
    parser.add_argument('-c', '--add-counter-panda', help='Enable counter-panda service', action='store_true')
    parser.add_argument('-g', '--add-gify-panda', help='Enable gify-panda service', action='store_true')
    args = parser.parse_args()
    sync_git()
    tasks_to_add = []
    tasks = read_yaml('automatic_deploy_tasks')
    if args.add_bamboo:
        tasks_to_add.append(tasks[0])
    if args.add_counter_panda:
        tasks_to_add.append(tasks[1])
    if args.add_gify_panda:
        tasks_to_add.append(tasks[2])
    if not tasks_to_add:
        raise ValueError('None of service had been choosen')
    save_yaml('base', tasks_to_add)
    launch_redeploy()
