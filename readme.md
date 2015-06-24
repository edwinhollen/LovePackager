# LovePackager

Easy building of [LÖVE](https://love2d.org) .love files, and packaging for Windows, OS X, and Linux.

*Requires Python 3.4+*

## Usage

### Build a .love file

1. Add a config file (json) to your project:

    `project.json`
    
        {
            "name": "MyLoveGame v5.0",
            "sources": ["src/*.lua", "assets/"],
            "output": "build/",
            "love": "C:/love/love.exe"
        }
    
    * **name** of the project will appear as the name of the .love file (`MyLoveGame v5.0.love`).
    
    * **sources** is a list of sources with glob support. Everything in this list will be copied into the built .love file. Directories are copied recursively with the same name.
    
    * **output** specifies where to place the built .love file.
    
    * **love** is optional, but lets you point the run flag at a particular LÖVE executable.

2. Use `lovepackager.py`:

    * Build
    
        `py lovepackager.py --config=project.json`
        
    * Build and run
    
        `py lovepackager.py --config=project.json --run`
        
### Package for other platforms

*Coming soon!*