# What this mpy ? (Nedir mpy ? )
Instead of simple tkinter message interfaces, mpy offers simple message interfaces made with tkinter that are completely under your control.
( mpy, basit tkinter mesaj arayüzleri yerine, tkinter ile yapılmış, tamamen kontrolünüz altında olan basit mesaj arayüzleri sunar.)

## How to install ?


## How to use ? (Nasıl kullanılır ? )

Youtube Video : https://youtu.be/V4MPTTfYuyI

#### Normal message box (Normal mesaj kutusu)

```py
from mpy import MessageTypes

MessageTypes.Normal("hello world")
```

#### Ok/Cancel message box (Tamam/Vazgeç mesaj kutusu)

```py
from mpy import MessageTypes

MessageTypes.okCancel("Create world ?", lambda: print("Creating world...")) # Lambda is the function to be executed when pressed, it can be assigned to an external function.
```

#### Yes/No message box (Tamam/Hayır mesaj kutusu)

```py
from mpy import MessageTypes

MessageTypes.yesNo("Create world ?", lambda: print("Creating world...")) # Lambda is the function to be executed when pressed, it can be assigned to an external function.
```

#### Ok/Help message box (Tamam/Yardım mesaj kutusu)

```py
from mpy import MessageTypes

MessageTypes.okhelp("Create world ?", lambda: print("Creating world..."),"https://google.com") # Lambda is the function to be executed when pressed, it can be assigned to an external function. The last parameter represents the web address to which the help button will be sent when pressed.
```
