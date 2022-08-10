# TEXT <-> IMAGE CONVERSION
## This utility allows you to convert a text into an image and vice-versa

### How the conversion is done
Every text character corresponds to a specific unicode value.
**Eg:**
- A -> 65
- B -> 66
- ...
- Z -> 90

Every image is composed by pixels and each pixel has a specific color express by RGB values.
RGB stands for Red, Green, Blue and indicates the 'combination' of the aforementioned colors.
This combination produces a unique color and it's saved in a tuple like RGB(a,b,c) where a, b and c
are integer numbers in range (0,255).

#### Text to image conversion
The script **text_to_image_converter.py** reads every character in the input file, convert it
into his corresponding unicode value and loads the obtained value inside a pixel.
**Eg:**
given the string "Hi!", the program extrapolates the values:
- H -> 72
- i -> 105
- ! -> 33
and then generates the RGB tuple: RGB(72,105,33)
This will represent the color of the first pixel of the image so, each pixel will contain 3 characters
of the original text.

#### Image to text conversion
This conversion is done by the **image_to_text_converter.py** script that basically executes the 
opposite operation performed by the previous one.
The script reads every pixel's RGB color and extrapolates 3 characters from it.
**Eg:**
The first pixel has the following value RGB(72,105,33), so the script will read the characters:
- 72  -> H
- 105 -> i
- 33  -> !

## Important remarks
**This script doesn't work for every character** in the world!
As I mentioned earlier every value inside the RGB tuple has a range **(0 -> 255)** so only characters which
have unicode values inside the range can be effectively converted and then correctly read back.
This is enough to include every latin character (upper or lower case), special symbols, numbers or 
accented letters but it won't work, for example, for chinese characters.

**The script ignores the NUL character**.
The NUL character is translated to unicode value 0 (zero) and since the default value of the RGB tuple for the empty pixels is
comprised of zeroes -> RGB(0,0,0) I chose to ignore it to avoid filling the resulting txt file with NULs characters when
converting an image back to text.

**Don't use the script to conceal sensitive information**.
Even though the resulting image may appear as an unsuspecting random cluster of colors at first glance, this is not an effective way to 
conceal or encrypt information!
This script is created for learning and educational purposes, if your objective is privacy and confidentiality then use a secure
encryption algorithm.