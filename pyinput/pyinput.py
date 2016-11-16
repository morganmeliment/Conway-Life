try:
	from browser import window, document
	from javascript import JSObject, JSConstructor
	from ggame import *

	jq = window.jQuery
	
	if not jq(".inputScreen").length:
		jq("body").append('<div class = "inputScreen" style = "position: fixed; top: 0; left: 0; width: 100%; height: 100%; background-color: rgba(0,0,0,0.2); z-index: 50;"><div style = "position: fixed; left: calc(50% - 150px); top: calc(50% - 75px); background-color: white;"><p id = "toPrompt"></p><input type = "text" id = "toInput"><input type = "submit" id = "toSubmit"></div></div>')
		jq(".inputScreen").hide()
		
	input_queue = []
	App1 = App
	def input_callback():
		try:
			input_value = App._win._w.document.getElementById('toInput').value
			App._win._w.document.getElementById('toInput').value = ''

			input_t = App._win._w.document.getElementById('toPrompt').textContent
			App._win._w.document.getElementById('toPrompt').textContent = ""

			global input_queue

			print(input_t + " " + input_value)
			input_queue[0][1](input_t, input_value)
			input_queue.pop(0)
			if len(input_queue) > 0:
				inputStart(input_queue[0][0])
		except:
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
		try:
			App._win._w.document.getElementById('inputScreen').style.display = "none"
			input_callback()
			App._win._w.document.getElementById('toSubmit').removeEventListener('click', input_fade)
		except:
			jq('.inputScreen').fadeOut(300, input_callback)
			jq('#toSubmit').off('click')

	def inputStart(text):
		try:
			App._win._w.document.getElementById('inputScreen').style.display = "block"
			App._win._w.document.getElementById('toPrompt').textContent = text
			App._win._w.document.getElementById('toSubmit').addEventListener('click', input_fade)
		except:
			jq('.inputScreen').fadeIn(300)
			jq('#toPrompt').text(text)
			jq('#toSubmit').on('click', input_fade)

	def input(text, callback):
		global input_queue
		input_queue.append([text, callback])
		if len(input_queue) == 1:
			inputStart(text)
	
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

