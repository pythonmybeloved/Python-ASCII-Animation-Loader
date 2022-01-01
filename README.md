Python-ASCII-Animation-Loader
Very bare-bones and simple ASCII animation loader used in the windows/mac/linux terminal that was made in python.

(CREATING ANIMATION):
To make the animation, create a .txt file. Create the frames like in the 3 included examples, with "/na/" in between them and "eoa" after the last frame. Place the .txt file in the same location as the animation loader.

(USING PROGRAM):
Open the terminal of your operating system (it will crash if you open it in python) and type the following:

cd path/to/your/file
python ascii.py

Replace "path/to/your/file" with the file location in which you placed the animation loader. After this, the program will prompt you to enter the file name. Enter the file name of the text file of your choosing, file extension (.txt) included. After this, just sit back and watch the program play your animation.

(EDITING THE ANIMATION LOADER):
To change the speed that it loads the ASCII animations at, open the file location where it is. Afterwards, right click and click "Rename". Replace ".py" with ".txt". Open the file with your text editor. Select every "time.sleep(0.5)" in between "if '/na/' in l" and "print(l)" and replace the "0.5" in the parentheses with however long you would like the time in between frames to be (Ex: 1 would be 1 second, 0.2 would be 1/5 of a second). Save the file after that, rename the file again to replace ".txt" with ".py".

And that's about it. I will make major updates to this as I learn python more and more.
