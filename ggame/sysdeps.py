def module_exists(module_name):
   try:
      __import__(module_name)
   except ImportError:
      return False
   else:
      return True
if module_exists('browser') and module_exists('javascript'):
   from browser import window, document
   from javascript import JSObject, JSConstructor
   #try:
   #   from pyinput import *
   #   didLoadPyinput = True
   #except:
   #   didLoadPyinput = False
   GFX = JSObject(window.PIXI)
   GFX_Rectangle = JSConstructor(GFX.Rectangle)
   GFX_Texture = JSConstructor(GFX.Texture)
   GFX_Texture_fromImage = JSConstructor(GFX.Texture.fromImage)
   GFX_Sprite = JSConstructor(GFX.Sprite)
   GFX_Graphics = JSConstructor(GFX.Graphics)()
   GFX_Text = JSConstructor(GFX.Text)
   GFX_DetectRenderer = GFX.autoDetectRenderer 
   SND = JSObject(window.buzz)
   SND_Sound = JSConstructor(SND.sound)
   class GFX_Window(object):
      def __init__(self, width, height, onclose):
         self._w = window.open("", "")
         self._stage = JSConstructor(GFX.Container)()
         self.width = width if width != 0 else int(window.innerWidth * 0.9)
         self.height = height if height != 0 else int(window.innerHeight * 0.9)
         self._renderer = GFX.autoDetectRenderer(self.width, self.height, {'transparent':True})
         self._w.document.body.appendChild(self._renderer.view)
         consoleArea = self._w.document.createElement('DIV')
         self.consoleText = self._w.document.createElement('TEXTAREA')
         self.consoleText.id = "textarea"
         consoleArea.id = "consoleArea"
         self.consoleText.readonly = True
         consoleArea.appendChild(self.consoleText)
         style = self._w.document.createElement('STYLE')
         css = '#consoleArea {width: 300px; height: 100%; background-color: black; position: fixed; right: 0; top: 0;} #textarea {color: white; background-color: rgba(0,0,0,0); width: 260px; height: 810px; position: fixed; top: 20px; right: 20px; margin: 0px; resize: none; border: none; outline: none;} .switch {position: relative; display: inline-block; width: 60px; height: 34px;} .switch input {display:none;} .slider {position: absolute;cursor: pointer;top: 0;left: 0;right: 0;bottom: 0;background-color: #ccc;-webkit-transition: .4s;transition: .4s;} .slider:before {position: absolute;content: "";height: 26px;width: 26px;left: 4px;bottom: 4px;background-color: white;-webkit-transition: .4s;transition: .4s;} input:checked + .slider {background-color: #2196F3;} input:focus + .slider {box-shadow: 0 0 1px #2196F3;} input:checked + .slider:before {-webkit-transform: translateX(26px);-ms-transform: translateX(26px);transform: translateX(26px);} .slider.round {border-radius: 34px;} .slider.round:before {border-radius: 50%;} body{-webkit-touch-callout: none;-webkit-user-select: none;-khtml-user-select: none;-moz-user-select: none;-ms-user-select: none;user-select: none;}'
         style.type = 'text/css'
         style.appendChild(document.createTextNode(css))
         self._w.document.head.appendChild(style)
         
         self._w.onunload = onclose
         #if didLoadPyinput:
         #   winput_init()
         consoleArea.insertAdjacentHTML('afterbegin', '<label class="switch"><input type="checkbox"><div class="slider round"></div></label>')
         #self._w.document.body.innerHTML += '<div id = "inputScreen" style = "display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background-color: rgba(0,0,0,0.2); z-index: 50;"><div style = "position: fixed; left: calc(50% - 150px); top: calc(50% - 75px); background-color: white;"><p id = "toPrompt"></p><input type = "text" id = "toInput"><input type = "submit" id = "toSubmit"></div></div>'
         self._w.document.body.appendChild(consoleArea)
      def bind(self, evtspec, callback):
         self._w.document.body.bind(evtspec, callback)

      def add(self, obj):
         self._stage.addChild(obj)

      def remove(self, obj):
         self._stage.removeChild(obj)

      def animate(self, stepcallback):
         self._renderer.render(self._stage)
         self._w.requestAnimationFrame(stepcallback)
         consoleText2 = document.getElementById("console").value
         self._w.document.getElementById("textarea").value = consoleText2

      def destroy(self):
         SND.all().stop()
         self._stage.destroy()
elif module_exists('pygame'):
   try:
      from ggame.pygamedeps import *
   except:
      from pygamedeps import *
else:
   try:
      from ggame.headlessdeps import *
   except:
      from headlessdeps import *

