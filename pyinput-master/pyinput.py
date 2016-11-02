try:
	from browser import window, document
	from javascript import JSObject, JSConstructor

	jq = window.jQuery

	input_c = None
	
	if not jq(".inputScreen").length:
		jq("body").append('<div class = "inputScreen" style = "position: fixed; top: 0; left: 0; width: 100%; height: 100%; background-color: rgba(0,0,0,0.2); z-index: 50;"><div style = "position: fixed; left: calc(50% - 150px); top: calc(50% - 75px); background-color: white;"><p id = "toPrompt"></p><input type = "text" id = "toInput"><input type = "submit" id = "toSubmit"></div></div>')
		jq(".inputScreen").hide()

	def input_callback():
	    input_value = jq('#toInput').val()
	    jq('#toInput').val('')

	    input_t = jq('#toPrompt').text()
	    jq('#toPrompt').text('')
    
	    print(input_t + " " + input_value)
	    input_c(input_t, input_value)

	def input_fade(ev):
	    jq('.inputScreen').fadeOut(300, input_callback)
	    jq('#toSubmit').off('click')

	def input(text, callback):
	    jq('.inputScreen').fadeIn(300)
	    jq('#toPrompt').text(text)
    
	    global input_c
	    input_c = callback
	    jq('#toSubmit').on('click', input_fade)
	
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

