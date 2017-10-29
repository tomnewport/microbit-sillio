# StupidIO - A really silly way to send data from micro:bit to your laptop

## ...why?

I got a microbit a couple of days ago. It's pretty awesome but I couldn't figure out how to get it 
to interact with python code on my laptop. So I wrote some code which can use my laptop webcam to
recognise my lovely micro:bit and tell me which LEDs are on and off.

## You realise there are better ways to do this?

You mean like [this](http://www.recantha.co.uk/blog/?p=15074)? I guess it's fun to try something
different (even if it's a silly idea).

## So how does this work?

Well... you flash the micro:bits with some python which lights up a ring of LEDs around the edge
of the display - that makes a pattern which is easy to find. One light is kept off so the computer
can tell which way round it is.

Then you run a python script on your laptop, which creates a website you can open in your web
browser. The website uses JavaScript to turn on your webcam and find bright lights in the video.
By looking for lines of bright lights, you can find the micro:bit display.

When you press `Button A`, it turns on more LEDs which tells the computer to start drawing a line.
When you press `Button B`, it turns on an LED which tells the computer to delete the line. The 
terminal tells you which lights are on and which buttons are pressed.

[![StupidIO](https://img.youtube.com/vi/kIft5X6lR3A/0.jpg)](https://www.youtube.com/watch?v=YkIft5X6lR3A)
