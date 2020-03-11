echo "Start wait device"
while ! (adb shell getprop sys.boot_completed)
do
  echo "Non si è avviato..."
  sleep 3
done
echo "Disabling animations."
adb shell settings put global window_animation_scale 0.0
adb shell settings put global transition_animation_scale 0.0
adb shell settings put global animator_duration_scale 0.0