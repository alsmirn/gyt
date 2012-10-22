#!/usr/bin/env python

import cmd
from subprocess import call, check_output


def get_git_commands():
    """Get git commands from 'git help' output."""

    names = []
    output = check_output(["git", "help", "-a"])

    for s in output.split('\n')[8:-2]:
        names.extend(cmd.strip() for cmd in s.split())

    return sorted(names)


class Gyt(cmd.Cmd):
    """Simple overdrive ;)"""

    prompt = "git "

    def do_git(self, cmd):
        cmd = ['git', ] + cmd.split()
        call(cmd, stdout=True)

    def get_names(self):
        return get_git_commands()

    def precmd(self, line):
        return "git %s" % line

    def completenames(self, text, *ignored):
        return [a for a in self.get_names() if a.startswith(text)]

    def do_EOF(self, line):
        return True


def main():

    try:
        Gyt().cmdloop()
    except KeyboardInterrupt:
        print('^C')
        exit(0)


if __name__ == '__main__':
    main()
