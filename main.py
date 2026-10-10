import Object, Window, Player

window = Window.Window()
test_object = Object.Object(150, 150, 100, 100, "blue", window.canvas)
test_player = Player.Player(250, 250, 50, 50, window.canvas)
test_object.draw()
test_player.draw()
window.run()