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
mv app/build/outputs/apk/debug/app-debug.apk app/FunesDroid-master/InputAPKs/app-debug.apk
cd app/FunesDroid-master/
python launchexp.py