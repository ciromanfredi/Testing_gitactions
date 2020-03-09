#!/bin/bash
# Copyright (c) Facebook, Inc. and its affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
#
# Extracted from https://github.com/facebook/react-native/blob/master/scripts/android-setup.sh

echo "Eseguo script funesDroid..."
chmod u+x ./gradlew
./gradlew assembleDebug
pwd
ls
cd app
echo "mi sposto in" + pwd
ls
cd build
echo "mi sposto in" + pwd
ls
cd outputs
echo "mi sposto in" + pwd
ls
cd apk
echo "mi sposto in" + pwd
ls
cd debug
echo "mi sposto in" + pwd
ls
cd ../../../../
echo "mi sposto in" + pwd
ls
cd FunesDroid-master
echo "mi sposto in" + pwd
ls
cd InputAPKs
echo "mi sposto in" + pwd
ls
mv app/build/outputs/apk/debug/app-debug.apk app/FunesDroid-master/InputAPKs/
cd app/FunesDroid-master/
python launchexp.py