if [ -x "$(command -v python3)" ]; then
    echo -e "Python3 is installed \e[1;32mOK\e[0m"
else
    echo "Python3 is not installed :("
    echo "Please install python3 and try again"
    exit 1
fi

echo "Installing headerc..."
echo "You may be prompted for your password"
echo ""

sudo cp headerc.py /usr/local/bin/headerc

if [ $? -eq 0 ]; then
    echo -e "Copying files \e[1;32mOK\e[0m"

else
    echo "There was an error in copying the file to /usr/local/bin :("
fi
sudo chmod +x /usr/local/bin/headerc


if [ $? -eq 0 ]; then
    echo "Installation was successful!"
else
    echo "There was an error in changing the permission of the file :("
fi