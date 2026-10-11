import Object, Window, Player
# Testing 
window = Window.Window()

test_object = Object.Object(150, 150, 100, 100, "blue", window.canvas, None, 1)
test_player = Player.Player(250, 250, 50, 50, window.canvas, image="assets\\sprites\\GmM1oT3Wasdasd0AAuHz4.png", image_scale=5)
test_object.draw()
test_player.draw()
window.run()