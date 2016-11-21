try:
	from browser import window, document
	from javascript import JSObject, JSConstructor
	from ggame import *

	jq = window.jQuery
	
	if not jq(".inputScreen").length:
		jq("body").append('<div class = "inputScreen" style = "position: fixed; top: 0; left: 0; width: 100%; height: 100%; background-color: rgba(0,0,0,0.2); z-index: 50;"><div style = "position: fixed; left: calc(50% - 150px); top: calc(50% - 75px); background-color: white;"><p id = "toPrompt"></p><input type = "text" id = "toInput"><input type = "submit" id = "toSubmit"></div></div>')
		jq(".inputScreen").hide()
		
	input_queue = []
	winput_queue = []
	#App1 = App
	winput_started = False
	def input_callback():
		input_value = jq('#toInput').val()
		jq('#toInput').val('')

		input_t = jq('#toPrompt').text()
		jq('#toPrompt').text('')

		global input_queue

		print(input_t + " " + input_value)
		input_queue[0][1](input_t, input_value)
		input_queue.pop(0)
		if len(input_queue) > 0:
			inputStart(input_queue[0][0])

	def input_fade(ev):
		jq('.inputScreen').fadeOut(300, input_callback)
		jq('#toSubmit').off('click')

	def inputStart(text):
		jq('.inputScreen').fadeIn(300)
		jq('#toPrompt').text(text)
		jq('#toSubmit').on('click', input_fade)

	def input(text, callback):
		global input_queue
		input_queue.append([text, callback])
		if len(input_queue) == 1:
			inputStart(text)
	
	def winput_callback():
		winput_value = App._win._w.document.getElementById('toInput').value
		App._win._w.document.getElementById('toInput').value = ''

		winput_t = App._win._w.document.getElementById('toPrompt').textContent
		App._win._w.document.getElementById('toPrompt').textContent = ""

		global winput_queue

		print(winput_t + " " + winput_value)
		winput_queue[0][1](winput_t, winput_value)
		winput_queue.pop(0)
		if len(winput_queue) > 0:
			winputStart(winput_queue[0][0])

	def winput_fade(ev):
		App._win._w.document.getElementById('inputScreen').style.display = "none"
		winput_callback()
		App._win._w.document.getElementById('toSubmit').removeEventListener('click', winput_fade)

	def winputStart(text):
		App._win._w.document.getElementById('inputScreen').style.display = "block"
		App._win._w.document.getElementById('toPrompt').textContent = text
		App._win._w.document.getElementById('toSubmit').addEventListener('click', winput_fade)

	def winput(text, callback):
		global winput_queue
		global winput_started
		winput_queue.append([text, callback])
		if winput_started:
			winputStart(text)
			winput_started = False
		print("winning")
				
	def winput_init():
		global winput_started
		winput_started = True
		try:
			winputStart(winput_queue[0][0])
		except:
			pass
		print("started")
				
except:
	underInput = input
	def input(text, callback):
		x = underInput(text+" ")
		callback(text, x)
		
#def first(text, result):
#    print("Hi " + result)
#    input("What's your favorite color?", second)


#def second(text, result):
#    print("Nice! I like " + result + " too.")

