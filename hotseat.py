
import RPi.GPIO as GPIO
from omxplayer import OMXPlayer
import time

#---------------------------

# Pinbelegung
# output
wind = 4
smoke1 = 17 #kiwi
smoke2 = 5 #kaffee
smoke3 = 13 #gluehwein
heat = 25 #heat

# input
play_button = 10 #play/pause button

#---------------------------

try:
# boardlayout festlegen
	GPIO.setmode(GPIO.BCM)

# output pins als output festlegen
	GPIO.setup(wind, GPIO.OUT, initial=GPIO.LOW)
	GPIO.setup(smoke1, GPIO.OUT, initial=GPIO.LOW)
	GPIO.setup(smoke2, GPIO.OUT, initial=GPIO.LOW)
	GPIO.setup(smoke3, GPIO.OUT, initial=GPIO.LOW)
	GPIO.setup(heat, GPIO.OUT, initial=GPIO.LOW)
	
# input pins als input festlegen
	GPIO.setup(play_button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
except:
	print("unable to set pin")

#---------------------------

# globale Variablen fuer play/pause button

global last_buttontime
last_buttontime = time.time()

global action_on
action_on = False

global pwm_wind, pwm_smoke1, pwm_smoke2, pwm_smoke3, pwm_heat

#----------------------------

# startet/pausiert das Video bei button druck
def play_callback(channel):

	global last_buttontime
	print('Taste erkannt')

	# manuelle Entprellung des play/pause buttons
	#(kann kurzzeitig zu wenig Strom bekommen und dadurch einen ungewissen state bekommen)
	if(time.time()-last_buttontime > 2):
		last_buttontime = time.time()
		player.play_pause()

	if(player.is_playing() == True):
		print('Player is playing')
	else:
		print('Player paused')
		GPIO_reset()

# wenn start/stop button gedrueckt wird -> dieses event wird ausgefuert (ist ebenfalls entprellt)
GPIO.add_event_detect(play_button, GPIO.FALLING, callback=play_callback, bouncetime=300)


# aktiviert angesteuerten Aktor mit bestimmter pwm
def action(windvalue, smoke1value, smoke2value, smoke3value, heatvalue):
	global action_ons
	global pwm_wind, pwm_smoke1, pwm_smoke2, pwm_smoke3, pwm_heat
	print('Action:')
	print(action_on)

        # action-status wird gewechselt -> fuer start/stop button
	if(action_on == False):
		action_on = True

		# angesprochener outputpin gibt pwm-Wert aus
		pwm_wind = GPIO.PWM(wind, 42)
		pwm_wind.start(windvalue)
		if(windvalue > 0): print('Wind an')
		
		pwm_smoke1 = GPIO.PWM(smoke1, 42)
		pwm_smoke1.start(smoke1value)
		if(smoke1value > 0): print('Smoke1 an')
		
		pwm_smoke2 = GPIO.PWM(smoke2, 42)
		pwm_smoke2.start(smoke2value)
		if(smoke2value > 0): print('Smoke2 an')
		
		pwm_smoke3 = GPIO.PWM(smoke3, 42)
		pwm_smoke3.start(smoke3value)
		if(smoke3value > 0): print('Smoke3 an')
		
		pwm_heat = GPIO.PWM(heat, 42)
		pwm_heat.start(heatvalue)
		if(heatvalue > 0): print('Heat an')


# setzt alle Aktoren auf 0 und wechselt den action-state
def GPIO_reset():
	print('Reset')
	global action_on
	global pwm_wind, pwm_smoke1, pwm_smoke2, pwm_smoke3, pwm_heat
	
	pwm_wind.stop()
	pwm_smoke1.stop()
	pwm_smoke2.stop()
	pwm_smoke3.stop()
	pwm_heat.stop()
	
	action_on = False

#-----------------------------
#Main code

try:
		# player-Objekt erzeugen,parametrieren und das Video und Aktoren auf 0 setzen
	player = OMXPlayer('/home/pi/Desktop/R_A_vid_v2.mp4', args=['--win', '0 0 1920 1080', '--no-osd'])
	player.set_position(0)
	player.play()
	action(0,0,0,0,0)

		# stetige Abfrage welche Aktoren angesteuert werden wollen. wenn nichts geschieht, GPIO_Reset wird ausgefuert
		# in den jeweiligen Zeitintervallen werden die Aktoren angesteuert
	while 1:
		while 3 < player.position() < 5 and player.is_playing():
			action(25,100,0,0,0)
			print(player.position())
		GPIO_reset()
		
		while 21-15 < player.position() < 21 and player.is_playing():
			action(0,0,0,0,100)
			print(player.position())
		GPIO_reset()
		
		while 21 < player.position() < 24 and player.is_playing():
			action(30,0,0,0,100)
			print(player.position())
		GPIO_reset()
		
		while 40 < player.position() < 48 and player.is_playing():
			action(60,0,0,0,0)
			print(player.position())
		GPIO_reset()
		
		while 98 < player.position() < 99 and player.is_playing():
			action(100,0,0,0,0)
			print(player.position())
		GPIO_reset()
		
		while 223 < player.position() < 230 and player.is_playing():
			action(0,0,0,0,100)
			print(player.position())
		GPIO_reset()
		
		while 230 < player.position() < 305 and player.is_playing():
			action(30,0,0,0,100)
			print(player.position())
		GPIO_reset()
		
		while 305 < player.position() < 312 and player.is_playing():
			action(0,0,0,0,100)
			print(player.position())
		GPIO_reset()
		
		while 312 < player.position() < 322 and player.is_playing():
			action(40,0,0,0,100)
			print(player.position())
		GPIO_reset()
		
		while 326 < player.position() < 328 and player.is_playing():
			action(25,0,100,0,0)
			print(player.position())
		GPIO_reset()
		
		while 353 < player.position() < 355 and player.is_playing():
			action(25,0,100,0,0)
			print(player.position())
		GPIO_reset()
		
		while 388 < player.position() < 390 and player.is_playing():
			action(25,0,0,100,0)
			print(player.position())
		GPIO_reset()
		
		while 416 < player.position() < 418 and player.is_playing():
			action(25,0,100,0,0)
			print(player.position())
		GPIO_reset()
		
		while 438 < player.position() < 450.5 and player.is_playing():
			action(100,0,0,0,0)
			print(player.position())
		GPIO_reset()
		
		while 450.5 < player.position() < 453 and player.is_playing():
			action(30,0,0,0,0)
			print(player.position())
		GPIO_reset()
		
		while 453 < player.position() < 466 and player.is_playing():
			action(100,0,0,0,0)
			print(player.position())
		GPIO_reset()
		
		while 466 < player.position() < 469 and player.is_playing():
			action(30,0,0,0,0)
			print(player.position())
		GPIO_reset()
		
		while 469 < player.position() < 495 and player.is_playing():
			action(100,0,0,0,0)
			print(player.position())
		GPIO_reset()


except KeyboardInterrupt:
	print("KeyboardInterrupt appeared")

except:
	print ("non specified error appeared")

finally:
#setzte alle ports zurueck, wenn das Programm geschlossen wird
	GPIO.cleanup()
	player.quit()

