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
      self.consoleText.readonly = True
      consoleArea.appendChild(self.consoleText)
      style = self._w.document.createElement('STYLE')
      css = 'div {width: 300px; height: 100%; background-color: black; position: fixed; right: 0; top: 0;} #textarea {color: white; background-color: rgba(0,0,0,0); width: 260px; height: 810px; position: fixed; top: 20px; right: 20px; margin: 0px; resize: none; border: none; outline: none;}'
      style.type = 'text/css'
      style.appendChild(document.createTextNode(css))
      self._w.document.head.appendChild(style)
      self._w.document.body.appendChild(consoleArea)
      self._w.onunload = onclose
  
    def bind(self, evtspec, callback):
      self._w.document.body.bind(evtspec, callback)
      
    def add(self, obj):
      self._stage.addChild(obj)
      
    def remove(self, obj):
      self._stage.removeChild(obj)
      
    def animate(self, stepcallback):
      self._renderer.render(self._stage)
      self._w.requestAnimationFrame(stepcallback)
      #consoleText2 = document.getElementById("console").innerHTML
      self.consoleText.innerHTML = "hello"
      
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
  
    
