# django-reverse-ajax

This demonstrates the use of `StreamingHttpResponse` and `yield` on the python side and `response.body.getReader()` on the JavaScript side to show how stream data to the browser as and when you want the server to send data in chunks - and not as a single response body - this is the equivalent of `flush(); ob_flush();` in PHP.

The receiving part on the client side is not exactly a one-liner code. Its not magic. Post calling `fetch`, we read it via `const  reader = response.body.getReader()` in chunks (`const {done, value} = await  reader.read()`)

# Directory Structure
I assume that `python -m venv env` was done in the directory **outside** of the django project directory.
In this case the file structure is like this :	
```
├── env
│    ├── bin
│    ├── include
│    ├── lib
│    └── pyvenv.cfg
└── reverse_ajax
    ├── LICENSE
    ├── README.md
    ├── application
    ├── db.sqlite3
    ├── manage.py
    ├── reverse_ajax
    └── templates
```


# Run the server

## macOS
```
source env/bin/activate
cd reverse_ajax
python3 manage.py runserver
```

## Windows 11 in PowerShell
```
env/Scripts/Activate.ps1
cd reverse_ajax
python manage.py runserver
```

## Load localhost in the browser

Goto http://localhost:8000
Click on the Click Me button
You should see numbers from 1 to 10 displayed over a period of 5 seconds in half seconds interval. The 0.5 second pause is from the server side as `time.sleep(0.5)` and not on the set in the browser's JavaScript as `setInterval` . The waiting is done in the browser as `const {done, value} = await  reader.read();` where if `done` is *true* then it breaks the loop waiting for chunks.

## Demo

https://yield.anjanesh.com

## Preview

https://github.com/anjanesh/django-reverse-ajax/assets/85973/df91a0f6-e581-4a6a-b103-e23f5ab5ddf7

