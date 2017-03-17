for file in *.mp3; do
  echo "Transfering = ${file}"
  adb push "${file}" /sdcard/Music
done
