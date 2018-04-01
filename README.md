# ASCIIEncoderDecoder

A program that implements lossless encoding and decoding of files containing ASCII art.

## Instructions

Below are the steps that describe how the ASCII Transport Format is to be used.

Import the file:

`from from ASCIIEncoderDecoder import ASCIIFormatTransporter`

Build the object that will contain the data from the ASCII art file:
`object = object = ASCIIFormatTransporter(file_name)`

Encode the object:
`object.encode()`

Decode the object:
`object.decode()`

##Unit Testing
In order to test the robustness of the program use the following command:

`python3 ASCIItests.py`


