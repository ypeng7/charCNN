# -*- coding: utf-8 -*-
"""

@file: data_preprocessing.py
@guid: ba002ed7475c4c87a85e73026f8fd81f

@author: Yue Peng
@email: yuepaang@gmail.com
@date: 2019-03-12 21:12:22
@modified:

@brief: combine all the txt file
"""
__author__ = "Yue Peng"
import os
import codecs

import pandas as pd

CURRENT_PATH = "/".join(os.path.abspath(__file__).split("/")[:-1])


def processing_dir(dn):
    sentences = []
    for fn in os.listdir(dn):
        if fn.endswith("txt"):
            with codecs.open(dn+"/"+fn, "r", encoding="utf-8") as f:
                for line in f.readlines():
                    if len(line.strip()) != 0:
                        sentences.append(line.strip())
    return sentences


def main():
    pos_path = os.path.abspath(os.path.join(
        CURRENT_PATH, "../data/hotel_rate/positive"))
    neg_path = os.path.join(CURRENT_PATH, "../data/hotel_rate/negative")
    pos_sentences = processing_dir(pos_path)
    neg_sentences = processing_dir(neg_path)
    df_pos = pd.DataFrame(
        {"query": pos_sentences, "label": [1] * len(pos_sentences)})
    df_neg = pd.DataFrame(
        {"query": neg_sentences, "label": [0] * len(neg_sentences)})
    df = pd.concat([df_pos, df_neg], axis=0)
    df = df.sample(frac=1.).reset_index(drop=True)

    save_path = os.path.join(CURRENT_PATH, "../data/hotel_rate")
    df.to_csv(save_path+"/data.tsv", sep="\t", index=None)


if __name__ == "__main__":
    main()
