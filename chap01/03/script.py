#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def main():
    sentence = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
    splitted = sentence.split()
    stripped = [word.strip(',').strip('.') for word in splitted]
    print([len(word) for word in stripped])


if __name__ == '__main__':
    main()
