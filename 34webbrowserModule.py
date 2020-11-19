# webbrowser.open()
# url: the URL to open in the web browser
# new: 0 opens the URL in the existing tab, 1 opens in a new window, 2 opens in new tab
# autoraise: if set to True, the window will be moved on top of the other windows

# webbrowser.open_new()
# url: the URL to open in the web browser

# webbrowser.open_new_tab()
# url: the URL to open in the web browser

# webbrowser.get()
# using: the browser to use

# webbrowser.register()
# url: browser name
# constructor: path to the executable browser (help)
# instance: An instance of a web browser returned from the webbrowser.get() method

# Opening a URL with Default Browser
import webbrowser
webbrowser.open("http://stackoverflow.com")
webbrowser.open_new("http://stackoverflow.com")
webbrowser.open_new_tab("http://stackoverflow.com")

# Opening a URL with Different Browsers
ff_path = webbrowser.get("C:/Program Files/Mozilla Firefox/firefox.exe")
ff = webbrowser.get(ff_path)
ff.open("http://stackoverflow.com/")
# Registering a browser type:
ff_path = webbrowser.get("C:/Program Files/Mozilla Firefox/firefox.exe")
ff = webbrowser.get(ff_path)
webbrowser.register('firefox', None, ff)
# Now to refer to use Firefox in the future you can use this
webbrowser.get('firefox').open("https://stackoverflow.com/")
