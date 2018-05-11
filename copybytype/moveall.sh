mkdir bin

echo "Generating filetype list... Please wait"
for EXTENSION in $(find . -type f | sed -n 's/..*\.//p' | sort | uniq)
do
  mkdir ./bin/$EXTENSION
  echo "copying $EXTENSION files... please wait"
  find . -name "*.$EXTENSION" -type f -exec cp {} ./bin/$EXTENSION/ \;
done
