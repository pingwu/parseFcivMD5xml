Use case:

Convert a fciv generated xml file to Linux compatble md5sum format.


The generated MD5.xml file will be the input of this script.


In Ubuntu Linux usage example:

~/parseMD5xml.py MD5.xml > md5.txt

md5sum -c md5.txt

Assume MD5.xml and all files are in the same folder.



For more info about fciv encoding info, please visit: http://support.microsoft.com/kb/841290

Assume the xml file was generated using this command in Windows environment

%path_to_fciv%\fciv %folder% -wp -bp %folder% -xml MD5.xml

Where %folder% will be replaced by the name that you will run the md5 check.

