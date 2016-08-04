# AppFramer
AppFramer helps to put your app screenshots in beautiful device frames with annotations by running a simple command.
Quickly put your screenshots into the various device frames needed for iTunesConnect submission.

## Installation
```sh
$ pip install appframer
```
#### Compatibility
* Linux / OSX


## Usage
* Go to the directory where you want the generate screen frames to be.
* Run the following command in your terminal.
```sh
$ appframer -i /path/to/screens.json
```

##Options
`appframer [-h] -i INPUT`

	-h --help				show help message and exit
	-i --input				path to data.json file that describes the screenshots to put in device frame

###Example
```sh
$ appframer -i /path/to/screens.json
```

###After
```
FramedAppScreens - 03-08-2016 AT 18.40
Using splash.jpg, timeline.jpg and profile.jpg as examples of screenshots listed in screens.json
The generated output folder will look like this:

│   ├── 3.5
│   │   └── splash.jpg
│   │   ├── timeline.jpg
|	|	├── profile.jpg
|   |
│   ├── 4
│   │   └── splash.jpg
│   │   ├── timeline.jpg
|	|	├── profile.jpg
|   |
│   ├── 4.7
│   │   └── splash.jpg
│   │   ├── timeline.jpg
|	|	├── profile.jpg
|   |
│   ├── 5.5
│   │   └── splash.jpg
│   │   ├── timeline.jpg
|	|	├── profile.jpg

```

###screens.json example
```
Screens.json is obviously a json file format
For iOS, take the screenshots you want to use on iPhone6s preferably because of the high resolution
and list them in your screens.json and appframer will take those screenshots and generate
the screenshots framed in different devices in the dimensions needed for iTunesConnect submission

NOTE: In the screens.json example below, I'm assuming the screenshot images are in the same directory
as the screens.json file itself and I'll be running the command from the same directory

{
    "device_type": "iOS",
    "screens": [
        {
            "file_path": "Live Video.jpeg",
            "title": "Live Video",
            "description": "Rain in Spain falls mainly in the plain",
            "title_color": "black",
            "description_color": "red"
        },
        {
            "file_path": "Profile.jpeg",
            "title": "Profile",
            "description": "Rain in Spain falls mainly in the plain",
            "title_color": "white",
            "description_color": "black"
        },
        {
            "file_path": "Search.jpeg",
            "title": "Search",
            "description": "Rain in Spain falls mainly in the plain",
            "title_color": "white",
            "description_color": "black"
        },
        {
            "file_path": "Status Update.jpeg",
            "title": "Status Update",
            "description": "Rain in Spain falls mainly in the plain",
            "title_color": "black",
            "description_color": "black"
        },
        {
            "file_path": "Timeline.jpeg",
            "title": "Timeline",
            "description": "Rain in Spain falls mainly in the plain",
            "title_color": "white",
            "description_color": "black"
        }
    ]
}

```
======

## The MIT License
> Copyright (c) 2016 Emmanuel Adegbite http://github.com/olucurious

> Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

> The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
