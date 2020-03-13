#!/bin/bash
# Copyright (c) Facebook, Inc. and its affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
#
# Extracted from https://github.com/facebook/react-native/blob/master/scripts/android-setup.sh

echo "Eseguo script funesDroid..."
mkdir -p FunesDroid-master/InputAPKs
mkdir -p FunesDroid-master/Results
mv app/build/outputs/apk/debug/app-debug.apk FunesDroid-master/InputAPKs
cd FunesDroid-master/
#python launchexp.py -les [doc|bf|stai] -nevent [n] -wtime [w] -api [a]
python launchexp.py -les 'doc' --nevent 1 --wtime 1 --apiversion 29
