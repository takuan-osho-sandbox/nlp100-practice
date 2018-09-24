#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def main():
    s1 = "パトカー"
    s2 = "タクシー"
    chunked_str_iter = (zipped_s[0] + zipped_s[1] for zipped_s in zip(s1, s2))
    print(''.join(chunked_str_iter))


if __name__ == '__main__':
    main()
