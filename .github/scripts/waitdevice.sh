while ! (adb shell getprop sys.boot_completed)
do
  echo "Non si è avviato..."
done