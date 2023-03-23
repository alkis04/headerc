# check if python3 is installed
if [ -x "$(command -v python3)" ]; then
    echo "Python3 is installed [OK]"
else
    echo "Python3 is not installed :("
    echo "Please install python3 and try again"
    exit 1
fi


sudo cp headerc.py /usr/local/bin/headerc

if [ $? -eq 0 ]; then
    echo "Copying files [OK]"

else
    echo "There was an error in copying the file to /usr/local/bin :("
fi
sudo chmod +x /usr/local/bin/headerc


if [ $? -eq 0 ]; then
    echo "Installation was successful!"
else
    echo "There was an error in changing the permission of the file :("
fi