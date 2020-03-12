#!/bin/bash
# Copyright (c) Facebook, Inc. and its affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
#
# Extracted from https://github.com/facebook/react-native/blob/master/scripts/android-setup.sh

echo "Eseguo script funesDroid..."
mkdir -p FunesDroid-master/InputAPKs
mv app/build/outputs/apk/debug/app-debug.apk FunesDroid-master/InputAPKs
cd FunesDroid-master/
python launchexp.py
